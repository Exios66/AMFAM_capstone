# Archive

Deprecated one-off scripts and large raw caches, kept for reference and reproducibility.
Nothing here is imported by active code, and the Quarto site build does not depend on any path in
this folder (it consumes committed outputs in `reports/` and `website/` instead).

## Contents

| Path | Former location | Status |
|---|---|---|
| `braintrust/create_smoke_v11_8_16_dataset.py` | `scripts/braintrust/` | Orphaned — zero references |
| `braintrust/create_v115_eval_dataset.py` | `scripts/braintrust/` | Orphaned — zero references |
| `braintrust/create_v115_v12_eval_dataset.py` | `scripts/braintrust/` | Orphaned — zero references |
| `braintrust/copy_braintrust_dataset.py` | `scripts/braintrust/` | Superseded by `copy_datasets_to_new_env.py` |
| `braintrust/run_v11_8_800_after_480.py` | `scripts/braintrust/` | Completed one-off run (research-funding-key example) |
| `site/build_wiki.py` | `scripts/site/` | Orphaned — zero references |
| `datasets/download_dataset.py` | `scripts/datasets/` | Superseded by the streaming `create_braintrust_*.py` builders |
| `chat_data/*.json` | `reports/chat_data/` | Raw Braintrust experiment-row caches (~26 MB); consumed by `scripts/site/build_chat_examples.py` (`CACHE_DIR` points here) |

## Why these moved

Repository hygiene: `scripts/` and `reports/` were crowded with artifact scripts, deprecated code,
and large caches. Moving them here (git-mv, history preserved) keeps the active locations canonical
without deleting anything. If a script is ever revived, move it back and update the references in
`AGENTS.md`, `README.md`, `docs/CLI_COMMANDS.md`, and `website/methods/cli-commands.qmd`
(`build_site.py` regenerates the last one from `docs/CLI_COMMANDS.md`).
