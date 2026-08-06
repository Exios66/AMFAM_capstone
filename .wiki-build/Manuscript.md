
# Introduction {#sec-intro}

Automated document classification is a prerequisite for document intelligence at scale — routing invoices, resumes, legal filings, and archival records to the correct downstream process. The RVL-CDIP benchmark (Harley, 2015) provides a canonical 400,000-image corpus (16 classes, 25,000 images per class) drawn from the IIT-CDIP tobacco-litigation archive (Lewis, 2006), and has driven a decade of convolutional and transformer-based document classifiers. Those approaches share a common cost: each requires labeled training data and a fine-tuning pipeline.

This work asks whether a **zero-shot, prompt-engineered** alternative built from general-purpose vision-language models (VLMs) can match that performance envelope at a fraction of the engineering and cost overhead. Rather than fine-tune a model, we iteratively refine a structured classification prompt and evaluate each version against balanced slices of RVL-CDIP through Braintrust, with OpenRouter as the model gateway (OpenRouter, 2026; @braintrust). No training is performed; every accuracy gain is attributable to prompt design.

The contribution is three-fold. First, we show that prompt engineering alone moves exact-match accuracy on a fixed 160-image slice from **80.1% (v1) to 99.4% (v11.8)** — a +19.3 percentage-point gain with the same model and the same images — and verify with a paired bootstrap that this is not slice over-fitting. Second, we characterize generalization to larger slices (82.6% at 1,120 images) and compare five models on the same slice. Third, we subject the pipeline to Monte Carlo robustness analysis (Metropolis, 1949) — ensemble voting, confidence-gated routing, hasty-stop trigger words, failure-pipeline behavior, and few-shot exemplar mining — and report both simulated and measured outcomes. All data, figures, and interactive tools are committed to the companion website.

# Related Work {#sec-related}

**Document image classification.** The field spans handcrafted layout features, deep CNNs, and vision transformers. Harley et al. established the deep-CNN baseline on RVL-CDIP in 2015 (Harley, 2015); subsequent fine-tuned transformers exceed 90% top-1 accuracy on the full test set. All of these methods are supervised and require training data. The task is not confined to the academic benchmark: Raj et al. described a document classification and information-extraction framework specifically for insurance applications at American Family Insurance, validating the production relevance of the 16-class taxonomy we target (Raj GV, 2021).

**Thread 1 — Supervised multimodal pretraining (LayoutLM family).** The LayoutLM line injects layout and visual signals into transformer pretraining for visually-rich document understanding: LayoutLM adds 2D position embeddings to a masked language model (Xu, 2020); LayoutLMv2 adds a spatial-aware self-attention module and image embeddings to combine text, layout, and visual information (Xu, 2021); LayoutLMv3 simplifies this into a single unified text-image masked pretraining objective (Huang, 2022). Donut sidesteps OCR entirely with an OCR-free end-to-end transformer that reads the image directly (Kim, 2022). These models set the supervised state of the art on RVL-CDIP-derived tasks, but each requires task-specific fine-tuning on labeled data — precisely the cost our zero-shot pipeline avoids.

**Thread 2 — Non-neural document classifiers.** Cooney et al. showed that RVL-CDIP classification does not require deep learning at all: an end-to-end pipeline that extracts text and layout, then classifies via assignment optimization, achieves competitive 16-class accuracy with fully interpretable decision rules and no model training (Cooney, 2023). This work is a useful point of reference because, like our pipeline, it treats classification as a promptable decision problem rather than a learned feature problem — but it still requires OCR text extraction and hand-built rule templates.

**Thread 3 — Hybrid OCR + LLM pipelines.** A parallel line composes OCR with general-purpose language models. LMDX couples a document text extractor with an LLM to perform zero-shot information extraction and localization (Perot, 2024); ChatIE frames joint extraction as multi-turn chat to exploit LLM zero-shot ability (Wei, 2023); and Wang and Shen describe a production OCR-LLM framework for enterprise document extraction under copy-heavy conditions (Wang, 2025). These systems target extraction (field-level values), not 16-class document-type classification, but they establish that off-the-shelf LLMs can perform document reasoning without fine-tuning when given the right prompting scaffolding.

