
**Research question:** Holding the prompt and the 160-image slice fixed, how do the candidate OpenRouter vision models rank on exact-match accuracy?

**Formal write-up:** [`results/experiment-log.qmd`](Experiment-Log) · [`docs/experiments/experiment_log.md`](https://github.com/Exios66/AMFAM_capstone/blob/main/docs/experiments/experiment_log.md)


## What questions or uncertainties remain?

Only qwen3.7-flash was run on the full prompt ladder; the other models were evaluated on fewer versions (kimi-k3 only v1; gemini only v3/v4/v11.8). Whether a v17.2-era prompt would close the gemini/qwen gap is untested. The 160-image sample is small (10/class) — per-model differences of a few points are within sampling error; a 320+ image head-to-head is needed for decisive ranking.

## What other levers may also improve model selection?

The [confidence-routing memo](Confidence-Routing) uses a stronger escalation model only on the low-confidence tail; the [ensemble memo](Ensemble-Voting) tests whether combining multiple model opinions (majority vote) beats any single model.


---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
