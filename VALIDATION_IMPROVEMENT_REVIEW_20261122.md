# Validation improvement review — 22 November 2026

## Kaggle continuation

The user requested continuing on Kaggle and investigating improvements. This supersedes the previous blanket continuation hold; held-out evaluation remains blocked. Before launch, the signed-in editor showed zero active events, renewed quota of 00:00 / 30 GPU hours, GPU T4 x2, Internet enabled, draft session off, and the original 2026-11-02 environment selected. Exactly one prior notebook input was updated through Kaggle's explicit version-4-to-version-5 dialog. Five source dataset inputs were preserved.

Version 6, **372483892**, was submitted once. Version history showed a **+0/-0 source diff**; the original protocol and nine-hour operational cap remain. The live viewer showed one active event and **Queued** at this review. This is a submitted continuation, not verified checkpoint recovery or new training progress.

- Live version: https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu?scriptVersionId=372483892
- Latest trusted published recovery remains V5: https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu/output?scriptVersionId=370300234
- Require all 6,917 source hashes to match, all nine indices reused, strict checkpoint acceptance, and explicit resume at epoch 9 batch 480 before claiming recovery. Do not repeat the saved 480 batches.
- The queued viewer labels its environment “Latest Container Image”, despite the editor's original pin. Actual runtime equivalence is unresolved and must be checked from execution evidence. Do not assert an environment match from draft settings alone.

## Tested candidate, separate from the active run

`scripts/training_diagnostics_candidate.py` is an opt-in module. The baseline notebook does not import it. It contains explicit FP32 soft-Dice computation preserving the original foreground/present-class objective, and aggregate per-class confusion counts with Dice, precision, sensitivity and their denominators. It writes no files and retains no case IDs, images or voxel prediction exports. Keep existing batch-mean validation Dice alongside pooled diagnostic Dice; they are different aggregations.

Three CPU tests passed with zero failures/errors/skips using PyTorch 2.11.0+cpu. The test extracts the original loss function from the supplied Stage 2 source without executing the notebook. At batch size 2 and resolution 256 x 256 with a dominant foreground class, an explicit FP16 probability reduction overflows; the original explicit-FP16 loss is 1.0. The candidate matches the original FP32 reference exactly (loss approximately 5.96e-8) and has finite backward gradients. Separate checks cover exact TP/FP/FN values, absent-class denominators, out-of-range labels and nonfinite diagnostic logits.

**This synthetic explicit-FP16 result does not establish a CUDA-autocast bug, the cause of low BraTS validation, or a real-data improvement.** CUDA autocast may already promote softmax to FP32. Check actual CUDA dtypes and compare losses/gradients under the real autocast policy before considering promotion. No new learning rate, architecture, sampling rule, label mapping or checkpoint alias is selected by these tests.

## Next validation-only investigations

1. Inspect the actual 21 local checkpoints read-only: bytes/SHA-256, model and EMA finiteness, completion flag, selected epoch and validation score, task heads, experiment/seed, training configuration, pipeline and dataset compatibility. Compare checkpoint selections to the already inspected histories. Do not request the histories again.
2. Preserve the older pairing audit. Inspect existing repair/execution evidence, or save a separately named current audit against the actual data. Verify distinct canonical BraTS modality files and source byte identity. The old duplicated-T2f rows do not establish what the models consumed.
3. On training/validation data only, record label histograms and per-class confusion counts. Check BraTS class mapping, positive-slice sampling, image/mask alignment and preprocessing against source assumptions. Determine whether low Dice reflects missed foreground, false positives, particular classes, or metric aggregation. Do not guess the cause.
4. If a defect is demonstrated, prepare a separately identified candidate configuration/pipeline and controlled validation comparison with the same patient splits, seeds and budget. Preserve the existing baseline results and checkpoint lineage. Freeze any selected configuration using validation evidence before held-out execution.

The local and Kaggle cohorts remain separate; the Kaggle-only 18,780 coverage target must not be applied to the local cohort. Original evaluator gates (21 compatible completed checkpoints; CUDA/MC/RNG checks; real-volume memory/disk checks; calibration/scenario completeness and live recovery) remain open. No held-out metrics, final models or performance gain are claimed.
