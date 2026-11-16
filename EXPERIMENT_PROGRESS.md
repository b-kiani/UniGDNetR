# UniGDNetR experiment progress — 16 November 2026

**Status: INCOMPLETE. These are provisional validation results, not final test results.**

## Saved session 2

Kaggle Version 2 (369935019) ended successfully after 36,062 seconds. The experiment paused at its ten-hour budget; session state was saved at 2026-11-16 01:17:19 UTC (06:17:19 Asia/Tashkent).

- Dataset integrity audit passed: 1,582 scan records and 5,335 image-mask combinations.
- Corrected preparation completed and GPU preflight passed for all three tasks.
- Run 1/21: UniGDNetR, seed 13. Epochs 1 and 2 completed.
- Epoch 3 completed 2,500 training batches. Validation last logged 500/567 batches (88.2%) before the budget pause.
- Saved recovery status: epoch 3/40, phase validation, batch 0. Validation restarts from its beginning; completed epoch-3 training is retained.
- Published output confirmed: UniGDNetR_seed13_resume.pt (20.14 MB), UniGDNetR_seed13_resume_status.json (348 B), and UniGDNetR_seed13.pt.

| Epoch | Validation macro Dice | Meaning |
| --- | --- | --- |
| 1 | 0.03487 | Internal validation only |
| 2 | 0.04724 | Internal validation only; best so far |

No epoch-3 score is reported because validation was incomplete. Zero of the 21 planned training runs have been verified complete. No final held-out evaluation has been completed.

## Continuation

Version 3 (370097607), named “Resume V2 checkpoint - epoch 3 validation”, was submitted with exactly one prior notebook output attached, the same five source datasets, GPU T4 x2, Internet enabled and the original pinned environment. Its live logs confirm running, mounting all five datasets, restoring the previous output at 72.8 seconds, and verifying all 15 repair files. CUDA is active. At 191.5 seconds, the new dataset fingerprint was `2b915d23dfe11c20fca2947abc78a66685bbfcb923402edb15f6a99d0e2db50d`, differing from Version 2 (`1547fb5aa79b786d8eabc7fed86ee4cbbedc3e1d0be7f3c19f348a0ec6ebf3cb`). The run requested index rebuilding. Version 3 was cancelled during preparation to avoid spending GPU quota on a continuation that had not verified checkpoint compatibility. No successful resume or new training is claimed. Version 2 remains the recovery source.

The current fingerprint includes absolute paths, byte sizes and nanosecond modification times. File timestamp changes after Kaggle output restoration are a possible cause; the cause has not yet been isolated. Do not overwrite the saved fingerprint or bypass compatibility checks. A safe recovery correction must establish identical immutable source versions, patient splits and repair contents, preserve the original checkpoint, and record any explicit fingerprint migration. Add persistent content-based provenance for future sessions.

- [Version 2 output](https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu/output?scriptVersionId=369935019)
- [Version 3](https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu?scriptVersionId=370097607)

The study retains seven variants, seeds 13/37/71, maximum 40 epochs per run, original early stopping and patient-grouped splits. No training settings were shortened to fit quota. Checkpoints and raw medical images stay in Kaggle; this repository contains code, provenance and small aggregate reports only.

## Finalization requirements

1. Continue only from the latest successfully saved compatible output, with no concurrent duplicate job.
2. Verify all 21 completion records and the best validation-selected checkpoint for each run.
3. Run a documented held-out evaluation across all test patients, keeping test data out of model selection. The original Stage 3 notebook was not supplied; its protocol/code remains an outstanding dependency. A replacement must be explicitly documented as a new implementation, not represented as the original pipeline.
4. Export case/task/class metrics, seed-level summaries, aggregate tables, learning curves and figures, plus configuration, split and source provenance. Document absent classes and metric conventions.
5. Verify checkpoint compatibility, cohort completeness and report consistency. Label validation and held-out results separately.
6. Publish the final report and small derived results in this repository only after the required checks pass. Include Kaggle output links for checkpoints and an explicit limitations section.

There is no reliable overall completion date yet. Further sessions and available GPU quota are required.

## Recovery correction prepared

A content-based recovery correction has passed local tests and exact comparison of all training Config values against the V2 preparation marker. Full V2/V3 output archive comparison found only fingerprint, inventory and session-state JSON changed; all other saved files are byte-identical. The generated notebook will hash current source content, verify the 41 anchored V2 artifacts, require unchanged splits/repairs/geometry/configuration and record a narrowly scoped legacy migration without rewriting checkpoint bytes. The immutable input version pins are documented in `RECOVERY_NOTES.md`. Live Kaggle recovery has not yet been verified. No additional training or final results are claimed.

