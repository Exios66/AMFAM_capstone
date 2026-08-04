# Repository Changelog

## Unreleased

### Changed

- **v17 prompt now default** — replaces v16 with a streamlined v11.9 derivative that removes the agency-estimate sub-protocol from check-7 (budget/invoice) and adds an explicit LETTER/MEMO OVERRIDE in check-2 (handwritten). Prompt is 4,627 chars lighter than v16 (46,277 vs 51,753), eliminating the finish_reason=length failures caused by qwen3.7-flash exhausting reasoning tokens on the bloated v11.9 check-7 section.
- **Reasoning effort reduced to `medium`** for qwen models (was `high`) to further cut token burn and eliminate `finish_reason=length` failures; 13 of 16 failed rows in v16 multispect were length-related.
- **MAX_TOKENS_CAP raised to 32,768** (was 16,384) as an additional safeguard against reasoning-token exhaustion.
- **Failed-row tracking** — errored rows now return an `ERROR:` sentinel output and are scored as both `exact_match` (miss) and a new tracked `failed` metric in Braintrust experiments.
- **HTTP timeout (300s)** added to the OpenAI client to prevent hung eval runs on stalled provider connections.
- **Manifest support** added to all eval launches for resumability after interruptions.

### Added

- Classification prompt `v16` (v11.9 + 2 worked examples for budget↔invoice and handwritten↔letter). Deprecated in favor of v17.
- `v16_multislice_evaluation_report.md` in `reports/` — full three-slice analysis identifying the three root causes of the drop from ~99% to ~80% exact_match.
- `eval_160_v16_v1.log`, `eval_160_v2_v16.log`, `eval_160_v3_v16.log` — raw v16 evaluation logs.
- `eval_v16_v{1,2,3}.jsonl` manifests in `reports/manifests/` for all v16 runs.
