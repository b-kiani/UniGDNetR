# UniGDNetR experiment progress — 16 November 2026

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


## Latest status — 22 November 2026: Kaggle continuation submitted

The user's new request authorizes Kaggle continuation and validation-based improvement work, superseding the earlier blanket launch hold. Fresh editor observations showed zero active events and renewed free GPU quota (00:00 / 30 hours). Exactly one prior notebook input was updated from V4 to V5; five source datasets were preserved. V6 **372483892** was submitted once with **+0/-0 source diff**, original protocol and nine-hour session cap. The live viewer showed **Queued**, one active event. Recovery is NOT yet verified: require the complete byte audit, nine index reuses, strict acceptance and explicit epoch-9/batch-480 resume. V5 remains the trusted published recovery source. Runtime environment equivalence remains unresolved (original editor pin versus queued viewer Latest Container Image).

A separate FP32-loss/per-class diagnostic candidate passed three synthetic CPU checks. It is not deployed to V6 and establishes no real-data performance gain or cause for the low local BraTS scores. See [the dated review](VALIDATION_IMPROVEMENT_REVIEW_20261122.md) and [test record](training_diagnostics_validation_20261122.json). The actual 21 local checkpoint inspections and execution/pairing provenance remain outstanding; supplied logs and notebook are already inspected. Held-out approval remains closed. Local and Kaggle cohort provenance remain distinct.


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

## Access and published recovery verified — 2026-11-16T13:53:12.063035+00:00

Kaggle and GitHub signed-in browser access worked. **V4 completed its session successfully after 36,029.6 seconds** and paused normally at **2026-11-16T13:27:02Z (18:27:02 Asia/Tashkent)**. Epoch 6 training completed 2,500/2,500 batches; validation last reached 300/567 (52.9%). This is a session pause, not a completed model.

The published output ZIP contains 53 files and passed archive integrity verification. The 20,143,417-byte recovery checkpoint loads with finite model/EMA tensors, expected optimizer/scheduler/scaler/RNG and pending training state, and history epochs 1–5. Its recovery status is epoch 6, phase validation, batch 0, saved 13:12:33Z; validation restarts while epoch-6 training is retained. The content manifest contains 6,917 hashed source entries; the explicit migration receipt, original anchored splits/repairs/pairing audit were verified. See `recovery_verification_v4.json` for hashes and checks. **V4 is the latest trusted published recovery output**; preserve V2 as historical backup and never recover from cancelled V3. Checkpoints stay in Kaggle.

A single new **Version 5 (370300234)** was started: https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu?scriptVersionId=370300234 . Kaggle confirmed the single notebook input update from version 2 to 4. Five dataset inputs, original pinned environment and Internet remained unchanged; GPU T4 x2 is selected and one active event was visible. Quota displayed 20:41/30 hours used, so the only code change (+1/-1 in saved-version diff) sets the operational session default to **9 hours** instead of 10, leaving time to publish before free quota exhaustion. All scientific training settings, 21-run plan and guards remain unchanged.

V5 mounted the five sources and began preparation; full content rehash, cached index reuse and strict checkpoint acceptance must be observed before claiming training resumed. No duplicate job was started. Still **0/21 completed models** and no final held-out results. Evaluation approval remains closed pending its documented gates.

## Version 5 — live checkpoint recovery verified — 2026-11-16T14:53:38Z

Live signed-in logs for **Version 5 (370300234)** establish successful continuation from the verified V4 output:

- 2,341.6 seconds: full content hash audit **6,917/6,917 (100%)**.
- 2,341.8–2,342.0 seconds: unchanged content fingerprint `e8ab1ec322826bd08a468e7d17ad4fe60858b1c5f8467e770c5e5dc671394cb6`, content provenance and preparation verified.
- 2,344.6–2,346.7 seconds: all **nine fingerprint-matched slice indices reused**.
- 2,354.5–2,354.7 seconds: GPU preflight passed for BraTS, LiTS and ACDC.
- 2,360.9 seconds: strict recovery header accepted, format 2, phase validation, epoch_index 5, batch 0, saved 2026-11-16T13:12:33Z. The log explicitly reports **RESUMED UniGDNetR/seed13 after training epoch 6; training will not repeat and validation will restart.**

Latest observed: **run 1/21, UniGDNetR seed 13, epoch 6 validation 325/567 (57.3%)**, second 3,546.6. V5 remains running; its operational session cap is 9 hours. V4 remains the latest trusted published output until V5 ends and publication is independently verified. No active job was changed or duplicated during this check. There is no new completed epoch score, completed model or held-out result: **0/21 completed models**, no reliable full-study finish estimate. Evaluation remains blocked pending the documented remaining gates.


