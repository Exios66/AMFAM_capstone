## Summary

<!-- What does this change do, and why? One short paragraph. -->

- Fixes #<issue> / Implements #<issue> (if applicable)

## Type of change

- [ ] Bug fix
- [ ] New feature / enhancement
- [ ] Prompt change (new version in `src/prompts.py`)
- [ ] Dataset / slice builder
- [ ] Docs / site / notebooks
- [ ] Tooling / CI / chore

## What changed

<!-- Bullet list of the concrete changes. For prompt changes, note the version delta
     (previous -> new) and the rationale. -->

- ...

## How it was tested

- [ ] `pytest` (which tests, pass/fail count)
- [ ] `python scripts/braintrust/preflight_eval.py --dataset <ds> --prompt-version <v>` (for eval-affecting changes)
- [ ] Eval run (if spent credits): model / prompt / dataset / experiment name + exact_match
- [ ] `quarto render website/` (for site/notebook changes; confirm 0 broken links/images)
- [ ] Notebooks regenerated: `python scripts/site/build_notebooks.py`

## Changelog

- [ ] `CHANGELOG.md` updated (code/config/tooling changes)
- [ ] `docs/CHANGELOG.md` updated (new prompt version + results)
- [ ] `AGENTS.md` updated if commands/conventions changed

## Screenshots / artifacts

<!-- Charts, confusion matrices, site renders, etc. -->

## Checklist

- [ ] No secrets committed (`.env`, `braintrust.env`, API keys)
- [ ] No generated output committed (`reports/`, `website/_site/`)
- [ ] Scripts run from any directory (repo-root path resolution)
