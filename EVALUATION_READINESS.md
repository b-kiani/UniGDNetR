# Held-out evaluation readiness — 16 November 2026

## V8 prolonged visible-log gap — 23 November 2026, 10:32 Asia/Tashkent

A fresh V8 **372832419** viewer reload still shows **Running**, one active event, runtime **14,275.6 s**. The latest visible progress remains epoch **16**, **75/2,500 batches at 11,828.3 s**: a **2,447.3 s (40.8 minute)** visible-log gap, increased from the earlier 16-minute observation. No exception is shown. This is a prolonged pause in observable progress and a possible stall; failure and cause are not established. No cancellation, restart, source/input change or duplicate launch was performed. Continue checking fresh logs; later forward progress must supersede this concern. See the appended follow-up in [epoch evidence](v8_epoch15_result_20261123.json).

Epoch 15 best provisional validation macro Dice remains **0.24846**, CSV remains at **15 epochs**, and V7 remains the trusted published recovery. The latest observed working checkpoint is epoch 16 batch 0 at 11,713.0 s, not published or byte-inspected. Run 1/21, zero completed Kaggle models and no held-out results. Original protocol, local evidence and held-out gates, runtime-provenance limitations, and isolated diagnostic-candidate status remain unchanged. No unchanged software tests were rerun.


## V8 epoch 15 completed — 23 November 2026

Live **V8 372832419** logs show epoch **15** ending at **11,713.0 s**, provisional slice-validation macro Dice **0.24846**, best **0.24846**, improved=True, bad_epochs=0 (previous best **0.23968**), duration **02:53:41**, including retained prior-session training time. Epoch **16** began at **11,713.1 s**; the latest visible training log is **75/2,500 batches (3%) at 11,828.3 s**. A fresh reload showed Running at **12,800.6 s**, one active event, approximately **16 minutes** after that last log. No exception or cause was observed and a stall is not established; continue monitoring freshness without changing the job. The latest observed working checkpoint is phase train, epoch 16 **batch 0 at 11,713.0 s**, not published or byte-inspected. See [dated epoch evidence](v8_epoch15_result_20261123.json). `provisional_validation.csv` now contains 15 consecutive epochs. The epoch-15 score is rounded from live logs; full precision and task-specific scores have not been inspected.

**V7 remains the latest trusted published recovery** until terminal V8 output verification. Still run **1/21**, UniGDNetR seed 13, zero completed Kaggle models and no held-out results. Healthy V8 was left unchanged; no duplicate was launched, diagnostic candidate deployed or unchanged software tests rerun. Original protocol, separate local 21-checkpoint/execution/repair provenance gates, held-out approval and full-container/bitwise CUDA limitations remain unchanged. This section supersedes earlier epoch-15-training/epoch-14-best descriptions below.


## V8 mid-epoch recovery verified — 23 November 2026

Live **V8 372832419** completed the **6,917/6,917 source-byte audit at 1,880.9 s**, logged the unchanged content fingerprint `e8ab1ec322826bd08a468e7d17ad4fe60858b1c5f8467e770c5e5dc671394cb6` at **1,881.1 s**, and **CONTENT PROVENANCE VERIFIED** at **1,881.5 s**. All **nine fingerprint-matched indices** were reused (1,884.3–1,886.7 s); GPU preflight passed for BraTS, LiTS and ACDC (1,892.2–1,892.3 s). The accepted format-2 train header at **1,898.3 s** has epoch_index **14**, batch **162**, saved **2026-11-23T01:20:19Z**. Explicit **RESUMED inside epoch 15 at batch 162** and **MID-EPOCH RESTORE** at **1,898.3 s** confirm offsets **108 samples/task**. Completed 162 batches were not repeated. The unchanged source validates the accumulation remainder and restores saved gradients before the restore log. Together with the independently inspected V7 remainder **2** and finite pending gradients, this supports normal-path restoration; no separate tensor-level CUDA equivalence test was performed.

Training reached **epoch 15, 825/2,500 batches (33%) at 3,736.8 s**; the UI was Running at **3,805.7 s**, with one active event. The latest observed working checkpoint is phase train, epoch 15 **batch 810 at 3,712.0 s**, not published or byte-inspected. No new completed-epoch score was observed; the CSV remains at 14 epochs and best saved validation macro Dice remains **0.23967909553470332** from epoch 14. See [dated recovery evidence](recovery_milestone_v8_20261123.json).

