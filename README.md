# Document Intelligence Pipeline with OpenRouter Vision Models

A Python toolkit for downloading the RVL-CDIP document image dataset, preprocessing pages, running exploratory data analysis, and evaluating vision model classification accuracy across multiple providers via OpenRouter and Braintrust.

## Project Structure

```
src/
  openrouter_classifier.py    — Classification prompt & prediction logic (16 classes)
scripts/
  download_dataset.py         — Download the RVL-CDIP dataset from Kaggle
  create_balanced_dataset.py  — Sample balanced subsets from RVL-CDIP
  create_fixed_size_dataset.py — Resize/pad images to fixed dimensions (e.g. 1024×1024)
  eda_analysis.py             — Exploratory data analysis & visualizations
  run_tiff_processing.py      — Batch convert TIFF pages to 300 DPI PNGs
  estimate_openrouter_cost.py — Single-image cost estimation & extrapolation
  braintrust_openrouter_input.py — Run Braintrust evaluation experiments
  braintrust_metrics_visual.py   — Generate confusion matrices, misclassification reports, and experiment logs
docs/
  experiment_log.md           — Full experiment history with metrics & cost projections
  model_comparison_1024x1024_160.md — Side-by-side model comparison table
  confusion_matrix_*.md       — Per-experiment confusion matrices
  misclassification_reasoning_*.md — Per-experiment error analysis with model reasoning
```

## Setup

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables (or use a `.env` file):

   ```bash
   export OPENROUTER_API_KEY=sk-or-v1-...
   export BRAINTRUST_API_KEY=...
   ```

## Experiment Workflow

### 1. Prepare the dataset

```bash
python scripts/create_balanced_dataset.py
python scripts/create_fixed_size_dataset.py
```

This creates padded 1024×1024 PNG images, balanced across 16 document classes (10 per class = 160 images for quick experiments).

### 2. Choose a model

Edit `MODEL` in `scripts/braintrust_openrouter_input.py`:

```python
MODEL = "google/gemini-3.6-flash"  # or any OpenRouter vision model
```

### 3. Run the evaluation

```bash
python scripts/braintrust_openrouter_input.py
```

This sends all images to the model via OpenRouter, scores predictions against ground truth, and logs results to Braintrust. The experiment ID is printed at the end (e.g., `main-1785367223`).

### 4. Generate reports

```bash
python scripts/braintrust_metrics_visual.py main-1785367223
```

This produces:
- Confusion matrix (markdown + PNG)
- Misclassification reasoning document with model chain-of-thought
- Experiment log entry with accuracy, token usage, and cost projections

### 5. Compare models

See `docs/model_comparison_1024x1024_160.md` for a summary table:

| Model | Cost | Accuracy | Pricing (per M tokens) |
|-------|-----:|---------:|------------------------|
| `google/gemini-3.6-flash` | $0.97 | **91.88%** | $0.15 in / $0.60 out |
| `openai/gpt-5.6-terra` | $0.72 | 91.25% | $2.50 in / $10.00 out |
| `anthropic/claude-sonnet-5` | $1.17 | 90.62% | $3.00 in / $15.00 out |
| `x-ai/grok-4.5` | $0.60 | 89.31% | $2.00 in / $6.00 out |
| `google/gemini-2.5-flash` | $0.28 | 85.00% | $0.15 in / $0.60 out |
| `moonshotai/kimi-k3` | $1.07 | 85.00% | $0.30 in / $15.00 out |

## Classification Prompt

The prompt in `src/openrouter_classifier.py` defines 16 document classes with detailed descriptions and critical disambiguation rules to reduce common confusions (e.g., presentation vs file_folder, budget vs invoice, form vs memo).

## Security Notes

- **Never commit `.env` or any file containing your API key.** `.env` is excluded by `.gitignore`.
- Generated datasets and image files are excluded from version control by `.gitignore`.
