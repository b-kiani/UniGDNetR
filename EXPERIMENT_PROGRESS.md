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