**Thread 4 — Small-model specialization.** A growing body of work shows that small, task-specialized models can approach frontier performance at a fraction of the cost. Extract-0 is a 7B-parameter model distilled specifically for document information extraction (Godoy, 2025); the Contextual Graph Transformer applies a small language model to engineering-document extraction (Reddy, 2025); Florence-2 introduces a unified sequence-to-sequence vision model that competes with much larger models on dense vision and document tasks (Xiao, 2024); Khan et al. fine-tune a vision-language model for engineering-drawing information extraction (Khan, 2024); and Christou and Tsoumakas report that sub-billion-parameter models rival frontier LLMs on relation extraction (Christou, 2026). The lesson we adopt is architectural: for a narrow, well-specified task, small models can dominate — a design point our cost analysis returns to (Section @sec-cost-results).

**Thread 5 — The unified small-model wave and cheap serving.** 2024–2025 saw compact general models designed to run locally at scale: SmolDocling (256M parameters) does end-to-end multimodal document conversion (Nassar, 2025); SmolVLM compresses a full VLM into a few billion parameters while retaining strong vision-language performance (Marafioti, 2025); and the Phi-4-mini, Gemma 3, Llama 3.2, Qwen2.5, SmolLM2, and Mistral 7B releases collectively established that small open models are viable deployment targets for document workloads (Abouelenin, 2025; @gemma3technical; @grattafiori2024llama3; @qwen252024; @benallal2025smollm2; @jiang2023mistral). Serving advances close the loop: GPTQ and AWQ quantize weights with minimal accuracy loss (Frantar, 2022; @lin2023awq); the GGUF format in llama.cpp makes quantized models portable to commodity hardware (Gerganov, 2023); speculative decoding accelerates inference without changing outputs (Leviathan, 2023); and PagedAttention removes the memory fragmentation that blocks long-context serving (Kwon, 2023).

**Position of this work.** The threads above optimize one of two axes — either supervised accuracy (Threads 1–2) or local cost at fixed quality (Threads 3–5). Our contribution sits on the third axis the literature largely assumes away: **whether prompt engineering alone can move a general-purpose hosted VLM's accuracy from roughly-chance to near-ceiling on a fixed 16-class taxonomy, with no training, no OCR, no fine-tuning, and no model swap.** We deliberately do not claim an extraction system or a "small document analyzer"; we measure a pure zero-shot classifier and report exactly what a prompt-only intervention buys — and where it stops generalizing.

**Vision-language models for OCR-free document understanding.** Recent VLM families — Qwen2.5-VL (Bai, 2025), Qwen3 (Qwen, 2025), Gemini 2.5 (Google, 2025), and the 2026 generation of reasoning-native models including Claude Fable 5 (Anthropic, 2026), Nex-N2-Pro (Nex, 2026), Grok 4.5 (xAI, 2026), and Kimi K3 (Moonshot, 2026) — perform joint layout-and-text understanding, enabling zero-shot classification from an image alone. In this work the models are accessed via OpenRouter, a unified API gateway (OpenRouter, 2026), and evaluated on Braintrust, an experiment-tracking and scoring platform (Braintrust, 2026).

**Robustness methodology.** Ensemble majority voting is grounded in Condorcet's jury theorem (de Condorcet, 1785); bootstrap resampling provides paired confidence intervals (Efron, 1993); and the failure pipeline analysis follows the Monte Carlo framework of Metropolis and Ulam (Metropolis, 1949).

# Methods {#sec-methods}

## Dataset and sampling {#sec-data}

RVL-CDIP contains 320,000 training, 40,000 validation, and 40,000 test images at up to 1,000 px per side (Harley, 2015). We sample **deterministic, class-balanced slices** from the Hugging Face parquet mirrors: every slice holds the same number of images per class × 16 classes, seeded with `random.Random(seed)`, and de-duplicated in rendered-pixel space (MD5 of the normalized grayscale PNG) both against prior slices and internally. Images are converted to 1024×1024 grayscale PNGs with aspect-ratio-preserving white padding. Slices used in this study: **160** (10/class), **320** (20/class), **480** (30/class), **800** (50/class), and **1,120** (70/class). Slices are uploaded to Braintrust as row attachments with ground-truth labels and provenance metadata.

