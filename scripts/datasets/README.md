# Dataset Scripts (`scripts/datasets/`)

Scripts for acquiring the RVL-CDIP dataset and producing the preprocessed, balanced, fixed-size
image sets used by the classification pipeline.

## Scripts

### `download_dataset.py`

Downloads the RVL-CDIP document-image dataset from Kaggle using `kagglehub` and prints the path to
the downloaded files.

```bash
python scripts/datasets/download_dataset.py
```

Requires Kaggle credentials to be configured for `kagglehub`.

### `create_balanced_dataset.py`

Samples `N` random images per class (default 50 × 16 = 800) from a source RVL-CDIP class directory
into a balanced output directory, then verifies the result.

- Configure `SOURCE_PATH`, `OUTPUT_PATH`, and `SAMPLES_PER_CLASS` in `main()`.
- Writes `sampling_log.json` and `verification_log.json` into the output directory.

```bash
python scripts/datasets/create_balanced_dataset.py
```

### `create_fixed_size_dataset.py`

Builds fixed-size, aspect-ratio-preserving image datasets with padding to a square canvas.

Two workflows are provided:

- `create_fixed_size_dataset` — resizes every image in a single input directory to a target size.
- `create_sampled_fixed_size_dataset` — samples `N` images per class from multiple source datasets
  and writes them to `output_dir/images/` at a target size (e.g. 2550×3300 for 300 DPI US Letter,
  1024×1024 for the eval set).

Configure `DATASETS` and the `configs` list in `main()` (target size, samples per class, seed).
Writes `resize_summary.json` per dataset. Already-populated output directories are skipped.

```bash
python scripts/datasets/create_fixed_size_dataset.py
```

### `run_tiff_processing.py`

Batch-converts the balanced TIFF dataset into 300 DPI grayscale PNG page images with spatial OCR
(per-word bounding boxes) using `ClassOrganizedBatchProcessor` from `src/document_processor.py`.

- Configure `INPUT_DIR` and `OUTPUT_DIR` in `main()`.
- Writes per-class organized output plus a `processing_summary.json`.

```bash
python scripts/datasets/run_tiff_processing.py
```

## Output convention

Input paths are configured in each script's `main()` block (they currently contain example
dev-machine paths — replace them). Generated JSON artifacts from these scripts stay local to their
configured output directories.