## Version 4 — live recovery verification

[Version 4](https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu?scriptVersionId=370110745), “V2 recovery with verified content provenance”, is running on GPU T4 x2. Only one active event was visible. The five source dataset snapshots were explicitly pinned to the exact V2 numbered versions (BraTS v1/v1, LiTS v5/v2, ACDC v2).

Live logs verified the exact 41 original V2 recovery artifacts at 63.4 seconds, all 15 repaired files, and the integrity audit of 1,582 records/5,335 image-mask combinations at 148.4 seconds. At 237.5 seconds, the new source content audit reached **400/6,917 files (5.8%)**. It is reading actual bytes, not rebuilding slice indices. The full checksum audit, explicit migration and checkpoint acceptance are still pending; **training resume has not yet been verified**.

Last verified log observation: 16 November 2026 around 03:31 UTC (08:31 Asia/Tashkent). Original V2 checkpoints remain preserved. Zero training runs and no final held-out evaluation are complete. The ten-hour session budget is a checkpoint pause limit, not a study completion estimate.

## Version 4 — checkpoint recovery verified

On 16 November 2026 around 04:07 UTC (09:07 Asia/Tashkent), Version 4 remained running with one active Kaggle event. Live logs establish the following milestones:

- 1,848.1 seconds: full SHA-256 source audit completed, **6,917/6,917 files (100%)**.
- 1,852.1 seconds: explicit V2 content migration and persistent provenance verified; original checkpoint bytes retained. New content fingerprint: `e8ab1ec322826bd08a468e7d17ad4fe60858b1c5f8467e770c5e5dc671394cb6`.
- Preparation verified with all nine fingerprint-matched cached indices reused; no slice-index rebuild.
- GPU preflight passed for all three tasks.
- 1,871.9 seconds: recovery header accepted (format 2, validation, epoch index 2, batch 0); log explicitly reports `RESUMED UniGDNetR/seed13 after training epoch 3; training will not repeat and validation will restart.`
- Latest observed progress: **run 1/21, UniGDNetR seed 13, epoch 3/40, validation 250/567 (44.1%)**, at session second 2,272.6. This validates recovery; it is not completion of epoch 3 or a trained model.

No job was restarted, cancelled, edited or duplicated during this check. No new epoch score or final held-out metric is claimed. Original V2 output remains the trusted published recovery source until Version 4 ends and its saved checkpoints, status and provenance are verified. The study remains **0/21 completed training runs**. There is no supported full-study finish estimate; task-dependent validation throughput varies substantially.

## Finalization preparation — original Stage 3 recovered

The existing `03_UniGDNetR_EVALUATE(2).ipynb` was found and read in full on 16 November 2026. The earlier missing-evaluator dependency is resolved. `EVALUATION_READINESS.md` records its provenance, checked source structure, numerical conventions and remaining Kaggle adaptation/memory/coverage gates. All code cells parse, with no stored outputs; this is not a successful evaluation. Current live Version 4 remains on run 1/21, UniGDNetR seed13, epoch3 validation; latest observed 525/567 batches (92.6%), session second3916.1. No additional GPU job was started. All21 completed models and validated held-out results remain required.

## Version 4 — epoch 3 complete, epoch 4 training

On 16 November 2026, the live log at session second4,545.3 completed epoch3 with provisional validation macro Dice **0.10908**, improved best0.10908 and bad_epochs0. Epoch4 then started. Latest observed training heartbeat: **100/2,500 batches (4.0%)**, session second5,244.8. A recovery checkpoint was saved at second5,244.6, phase train, epoch4, batch99, reason time interval. This is a logged working-directory save; published output remains pending until the session ends. V2 remains the preserved trusted published recovery source.

This is still run1/21 (UniGDNetR, seed13), with **0/21 completed models** and no held-out evaluation. `provisional_validation.csv` now includes the rounded live epoch3 validation value. No full-study finish estimate is supported by the current variable throughput.

A guarded Kaggle evaluation **candidate**, not an approved production evaluator, has been generated from the recovered Stage3 source and current RAM-fixed Kaggle preparation. Six local tests passed: exact prediction buffer equivalence/cleanup, sampled and unsampled ECE agreement, invalid/incomplete buffer rejection, execution-gate rejection/code parsing, synthetic orientation/resampling/normalisation equivalence, and unchanged absent-class/HD95 spacing conventions. See `EVALUATION_READINESS.md` for remaining gates. No additional Kaggle job was created and the active training source was not edited.