## Model and prompt versions {#sec-model}

The primary model is the Qwen3-family `qwen3.7-flash` accessed through OpenRouter (OpenRouter, 2026), with comparisons against `qwen3.5-35b-a3b`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, and `kimi-k3`. Prompts are versioned append-only in `src/prompts.py` (v0–v17.2). Each version specifies the 16 output labels, a mandatory reasoning scratchpad, and an ordered 14-check disambiguation cascade. The current default, v17.2, is 42,530 characters and instructs the model to "judge each page by its FUNCTION, not its subject matter" and to stop at the first check with concrete, quotable evidence.

::: {.callout-note title="Excerpt — PROMPT_V17_2 (opening instructions)"}
> You classify scanned business documents (tobacco-industry archive, 300 DPI grayscale) into exactly one of 16 categories.
>
> Judge each page by its **FUNCTION**, not its subject matter: a page full of technical data can still be a form, and a page about money can still be a form — but a bill is a bill even when it is printed on a form. Do not rush to the label that matches the page's subject matter — deliberate through the checks below, in order, and commit to the FIRST one with strong, concrete evidence you can actually read on the page (a header, a field label, a masthead, an approval block — not a guess from the topic). Once an earlier check matches, later checks do not override it.
>
> Before answering, work through the page in a `<scratchpad>`. … Walk checks 1–14 below IN ORDER. For each check, before moving to the next one, briefly state: what specific evidence for this check IS present on the page … or "none" if nothing supports it. If evidence is present: STOP HERE. … After the scratchpad, output your final answer.
:::

## Evaluation harness {#sec-harness}

Each prompt version is evaluated as a Braintrust experiment against a slice. The runner (`braintrust_openrouter_input.py`) wraps an OpenAI client pointed at OpenRouter with `braintrust.wrap_openai()`, runs at `max_concurrency = 8`, and retries transient provider failures up to 3 times, growing `max_tokens` on truncation up to a 32,768 cap. Accuracy is **exact match**: `output.strip().lower() == expected_class`, scored 1.0/0.0 per row. A separate failure scorer flags `ERROR:` rows. Cost is recorded per row from OpenRouter's billed `usage.cost`. Near-miss (runner-up = expected while predicted ≠ expected) is computed locally from the manifest.

## Cost accounting {#sec-cost}

We record two cost measures per run: **expected cost** = (prompt tokens × input price + completion tokens × output price) / 1e6, a list-price projection from measured token counts, and **actual cost** = the sum of OpenRouter's billed per-row `usage.cost`. Per-model single-image metrics are captured by running one image per model and recording the actual API response (tokens and `usage.cost`); input/output per-million-token prices are then **derived from those measured metrics**, so defaults reflect observed behavior rather than list prices.

## Monte Carlo analyses {#sec-montecarlo}

All simulations follow the same pattern: draw bootstrap samples from the committed per-image corpus (`reports/monte_carlo/corpus.jsonl`, 1,912 rows), compute the statistic on each draw, and report the mean and 95% interval (Efron, 1993). We analyze (a) **ensemble voting** — committees of *K* independent reads with majority vote (de Condorcet, 1785); (b) **confidence-gated escalation** — routing the lowest-confidence α fraction to a stronger model at 3× cost; (c) **hasty-stop triggers** — accumulated local effects (ALE) of reasoning-trace features on correctness; (*d*) **failure pipeline** — a Markov model of retry/fallback behavior at scale; and (e) **few-shot exemplar mining** — injecting exemplars for the top confusion pairs.

# Results {#sec-results}

## Prompt engineering is the dominant lever {#sec-arc}

On the fixed 160-image slice with `qwen3.7-flash`, exact-match accuracy climbs monotonically in the aggregate from **80.1% (v1)** to **99.4% (v11.8, 157/158)**, with v10's disambiguation cascade contributing the single largest step (+14.0 *pp* over v9). The paired bootstrap confirms transfer: on 898 shared images, v11.8 outperforms the v0 baseline by **+13.0 ***pp** (0.732 → 0.862, 95% **CI** [0.101, 0.159], *P*(v0 wins) = 0.000); on 155 shared images, v17 outperforms v0 by **+28.4 **pp* (0.677 → 0.961, *CI* [0.213, 0.361]) (Efron, 1993).