V8 reports Python **3.13.16**, PyTorch **2.11.0+cu130**, CUDA runtime **13.0** and Tesla **T4** at 88.8 s, matching the four previously reported V5/V6/V7 fields. Full container/package identity and bitwise CUDA trajectory remain unverified. **V7 remains the latest trusted published recovery** until terminal V8 output verification. Still run **1/21**, UniGDNetR seed 13, zero completed Kaggle models and no held-out results. Healthy V8 was left unchanged; no duplicate was launched, diagnostic candidate deployed or unchanged software tests rerun. Original protocol, separate local 21-checkpoint/execution/repair provenance and held-out gates remain unchanged. This section supersedes earlier V8-startup-only/unverified descriptions below.


## V7 published recovery verified; V8 started — 23 November 2026

V7 **372675512** completed successfully after **32,592.8 s**, with a normal budget pause saved **2026-11-23T01:20:19Z** (06:20:19 Asia/Tashkent), elapsed **9.0467 hours**. Its published ZIP contains **53 files** and passes CRC validation. The CPU-loaded format-2 checkpoint preserves epoch **15, batch 162/2,500**, **54 batches and 108 consumed samples per task**, accumulation remainder **2** with finite pending gradients, and optimizer/scheduler/scaler/RNG/progress. Model, EMA, optimizer tensors and best weights are finite. Resume checkpoint: **25,162,059 bytes**, SHA-256 **c6ec38a1d3b0c93e9bbef8eb67cd1f91e67d0f4ac4432b47feb9aaebea9149ce**. Configuration/task specifications/fingerprints match V6; **46 immutable artifacts are byte-identical**, including provenance, indices, splits, repairs and audit. All 21 scientific plan rows match apart from worker identifiers. Source dataset inventory matches; only the mounted prior-notebook output size differs. Checkpoint history matches all 14 saved CSV epochs. See [verification](recovery_verification_v7.json).

Epoch **14** ended at **31,971.0 s**, provisional validation macro Dice **0.23968**, best improved=True, bad_epochs=0, duration **02:33:46**. Best saved epoch 14 score is **0.23967909553470332**. Its BraTS validation Dice remains low at **0.012796476655246008**; no cause is established. These are slice-validation results, with no held-out evaluation. `provisional_validation.csv` now has 14 consecutive epochs.

**V7 is now the latest trusted published recovery**, preserving V6/V5/V4/V2 backups and never using cancelled V3. Before continuation the live UI showed zero active events and **18:10/30 GPU hours used**. Exactly one prior notebook input was updated from V6 to V7 through the confirmed dialog. Five source inputs, T4 x2, Internet on, original editor environment selection and nine-hour operational cap were retained. Exactly one Save & Run All launched **V8 372832419**, source diff **+0/-0**. [Live V8](https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu?scriptVersionId=372832419) was Running at **43.3 s**, one active event, startup mounts visible. **V8 recovery is not yet verified**: require the 6,917-file byte audit, nine index reuses, strict checkpoint acceptance and explicit epoch-15 batch-162 resume with offsets **108 samples/task** and pending accumulation restoration. Completed 162 batches must not repeat. See [launch evidence](v8_launch_20261123.json).

Still run **1/21**, UniGDNetR seed 13, zero completed Kaggle models and no held-out results. Full-container/package identity and bitwise CUDA trajectory remain unverified; the viewer says Latest Container Image while the editor retains the original environment selection. Local 21-checkpoint/execution/repair provenance and held-out gates remain separate and unchanged. No diagnostic candidate was deployed or unchanged software tests rerun. This section supersedes older V7-active/V6-latest-published statements below.


## V7 epoch 13 completed — 23 November 2026

Live V7 **372675512** logs show epoch **13** ending at **22,743.7 s**, provisional slice-validation macro Dice **0.23598**, best **0.23598**, improved=True, bad_epochs=0 (previous best **0.22563**), logged duration **02:25:12**. Epoch **14** began at **22,743.7 s** and reached **275/2,500 batches (11%) at 23,376.0 s**; the UI was Running at 23,418.1 s with one active event. The latest observed working recovery checkpoint was epoch 14, phase train, **batch 264 at 23,352.2 s**. It is not published or independently byte-inspected. See [dated epoch evidence](v7_epoch13_result_20261123.json) and `provisional_validation.csv` (13 consecutive epochs). Full precision and task-specific epoch-13 scores have not been inspected; the reported score is rounded from live logs.

