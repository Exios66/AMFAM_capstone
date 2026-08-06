
**Research question:** If the classifier abstains on its lowest-confidence tail and a stronger model re-scores those images, how does accuracy change as a function of the escalate fraction (α) and cost?

**Formal write-up:** [`montecarlo/routing-abstention.qmd`](Routing-Abstention) · [`reports/monte_carlo/routing_abstention.md`](https://github.com/Exios66/AMFAM_capstone/blob/main/reports/monte_carlo/routing_abstention.md)


## What questions or uncertainties remain?

Two big assumptions are unmeasured: (1) that a 90%-accurate escalation model exists at 3× cost, and (2) that the confidence ordering is *calibrated* — that the model's low-confidence tail is genuinely more error-prone. The [verification study](Verification) measured a small escalation slice: base accuracy 0.667 vs escalated 0.625 — i.e., **no measured gain** on those 48 images, which undercuts the simulated +. This is the single most important open question for the routing claim.

## What other levers may also improve accuracy?

Where escalation under-delivers, [ensemble voting](Ensemble-Voting) and [few-shot exemplars](Exemplar-Mining) are complementary; the [verification memo](Verification) directly tests simulated-vs-measured for both routing and exemplars.


---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