## Progress check and evaluation preparation — 2026-11-16T05:43:42+00:00

Version4 remained running on run1/21, UniGDNetR seed13, epoch4. Latest observed training heartbeat: **750/2,500 batches (30.0%)**, session second8,112.5; a working recovery checkpoint was logged at second7,717.6, epoch4 batch681. No failure was observed. The published recovery source remains V2 until V4 ends and its output is verified. Still0/21 completed models and no final held-out results. No training edit, restart, cancellation or duplicate job occurred.

The blocked evaluation candidate now adds exact held-out matrix/absence checks, patient leakage rejection, disk reservation, per-case metric/RNG recovery, stable checkpoint-content cache identity and pause-safe completion markers. Fifteen evaluation tests plus one export integration test pass locally. These are synthetic/local software checks, not medical test results. PyTorch/CUDA and live recovery/memory validation remain pending; see EVALUATION_READINESS.md.

## Local CPU evaluation validation — 2026-11-16T06:39:53+00:00

The live Version4 job remained on run1/21, UniGDNetR seed13, epoch4. Latest observed heartbeat: **1,775/2,500 training batches (71%)**, session second11,395.7. A working recovery checkpoint was logged at second10,227.5, epoch4 batch1,317. No training edit, restart, cancellation or extra Kaggle job occurred. Still0/21 completed models, no held-out evaluation and no reliable full-study finish estimate.

The evaluation candidate passed **21 local software tests** on PyTorch2.11 CPU; these are not21 trained models. Actual-model synthetic volume predictions match the recovered original across20 task/MC/corruption/missing-MRI comparisons, and CPU dropout/RNG recovery matches uninterrupted execution. HD95 and region memory reductions were checked against the original and profiled on synthetic CPU masks. Details and remaining CUDA/real-volume/live-session gates are in EVALUATION_READINESS.md and the two small validation/profile JSON reports. The candidate remains blocked from held-out execution.

## Version 4 — epoch 4 completed, epoch 5 training — 16 November 2026, 08:14 UTC

Live signed-in Kaggle logs confirmed **run 1/21, UniGDNetR seed 13** completed epoch 4 at session second **15,727.6**. Provisional validation macro Dice is **0.12009**, improved best 0.12009, bad_epochs 0 (epoch 3: 0.10908). The log reports 03:06:21 for epoch 4; this single-epoch measurement is not a reliable estimate for the full study.

Epoch 5 training reached **475/2,500 batches (19%)** at session second **17,151.7**. A recovery checkpoint was logged at second **16,936.5**, phase train, epoch 5, batch 366. These saves are in the active working directory, not yet verified published outputs. Version 4 remains active and unchanged; V2 remains the trusted published recovery source pending V4 output verification. No restart, cancellation, edit or duplicate job occurred.

Still **0/21 completed models** and **no held-out results**. The rounded epoch 4 value is added to `provisional_validation.csv`; it is not a final test metric. Evaluation readiness remains as recorded in `EVALUATION_READINESS.md`: 21 local CPU software tests passed, but CUDA/real-volume/calibration/scenario and live recovery gates remain unresolved. No unchanged checks were rerun and no evaluation job was launched.

## Version 4 — epoch 5 completed, epoch 6 training — 2026-11-16T12:28:41Z

Signed-in live Kaggle logs confirm run **1/21, UniGDNetR seed 13** completed epoch 5 at session second **27,753.0**. Provisional validation macro Dice **0.13780** improved the best score (epoch 4: 0.12009), with bad_epochs 0. The epoch took 03:20:24 according to the log; this is a measured epoch duration, not a finish estimate for all models.

Epoch 6 training reached **1,475/2,500 batches (59%)** at second **32,338.0**. A working recovery checkpoint was logged at second **32,280.6**, epoch 6, phase train, batch **1,434**. The session is still running, around nine hours elapsed. A pause near the ten-hour budget is expected, but has not occurred or been verified. V2 remains the trusted published recovery output until V4 ends and its published checkpoints, recovery status, migration receipt and content provenance are verified. No healthy job was edited, cancelled, restarted or duplicated.

Still **0/21 completed models**, no held-out results, and no supported full-study finish estimate. The CSV contains rounded provisional validation scores only. Evaluation remains blocked pending the documented CUDA, real-volume, calibration/scenario and live pause/resume gates; the 21 passing local tests do not count as completed models.