**V6 remains the latest trusted published recovery** until terminal V7 output verification. Still run **1/21**, UniGDNetR seed 13, zero completed Kaggle models and no held-out results. Healthy V7 was left unchanged; no duplicate was launched. Original protocol, separate local 21-checkpoint/execution/repair provenance gates, held-out approval and full-container/bitwise CUDA limitations remain unchanged. No diagnostic candidate was deployed or unchanged software tests rerun. This dated update supersedes earlier active epoch-13 descriptions below.


## V7 epoch 12 completed — 23 November 2026

Live V7 **372675512** logs show epoch **12** ending at **14,030.7 s**, provisional slice-validation macro Dice **0.22563**, best **0.22563**, improved=True, bad_epochs=0 (previous best **0.20937**), logged duration **02:28:07**. Epoch **13** began at **14,030.7 s** and reached **750/2,500 batches (30%) at 16,114.8 s**; the UI was Running at 16,171.9 s with one active event. The latest observed working recovery checkpoint was epoch 13, phase train, **batch 618 at 15,901.8 s**. It is not published or independently byte-inspected. See [dated epoch evidence](v7_epoch12_result_20261123.json) and `provisional_validation.csv` (12 consecutive epochs). These are rounded live-log scores; full precision and task-specific epoch-12 scores have not been inspected.

**V6 remains the latest trusted published recovery** until terminal V7 output verification. Still run **1/21**, UniGDNetR seed 13, zero completed Kaggle models and no held-out results. Healthy V7 was left unchanged; no duplicate was launched. The original protocol, separate local 21-checkpoint/execution/repair provenance gates, held-out approval and full-container/bitwise CUDA limitations remain unchanged. No diagnostic candidate was deployed or unchanged software tests rerun. This dated update supersedes earlier active epoch-12 descriptions below.


## V7 recovery verified and epoch 11 completed — 22 November 2026

V7 **372675512** completed the **6,917/6,917 source-byte audit at 1,951.0 s** and verified the unchanged content fingerprint at **1,951.3 s**. All **nine fingerprint-matched indices** were reused (1,954.4–1,957.0 s), and CUDA preflight passed for all three tasks (1,964.6–1,964.8 s). The accepted recovery header at **1,971.8 s** is format 2, train, epoch_index 10, batch 1,887, saved 2026-11-22T15:54:50Z. Explicit **RESUMED inside epoch 11 at batch 1,887** and **MID-EPOCH RESTORE** at 1,971.9 s confirm sampler offsets **1,258/task**; completed batches were not repeated. The unchanged source validates the accumulation remainder and restores saved gradients before emitting that restore log. Together with the inspected V6 remainder 3 and finite pending gradients, this supports restoration through the normal recovery path; no separate tensor-level CUDA equivalence test was performed.

Epoch **11** ended at **5,143.1 s**, provisional slice-validation macro Dice **0.20937**, best **0.20937**, improved=True, bad_epochs=0 (previous best **0.19410**), logged duration **02:40:09** including retained prior-session training time. Epoch **12** is training, **50/2,500 at 5,396.2 s**; the working checkpoint at epoch 12 batch 0 (5,143.1 s) is not yet published or byte-inspected. One active event; healthy job unchanged, no duplicate launched. See [dated recovery and epoch evidence](recovery_milestone_v7_20261122.json) and the 11-epoch `provisional_validation.csv`.

V7 reports Python 3.13.16, PyTorch 2.11.0+cu130, CUDA runtime 13.0 and Tesla T4, matching the four reported V5/V6 fields. Full container/package identity and a bitwise CUDA trajectory remain unverified. **V6 remains the latest trusted published recovery** until terminal V7 outputs are verified. Still run 1/21, UniGDNetR seed 13, zero completed Kaggle models and no held-out results. Original protocol, separate local checkpoint/execution/repair provenance gates and held-out approval remain unchanged. No diagnostic candidate was deployed or unchanged software tests rerun.


## V6 published recovery verified; V7 launched — 22 November 2026

