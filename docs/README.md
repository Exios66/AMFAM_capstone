# Documentation Index

## Quick Start

- [`CLI_COMMANDS.md`](CLI_COMMANDS.md) — The most common / most useful CLI commands for this project (setup, data pipeline, EDA, cost estimation, Braintrust evaluation workflow).

## Experiment Log & Results (`experiments/`)

The canonical home for experiment tracking and results.

- [`experiments/experiment_log.md`](experiments/experiment_log.md) — Running log of every Braintrust experiment (auto-appended by `scripts/braintrust/braintrust_metrics_visual.py`).
- [`experiments/braintrust_dataset_run_gemini25flash.md`](experiments/braintrust_dataset_run_gemini25flash.md) — Gemini 2.5 Flash, 160 images (10/class).
- [`experiments/800pic_tst_notes.md`](experiments/800pic_tst_notes.md) — Gemini 2.5 Flash, 800 images (50/class) — cost & results.
- [`experiments/1pic_cost_estimation.md`](experiments/1pic_cost_estimation.md) — OpenRouter token/cost projections from single-image runs (updated by `scripts/openrouter/estimate_openrouter_cost.py`).
- `experiments/confusion_matrix_main-*.md` — Confusion matrix summaries per experiment ID.
- `experiments/misclassification_reasoning_main-*.md` — Misclassification reasoning traces per experiment ID.

## Design & Reference

- [`prompt_rules_provenance.md`](prompt_rules_provenance.md) — Sources and validation status of classification rules across prompt versions (v1 → v11).
- [`document_processor.md`](document_processor.md) — Reference for the `document_processor` module (PDF→PNG + spatial OCR).

## Generated Output

Script-generated artifacts (charts, heatmaps, `report_*.md`, `dimensions_summary.json`) are written to the top-level `reports/` directory, not `docs/`.
