"""Build a guarded evaluation candidate. Does not start training or evaluation."""
import ast
import copy
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
original=ROOT/'notebooks/03_UniGDNetR_EVALUATE_original.ipynb'
assert hashlib.sha256(original.read_bytes()).hexdigest()=='d34591cd0da8d65fff1da459f54dc47a95ab4e773af5fd8f231a3e2f6e3298f9'
evaluation=json.loads(original.read_text())
training=json.loads((ROOT/'notebooks/UniGDNetR_Kaggle_Full_Experiment.ipynb').read_text())
def cell(kind,text):
    result={'cell_type':kind,'metadata':{},'source':text.splitlines(True)}
    if kind=='code':result.update(outputs=[],execution_count=None)
    return result
new=[cell('markdown','''# UniGDNetR Kaggle evaluation — CANDIDATE, NOT VALIDATED

Derived from the recovered original Stage 3 and the verified Kaggle training preparation.
Do not launch while training is active. Requires all 21 completed compatible models and
latest published stable provenance. Local tests cover buffers, ECE, geometry, coverage
and Python/NumPy case recovery. Neural/GPU equivalence, large-volume HD95 memory and
live session recovery still need validation. Do not approve execution until recorded.
'''),cell('code','''import os, json
from pathlib import Path
if os.environ.get('UNIGDNETR_EVALUATION_PORT_APPROVED') != '1':
    raise RuntimeError('Evaluation candidate is not yet validated. See EVALUATION_READINESS.md.')
markers=list(Path('/kaggle/input').rglob('unigdnetr_kaggle_session.json'))
if len(markers)!=1:
    raise RuntimeError('Attach exactly one latest trusted completed training output.')
state=json.loads(markers[0].read_text())
if state.get('state') != 'training_complete':
    raise RuntimeError('All training must finish before held-out evaluation.')
if not (markers[0].parent/'content_provenance.json').is_file():
    raise RuntimeError('Stable content provenance is required; legacy migration is not evaluation preparation.')
''')]
# Reuse the exact current Kaggle preparation, RAM fixes, architecture and metadata
# guards. Exclude the training registry runner and resume loop (cells19/20).
for i in range(1,19):
    c=copy.deepcopy(training['cells'][i])
    if i==1:
        bootstrap=''.join(c['source'])
        start=bootstrap.index('(KAGGLE_OUTPUT / "manifests" / "unigdnetr_kaggle_session.json").write_text(')
        end=bootstrap.index('}, indent=2))',start)+len('}, indent=2))')
        bootstrap=bootstrap[:start]+'shutil.copy2(resume_markers[0], KAGGLE_OUTPUT / "manifests" / "unigdnetr_kaggle_session.json")'+bootstrap[end:]
        bootstrap+='\n(KAGGLE_OUTPUT / "results" / "automatic_evaluation_complete.json").unlink(missing_ok=True)\n'
        c=cell('code',bootstrap)
    if i==4:
        c=cell('code','PIPELINE_STAGE="evaluate"\nREAD_ONLY_PREPARED_ARTIFACTS=True\nREQUIRE_PREPARED_INDICES=True\n')
    new.append(c)