V6 completed its session normally after **32,816.7 s**, with a budget pause saved **15:54:50 UTC** (20:54:50 Asia/Tashkent). Its published ZIP has **53 files** and passes CRC validation. The CPU-loaded format-2 checkpoint preserves epoch 11 **batch 1,887/2,500**, 629 batches and 1,258 consumed samples per task, optimizer/scheduler/scaler/RNG, and accumulation remainder **3** with finite pending gradients. Model/EMA and best-checkpoint weights are finite. Resume checkpoint: **25,170,617 bytes**, SHA-256 **6926f58ec65c1182eb2fc0581ae97642cb5260dcb5cb87261d5e89f5b15c89be**. Configuration/task specifications/fingerprints match verified V5; **46 immutable files** are byte-identical, including content provenance, splits, audit, repairs and indices. All 21 scientific plan rows match; only worker identifiers differ. Dataset inventory differs only in mounted prior-notebook output size; source dataset inventory matches. Best saved checkpoint is epoch **10**, validation macro Dice **0.19409821826586374**, training_complete=False. The checkpoint history matches the 10-row saved CSV. See [verification](recovery_verification_v6.json).

**V6 is now the latest trusted published recovery**, retaining V5/V4/V2 backups and never using cancelled V3. After the live UI showed zero active events and **09:06/30 hours used**, exactly one prior notebook input was updated from V5 to V6 via the confirmed update dialog. Five source inputs, T4 x2, Internet on, original editor environment selection, 9-hour operational cap and scientific protocol were retained. One Save & Run All launched **V7 372675512**, source diff **+0/-0**, one active event. [Live V7](https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu?scriptVersionId=372675512) shows Running and startup mounts; **V7 checkpoint recovery is not yet verified**. Require the full 6,917-file byte audit, nine index reuses, strict checkpoint acceptance and explicit epoch-11 batch-1,887 restore with pending accumulation before claiming resumed. Do not repeat completed batches or launch duplicates. See [launch evidence](v7_launch_20261122.json).

Still run 1/21, seed 13, zero completed Kaggle models and no held-out results. Epoch-10 BraTS validation Dice is **0.028906655730214784** and remains low; no cause is established. Isolated diagnostic candidates were not deployed. Local 21-checkpoint/execution/repair provenance gates, held-out approval and full-container/bitwise CUDA limitations remain unchanged. No unchanged software tests were rerun.


## V6 epoch 10 completed — 22 November 2026

Epoch 10 ended at **26,364.3 s**, provisional slice-validation macro Dice **0.19410**, best **0.19410**, improved=True, bad_epochs=0 (previous best **0.17245**). Epoch 11 started at **26,364.4 s**. The UI remains Running with one active event. A working recovery checkpoint was saved for epoch 11, phase train, batch 0; its bytes are not published or independently inspected. This remains run **1/21**, UniGDNetR seed 13, **zero completed Kaggle models and no held-out results**. V5 remains the trusted published recovery source until terminal V6 output verification.

The healthy job and original protocol were unchanged. Local 21-checkpoint/provenance gates and full-container/bitwise CUDA limitations remain in force. No unchanged software tests were rerun. See [dated epoch result](v6_epoch10_result_20261122.json) and `provisional_validation.csv` (epochs 1–10).


## V6 forward progress observed after long pause — 22 November 2026

Subsequent live logs confirm a new epoch-10 working checkpoint at **batch 147, 13,787.4 s**, then training **150/2,500 batches (6%) at 13,796.5 s**. Forward progress has resumed without intervention. This supersedes the immediately preceding possible-stall status, while preserving the observed approximately one-hour log/training gap as a historical event with unknown cause. No restart, cancellation, source edit or duplicate launch occurred. The working checkpoint is not yet published. Epoch 9 best provisional validation macro Dice remains **0.17245**; run 1/21, zero completed Kaggle models and no held-out results. See the subsequent-forward-progress field in [dated evidence](v6_epoch9_result_20261122.json).


## V6 epoch 9 result and log-freshness concern — 22 November 2026

Epoch 9 completed at **9,448.3 s**, provisional macro validation Dice **0.17245**, best **0.17245**, improved=True, bad_epochs=0 (previous best 0.15813). Epoch 10 began immediately. Latest observed training is **125/2,500 batches (5%) at 10,195.2 s**; the most recent working checkpoint was logged at epoch 10 batch 99 at 10,159.6 s. These working files have not been published or independently inspected. The new row in `provisional_validation.csv` is internal slice-validation evidence, not a volumetric held-out score or completed model.

