
**Research question:** What fraction of rows fail to produce a usable prediction, and does the retry/fallback pipeline keep the failure rate tolerable when extrapolated to 800 / 25,000 / 320,000 images?

**Formal write-up:** [`montecarlo/failure-pipeline.qmd`](Failure-Pipeline) · [`reports/monte_carlo/failure_pipeline.md`](https://github.com/Exios66/AMFAM_capstone/blob/main/reports/monte_carlo/failure_pipeline.md)


## What questions or uncertainties remain?

The model is fitted on qwen3.7-flash-specific failure data; other providers (gemini, kimi) have different transient/429 profiles and were not fitted. The 94.6% first-success rate will drift with provider status and prompt length (longer v11.8+ prompts push token caps). The residual failures are persistent, so no retry policy eliminates them — only a fundamentally different fallback (e.g., a cheaper non-reasoning model) would.

## What other levers may also improve accuracy?

Failure rows are separate from accuracy misses; the accuracy levers are covered in the [hardest-classes](Hardest-Classes), [ensemble](Ensemble-Voting), and [confidence-routing](Confidence-Routing) memos.


---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
