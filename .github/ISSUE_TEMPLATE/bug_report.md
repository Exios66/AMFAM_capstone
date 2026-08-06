---
name: Bug report
about: Report a bug or failure in the pipeline (eval runner, dataset build, reporting, site, notebooks)
title: "[BUG] "
labels: bug
assignees: ''
---

## Description

<!-- What went wrong? One or two sentences. -->

## Where it happens

<!-- Which part of the pipeline does this affect? Delete those that don't apply. -->
- [ ] Eval runner (`braintrust_openrouter_input.py`)
- [ ] Dataset build / upload (`create_braintrust_*.py`)
- [ ] Report / charts / experiment log (`braintrust_report.py`, `braintrust_metrics_visual.py`, `build_site*.py`)
- [ ] Quarto site / notebooks
- [ ] Prompts (`src/prompts.py`) or classifier (`src/openrouter_classifier.py`)
- [ ] Shared library (`src/`)
- [ ] Other: ____

## Reproduction

1. Exact command run (with `--flags`):
   ```
   python scripts/braintrust/...
   ```
2. Prompt version / model / dataset / experiment name (if eval-related):
   ```
   prompt_version: 
   model: 
   dataset: 
   experiment_name: 
   manifest: reports/manifests/...
   ```
3. What happened vs. what you expected:
   - Expected: ...
   - Actual: ...

## Error output

<!-- Paste the relevant log/error lines. Trim to the important part. -->

```
```

## Environment

- OS: 
- Python version: `python3 --version`
- Quarto version (site issues only): `quarto --version`
- Tesseract / Poppler installed? (yes/no)
- Git branch / commit: 

## Additional context

<!-- Screenshots, report artifacts, links to Braintrust experiment, etc. -->

> **Security:** never paste `.env`, `braintrust.env`, or any API key/token in an issue.