**Possible training or log-delivery stall:** after a fresh reload the UI still reports Running with one active event, but its runtime counter **13,640.3 s** is **3,445.1 s (about 57 minutes)** beyond the latest available log entry. There is no logged exception or confirmed cause. A running badge alone does not establish healthy forward progress; neither does the log gap by itself prove process failure. Preserve the job and monitor for renewed logs or terminal evidence; do not cancel/restart or create duplicate jobs based on an unconfirmed cause. No job was modified.

See [dated result and freshness evidence](v6_epoch9_result_20261122.json) and [live logs](https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu/log?scriptVersionId=372483892). Still run 1/21, zero completed Kaggle models and no held-out results. V5 remains the trusted published recovery source. Local checkpoint/provenance gates and the recorded full-container/bitwise runtime limitations remain in force.


## V6 epoch 9 training finished; validation underway — 22 November 2026

Live V6 logs record epoch 9 training completion and a working pre-validation checkpoint at **6,485.6 s** (phase validation, batch 0). Validation reached **500/567 batches (88.2%) at 8,306.7 s**. No epoch-9 score is available at this observation. The job remains running and unchanged, run 1/21, seed 13. This is phase progress, not model completion or published checkpoint verification. V5 remains the trusted published recovery source; no held-out results exist.

A fresh read of archived V5 logs (103.7 s) and V6 logs (92.4 s) establishes matching reported **Python 3.13.16, PyTorch 2.11.0+cu130, CUDA runtime 13.0 and Tesla T4**. This narrows the editor/viewer environment discrepancy to an unresolved full-container identity question; it does not establish complete package/image equivalence or a bitwise CUDA trajectory. Earlier unverified-runtime statements are refined by this four-field comparison, not erased. See [dated evidence](v6_epoch9_validation_20261122.json). Local checkpoint/provenance and evaluator approval gates remain unchanged.


## Verified V6 mid-epoch recovery — 22 November 2026

V6 **372483892 is RUNNING**, with recovery verified from live logs. Full source byte audit reached **6,917/6,917 at 2,155.7 s**; content provenance was verified at 2,156.1 s with unchanged fingerprint `e8ab1ec322826bd08a468e7d17ad4fe60858b1c5f8467e770c5e5dc671394cb6`. All nine fingerprint-matched indices were reused. CUDA preflight passed for BraTS, LiTS and ACDC. At **2,175.4 s** the checkpoint header was accepted (format 2, train, epoch_index 8, batch 480, saved 2026-11-16T22:56:43Z), followed by explicit `RESUMED ... inside epoch 9 at batch 480; completed samples will not be reloaded` and sampler-offset restoration (320 per task). This verifies live recovery without repeating the saved 480 batches.

Latest observed training: **epoch 9, 1,750/2,500 batches (70%) at 4,855.5 s**. A working checkpoint was logged at batch **1,518**, 4,430.8 s; it is not yet published or independently inspected. **No new epoch score, completed Kaggle model or held-out result.** V5 remains the trusted published recovery source until V6 ends and its outputs are verified. Healthy V6 was left unchanged; no duplicate job was launched.

Actual runtime logs show **Python 3.13.16, PyTorch 2.11.0+cu130, CUDA runtime 13.0, Tesla T4**. The viewer says Latest Container Image; this records actual runtime facts, not proof of equivalence to the historical environment or bitwise CUDA trajectory. The prior editor-pin discrepancy remains a provenance limitation pending historical comparison. See [live logs](https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu/log?scriptVersionId=372483892) and [structured milestone](recovery_milestone_v6_20261122.json). Local checkpoint verification and all held-out gates remain unchanged; the isolated diagnostic candidate is not deployed to this run.


## Latest gate update — 22 November 2026

Kaggle training continuation V6 **372483892** is authorized and submitted, last observed queued; this does not authorize held-out evaluation. No checkpoint recovery is claimed until the V5 byte audit, nine index reuses, strict acceptance and epoch-9/batch-480 resume are logged. Preserve the active job. All checkpoint, CUDA/MC/RNG, real-volume memory/disk, calibration, scenario and cohort coverage gates remain in force. The actual runtime environment still needs verification.