new.append(cell('code',(ROOT/'scripts/evaluation_buffers.py').read_text()))
new.append(cell('code',(ROOT/'scripts/evaluation_memory.py').read_text()))
new.append(cell('code',(ROOT/'scripts/evaluation_guardrails.py').read_text()+'\nprint(\"PATIENT SPLITS VERIFIED\", validate_splits(splits))\n'))
port_sources=[original,Path(__file__),ROOT/'notebooks/UniGDNetR_Kaggle_Full_Experiment.ipynb']+[ROOT/'scripts'/name for name in ['evaluation_buffers.py','evaluation_memory.py','evaluation_guardrails.py','evaluation_case_cache.py','evaluation_case_runtime.py']]
port_digest=hashlib.sha256(b''.join(path.read_bytes() for path in port_sources)).hexdigest()
new.append(cell('code',(ROOT/'scripts/evaluation_case_cache.py').read_text()+f'\nEVALUATION_PORT_ID = {port_digest!r}\nEVALUATION_SESSION_PAUSED = False\n'))
for i,c in enumerate(evaluation['cells']):
    if i<26:continue
    c=copy.deepcopy(c)
    if c['cell_type']=='code':
        s=''.join(c['source'])
        if i==27:
            start=s.index('@torch.no_grad()\ndef predict_volume(')
            end=s.index('\ndef binary_metrics',start)
            prediction=s[start:end]
            prediction=prediction.replace('    probs_out, entropy_out = [], []','    store = DiskPrediction(TASK_SPECS[task]["classes"], (h,w,depth))\n    next_slice = 0')
            prediction=prediction.replace('            probs_out.extend(mean_prob.cpu().numpy())\n            entropy_out.extend(entropy.cpu().numpy())','            store.write(next_slice, mean_prob.cpu().numpy(), entropy.cpu().numpy())\n            next_slice += len(batch_x)')
            old='    probs = np.stack(probs_out, axis=-1)  # classes,H,W,D\n    entropy = np.stack(entropy_out, axis=-1)\n    pred = probs.argmax(0).astype(np.int16)\n    return pred, probs, entropy, mask'
            assert old in prediction
            prediction=prediction.replace(old,'    store.require_complete()\n    return store, mask')
            # Ensure temporary files close on an inference exception too.
            begin=prediction.index('    batch_x = []')
            body=prediction[begin:]
            prediction=prediction[:begin]+'    try:\n'+''.join('    '+line+'\n' for line in body.splitlines())+'    except BaseException:\n        store.close()\n        raise\n'
            s=s[:start]+prediction+s[end:]
            start=s.index('        pred, probs, entropy, gt = predict_volume(')
            end=s.index('    return pd.DataFrame(rows)',start)
            body=s[start:end]
            call_end=body.index('corruption)')+len('corruption)')
            call=body[:call_end].replace('pred, probs, entropy, gt =','store, gt =')
            rest=body[call_end:].lstrip('\n')
            replacement=call+'\n        CASE_CACHE.clear()\n        with store:\n            pred, probs, entropy = store.pred, store.probs, store.entropy\n'+''.join('    '+line+'\n' for line in rest.splitlines())
            s=s[:start]+replacement+s[end:]
            # Keep exact original ECE voxel sampling/bin convention with bounded buffers.
            s+='\nece_score = chunked_ece\n'
            s+='\nhd95_binary = hd95_cropped_sequential\n'
            s=s.replace('for region, (p, y) in task_regions(task, pred, gt).items():',
                        'for region, (p, y) in iter_task_regions(task, pred, gt, TASK_SPECS):')
            s=s.replace('affine = nib.as_closest_canonical(nib.load(record["images"][0])).affine',
                        'affine = canonical_header(record["images"][0]).affine')
        if i==27:
            s+='\n'+(ROOT/'scripts/evaluation_case_runtime.py').read_text()
        if i==33:
            s=s.replace('"cache_revision": EVALUATION_CACHE_REVISION,','"cache_revision": EVALUATION_CACHE_REVISION,\n        "evaluation_port_id": EVALUATION_PORT_ID,')
            s=s.replace('missing_modalities=missing_modalities, corruption=corruption,','missing_modalities=missing_modalities, corruption=corruption, case_cache_key=cache_key,')
            s+='''
_EVAL_CHECKPOINT_SIGNATURES = {}
def _checkpoint_file_signature(path: Path) -> dict:
    identity=str(path.resolve())
    if identity not in _EVAL_CHECKPOINT_SIGNATURES:
        _EVAL_CHECKPOINT_SIGNATURES[identity]={"name":path.name,"size":path.stat().st_size,"sha256":sha256_file(path)}
    return _EVAL_CHECKPOINT_SIGNATURES[identity].copy()
'''
        if i==35:
            s+='\nclean_coverage_receipt = validate_clean_coverage(clean_results_df.to_dict("records"), splits, EXPERIMENTS, EVALUATION_SEEDS, TASK_SPECS)\n_atomic_json_save(clean_coverage_receipt, OUTPUT_ROOT / "results" / "clean_coverage_verified.json")\nprint("FULL CLEAN COVERAGE VERIFIED", clean_coverage_receipt["observed_rows"])\n'
        if i==51:
            s=s.replace('"automatic_evaluation": True,','"automatic_evaluation": True,\n    "evaluation_port_id": EVALUATION_PORT_ID,')
        if i>=35:
            s='if not EVALUATION_SESSION_PAUSED:\n    try:\n'+''.join('        '+line+'\n' for line in s.splitlines())+'    except SessionBudgetReached:\n        EVALUATION_SESSION_PAUSED=True\n        print("EVALUATION PAUSED: saved case metrics and RNG state retained.",flush=True)\n'
        c=cell('code',s)
    new.append(c)
new.append(cell('code','''evaluation_session={"state":"evaluation_paused" if EVALUATION_SESSION_PAUSED else "evaluation_complete",
                    "evaluation_port_id":EVALUATION_PORT_ID,"dataset_fingerprint":DATASET_FINGERPRINT,
                    "saved_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())}
_atomic_json_save(evaluation_session,OUTPUT_ROOT / "manifests" / "unigdnetr_kaggle_evaluation_session.json")
print(evaluation_session,flush=True)
'''))
for i,c in enumerate(new):
    if c['cell_type']=='code':ast.parse(''.join(c['source']),filename=f'evaluation_candidate_cell_{i}')
nb={'cells':new,'metadata':training['metadata'],'nbformat':4,'nbformat_minor':5}
target=ROOT/'notebooks/UniGDNetR_Kaggle_Evaluation_CANDIDATE.ipynb'
target.write_text(json.dumps(nb,indent=1)+'\n')
print(target)
