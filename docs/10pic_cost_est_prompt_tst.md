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

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 2550×3300 images)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 2,960,800 | 334,555 | 3,295,355 | **$0.64** |
| 25,000 | 92,525,000 | 10,454,843 | 102,979,843 | **$20.15** |
| 320,000 | 1,184,320,000 | 133,822,000 | 1,318,142,000 | **$257.94** |

---

## Experiment: `google/gemini-2.5-flash` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785272634
**Dataset:** `2550x3300_10perclass_160/images/` (2550×3300 padded PNGs, 300 DPI)
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`
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

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 2550×3300 images)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 2,960,800 | 333,902 | 3,294,701 | **$0.64** |
| 25,000 | 92,525,000 | 10,434,437 | 102,959,437 | **$20.14** |
| 320,000 | 1,184,320,000 | 133,560,800 | 1,317,880,799 | **$257.78** |

---

## Experiment: `google/gemini-2.5-flash` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785272634
**Dataset:** `2550x3300_10perclass_160/images/` (2550×3300 padded PNGs, 300 DPI)
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`
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

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 2550×3300 images)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 2,960,800 | 333,902 | 3,294,701 | **$0.64** |
| 25,000 | 92,525,000 | 10,434,437 | 102,959,437 | **$20.14** |
| 320,000 | 1,184,320,000 | 133,560,800 | 1,317,880,799 | **$257.78** |

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

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 2550×3300 images)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 2,960,800 | 334,555 | 3,295,355 | **$0.64** |
| 25,000 | 92,525,000 | 10,454,843 | 102,979,843 | **$20.15** |
| 320,000 | 1,184,320,000 | 133,822,000 | 1,318,142,000 | **$257.94** |

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

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 2550×3300 images)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | 2,960,800 | 334,555 | 3,295,355 | **$0.64** |
| 25,000 | 92,525,000 | 10,454,843 | 102,979,843 | **$20.15** |
| 320,000 | 1,184,320,000 | 133,822,000 | 1,318,142,000 | **$257.94** |