The opt-in training diagnostic candidate passed three synthetic CPU tests, remains outside the baseline notebook, and provides no evidence of improved held-out performance. Its explicit-FP16 overflow fixture must not be attributed to actual CUDA autocast or the low local BraTS results. See [validation review](VALIDATION_IMPROVEMENT_REVIEW_20261122.md). All 21 supplied local histories are already inspected; next evidence is actual checkpoint inspection and execution/repair provenance or a separately saved fresh pairing audit. Keep the older audit and separate cohort coverage.


**Status: candidate passed local synthetic CPU checks; held-out evaluation has not run. CUDA/real-cohort approval remains pending.**

The saved `03_UniGDNetR_EVALUATE(2).ipynb` was located and read in full from the user's existing files on 16 November. The recovered source is stored as `notebooks/03_UniGDNetR_EVALUATE_original.ipynb` in the source archive and as a convenient repository-root copy. It is the existing Stage 3 source, not a newly invented replacement. The earlier missing-file blocker is resolved. This does not establish compatibility with the Kaggle RAM-fixed training port.

## Source provenance

- Original filename: `03_UniGDNetR_EVALUATE(2).ipynb`.
- Saved file version: 2, last modified 25 October 2026.
- Recovered text bytes: 182,571; SHA-256: `d34591cd0da8d65fff1da459f54dc47a95ab4e773af5fd8f231a3e2f6e3298f9`.
- All code cells parse. There are no saved output cells; no historical metric values are imported.
- Architecture and loss/metric cells 21 and 23 match the supplied RAM-fixed Stage 2 source exactly. Data/cache cell 17 and training/checkpoint cell 25 differ and require explicit adaptation review.
- Source pipeline revision: `2026-10-25-brats-schema-rc-longitudinal-v7`.

## Mandatory gates before execution

1. Preserve the healthy training job. Require all seven variants × seeds 13/37/71 to have compatible `training_complete=True` best-validation checkpoints. The source requires all checkpoints; keep that gate. A session pause is not a completed model.
2. Copy the latest verified published output into a separate evaluation working directory. Keep immutable source version pins, source content hashes, repair digests, full patient splits, configuration and pipeline checks. Verify expected checkpoint SHA-256 values and record the selected epoch and validation score. Never choose a checkpoint using test metrics.
3. Port source discovery and preparation to the existing Kaggle mounts, verified repairs and stable content identity. Reuse the prepared nine indices; never regenerate patient splits. The evaluator currently uses Windows paths and a legacy stat-based fingerprint. Do not run it unchanged on Kaggle or disable its guards to make it pass.
4. Carry forward the bounded Stage 2 cache implementation after reviewing code differences. The evaluator has an older six-case cache. Full-volume probability/entropy arrays and distance-transform buffers can also be large, especially for LiTS; implement and test bounded-memory inference/storage without changing predictions or the metrics. Compare any streaming implementation against the original on small synthetic volumes.
5. Test geometry/orientation, label schema, task heads, foreground regions, boundary slices, spacing in millimetres, MC dropout, calibration, missing-modality masking and corruption reproducibility. Confirm zero overlap among train/validation/test patient groups and exact expected case/region rows.
6. Produce an explicit adaptation diff and execution provenance. The recovered original supplies the protocol, but the Kaggle adaptation still needs numerical and live validation. Do not label an untested port as equivalent.

## Existing source protocol to preserve and audit

- Full volumetric inference reassembles every slice at original in-plane resolution. Clean evaluation covers every held-out scan: BraTS 187 scans/170 patients, LiTS 20 scans/20 patients, ACDC 30 frames/15 patients, as established by current splits. These are internal patient-held-out sets, not official challenge test-set scores.
- Temperature is fitted on validation pixels only (up to 80 validation batches per task), then frozen for test evaluation. Record calibration seed and fitted temperature. Full mode configures eight MC dropout samples. Keep calibrated and raw outputs clearly distinguished where both are reported.
- Record case/task/region/seed Dice, IoU, sensitivity, precision, HD95, ECE and entropy, along with predicted and ground-truth voxel counts. Preserve modern BraTS NETC=1, SNFH=2, ET=3, RC=4; the existing WT/TC unions exclude RC, and this convention must be stated.
- Original binary metric conventions: both-empty Dice/IoU are NaN; one-empty Dice is zero; sensitivity is NaN when ground truth is empty; precision is NaN when prediction is empty. HD95 is NaN if either mask is empty. Report eligible/excluded counts and one-empty failures explicitly so means do not hide failures. Do not silently convert NaN to perfect scores or fabricate RC examples.
- The source includes missing-MRI and controlled acquisition-corruption evaluations. Preserve scenarios, severities, checkpoint-specific cache identity and deterministic seeds; audit exact cohort coverage for every scenario.
- Statistical code averages longitudinal sessions and repeated seeds within patient before patient-bootstrap confidence intervals (10,000 resamples), paired Wilcoxon tests and Holm adjustment. Also retain separate per-seed summaries and SD; do not mistake the patient-averaged CI for variability across independent training seeds.
- Verify each claimed output actually exists. Markdown mentions risk–coverage and uncertainty/error analyses; do not infer implementation or completion from that description. Optional nnU-Net export is not a trained baseline and is outside the existing 21-run completion count. Report it as unperformed unless independently executed and validated.

