# EDA Scripts (`scripts/eda/`)

Exploratory data analysis for the RVL-CDIP document image datasets. Both scripts write their
generated artifacts to the top-level `reports/` directory.

## Scripts

### `eda_analysis.py`

Runs full EDA on a dataset directory:

- Class distribution (bar + pie charts)
- Image dimension statistics (width/height/aspect ratio)
- File size statistics
- Image color-mode breakdown
- Sample image grid (only when the dataset has fewer than 10,000 images)

Outputs (written to `reports/`):

- `class_distribution.png`, `image_dimensions.png`, `dimensions_by_class.png`
- `file_sizes.png`, `image_modes.png`, `sample_images.png`
- `eda_report.json` — aggregated statistics

Configure `DATASET_PATH` in `main()` (currently a dev-machine example path) before running.
`run_full_eda(sample_size=None)` analyzes the full dataset; pass a number to sample for a faster run.

```bash
python scripts/eda/eda_analysis.py
```

### `eda_dimensions_summary.py`

Computes average/median/min/max/std of image dimensions and aspect ratios across every dataset in
the `DATASETS` dictionary and writes `reports/dimensions_summary.json`.

```bash
python scripts/eda/eda_dimensions_summary.py
```

## Output convention

All charts and JSON land in `reports/` (see `reports/README.md`).
