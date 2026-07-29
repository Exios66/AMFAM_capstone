# Braintrust Prompt Evaluation Results

## Experiment: `moonshotai/kimi-k3` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785257772  
**Link:** https://www.braintrust.dev/app/DSHB_amfam_capstone_2026/p/AMFAM-Doc-Classification/experiments/main-1785257772  
**Dataset:** `fixed_size_sampled/images/` (1024×1024 padded PNGs)  
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`  
**Settings:** `max_tokens=500`, `temperature=0.1`
**image size:** `1024×1024`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **70.00%** (112/160 correct) |
| Prompt tokens (avg) | 1,768.89 |
| Prompt cached tokens (avg) | 872.80 |
| Completion tokens (avg) | 171.51 |
| Completion reasoning tokens (avg) | 156.02 |
| Total tokens (avg) | 1,940.41 |
| Duration (avg) | 106.74s |
| LLM duration (avg) | 10.08s |
| Time to first token (avg) | 10.06s |
| Errors | 0 |

### Notes

- First run (main-1785255418) scored 0% due to `max_tokens=20` — reasoning model used all tokens on hidden reasoning, leaving nothing for output.
- Bumping to `max_tokens=500` resolved the issue.
- ~156 of ~171 completion tokens are hidden reasoning tokens (not visible in output).
- 48 misclassifications need investigation in Braintrust UI to identify confused class pairs.
- Images resized to 1024×1024 (vs original full-res) significantly reduces prompt tokens (1,769 vs 11,996 in original test).

### Cost Projections (Kimi K3, `max_tokens=500`, 1024×1024 images)

**Pricing:** $0.30/M input tokens, $15.00/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 1,415,112 | 137,208 | 1,552,320 | **$2.48** |
| 25,000 | 44,222,250 | 4,287,750 | 48,510,000 | **$64.74** |
| 320,000 | 566,044,800 | 54,883,200 | 620,928,000 | **$823.57** |

**vs. Original Kimi K3 estimate (full-res images, `max_tokens=20`):** $1,257.98 for 320K — resizing to 1024×1024 saves ~$434.

---

## Experiment: `google/gemini-2.5-flash` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785265188  
**Link:** https://www.braintrust.dev/app/DSHB_amfam_capstone_2026/p/AMFAM-Doc-Classification/experiments/main-1785265188  
**Dataset:** `fixed_size_sampled/images/` (1024×1024 padded PNGs)  
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`  
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`  
**Image size:** `1024×1024`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **74.38%** (119/160 correct) |
| Prompt tokens (avg) | 1,637 |
| Prompt cached tokens (avg) | 8.17 |
| Completion tokens (avg) | 415.64 |
| Completion reasoning tokens (avg) | 413.82 |
| Total tokens (avg) | 2,052.64 |
| Duration (avg) | 48.10s |
| LLM duration (avg) | 4.60s |
| Time to first token (avg) | 4.58s |
| Errors | 0 |

### Notes

- +4.38% accuracy over Kimi K3 (74.38% vs 70.00%) with 13 improvements and 6 regressions.
- Reasoning tokens are visible in Braintrust UI metadata for debugging misclassifications.
- 2.2x faster than Kimi K3 (48s vs 107s avg duration per image).
- More completion tokens (416 vs 172) due to visible reasoning chain, but cheaper output pricing.
- 41 misclassifications to investigate in Braintrust UI.

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 1024×1024 images)

**Pricing:** $0.15/M input tokens, $0.60/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 1,309,600 | 332,512 | 1,642,112 | **$0.40** |
| 25,000 | 40,925,000 | 10,391,000 | 51,316,000 | **$12.37** |
| 320,000 | 523,840,000 | 133,004,800 | 656,844,800 | **$158.38** |

**vs. Kimi K3 at 320K:** $158 vs $824 — Gemini 2.5 Flash is **~5.2x cheaper** with higher accuracy.

---

## Experiment: `google/gemini-2.5-flash` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785270444
**Dataset:** `2550x3300_10perclass_160/images/` (2550×3300 padded PNGs, 300 DPI)
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`
**Image size:** `2550×3300`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **73.75%** (118/160 correct) |
| Prompt tokens (avg) | 3,701.00 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 418.19 |
| Total tokens (avg) | 4,119.19 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Notes