## Deliverables required for final status

- 21-checkpoint completion and compatibility inventory, selection provenance and Kaggle checkpoint links.
- Exact held-out coverage and split-overlap audit; case/region/seed tables with denominators and absence conventions.
- Seed summaries, patient-level confidence intervals, paired comparisons, robustness/calibration outputs and validated learning curves.
- Reproducible source/environment/content provenance, hashes, adaptation notes and final report with limitations.
- Small derived reports in GitHub; raw volumes, full voxel predictions, checkpoints, credentials and lock files remain outside GitHub.

A final evaluation completion marker alone is insufficient: independently check the expected matrix and coverage before publication. All training, held-out evaluation and report consistency gates must pass before describing the study as finalized.

## Evaluation candidate prepared — local validation only

`UniGDNetR_Kaggle_Evaluation_CANDIDATE.ipynb` and `scripts/build_evaluation_candidate.py` reuse the current Kaggle preparation, bounded Stage2 cache, architecture and checkpoint metadata guards. All21 completed compatible checkpoints remain required. The candidate refuses execution by default; approval must follow the remaining validation, not merely setting an environment variable. The active training notebook has not been changed.

`evaluation_buffers.py` stores prediction probabilities, entropy and labels in temporary memory-mapped files instead of full-volume Python lists plus stacked copies. It verifies every slice was written once and cleans up temporary files. Chunked ECE preserves the original seed13 voxel sample and bin convention; floating-point summation order can differ slightly.

Six local tests passed with NumPy/SciPy/NIfTI fixtures: disk buffers exactly match original stacked probabilities/entropy/argmax labels; ECE agrees within 1e-6 with and without250,000-voxel sampling; invalid/incomplete/duplicate batches are rejected; code parses and unapproved execution is refused; the RAM-fixed loader matches original orientation/resampling and CT normalisation within1e-7; original absent-class and anisotropic HD95 conventions are preserved. Tests initially needed missing fixture globals, which were supplied before the passing run.

**Still pending:** neural inference equivalence on a PyTorch-enabled runtime (PyTorch is absent from this local runtime); high-volume distance-transform/region-mask memory profiling and disk capacity checks; deterministic MC-dropout/scenario testing; complete case/region/seed coverage checks; efficient per-case/session recovery for long evaluation jobs; and a live Kaggle preflight after all21 models finish. The candidate is not approved and no held-out evaluation has run. The existing completion marker cannot substitute for these checks.

## Coverage and case recovery candidate — additional local checks

The candidate now checks patient separation across all three splits and the exact clean evaluation matrix: experiment × seed × selected task × held-out case/patient × required region. Current cohort sizes imply **18,780 expected clean region-level rows**. This is an expected count, not measured test output. Missing/extra/duplicate rows, unknown patients/seeds, mixed scenarios, invalid metric ranges and wrong absent-class conventions block completion. A coverage receipt is saved only after successful validation.

Prediction buffers check free disk capacity before allocation, including20% plus64MiB reserve. This does not establish that large-volume distance-transform RAM use is safe.

Per-case metrics and post-case RNG state are saved atomically with a content checksum and a verified pre-case RNG chain. The checkpoint signature uses name/size/SHA-256 rather than mount path/mtime; cache identity also includes the evaluation source digest and scenario. This deliberately revises the source's volatile cache-key seed derivation. Equivalence must be checked against an uninterrupted execution using the same stable job identity; historical stat-key random draws are not asserted identical. Python/NumPy interruption recovery matches uninterrupted draws exactly in a simulation. Actual PyTorch/CUDA state and MC-dropout equivalence remain unverified.

