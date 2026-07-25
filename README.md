# Document Intelligence Pipeline with OpenRouter Vision Models

A Python toolkit for downloading the RVL-CDIP document image dataset, preprocessing pages, running exploratory data analysis, and classifying documents with vision models through OpenRouter.

## What's Included

- `download_dataset.py` — Download the RVL-CDIP dataset from Kaggle.
- `create_balanced_dataset.py` — Sample a balanced subset (50 images per class) from RVL-CDIP.
- `eda_analysis.py` — Exploratory data analysis: class distribution, dimensions, file sizes, visualizations.
- `document_processor.py` — Convert TIFF/PDF pages to 300 DPI grayscale PNGs and run OCR with bounding boxes.
- `run_tiff_processing.py` — Batch process the balanced TIFF dataset with `document_processor.py`.
- `openrouter_classifier.py` — Send a document image to an OpenRouter vision model for one of 16 class predictions.
- `estimate_openrouter_cost.py` — Run one image through an OpenRouter vision model and extrapolate token usage/cost for 800, 25,000, and 320,000 images.
- `openrouter_token_calculation.md` — Cost projections based on actual API responses.
- `requirements.txt` — Python dependencies.
- `.env.example` — Template for API key environment variable.

## Setup

1. Install system dependencies:
   - [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
   - [Poppler](https://github.com/oschwartz10612/poppler-windows) (for `pdf2image`)

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your OpenRouter API key:

   ```bash
   cp .env.example .env
   ```

   Edit `.env`:

   ```text
   OPENROUTER_API_KEY=sk-or-v1-...
   ```

## Usage Workflow

1. **Download the dataset**

   ```bash
   python download_dataset.py
   ```

2. **Create a balanced subset**

   ```bash
   python create_balanced_dataset.py
   ```

3. **Run EDA**

   ```bash
   python eda_analysis.py
   ```

4. **Process TIFF pages to PNGs**

   ```bash
   python run_tiff_processing.py
   ```

5. **Estimate OpenRouter cost for a model**

   Edit `MODEL` in `estimate_openrouter_cost.py`, then run:

   ```bash
   python estimate_openrouter_cost.py
   ```

   This updates `openrouter_token_calculation.md` automatically.

6. **Classify a single image**

   ```bash
   python openrouter_classifier.py
   ```

## Security Notes

- **Never commit `.env` or any file containing your API key.** `.env` is excluded by `.gitignore`.
- `.env.example` is safe to commit because it contains a placeholder value only.
- Generated datasets, images, and report files are excluded from version control by `.gitignore`.

## Notes

- The scripts contain example `__main__` blocks with hardcoded paths for local testing. Update the `*_PATH` variables in each script to match your environment before running.
- Cost projections are linear extrapolations from a single representative image per model. Actual costs may vary with image size, content, and OpenRouter pricing changes.
