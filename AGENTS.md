# AGENTS.md

## Project Overview

Python document classification pipeline: RVL-CDIP images → OpenRouter vision models → Braintrust evaluation. 16 document classes.

## Commands

```bash
# Install
pip install -r requirements-dev.txt

# Test
pytest                              # all tests
pytest tests/test_prompts.py -v     # single file
pytest -k "test_clean_prediction"   # by name match

# Coverage
pytest --cov=src --cov=scripts --cov-report=term-missing

# Run scripts (work from any directory)
python scripts/datasets/download_dataset.py
python scripts/braintrust/braintrust_report.py
python src/openrouter_classifier.py
```

No linter, formatter, or typecheck is configured.

## Environment

Two env files (both gitignored):

- `.env` — API keys: `OPENROUTER_API_KEY`, `BRAINTRUST_API_KEY`
- `braintrust.env` — single source of truth for Braintrust org/project/dataset/model config, loaded by `src/braintrust_config.py`

Copy `*.env.example` templates to create them. Missing env vars cause `sys.exit(1)` via `src/env_utils.require_env()`.

System binaries required: **Tesseract OCR** and **Poppler** (for `pdf2image`).

## Architecture

- `src/` — shared library (no CLI); scripts import via `from src.<module> import ...`
- `scripts/` — runnable scripts grouped by purpose (`datasets/`, `eda/`, `braintrust/`, `openrouter/`)
- `reports/` — generated artifacts (charts, confusion matrices, JSON)
- `docs/experiments/` — curated experiment documentation (links back to `reports/`)
- `conftest.py` adds project root to `sys.path` and sets matplotlib backend to `Agg`

Scripts resolve the repo root via `Path(__file__).resolve().parents[2]`, so they can be run from anywhere.

## Key Files

- `src/constants.py` — 16 `DOCUMENT_CLASSES` and `IMAGE_EXTENSIONS`
- `src/prompts.py` — versioned prompts (v1–v17); `DEFAULT_PROMPT_VERSION` is current
- `src/braintrust_config.py` — `load_braintrust_config()` dataclass; reads `braintrust.env`, falls back to `.env`
- `src/evaluation.py` — `validate_dataset()`, `ManifestStore` for resumable eval runs

## Conventions

- Scripts keep example `__main__` blocks with hardcoded dev-machine paths — update path constants before running locally
- Generated output goes to `reports/`, not `docs/`
- Prompt versions are append-only in `src/prompts.py`; register new versions in the `PROMPTS` dict and update `DEFAULT_PROMPT_VERSION`
