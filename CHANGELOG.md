# Repository Changelog

## Unreleased

### Added

- Added classification prompt `v15` and made it the default prompt version.
- Added `scripts/braintrust/create_braintrust_160_v3_v4_datasets.py` for creating two disjoint 160-image validation slices.
- Added source-hash, source-index, per-class, and Braintrust metadata validation for fresh slices.

### Changed

- Fresh-slice sampling now uses the full Hugging Face `chainyo/rvl-cdip` test split as the primary source.
- Added a Kaggle RVL-CDIP test-set fallback when the primary source cannot satisfy disjoint per-class quotas.
- Updated repository and prompt documentation for v15 and the new Braintrust datasets.

### Added

- `braintrust_openrouter_input.py` now accepts `--temperature` and `--reasoning-effort` flags; reasoning effort defaults to the maximum each model family supports (qwen `high`, kimi `xhigh`, gemini `max`), and temperature/reasoning are recorded in the Braintrust experiment metadata.
- Ran v11.8 prompt cross-model evals on `fixed_size_sampled` (v1) and `qwen_v12_retroactive_eval`: qwen3.7-flash @ temp 0.3 (98.7%), qwen3.5-35b-a3b @ temp 0.1 (98.7%), kimi-k2.6 @ temp 0.1 (aborted mid-run by a Braintrust network outage; partial experiment not comparable), gemini-2.5-flash-lite @ temp 0.2 with max reasoning (86.9%), and qwen3.5-35b-a3b on the 52-row v12 retroactive slice (30.8%).
- Reports, confusion matrices, per-class charts, and misclassification-reasoning docs written to `reports/` for each completed run; experiment log updated in `docs/experiments/experiment_log.md`.
