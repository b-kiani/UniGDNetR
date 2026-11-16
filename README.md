# UniGDNetR

Kaggle port of the supplied `02_UniGDNetR_TRAIN_RAM_Fixed.ipynb`.

## Run

Open the [Kaggle notebook](https://www.kaggle.com/code/bcau2025/unigdnetr-full-experiment-gpu/edit), select **GPU T4 x2**, enable Internet, then use **Save Version → Save & Run All**. The port preserves the original CUDA model and uses one GPU per training run. TPU/XLA and distributed training are not implemented.

The original notebook is in `notebooks/02_UniGDNetR_TRAIN_RAM_Fixed.ipynb`. The runnable port is `notebooks/UniGDNetR_Kaggle_Full_Experiment.ipynb`; `python scripts/build_kaggle.py` rebuilds it reproducibly.

## Dataset inputs

| Task | Kaggle source | Verified file coverage |
| --- | --- | --- |
| BraTS2023 GLI | [Part 1](https://www.kaggle.com/datasets/aiocta/brats2023-part-1), [Part 2](https://www.kaggle.com/datasets/aiocta/brats2023-part-2zip) | 625 + 626 scans, each with four modalities and a segmentation |
| LiTS | [Part 1](https://www.kaggle.com/datasets/andrewmvd/liver-tumor-segmentation), [Part 2](https://www.kaggle.com/datasets/andrewmvd/liver-tumor-segmentation-part-2) | 51 + 80 CT volumes; 131 masks in part 1 |
| ACDC | [MICCAI17 source](https://www.kaggle.com/datasets/samdazel/automated-cardiac-diagnosis-challenge-miccai17) | Only `database/training` is used: 100 patients, 200 labeled frames |

Kaggle attaches the datasets as read-only inputs. Their original data cards, citations, and access conditions apply. The original research datasets and licenses are not redistributed by this repository. BraTS: cite the applicable BraTS benchmark publications. LiTS: Bilic et al., *The Liver Tumor Segmentation Benchmark*, Medical Image Analysis 2023, DOI 10.1016/j.media.2022.102680. ACDC: Bernard et al., *Deep Learning Techniques for Automatic MRI Cardiac Multi-Structures Segmentation and Diagnosis*, IEEE TMI 2018, DOI 10.1109/TMI.2018.2837502; retain `MANDATORY_CITATION.md` from the dataset.

### Damaged mirror files

The first Kaggle job stopped during its integrity audit: the `aiocta/brats2023-part-2zip` mirror contains **ten zero-byte files** across `BraTS-GLI-00818-000`, `BraTS-GLI-01462-000`, and `BraTS-GLI-01486-000`. A second Kaggle mirror reproduced the same damage. No training results were produced by that job.

`scripts/repair_brats.py` downloads all five files for each affected scan from [MedOtter/brats2023-gli-dataset](https://huggingface.co/datasets/MedOtter/brats2023-gli-dataset), pinned to revision `b032d353a3e80911a5f850bc54e6fb575298a354`. `brats_repair_sources.json` records all 15 filenames, byte sizes and LFS SHA-256 digests. Files are saved only under Kaggle output `UniGDNetR/data_repairs/`, never committed here. Each replacement is checked for its checksum, full array readability, finite values, shape, and allowed segmentation labels. For the five non-empty original files in those scans, the replacement must also match the original voxel array and affine. A mismatch blocks training. All 1,251 scans and their patient groups are retained; missing values are never fabricated.

## Scientific protocol

- Three seeds: 13, 37, 71. Seven variants: main model, Uniform-slice, Shared-no-FiLM, No-boundary, and three single-task models. Total: 21 runs.
- Maximum 40 epochs per run; original early stopping remains active.
- Original image size, batch size, accumulation, learning rate and loss weights are retained.
- Training uses at most 2,500 batches per epoch; validation is capped at 200 batches per task.
- Patient groups are split 70/15/15 with seed 13. This is an internal patient split, not an official challenge test evaluation. Both ACDC frames and longitudinal BraTS scans remain grouped by patient.
- Modern BraTS labels retain ET=3 and RC=4; no conversion to the historical ET=4 convention is made.
- Full-cohort guards reject missing tasks or incomplete source coverage. Empty files and truncated uncompressed NIfTI files block training before model creation. Header geometry is audited without loading whole image arrays, using eight bounded I/O threads.
- Synthetic CUDA forward/backward checks cover all three task heads before training.

This repository contains **Stage 2 training**, not the missing original Stage 3 evaluation notebook. Training/validation scores are provisional; no final held-out paper results are claimed. BraTS2023 GLI may have no observed RC examples despite the original five-class architecture; label 4 is not fabricated.

## Sessions and recovery

Kaggle reported a 30-hour remaining weekly GPU allowance during setup on 15 November 2026. Availability and quota may change. The entire 21-run study is not guaranteed to fit in that allowance or one session.

Each session has a 10-hour soft budget. During training, atomic recovery checkpoints are written every 300 batches or 10 minutes, and at phase/epoch boundaries. A budget stop occurs after saving training state, or during validation when a pre-validation checkpoint already exists. Validation restarts for that epoch on the next session. The training protocol is not shortened to fit the session.

After a paused background version finishes:

1. Open this same notebook for editing.
2. Add Input → Notebook, select exactly the latest completed saved version of this notebook's output.
3. Keep the same dataset versions attached; remove older output inputs if any.
4. Save & Run All again. The bootstrap restores checkpoints, indices, manifests, logs, reports and checksum-verified repair files to writable output, excluding stale VM lock files.
5. Inspect `UniGDNetR/manifests/unigdnetr_kaggle_session.json`. `paused` means more sessions are required. Only `training_complete` means every selected training run finished. `final_test_evaluation_complete` remains false until the original Stage 3 pipeline runs.

Checkpoint compatibility uses dataset fingerprints, model settings, pipeline revision, experiment and seed. If an input version or path changes, compatibility checks refuse to silently mix results. A sudden VM termination can lose progress after the most recent saved checkpoint. A failed Kaggle job's outputs must be verified accessible before relying on them for recovery.

## Results

Kaggle output under `/kaggle/working/UniGDNetR` holds checkpoints, preparation manifests, logs, and any reports. Large checkpoints remain there. `scripts/sync_results.py` copies an allowlist of small reports into `results/`. You can commit and push those reports with an existing authorized GitHub CLI session. It excludes raw NIfTI volumes, checkpoints, credentials and lock files.

Example after downloading a saved Kaggle version's output:

```bash
python scripts/sync_results.py /path/to/downloaded/UniGDNetR
git add results
git commit -m "Record Kaggle experiment progress"
git push
```

No background result synchronization is active. Do not store Kaggle API credentials or GitHub tokens in notebook source or Git history. The complete source tree is also distributed as `UniGDNetR_Source_20261116.zip`. Extract it at the repository root to restore the `notebooks/` and `scripts/` layout. A convenient runnable notebook copy is available at the repository root. See `EXPERIMENT_PROGRESS.md` and `provisional_validation.csv` for dated, explicitly provisional results. The full study and held-out evaluation are incomplete.
