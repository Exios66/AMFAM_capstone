
**Research question:** If we ran the classifier *K* times per image and took a majority vote, how much accuracy would we recover — and at what cost multiplier?

**Formal write-up:** [`montecarlo/ensemble-voting.qmd`](Ensemble-Voting) · [`reports/monte_carlo/ensemble_accuracy_vs_k.md`](https://github.com/Exios66/AMFAM_capstone/blob/main/reports/monte_carlo/ensemble_accuracy_vs_k.md)


## What questions or uncertainties remain?

The simulation reuses the *same model's* per-image prediction distribution (draws from observed correct/incorrect labels), so it measures label-noise averaging, not the benefit of *diverse* models. A heterogeneous committee (different models per vote) would likely beat same-model voting; that is untested.

## What other levers may also improve accuracy?

[Confidence-gated escalation](Confidence-Routing) targets the same error budget for 1.02–1.8× cost instead of 3–25× — strictly better on cost per *pp*. [Few-shot exemplars](Exemplar-Mining) attack the deterministic-error classes that voting cannot fix.


---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
