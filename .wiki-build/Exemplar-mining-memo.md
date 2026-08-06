
**Research question:** Can injecting a handful of correct reasoning traces (exemplars) for the top confusion pairs recover the near-miss errors — and does the measured gain match the simulated gain?

**Formal write-up:** [`montecarlo/exemplar-mining.qmd`](Exemplar-Mining) · [`montecarlo/verification.qmd`](Verification) · [`reports/monte_carlo/exemplar_candidates.md`](https://github.com/Exios66/AMFAM_capstone/blob/main/reports/monte_carlo/exemplar_candidates.md)


## What questions or uncertainties remain?

The verification slice is small (48 rows) and the delta (−0.042) is within sampling error — a 95% *CI* would span ~±0.14. The exemplar prompt (v18) also differs from the base (v17.2) in more than the exemplars, so the measured regression is not a clean single-cause test. A larger, controlled exemplar-vs-base A/B with the *same* prompt text except the exemplar block is the decisive experiment.

## What other levers may also improve accuracy?

The [hasty-stop memo](Hasty-Stop-Words) identifies the mechanism (premature commit) that exemplars were meant to correct; the [confidence-routing memo](Confidence-Routing) shows the same simulated-vs-measured caveat applies to escalation. See the [verification page](Verification) for both measured/simulated comparisons.


---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
