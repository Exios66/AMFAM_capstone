# Reports (`reports/`)

Generated artifacts live here, separate from the curated experiment documentation in `docs/`.
This directory is produced by the scripts — contents are regenerated on each run.

## What lands here

| Artifact | Produced by |
|---|---|
| `dimensions_summary.json` | `scripts/eda/eda_dimensions_summary.py` |
| `eda_report.json` | `scripts/eda/eda_analysis.py` |
| `class_distribution.png`, `image_dimensions.png`, `dimensions_by_class.png`, `file_sizes.png`, `image_modes.png`, `sample_images.png` | `scripts/eda/eda_analysis.py` |
| `confusion_matrix_<experiment>.png/.md` | `scripts/braintrust/braintrust_report.py`, `braintrust_metrics_visual.py` |
| `per_class_accuracy_<experiment>.png` | `scripts/braintrust/braintrust_report.py`, `braintrust_metrics_visual.py` |
| `misclassification_reasoning_<experiment>.md` | `scripts/braintrust/braintrust_report.py`, `braintrust_metrics_visual.py` |
| `report_<experiment>.md` | `scripts/braintrust/braintrust_report.py` |

## Notes

- The curated, human-readable summaries of these artifacts live in `docs/experiments/` (see
  `docs/README.md`). Documents there link back to charts here via `../../reports/...`.
- Markdown image links from `docs/experiments/` resolve to this directory (e.g.
  `![Confusion Matrix](../../reports/confusion_matrix_main-123.png)`).