Session budget checks run before each case. A budget pause skips downstream analyses/final completion and records `evaluation_paused`; copied old completion markers are removed from writable output at startup, while the immutable source is preserved. The source training-complete marker is retained, so a later evaluation session can attach the prior evaluation output. Full live evaluation-resume behavior remains to be checked on Kaggle after training.

**15 evaluation tests and one report-export integration test pass locally.** Additional tests cover full-matrix expectations, patient leakage, invalid/partial results, absent-class counts, insufficient disk, interrupted RNG recovery, corrupted cache rejection, stable checkpoint identity and preventing final completion on pause. Runtime case/RNG caches and repeated job caches are excluded from report export. No GPU job was launched or changed. The approval gate remains closed. Remaining work includes GPU/neural/MC equivalence, large-volume HD95/region memory profiling and a live paused/resumed evaluation preflight; the candidate must not be approved merely because these local tests pass.

## Local neural equivalence and memory profile — 16 November 2026

The prior lack of local PyTorch is resolved. An isolated CPU-only installation from the official PyTorch wheel index was pinned to **2.11.0+cpu**, matching the training framework's2.11 release but not its CUDA device/runtime. Active Kaggle training and its environment were not changed.

**21 local evaluation tests passed, with zero failures/errors/skips.** `local_evaluation_test_report.json` records the environment and tested notebook/source hashes. The actual UniGDNetR architecture (base24, embedding48, dropout0.1) was compared against the recovered original inference code on synthetic19×23×5 volumes resized to32×32. Twenty comparisons covered all three task heads; clean MC1/MC8; Gaussian noise, blur, resolution and gamma atMC2; and BraTS single-missing/single-available MRI atMC8. Probabilities, entropy, argmax labels and CPU Torch RNG states matched exactly. A separate CPU dropout test preserved the exact interrupted/resumed random stream. These small synthetic CPU checks do not establish full-size CUDA or real-cohort equivalence.

The HD95 candidate retains the original definition and NaN convention. It crops to the joint foreground bounding box with a one-voxel halo and computes the two directed distance fields sequentially. Random sparse/dense, boundary-touching, hole, singleton and anisotropic fixtures matched the original exactly. Instrumentation confirmed only one distance field is retained. Foreground regions are yielded individually; cached image volumes are released before metric calculation; affine spacing uses the verified header-only canonical geometry.

`synthetic_evaluation_memory_profile.json` records fresh-process local CPU profiles on192×192×128 synthetic masks (NumPy2.3.5, SciPy1.17.0):

| Synthetic foreground | Original process peak RSS (MiB) | Candidate process peak RSS (MiB) | HD95 match |
| --- | ---: | ---: | --- |
| Compact | 330.21 | 54.45 | Exact |
| Broad | 332.72 | 287.58 | Exact |

These are whole-process synthetic peaks, not GPU VRAM or real LiTS memory guarantees. CUDA/MC equivalence and RNG recovery, largest real-volume memory/disk validation, calibration and full scenario/coverage audits, and a live paused/resumed Kaggle evaluation preflight remain mandatory. All21 compatible completed models are still required before held-out execution. The approval gate remains closed. Earlier missing-PyTorch and untested-CPU statements describe the prior state.


## Local PC evidence gate — 18 November 2026

The uploaded local `logs.zip` contains the 21 expected histories and 760 sequential epoch rows. All numeric fields are finite; stopping is consistent with the 40-epoch cap or patience 10. See `local_training_history_review_20261118.json` for checks and per-run validation summaries. This is stronger evidence of local training progression than completion JSON alone, but checkpoint bytes, selected checkpoint metadata, historical inputs and execution remain unverified. BraTS slice-validation Dice is very low and needs investigation using training/validation evidence. The stale-or-inconsistent duplicated-T2f pairing audit remains unresolved. Current notebook source rejects duplicates and resamples grids; source inspection does not prove what previously executed.

Hold redundant Kaggle training and held-out evaluation approval while reconciling the local set. Recompute exact patient/case/task/class/seed/scenario coverage from the local cohorts; do not reuse the Kaggle 18,780-row target. Existing evaluator software checks and pending CUDA/real-volume/RNG/calibration/recovery gates remain in force. New raw volumes, voxel predictions, checkpoint weights and runtime RNG must not enter GitHub.