## Version 5 — epoch 6 completed, epoch 7 training — 2026-11-16T15:47:32Z

Signed-in Kaggle logs confirm **Version 5 (370300234) remains running**, run **1/21, UniGDNetR seed 13**. Epoch 6 validation completed **567/567 batches** at session second **5,814.6**. At second **5,814.8**, the log reports provisional validation macro Dice **0.13447**, best **0.13780** (epoch 5), improved False and bad_epochs 1. The reported epoch duration is 03:00:47; it spans resumed work and is not an estimate for the full study. Epoch-6 training was preserved from V4 and was not repeated.

Epoch 7 began normally and reached **225/2,500 training batches (9%)** at second **6,981.9**. Working recovery saves were logged at second 5,814.8 (epoch 7, phase train, batch 0, epoch completed) and **6,421.9** (epoch 7, phase train, batch **99**, time interval). These are active working-directory saves; published V5 output has not yet been verified. **V4 remains the latest trusted published recovery source.** No healthy job was edited, cancelled, restarted or duplicated. Kaggle and GitHub access both worked during this check.

Still **0/21 completed models** and **no held-out results**. The CSV now includes the rounded provisional epoch-6 validation score, not a test metric. No reliable full-study finish estimate is available. Evaluation remains blocked by the documented CUDA/real-volume/calibration/scenario and live recovery gates in EVALUATION_READINESS.md. No unchanged local tests were rerun and no evaluation or duplicate GPU job was launched.


## Version 5 — epoch 7 improved, epoch 8 training — 2026-11-17 00:39 Asia/Tashkent

Live signed-in Kaggle logs confirm **Version 5 (370300234) remains running**, run **1/21, UniGDNetR seed 13**. Epoch 7 completed at session second **18,168.0**, with provisional validation macro Dice **0.14660**, improved best **0.14660**, bad_epochs **0**. The preceding best was 0.13780 at epoch 5; epoch 6 was 0.13447. The log reports epoch-7 duration **03:25:52**. This is measured epoch throughput, not a reliable full-study finish estimate.

Epoch 8 training reached **825/2,500 batches (33%)** at second **20,692.5**. A working recovery checkpoint was logged at second **20,613.2**, phase train, epoch 8, batch **795**, reason time interval. V5 was running for 20,895.6 seconds when observed. These active working-directory saves are not yet independently verified published output. **V4 remains the latest trusted published recovery source**, with V2 preserved as historical backup. The healthy job was not edited, cancelled, restarted or duplicated.

Still **0/21 completed models** and **no held-out results**. The CSV now includes the rounded epoch-7 provisional validation score. Kaggle logs and GitHub reports were accessible. Evaluation remains blocked by its documented CUDA/real-volume/calibration/scenario and live recovery gates, and by the requirement for all 21 compatible completed models. No unchanged passing local tests were rerun and no evaluation job was launched.


## Version 5 — epoch 8 improved, epoch 9 training — 2026-11-17 03:26 Asia/Tashkent

Signed-in Kaggle logs confirm **Version 5 (370300234) remains running**, run **1/21, UniGDNetR seed 13**. Epoch 8 completed at session second **30,091.5**, provisional validation macro Dice **0.15813**, improved best **0.15813**, bad_epochs **0**. The previous best was 0.14660 at epoch 7. Epoch 8 took **03:18:43** according to the log. This measures one epoch and does not establish a full-study finish date.

Epoch 9 training began at second 30,091.6 and reached **75/2,500 batches (3%)** at second **30,709.8**. A working recovery checkpoint was logged at second **30,696.2**, phase train, epoch 9, batch **63**. The page reported running for **30,914.3 seconds**, approaching the operational nine-hour cap; no pause or published V5 output was observed yet. These working saves are not independently verified published checkpoints. **V4 remains the latest trusted published recovery source**. The healthy job was not edited, cancelled, restarted or duplicated.

Still **0/21 completed models**, **no held-out results** and no reliable full-study finish estimate. The CSV adds the rounded provisional epoch-8 validation score only. Kaggle and GitHub reports were accessible. Evaluation remains blocked by the documented remaining validation gates and the requirement for 21 compatible completed models. No unchanged passing tests were rerun and no evaluation job was launched. At the eventual session pause, published status/checkpoints/provenance must be verified before selecting the next recovery source; remaining free quota must be checked before any continuation.


## Version 5 — normal budget pause, published recovery verified — 2026-11-17 04:55 Asia/Tashkent

