---
name: Feature request
about: Suggest an enhancement to the pipeline, prompts, reporting, or site
title: "[FEATURE] "
labels: enhancement
assignees: ''
---

## Motivation

<!-- What problem does this solve? What use case is missing? -->

## Proposed solution

<!-- Describe the change you'd like to see. If it touches prompts, name the target version and the expected effect. -->

## Alternatives considered

<!-- Other approaches you evaluated and why you did not pick them. -->

## Impact

- [ ] Prompt change (new version in `src/prompts.py` + `docs/CHANGELOG.md` + `DEFAULT_PROMPT_VERSION`?)
- [ ] New/changed script in `scripts/`
- [ ] New/changed shared helper in `src/`
- [ ] Dataset slice / builder change
- [ ] Site / notebook update (`website/`, `scripts/site/`)
- [ ] Documentation / changelog only

## Acceptance criteria

<!-- How would we verify this is done? Concrete, testable bullets. -->

- [ ] ...
- [ ] Tests pass: `pytest`
- [ ] Preflight passes for any affected eval: `python scripts/braintrust/preflight_eval.py --dataset <ds> --prompt-version <v>`

## Additional context

<!-- Links to experiments, reports, docs, or related issues. -->