![Exact-match accuracy of `qwen3.7-flash` on the 160-image slice across prompt versions. The full gain (+19.3 *pp*) requires no model or data change.](figures/f1_accuracy_arc.svg){#fig-arc}

::: {#tbl-arc}
| Version | What changed | Accuracy |
|:---|:---|---:|
| v1 | baseline class definitions | 80.1% (125/156) |
| v4 | first disambiguation rules | 83.5% (132/158) |
| v7 | presentation cover/slide rules | 91.1% (144/158) |
| v10 | full disambiguation cascade | 97.5% (154/158) |
| v11 | estimate-vs-bill rule | 98.7% (156/158) |
| v11.8 | form-vs-budget + memo-vs-letter fixes | 99.4% (157/158) |
| v17.2 | 14-check verification cascade | 96.2–98.7% (slice-dependent) |

Key arc points (qwen3.7-flash, 160-image slice).
:::

## Generalization to larger slices {#sec-falloff}

Accuracy at v11.8 attenuates with slice size: **99.4% at 160 → 87.2% at 320 → 89.1% at 480 → 83.1% at 800 → 82.6% at 1,120**. The falloff is consistent with larger slices exposing more intra-class layout variation and noisier scans rather than any prompt-specific failure; near-misses (runner-up = expected) account for 36.9% of the 1,120-image misses, indicating a recoverable fraction of the residual error.

![v11.8 accuracy as a function of slice size. Error bars omitted for clarity; see the report files for per-run counts.](figures/f2_generalization_falloff.svg){#fig-falloff}

## Model comparison on the 160-image slice {#sec-models}

![Best-per-model accuracy with 95% Wilson score intervals on the 160-image slice.](figures/f3_model_comparison.svg){#fig-models}

::: {#tbl-models}
| Model | Prompt | Accuracy | 95% *CI* |
|---|---:|---:|---:|
| `qwen3.7-flash` | v11.8 | 98.7% (157/159) | [95.5, 99.7] |
| `qwen3.5-35b-a3b` | v11.8 | 98.7% (155/157) | [95.5, 99.6] |
| `gemini-2.5-flash-lite` | v11.8 | 86.9% (139/160) | [80.8, 91.3] |
| `gemini-2.5-flash` | best | 74.4% (119/160) | [67.1, 80.5] |
| `kimi-k3` | best | 70.0% (112/160) | [62.5, 76.6] |

Model comparison on the 160-image slice (Wilson intervals).
:::

The best confusion matrix (Fig. @fig-confusion) is concentrated on the diagonal; the highest-confusion pairs (budget/invoice, form boundaries, memo/letter) are precisely the pairs the prompt's check cascade targets.

![Confusion matrix for the best run (qwen3.7-flash, v11.8, 160-image slice), row-normalized to 100%.](figures/f4_confusion_heatmap.svg){#fig-confusion}

![Per-class accuracy on the 1120-image run (overall 82.6%). Colors: ≥90% green, 70–90% amber, <70% red.](figures/f5_per_class_accuracy.svg){#fig-perclass}

## Cost {#sec-cost-results}

Measured steady-state cost for the primary model is **≈ $0.0004 per image**, and the 1,120-image run billed **$0.4937** versus an expected list-price projection of **$0.6815** — actual cost runs below list projection across runs. Per-model OpenRouter-reported single-image metrics are shown in Table @tbl-cost and Fig. @fig-cost. The derived input/output prices reproduce the measured billed costs, and the cost calculator page exposes these as interactive sliders.

![OpenRouter-reported per-image cost (left) and linear scale-up to 800 / 25k / 320k images (right).](figures/f6_cost_projections.svg){#fig-cost}

::: {#tbl-cost}
| Model | Prompt in / out tokens | Billed cost / image | Derived $/*M* in / out |
|---|---:|---:|---:|
| `nex-agi/nex-n2-pro` | 13,231 / 5 | $0.00331 | $0.25 / $1.00 |
| `moonshotai/kimi-k3` | 11,996 / 20 | $0.00393 | $0.30 / $15.00 |
| `x-ai/grok-4.5` | 2,954 / 53 | $0.00601 | $1.93 / $6.00 |
| `anthropic/claude-fable-5` | 5,313 / 6 | $0.05343 | $10.00 / $50.00 |

Per-model single-image usage and derived prices, from OpenRouter-reported metrics (`docs/experiments/1pic_cost_estimation.md`). The primary classifier (`qwen3.7-flash`) is omitted as it is billed at ≈ $0.0004/image.
:::

## Monte Carlo robustness {#sec-mc-results}

**Ensemble voting.** Majority vote across *K* independent reads raises simulated accuracy from **0.821 (***K*** = 1)** to **0.863 (***K*** = 25)**, with diminishing returns beyond **K** = 5–7 (Fig. @fig-ensemble). The gain is consistent with Condorcet's theorem when per-read accuracy exceeds 0.5 (de Condorcet, 1785).

![Simulated majority-vote accuracy with 95% *CI* across committee size *K* (2,000 simulations of 1,512 images).](figures/f7_ensemble_vs_k.svg){#fig-ensemble}

**Confidence-gated routing.** Escalating the lowest-confidence α fraction to a stronger model (assumed 0.90 accuracy, 3× cost) peaks at **0.919 simulated accuracy at α = 40% and 1.8× cost** (Fig. @fig-routing). The measured escalation slice did **not** reproduce the simulated gain (base 0.667 → escalated 0.625 on 48 low-confidence images), an important negative result discussed in Section @sec-limitations.

![Simulated escalation accuracy (solid) and cost factor (dashed) vs the escalation fraction α. The measured escalation slice regressed (0.667 → 0.625), diverging from simulation.](figures/f8_routing.svg){#fig-routing}

**Hasty-stop triggers.** Baseline traces stop at check 9.4 of 14, with a 17.1% overall error rate. ALE of the stop-position feature identifies trigger words — *minutes*, *routing*, *variance*, *products*, *meeting*, *survey* — that push the model to commit early and are associated with elevated error (Fig. @fig-hasty). Prompt edits targeting these words are a candidate next iteration.

![Top hasty-stop trigger words by hasty-score (early stop + elevated error, frequency-weighted).](figures/f9_hasty_stop.svg){#fig-hasty}

**Failure pipeline.** The fitted retry model (P(first success) = 0.946) shows the current configuration — 3 tries, 2 API keys, fallback on — reduces the simulated pipeline failure rate from the observed 2.716% (no pipeline) to **0.114%**, with 364 expected failures at 320,000 images (Fig. @fig-failure, left panel).

**Exemplar mining negative result.** The exemplar simulation projected flipping 4.27% of the corpus error pool; the measured 48-image exemplar slice **regressed** (v18 64.6% vs v17.2 68.8%, Δ = −4.2 **pp**) (Fig. @fig-failure, right panel). The appendix appended to v18 did not help and slightly hurt — a caution against trusting simulation without measurement.

![Left: simulated pipeline failure rate by configuration (fallback collapses 2.86% → 0.114%). Right: measured vs simulated exemplar gain.](figures/f10_failure_and_exemplar.svg){#fig-failure}

::: {#tbl-mc}
| Analysis | Key result | Measured | Simulated |
|---|---|---:|---:|
| Ensemble voting | **K** = 25 vs **K** = 1 | — | 0.863 vs 0.821 |
| Routing | α = 40% escalation | 0.667 → 0.625 | 0.919 @ 1.8× |
| Hasty-stop | baseline stop pos. | 9.4/14, 17.1% err | ALE curves |
| Failure pipeline | fallback on vs off | 2.716% (no pipeline) | 0.114% |
| Exemplars | top confusion pairs | −4.2 **pp* (v18) | +4.27% of error pool |

Summary of Monte Carlo analyses (`reports/monte_carlo/`).
:::

# Discussion {#sec-discussion}

Prompt engineering is the cheapest and most transferable lever we tested: the +19.3 *pp* arc cost nothing beyond prompt text and is verified against the same images with the same model. The attenuation on larger slices (82.6% at 1,120) is the honest headline — the curated slice is cleaner than the full benchmark — but 82.6% with zero training remains useful for triage, and near-miss analysis identifies a recoverable fraction. Cost is a decisive advantage: at ≈ $0.0004/image and with measured rather than projected billing, even 320,000-image runs are budgetable. The two Monte Carlo negative results — routing and exemplars — are as informative as the positive ones: simulations that assume an abstract "stronger model" or an optimistic exemplar efficacy do not survive contact with measurement, reinforcing the paired-measurement discipline used throughout this project.

The interactive pages (Cost Calculator and Experiment Explorer) and the data layer that feeds them are intended as reproducibility artifacts: every number in this manuscript is traceable to a committed markdown report.

# Limitations {#sec-limitations}

- **Slice bias.** All accuracy figures are on balanced slices of the 100-image/class mirror, not the full 320,000-image RVL-CDIP test set; the mirror itself is a filtered subset.
- **Single-slice comparisons.** Model comparisons use the 160-image slice; statistical power is limited, as the overlapping CIs in Table @tbl-models indicate.
- **Routing negative result.** The escalation simulation assumed a 0.90-accuracy escalator; the measured slice used the same model at higher reasoning effort, which did not deliver the assumed accuracy (0.625), so the simulated 0.919 should not be read as a deployment promise.
- **Exemplar negative result.** Exemplar selection and prompt injection for v18 were single-shot; different injection styles or pair coverage might differ.
- **Version attribution.** Prompt versions bundle multiple edits; a factorial single-edit study would decompose the cascade's contribution.
- **Cost extrapolation.** Linear scale-up ignores provider pricing changes, batch discounts, and cache effects; the interactive calculator exposes these assumptions.

# Conclusion {#sec-conclusion}

A zero-shot, prompt-engineered VLM pipeline classifies RVL-CDIP document types at 99.4% on a curated slice and 82.6% at 1,120 images, at ≈ $0.0004/image, with no training data or fine-tuning. Monte Carlo analysis bounds the ensemble, routing, and reliability frontiers and surfaced two measured negative results that refine the design space. The full methodology, versioned prompts, all slices, evaluation harness, and interactive cost/experiment tools are publicly reproducible at [github.com/Exios66/AMFAM_capstone](https://github.com/Exios66/AMFAM_capstone).

# Acknowledgements {#sec-acknowledgements}

We thank our Project Advisor, **Siddharth Suresh**, for his mentorship and guidance throughout the project. We thank the Data Science Hub (DSHB) at the University of Wisconsin–Madison for the capstone program that made this work possible. We thank the University of Wisconsin–Madison Center for High Throughput Computing (CHTC) for computing resources and consultation. We thank **Dr. Timothy Rogers** for his guidance and instruction, and **Dr. Caitlin Roa**, DSHB Program Director, for her guidance and advocacy for research funding. Any errors are our own.

# References

## References

- Abouelenin, Abdelrahman and others (2025). Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs. *arXiv preprint arXiv:2503.01743*.
- Anthropic (2026). Claude Fable 5: Model Card and System Card. Model documentation.
- Artifex Software (2026). PyMuPDF: Python Bindings for MuPDF. Open-source software.
- Bai, Shuai and others (2025). Qwen2.5-VL Technical Report. *arXiv preprint arXiv:2502.13923*.
- Ben Allal, Loubna and Lozhkov, Anton and Bakouch, Elie and Bl\'azquez, Gabriel Mart\'in and Penedo, Guilherme and Tunstall, Lewis and Marafioti, Andr\'es and Kydl\'i\vc (2025). SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model. *arXiv preprint arXiv:2502.02737*.
- Braintrust (2026). Braintrust: The AI-Native Eval Platform. Software platform.
- Christou, Despina and Tsoumakas, Grigorios (2026). Sub-Billion, Super-Frontier: Small Language Models Rival Zero-Shot Frontier LLMs on General and Literary Relation Extraction. *arXiv preprint arXiv:2606.22606*.
- Cooney, Ciaran and Cavadas, Joana and Madigan, Liam and Savage, Bradley and Heyburn, Rachel and O'Cuinn, Mairead (2023). End-to-End Document Classification and Key Information Extraction using Assignment Optimization. *arXiv preprint arXiv:2306.00750*.
- de Condorcet, Nicolas (1785). *Essai sur l'application de l'analyse \`a la probabilit\'e des d\'ecisions rendues \`a la pluralit\'e des voix*. L'Imprimerie Royale.
- Efron, Bradley and Tibshirani, Robert J. (1993). *An Introduction to the Bootstrap*. Chapman \& Hall/CRC.
- Frantar, Elias and Ashkboos, Saleh and Hoefler, Torsten and Alistarh, Dan (2022). GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers. *arXiv preprint arXiv:2210.17323*.
- Freedesktop.org (2026). Poppler: PDF Rendering Library. Open-source software.
- Gemma Team (2025). Gemma 3 Technical Report. *arXiv preprint arXiv:2503.19786*.
- Gerganov, Georgi (2023). llama.cpp: LLM Inference in C/C++ (GGUF format). Open-source software.
- Godoy, Henrique and others (2025). Extract-0: A Specialized Language Model for Document Information Extraction. *arXiv preprint arXiv:2509.22906*.
- Google DeepMind (2025). Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long-Context Understanding. Model documentation.
- Grattafiori, Aaron and others (2024). The Llama 3 Herd of Models. *arXiv preprint arXiv:2407.21783*.
- Harley, Adam W. and Ufkes, Alex and Derpanis, Konstantinos G. (2015). Evaluation of Deep Convolutional Nets for Document Image Classification and Retrieval. In *Proceedings of the 13th International Conference on Document Analysis and Recognition (ICDAR)*. https://doi.org/10.1109/ICDAR.2015.7333910
- Huang, Yupan and Lv, Tengchao and Cui, Lei and Lu, Yutong and Wei, Furu (2022). LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking. In *Proceedings of the 30th ACM International Conference on Multimedia* (pp. 4083--4091). https://doi.org/10.1145/3503161.3548112
- Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and de las Casas, Diego and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and Lavaud, L\'elio Renard and Lachaux, Marie-Anne and Stock, Pierre and Le Scao, Teven and Lavril, Thibaut and Wang, Thomas and Lacroix, Timoth\'ee and El Sayed, William (2023). Mistral 7B. *arXiv preprint arXiv:2310.06825*.
- Khan, Muhammad Tayyab and Chen, Lequn and Ng, Ye Han and Feng, Wenhe and Tan, Nicholas Yew Jin and Moon, Seung Ki (2024). Fine-Tuning Vision-Language Model for Automated Engineering Drawing Information Extraction. *arXiv preprint arXiv:2411.03707*.
- Kim, Geewook and Hong, Teakgyu and Yim, Moonbin and Park, Jinyoung and Yim, Jinyeong and Hwang, Wonseok and Yun, Sangdoo and Han, Dongyoon and Park, Seunghyun (2022). OCR-Free Document Understanding Transformer. In *Computer Vision -- ECCV 2022* (pp. 498--517).
- Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion (2023). Efficient Memory Management for Large Language Model Serving with PagedAttention. In *Proceedings of the 29th Symposium on Operating Systems Principles (SOSP)* (pp. 611--626).
- Leviathan, Yaniv and Kalman, Matan and Matias, Yossi (2023). Fast Inference from Transformers via Speculative Decoding. In *Proceedings of the 40th International Conference on Machine Learning (ICML)* (pp. 19274--19289).
- Lewis, David and Agam, Gady and Argamon, Shlomo and Frieder, Ophir and Grossman, David and Heard, Jack (2006). Building a Test Collection for Complex Document Information Processing. In *Proceedings of the 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)* (pp. 665--666). https://doi.org/10.1145/1148170.1148307
- Lhoest, Quentin and others (2021). Datasets: A Community Library for Natural Language Processing. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing: System Demonstrations* (pp. 175--184). https://doi.org/10.18653/v1/2021.emnlp-demo.21
- Lin, Ji and Tang, Jiaming and Tang, Haotian and Yang, Shang and Dang, Xingyu and Han, Song (2023). AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration. *arXiv preprint arXiv:2306.00978*.
- Marafioti, Andr\'es and Zohar, Orr and Farr\'e, Miquel and Noyan, Merve and Bakouch, Elie and Cuenca, Pedro and Zakka, Cyril and Ben Allal, Loubna and Lozhkov, Anton and Tazi, Nouamane and Srivastav, Vaibhav and Lochner, Joshua and Larcher, Hugo and Morlon, Mathieu and Tunstall, Lewis and von Werra, Leandro and Wolf, Thomas (2025). SmolVLM: Redefining small and efficient multimodal models. *arXiv preprint arXiv:2504.05299*.
- Metropolis, Nicholas and Ulam, Stanislaw (1949). The Monte Carlo Method. *Journal of the American Statistical Association*, *44*, 335--341. https://doi.org/10.1080/01621459.1949.10483310
- Moonshot AI (2026). Kimi K3: Model Overview. Model documentation.
- Nassar, Ahmed and Marafioti, Andres and Omenetti, Matteo and Lysak, Maksym and Livathinos, Nikolaos and Auer, Christoph and Morin, Lucas and de Lima, Rafael Teixeira and Kim, Yusik and Gurbuz, A. Said and Dolfi, Michele and Farr\'e, Miquel and Staar, Peter W. J. (2025). SmolDocling: An ultra-compact vision-language model for end-to-end multi-modal document conversion. *arXiv preprint arXiv:2503.11576*.
- Nex AGI (2026). Nex-N2-Pro: Agentic MoE Model Card. Model documentation.
- OpenRouter (2026). OpenRouter: Unified Interface for LLM APIs. Software platform.
- Perot, Vincent and Kang, Kai and Luisier, Florian and Su, Guolong and Sun, Xiaoyu and Boppana, Ramya Sree and Wang, Zilong and Wang, Zifeng and Mu, Jiaqi and Zhang, Hao and Lee, Chen-Yu and Hua, Nan (2024). LMDX: Language Model-based Document Information Extraction and Localization. In *Findings of the Association for Computational Linguistics: ACL 2024* (pp. 15140--15168). https://doi.org/10.18653/v1/2024.findings-acl.899
- Qwen Team (2025). Qwen3 Technical Report.
- Raj GV, Ananth and You, Qian and Bunch, Eric and Kim, James and Santosh, Marepally and Fung, Glenn (2021). Document Classification and Information Extraction Framework for Insurance Applications. In *Proceedings of the 20th IEEE International Conference on Machine Learning and Applications (ICMLA)*.
- Reddy, Karan and Pal, Mayukha (2025). Contextual Graph Transformer: A Small Language Model for Enhanced Engineering Document Information Extraction. *arXiv preprint arXiv:2508.02532*.
- Smith, Ray (2007). An Overview of the Tesseract OCR Engine. *Proceedings of the Ninth International Conference on Document Analysis and Recognition (ICDAR)*, *2*, 629--633. https://doi.org/10.1109/ICDAR.2007.4376991
- Wang, Zilong and Shen, Xiaoyu (2025). Hybrid OCR-LLM Framework for Enterprise-Scale Document Information Extraction Under Copy-heavy Task. *arXiv preprint arXiv:2510.10138*.
- Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan (2023). ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT. *arXiv preprint arXiv:2302.10205*.
- xAI (2026). Grok 4.5: Documentation. Model documentation.
- Xiao, Bin and Wu, Haiping and Xu, Weijian and Dai, Xiyang and Hu, Houdong and Lu, Yifan and Zeng, Michael and Liu, Chen-Liang and Yuan, Lu (2024). Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 4818--4829).
- Xu, Yang and Xu, Yiheng and Lv, Tengchao and Cui, Lei and Wei, Furu and Wang, Guoxin and Lu, Yijuan and Florencio, Dinei and Zhang, Cha and Che, Wanxiang and Zhang, Min and Zhou, Lidong (2021). LayoutLMv2: Multi-modal Pre-training for Visually-Rich Document Understanding. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)* (pp. 2579--2591). https://doi.org/10.18653/v1/2021.acl-long.201
- Xu, Yiheng and Li, Minghao and Cui, Lei and Huang, Shaohan and Wei, Furu and Zhou, Ming (2020). LayoutLM: Pre-training of Text and Layout for Document Image Understanding. In *Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining* (pp. 1192--1200). https://doi.org/10.1145/3394486.3403172
- Yang, An and others (2024). Qwen2.5 Technical Report. *arXiv preprint arXiv:2412.15115*.

---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