- Switching from 1024×1024 to full-res 2550×3300 doubled prompt tokens (1,637 → 3,701) but accuracy dropped slightly (74.38% → 73.75%), suggesting higher resolution does not help and may add noise.
- Cost per image roughly doubled vs 1024×1024 ($0.64 vs $0.40 for 800 images) with no accuracy gain — 1024×1024 is the better cost/performance tradeoff.

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 2550×3300 images)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 2,960,800 | 334,555 | 3,295,355 | **$0.64** |
| 25,000 | 92,525,000 | 10,454,843 | 102,979,843 | **$20.15** |
| 320,000 | 1,184,320,000 | 133,822,000 | 1,318,142,000 | **$257.94** |

---

## Experiment: `google/gemini-2.5-flash` — 800 Images (50 per class × 16 classes)

**Experiment ID:** main-1785272634
**Dataset:** `2550x3300_50perclass_800/images/` (2550×3300 padded PNGs, 300 DPI)
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py` (baseline, pre-disambiguation)
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`
**Image size:** `2550×3300`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **72.88%** (583/800 correct) |
| Prompt tokens (avg) | 3,701.00 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 417.38 |
| Total tokens (avg) | 4,118.38 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Notes

- Scaling from 160 → 800 images held steady at ~73% accuracy, confirming the 10-per-class sample is representative.
- `form` (30%), `presentation` (36%), and `specification` (46%) are the worst-performing classes — `scientific_report` is massively over-predicted with 64 false positives across 7 classes.
- Reasoning trace analysis revealed the model confuses fax cover sheets with memos, specs with scientific reports, and press releases with news articles — leading to the disambiguation prompt update.
- See `docs/50pic_cost_est_tst.md` for full per-class accuracy breakdown and confused pairs analysis.
- See `docs/confusion_matrix_main-1785272634.md` for confusion matrix.
- See `docs/misclassification_reasoning_main-1785270444.md` for reasoning trace analysis.

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 2550×3300 images)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 2,960,800 | 333,902 | 3,294,701 | **$0.64** |
| 25,000 | 92,525,000 | 10,434,437 | 102,959,437 | **$20.14** |
| 320,000 | 1,184,320,000 | 133,560,800 | 1,317,880,799 | **$257.78** |

---

## Experiment: `google/gemini-2.5-flash` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785277280
**Dataset:** 2550×3300 padded PNGs, 300 DPI
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`
**Image size:** `2550×3300`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **83.75%** (134/160 correct) |
| Prompt tokens (avg) | 4,368.00 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 412.39 |
| Total tokens (avg) | 4,780.39 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 2550×3300 images)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 3,494,400 | 329,915 | 3,824,315 | **$0.72** |
| 25,000 | 109,200,000 | 10,309,843 | 119,509,843 | **$22.57** |
| 320,000 | 1,397,760,000 | 131,966,000 | 1,529,726,000 | **$288.84** |

### Notes

- **+10% accuracy jump** (73.75% → 83.75%) from adding disambiguation rules to the prompt — largest single improvement across all experiments.
- Prompt tokens increased from 3,701 → 4,368 due to longer prompt with disambiguation rules, but the accuracy gain far outweighs the ~$0.08 cost increase per 800 images.
- Only 26 errors remain (down from 42). Top confusion is now `presentation → file_folder` (4 errors) where cover/divider pages get misclassified.
- See `docs/confusion_matrix_main-1785277280.md` and `docs/misclassification_reasoning_main-1785277280.md` for detailed breakdown.

---

## Experiment: `google/gemini-2.5-flash` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785361122
**Dataset:** 1024×1024 padded PNGs
**Prompt:** `CLASSIFICATION_PROMPT` v1 (with disambiguation rules)
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`
**Image size:** `1024×1024`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **85.00%** (136/160 correct) |
| Prompt tokens (avg) | 2,304.00 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 413.77 |
| Total tokens (avg) | 2,717.77 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Cost Projections (`google/gemini-2.5-flash`, `max_tokens=1024`, 1024×1024 images)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 1,843,200 | 331,015 | 2,174,215 | **$0.48** |
| 25,000 | 57,600,000 | 10,344,218 | 67,944,218 | **$14.85** |
| 320,000 | 737,280,000 | 132,406,000 | 869,686,000 | **$190.04** |

---

