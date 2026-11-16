# Held-out evaluation readiness — 16 November 2026

**Status: original Stage 3 source recovered; evaluation not run. No final results.**

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