Version 5 (370300234) paused normally at **2026-11-16T22:56:43Z (17 November 03:56:43 Asia/Tashkent)** after 9.1039 hours. Logs explicitly report the session budget pause. Epoch 9 training last printed 475/2,500; the published checkpoint/status preserve **480/2,500 batches (19.2%)**, 160 batches per task. Epochs **1–8** are complete; best provisional validation macro Dice remains **0.15813** at epoch 8. This is a session pause, not model completion.

The published output ZIP contains **53 files** and passes integrity verification. Its resume checkpoint loads locally with finite model/EMA tensors, format 2, phase train, epoch_index 8/epoch_completed 8, expected optimizer/scheduler/scaler/RNG and training progress. Configuration, task specifications and content/task fingerprints match verified V4. All **46 immutable files** checked are byte-identical to V4, including provenance/migration/splits/repairs/pairing audit/indices; the content manifest still holds 6,917 source entries. All 21 scientific experiment-plan rows match; only the runtime worker identifier differs. See `recovery_verification_v5.json` for checksums and verification details. **V5 is now the latest trusted published recovery output**: https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu/output?scriptVersionId=370300234 . Preserve V4 and V2 backups; never use V3.

Kaggle reports **29:48/30 GPU hours used**, leaving approximately **12 minutes**, less than the required full source byte audit alone. Draft session is off. No new job was launched, no source/input was changed, and no paid compute was used. Continuation must wait for sufficient renewed free quota; no reset date was displayed or assumed. When available, attach exactly V5 output, retain the five pinned sources/environment, rehash bytes/reuse indices and require strict mid-epoch recovery acceptance before claiming epoch 9 resumed. Stop treating terminal V5 as an active job.

Still **0/21 completed models** and **no held-out results**. Evaluation remains blocked by all 21 completed-checkpoint and remaining CUDA/real-volume/calibration/scenario/live recovery gates. No unchanged software tests were rerun. The quota wait is temporary; the study is not finalized and has no supported finish date.


## Local PC histories reviewed — 18 November 2026 (Asia/Tashkent)

The user supplied completion records for the same 21 expected local checkpoint paths, the preparation/fingerprint/split manifests, the current training notebook source, and now `logs.zip`. The archive SHA256 is `63f9871ce23caae3e8c7f16959f2933f52b7ec8d8ee176e5c81d9c391f93b204`. Its 21 expected unique CSV histories pass ZIP CRC verification and contain 760 consecutive epoch rows with finite numeric values and in-range Dice values. Seventeen histories end at epoch 40. SingleTask-brats seeds 13/37/71 end at epochs 12/12/18 (best epochs 2/2/8); SingleTask-lits seed 71 ends at epoch 38 (best epoch 28). All four are consistent with the source's patience of 10 strictly non-improving epochs. Logged macro scores equal the mean of selected task Dice scores within floating-point tolerance.

UniGDNetR seeds 13/37/71 have best logged validation macro task Dice 0.36324413/0.35940142/0.37107588 at epochs 40/39/40. BraTS Dice at these respective epochs is only 0.02958132/0.01815885/0.05034815. These are slice-validation metrics, not held-out volumetric results or independently verified checkpoint selections. See `local_training_history_review_20261118.json` and `local_training_history_summary_20261118.csv` for every run. The histories support the reported local training progression but cannot prove which dataset bytes or source were executed, or verify model weights.

Local and Kaggle evidence remain separate. Local supplied splits contain BraTS 1120/241/260 scans and ACDC 210/44/46 frames, differing from Kaggle's cohorts; the Kaggle 18,780-row clean evaluation target must not be reused for this local cohort. Supplied local splits have no duplicate cases or canonical patient overlap. The local pairing audit lists duplicated T2f and no T2w for all 1,621 BraTS cases, while supplied splits contain four distinct files. The uploaded notebook's 33 cell sources exactly match the repository notebook and reject duplicate images before audit output, but contain no saved execution outputs. The audit may be stale; its cause and historical training inputs remain unresolved. Five LiTS affine mismatch flags are handled by canonical-grid resampling in the current source, which does not establish historical execution. Local fingerprints cover path/size/mtime metadata rather than source-byte SHA256.

Next verification requires read-only metadata and SHA256 inventory of the 21 actual checkpoints (including selected epochs/scores, completion flags/configuration and finite model tensors), plus existing execution/repair evidence or a separately saved fresh pairing audit. Preserve the old audit. Do not rerun training or overwrite evidence to recreate history. Keep redundant Kaggle launches and held-out approval on hold. Kaggle V5 remains a separately verified paused backup at epoch 9 batch 480; earlier 0/21 counts refer to Kaggle, not the user-reported local set.