## Experiment: `moonshotai/kimi-k3` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785362441
**Dataset:** 1024×1024 padded PNGs
**Prompt:** `CLASSIFICATION_PROMPT` v1 (with disambiguation rules)
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`
**Image size:** `1024×1024`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **85.00%** (136/160 correct) |
| Prompt tokens (avg) | 2,454.26 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 91.55 |
| Total tokens (avg) | 2,545.81 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Cost Projections (`moonshotai/kimi-k3`, `max_tokens=1024`, 1024×1024 images)

**Pricing:** $0.30/M input tokens, $15.00/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 1,963,409 | 73,240 | 2,036,650 | **$1.69** |
| 25,000 | 61,356,562 | 2,288,750 | 63,645,312 | **$52.74** |
| 320,000 | 785,364,000 | 29,296,000 | 814,660,000 | **$675.05** |

---

## Experiment: `google/gemini-2.5-flash` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785364141
**Dataset:** 1024×1024 padded PNGs
**Prompt:** `CLASSIFICATION_PROMPT` v2 (expanded disambiguation rules)
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`
**Image size:** `1024×1024`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **85.00%** (136/160 correct) |
| Prompt tokens (avg) | 2,674.00 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 412.06 |
| Total tokens (avg) | 3,086.06 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Cost Projections (`google/gemini-2.5-flash`, `max_tokens=1024`)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 2,139,200 | 329,645 | 2,468,845 | **$0.52** |
| 25,000 | 66,850,000 | 10,301,406 | 77,151,406 | **$16.21** |
| 320,000 | 855,680,000 | 131,858,000 | 987,538,000 | **$207.47** |

---

## Experiment: `openai/gpt-5.6-terra` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785364901
**Dataset:** 1024×1024 padded PNGs
**Prompt:** `CLASSIFICATION_PROMPT` v2 (expanded disambiguation rules)
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`
**Image size:** `1024×1024`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **91.25%** (146/160 correct) |
| Prompt tokens (avg) | 2,451.18 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 22.69 |
| Total tokens (avg) | 2,473.87 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Cost Projections (`openai/gpt-5.6-terra`, `max_tokens=1024`)

**Pricing:** $2.5/M input tokens, $10.0/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 1,960,940 | 18,155 | 1,979,095 | **$5.08** |
| 25,000 | 61,279,375 | 567,343 | 61,846,718 | **$158.87** |
| 320,000 | 784,376,000 | 7,262,000 | 791,638,000 | **$2033.56** |

---

## Experiment: `x-ai/grok-4.5` — 159 Images (9 per class × 16 classes)

**Experiment ID:** main-1785365569
**Dataset:** 1024×1024 padded PNGs
**Prompt:** `CLASSIFICATION_PROMPT` v2 (expanded disambiguation rules)
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`
**Image size:** `1024×1024`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **89.31%** (142/159 correct) |
| Prompt tokens (avg) | 2,586.00 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 164.55 |
| Total tokens (avg) | 2,750.55 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Cost Projections (`x-ai/grok-4.5`, `max_tokens=1024`)

**Pricing:** $2.0/M input tokens, $6.0/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 2,068,800 | 131,640 | 2,200,440 | **$4.93** |
| 25,000 | 64,650,000 | 4,113,750 | 68,763,750 | **$153.98** |
| 320,000 | 827,520,000 | 52,656,000 | 880,176,000 | **$1,970.98** |

---

## Experiment: `anthropic/claude-sonnet-5` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785366469
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **90.62%** (145/160 correct) |
| Prompt tokens (avg) | 3,620.00 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 5.00 |
| Total tokens (avg) | 3,625.00 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Cost Projections (`anthropic/claude-sonnet-5`, `max_tokens=1024`)

**Pricing:** $3.0/M input tokens, $15.0/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 2,896,000 | 4,000 | 2,900,000 | **$8.75** |
| 25,000 | 90,500,000 | 125,000 | 90,625,000 | **$273.38** |
| 320,000 | 1,158,400,000 | 1,600,000 | 1,160,000,000 | **$3499.20** |

---

## Experiment: `google/gemini-3.6-flash` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785367223
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **91.88%** (147/160 correct) |
| Prompt tokens (avg) | 2,473.82 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 311.05 |
| Total tokens (avg) | 2,784.87 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Cost Projections (`google/gemini-3.6-flash`, `max_tokens=1024`)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 1,979,055 | 248,840 | 2,227,895 | **$0.45** |
| 25,000 | 61,845,468 | 7,776,250 | 69,621,718 | **$13.94** |
| 320,000 | 791,622,000 | 99,536,000 | 891,158,000 | **$178.46** |
