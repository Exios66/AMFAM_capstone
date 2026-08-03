# OpenRouter Scripts (`scripts/openrouter/`)

OpenRouter-specific tooling. The main classifier itself lives in the core library at
`src/openrouter_classifier.py`; this directory holds cost-estimation tooling built on it.

## Scripts

### `estimate_openrouter_cost.py`

Runs a single representative image through an OpenRouter vision model and extrapolates token usage
and USD cost for the full dataset (800, 25,000, and 320,000 images), using the actual API response
tokens multiplied by model pricing.

Configure the constants in the script (near the top, in `main()`/module config) before running:

- `MODEL` — OpenRouter model id (e.g. `google/gemini-2.5-flash`, `moonshotai/kimi-k3`).
- `IMAGE_PATH` — path to one representative document image.
- `IMAGE_COUNTS` — list of dataset sizes to project for.
- `INPUT_PRICE` / `OUTPUT_PRICE` — USD per 1M tokens for the model.

```bash
python scripts/openrouter/estimate_openrouter_cost.py
```

The script updates `docs/experiments/1pic_cost_estimation.md` automatically, inserting or replacing
the section for `MODEL`.

## Related

- `src/openrouter_classifier.py` — `classify_image()`, `clean_prediction()`, `VALID_CLASSES`.
- `src/openrouter_utils.py` — API endpoints and message-building helpers.
- `docs/experiments/1pic_cost_estimation.md` — the generated cost projections document.
