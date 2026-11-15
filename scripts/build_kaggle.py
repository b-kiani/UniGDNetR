"""Build the Kaggle port from the supplied training notebook without changing the model protocol."""
import ast
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "notebooks/02_UniGDNetR_TRAIN_RAM_Fixed.ipynb"
nb = json.loads(SOURCE.read_text())

def cell(kind, source):
    c = {"cell_type": kind, "metadata": {}, "source": source.splitlines(True)}
    if kind == "code":
        c.update(execution_count=None, outputs=[])
    return c

bootstrap = '''import os, sys, json, shutil, time, hashlib
from pathlib import Path
KAGGLE_SESSION_STARTED = time.monotonic()
KAGGLE_SESSION_HOURS = float(os.environ.get("UNIGDNETR_SESSION_HOURS", "10"))
if not 0.1 <= KAGGLE_SESSION_HOURS <= 10:
    raise ValueError("Session budget must be between 0.1 and 10 hours.")
class SessionBudgetReached(RuntimeError):
    pass
def check_session_budget():
    if time.monotonic() - KAGGLE_SESSION_STARTED >= KAGGLE_SESSION_HOURS * 3600:
        raise SessionBudgetReached("Session budget reached; saved outputs must be attached to the next session.")

KAGGLE_OUTPUT = Path("/kaggle/working/UniGDNetR")
KAGGLE_OUTPUT.mkdir(parents=True, exist_ok=True)
SOURCE_HANDLES = [
    "aiocta/brats2023-part-1",
    "aiocta/brats2023-part-2zip",
    "andrewmvd/liver-tumor-segmentation",
    "andrewmvd/liver-tumor-segmentation-part-2",
    "samdazel/automated-cardiac-diagnosis-challenge-miccai17",
]
source_roots = {}
for handle in SOURCE_HANDLES:
    owner, slug = handle.split("/")
    candidates = [Path("/kaggle/input/datasets") / handle, Path("/kaggle/input") / slug]
    found = next((p for p in candidates if p.is_dir()), None)
    if found is None:
        raise FileNotFoundError(f"Attach the required Kaggle input: {handle}")
    source_roots[handle] = found
    print("MOUNTED", handle, "->", found, flush=True)

# Saved notebook outputs are immutable inputs. Copy only this experiment's
# state to writable working storage. Never import a run lock from another VM.
resume_markers = list(Path("/kaggle/input").rglob("unigdnetr_kaggle_session.json"))
if len(resume_markers) > 1:
    raise RuntimeError("Attach exactly one previous UniGDNetR notebook output for recovery.")
if resume_markers:
    resume_root = resume_markers[0].parent.parent
    for name in ("manifests", "slice_indices", "checkpoints", "results", "figures", "tables", "logs"):
        if (resume_root / name).exists():
            shutil.copytree(resume_root / name, KAGGLE_OUTPUT / name,
                            dirs_exist_ok=True, ignore=shutil.ignore_patterns("*.lock", "*.tmp", "locks"))
    print("Restored previous output:", resume_root, flush=True)
else:
    print("No previous output attached: starting a new experiment.", flush=True)
(KAGGLE_OUTPUT / "manifests").mkdir(exist_ok=True)
(KAGGLE_OUTPUT / "manifests" / "unigdnetr_kaggle_session.json").write_text(json.dumps({
    "state": "running", "sources": SOURCE_HANDLES,
    "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "final_test_evaluation_complete": False,
}, indent=2))
'''

intro = '''# UniGDNetR — Kaggle full experiment

Port of the supplied RAM-fixed Stage 2 notebook. The original model, three seeds
(13, 37, 71), 40-epoch maximum, 2,500 training batches per epoch and patient-grouped
70/15/15 splits are retained. Seven variants × three seeds = 21 runs.

Use **GPU T4 x2**, Internet on, and **Save Version → Save & Run All**.
The current PyTorch model uses one GPU. The second GPU is not used by this port.
Raw datasets remain mounted as read-only Kaggle inputs; they are never copied to
the limited output disk or uploaded to GitHub.

The run stops cleanly after a 10-hour session budget, saves compatible recovery
checkpoints, and reports `paused`, never `complete`, for unfinished work. To
continue, attach exactly one previous version's notebook output as Input and run
again. Checkpoint fingerprints and configuration must still match.

The original Stage 3 evaluation notebook was not supplied. Training/validation
logs are not final held-out paper results. No test-set scores are invented here.
'''

