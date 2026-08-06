
**Research question:** What is the measured per-image cost of 16-class classification, and how does it extrapolate to 800 / 25,000 / 320,000 images across candidate models?

**Formal write-up:** [`cost/cost-estimation.qmd`](Cost-Estimation) · [`cost/cost-projections.qmd`](Cost-Projections) · [`docs/experiments/1pic_cost_estimation.md`](https://github.com/Exios66/AMFAM_capstone/blob/main/docs/experiments/1pic_cost_estimation.md)


## What questions or uncertainties remain?

Actuals depend on provider pricing, prompt caching hit rate, and reasoning-token volume — all of which drift. The single-image extrapolations assume linear token growth with image count; caching behavior at batch scale could push actuals lower. The next-n2-pro/grok/claude figures are single-image projections, not measured batch runs.

## What other levers may also reduce cost?

The [confidence-routing memo](Confidence-Routing) shows escalating only the low-confidence tail keeps cost at 1.02–1.8× while recovering accuracy — cheaper than full-model upgrades. [Ensemble voting](Ensemble-Voting) trades +4 *pp* accuracy for 3–25× cost, useful only where accuracy dominates budget.


---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
