
**Research question:** Does the ~99% accuracy achieved on the curated 160-image slice hold when the same prompt is run on larger, independently sampled, noisier evaluation slices?

**Formal write-up:** [`results/headline-results.qmd`](Headline-Results) · [`docs/experiments/experiment_log.md`](https://github.com/Exios66/AMFAM_capstone/blob/main/docs/experiments/experiment_log.md)


## What questions or uncertainties remain?

Why the 320 slice (87.2%) scores *lower* than the 480 slice (89.1%) despite being smaller and a strict subset of the 480 is open — seed differences and sampling noise are the leading explanations; a repeat of the 320 slice under a fresh seed would quantify it. The "production-like" ceiling of ~82–87% is estimated from four slices; a dedicated production-noise slice would tighten the estimate.

## What other levers may also recover the generalization gap?

The Monte Carlo robustness studies target exactly this: [ensemble voting](Ensemble-Voting) recovers ~+4 *pp* at 25× cost, [confidence-gated routing](Confidence-Routing) recovers ~+5–10 *pp* on the low-confidence tail, and [few-shot exemplars](Exemplar-Mining) attack the near-miss ceiling. See also the [hardest-classes memo](Hardest-Classes) for which pairs dominate the larger-slice miss budget.


---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