new = [cell("markdown", intro), cell("code", bootstrap)]
for i, original in enumerate(nb["cells"]):
    if original["cell_type"] != "code" or not "".join(original.get("source", [])).strip():
        continue
    s = "".join(original["source"])
    if i == 5:
        s = s.replace('data_root: str = r"D:\\Datasets"', 'data_root: str = "/kaggle/input"')
        s = s.replace('output_root: str = r"D:\\Papers\\UniGDNetR"', 'output_root: str = "/kaggle/working/UniGDNetR"')
        s = s.replace('checkpoint_every_batches: int = 2500', 'checkpoint_every_batches: int = 300')
        s = s.replace('checkpoint_every_minutes: float = 20.0', 'checkpoint_every_minutes: float = 10.0')
        s += '\nif not torch.cuda.is_available():\n    raise RuntimeError("Enable a Kaggle GPU before training; TPU requires a separate XLA port.")\n'
        s += '\n_atomic_environment = {"python": sys.version, "torch": torch.__version__, "cuda": torch.version.cuda, "gpus": [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())]}\n'
        s += '(OUTPUT_ROOT / "manifests" / "kaggle_environment.json").write_text(json.dumps(_atomic_environment, indent=2))\n'
    elif i == 6:
        s = 'PIPELINE_STAGE = "prepare_then_train"\nREAD_ONLY_PREPARED_ARTIFACTS = False\nREQUIRE_PREPARED_INDICES = False\n'
    elif i == 11:
        start = s.index('brain_root = DATA_ROOT / "Brain"')
        end = s.index('\nfor task, records in all_records.items():', start)
        s = s[:start] + '''brain_root = DATA_ROOT
liver_root = DATA_ROOT
cardio_root = DATA_ROOT
brats_sources = [source_roots[h] for h in SOURCE_HANDLES if h.startswith("aiocta/")]
lits_sources = [source_roots[h] for h in SOURCE_HANDLES if h.startswith("andrewmvd/")]
acdc_source = source_roots[SOURCE_HANDLES[-1]]
# Use only the original ACDC training cohort; keep official test cases unused.
acdc_training = [p for p in acdc_source.rglob("training") if p.is_dir()]
if len(acdc_training) != 1:
    raise RuntimeError(f"Expected one ACDC training folder, found {acdc_training}")
all_records = {
    "brats": [r for p in brats_sources for r in discover_brats(p)],
    "lits": discover_lits(source_roots[SOURCE_HANDLES[2]].parent),
    "acdc": discover_acdc(acdc_training[0]),
}
# LiTS segmentation files occur in both parts. Pair the full source tree once,
# so masks from part 1 can match image volumes from part 2.
for task, records in all_records.items():
    unique = {}
    for r in records:
        identity = r.get("subject_id") if task == "brats" else r["case_id"]
        if identity in unique:
            raise RuntimeError(f"Duplicate case identity across source parts: {task}/{identity}")
        unique[identity] = r
    if not records:
        raise RuntimeError(f"Required task is absent: {task}")
cohort_counts = {t: {"scans": len(rs), "patients": len({r.get("group_id", r["case_id"]) for r in rs})} for t, rs in all_records.items()}
(OUTPUT_ROOT / "manifests" / "kaggle_cohorts.json").write_text(json.dumps(cohort_counts, indent=2))
print("Cohort coverage:", json.dumps(cohort_counts, indent=2), flush=True)
if cohort_counts["brats"]["scans"] != 1251:
    raise RuntimeError("Expected all 1,251 labeled BraTS2023 GLI scans; refuse a partial-cohort paper run.")
if cohort_counts["lits"]["scans"] != 131:
    raise RuntimeError("Expected all 131 labeled LiTS scans; refuse a partial-cohort paper run.")
if cohort_counts["acdc"]["patients"] != 100 or cohort_counts["acdc"]["scans"] != 200:
    raise RuntimeError("Expected ACDC training: 100 patients, two labeled frames each.")
''' + s[end:]
    elif i == 13:
        s = s.replace('def canonical_header(path: str):\n    return nib.as_closest_canonical(nib.load(path))', '''def canonical_header(path: str):
    # Reproduce canonical geometry without touching the voxel-array proxy.
    from types import SimpleNamespace
    image = nib.load(path)
    orientation = nib.orientations.io_orientation(image.affine)
    order = np.argsort(orientation[:, 0]).astype(int)
    shape = tuple(int(image.shape[int(axis)]) for axis in order)
    affine = image.affine @ nib.orientations.inv_ornt_aff(orientation, image.shape[:3])
    return SimpleNamespace(shape=shape, affine=affine)''')
    elif i == 17:
        # A callback checkpoint is not needed yet: completed case indices persist
        # only after each split finishes, just as in the source notebook.
        s = s.replace('for record in tqdm(records, desc=f"Indexing {task}/{split_name}"):\n',
                      'for record in tqdm(records, desc=f"Indexing {task}/{split_name}"):\n        check_session_budget()\n')
    elif i == 25:
        s = s.replace('                    )\n\n                train_log, train_seconds = train_one_epoch(',
                      '                    )\n                    check_session_budget()\n\n                train_log, train_seconds = train_one_epoch(')
        s = s.replace('            resume_train_state = None\n            resume_phase = "train"',
                      '            check_session_budget()\n            resume_train_state = None\n            resume_phase = "train"')
        s = s.replace('            for batch in task_loaders[task]:\n',
                      '            for batch in task_loaders[task]:\n                check_session_budget()\n')
    elif i == 30:
        s = s.replace('display(plan_df)', 'display(plan_df)\nplan_df.to_csv(OUTPUT_ROOT / "manifests" / "experiment_plan.csv", index=False)')
        start = s.index('trained_checkpoints = []')
        # Wrap the existing training loop so a time budget leaves an explicitly
        # incomplete session while preserving the source loop's lock release.
        tail = s[start:]
        s = s[:start] + 'session_paused = False\ntry:\n    check_session_budget()\n' + '\n'.join('    '+line for line in tail.splitlines())
        s += '\nexcept SessionBudgetReached as exc:\n    session_paused = True\n    print("SESSION PAUSED:", exc, flush=True)\n'
        s += '''
session_record = {
    "state": "paused" if session_paused else "training_complete",
    "pipeline_revision": PIPELINE_REVISION,
    "dataset_fingerprint": DATASET_FINGERPRINT,
    "sources": SOURCE_HANDLES,
    "elapsed_hours": (time.monotonic() - KAGGLE_SESSION_STARTED) / 3600,
    "final_test_evaluation_complete": False,
    "saved_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}
_atomic_json_save(session_record, OUTPUT_ROOT / "manifests" / "unigdnetr_kaggle_session.json")
print(json.dumps(session_record, indent=2), flush=True)
'''
    new.append(cell("code", s))
    if i == 23:
        new.append(cell("markdown", '## GPU preflight\nSynthetic forward/backward checks for every task; these are not study results.\n'))
        new.append(cell("code", '''seed_everything(13)
smoke_net = UniGDNetR(TASK_SPECS, CFG.base_channels, CFG.task_embedding_dim, CFG.dropout).to(DEVICE)
smoke_loss = CompoundSegmentationLoss()
for task, spec in TASK_SPECS.items():
    smoke_net.zero_grad(set_to_none=True)
    x = torch.randn(CFG.batch_size, spec["modalities"] * CFG.context_slices, CFG.image_size, CFG.image_size, device=DEVICE)
    y = torch.randint(spec["classes"], (CFG.batch_size, CFG.image_size, CFG.image_size), device=DEVICE)
    with torch.autocast(device_type="cuda", dtype=torch.float16):
        logits = smoke_net(x, task)
        loss, _ = smoke_loss(logits, y)
    assert logits.shape == (CFG.batch_size, spec["classes"], CFG.image_size, CFG.image_size)
    assert torch.isfinite(loss), f"Nonfinite smoke loss: {task}"
    loss.backward()
    assert all(torch.isfinite(p.grad).all() for p in smoke_net.parameters() if p.grad is not None)
    print("GPU PREFLIGHT PASSED", task, float(loss.detach()), flush=True)
del smoke_net, smoke_loss, x, y, logits, loss
torch.cuda.empty_cache()
seed_everything(SEEDS[0])
'''))

new.append(cell("markdown", '''## Saved outputs and GitHub

`UniGDNetR/manifests/experiment_plan.csv` lists the complete plan. Check
`UniGDNetR/manifests/unigdnetr_kaggle_session.json` for an explicit `paused` or
`training_complete` state. Atomic `.pt` checkpoint files remain in Kaggle output.
Logs and validation curves are provisional until Stage 3 evaluates completed
models on the held-out patients. Use the repository's `sync_results.py` to export
an allowlist of small reports; raw data and credentials are always excluded.
'''))
for j, c in enumerate(new):
    if c['cell_type'] == 'code':
        ast.parse(''.join(c['source']), filename=f'kaggle_cell_{j}')
nb['cells'] = new
nb['metadata'] = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                  "language_info": {"name": "python", "version": "3.11"}}
target = ROOT / "notebooks/UniGDNetR_Kaggle_Full_Experiment.ipynb"
target.write_text(json.dumps(nb, indent=1))
print(target)
