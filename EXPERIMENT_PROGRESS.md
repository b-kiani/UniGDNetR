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
