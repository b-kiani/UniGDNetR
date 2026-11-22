# Held-out evaluation readiness — 16 November 2026

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
