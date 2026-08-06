
**Research question:** Across 27 versioned prompt iterations (v0 → v17.2), how much of the classification accuracy gain is attributable to prompt engineering rather than model choice or data?

**Formal write-up:** [`prompts/prompt-changelog.qmd`](Prompt-Changelog) · [`docs/experiments/experiment_log.md`](https://github.com/Exios66/AMFAM_capstone/blob/main/docs/experiments/experiment_log.md)


## What questions or uncertainties remain?

Whether the v0 → v17.2 gains reflect better rule coverage, better scratchpad self-criticism, or both is not separately identified — every version bundled multiple edits. A true single-edit factorial (one rule changed per run) would decompose the 14-check cascade's contribution. The v11.8 → v17.x comparison on the 160 slice is statistically marginal (*P* = 0.932 "A likely", not decisive), so the current default (v17.2) is not measurably better than v11.8 on that slice.

## What other levers may also improve accuracy?

The near-miss analysis in the [hardest-classes memo](Hardest-Classes) shows ~37% of remaining misses are near-misses (runner-up = expected), a ceiling reachable by [few-shot exemplars](Exemplar-Mining). Model choice adds a smaller but real increment — see the [model comparison memo](Model-Comparison).


---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
