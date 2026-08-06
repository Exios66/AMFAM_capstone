# Full Report — qwen3.7-flash_v18.1_high_320

**Model:** `qwen/qwen3.7-flash`  
**Prompt version:** `v18.1`  
**Dataset:** `fixed_size_sampled_320` (19 per class × 16 classes = 317 images)  
**Image size:** 1024x1024  
**Reasoning:** enabled (effort=high), trace logged  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **84.86%** (269/317) |
| Scored rows | 317 |
| Failed/empty rows | 2 |
| Failure rate | 0.6% |
| **Near-miss** (correct answer was model's runner-up) | **33** (10.3% of rows; 68.8% of all misses) |
| Runner-up coverage | 295/317 completed rows |
| Prompt tokens (avg) | 11,891.3 |
| Prompt cached tokens (avg) | 7,634.4 |
| Completion tokens (avg) | 1,727.4 |
| Completion reasoning tokens (avg) | 1,397.7 |
| Total tokens (avg) | 13,618.8 |
| Time to first token (avg) | 40.52s |
| Duration (avg) | 0.00s |

## Cost — Expected vs Actual

**List pricing:** $0.03/M input tokens, $0.13/M output tokens (`qwen/qwen3.7-flash`, per OpenRouter model listing).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 3,769,557 |
| Total completion tokens (measured) | 547,589 |
| Total tokens (measured) | 4,317,146 |
| **Expected cost** (list price × measured tokens) | **$0.1843** |
| **Actual cost** (OpenRouter billed, all calls incl. retries) | **$0.1972** |
| Difference (expected − actual) | $-0.0130 (-7.0%) |
| Cost coverage | 317/317 rows with billed cost |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.47 | $0.50 |
| 25,000 | $14.53 | $15.55 |
| 320,000 | $186.02 | $199.10 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_qwen3.7-flash_v18.1_high_320.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 18 | 20 | 90% |
| `budget` | 17 | 20 | 85% |
| `email` | 20 | 20 | 100% |
| `file_folder` | 16 | 20 | 80% |
| `form` | 15 | 18 | 83% |
| `handwritten` | 18 | 20 | 90% |
| `invoice` | 14 | 20 | 70% |
| `letter` | 15 | 20 | 75% |
| `memo` | 20 | 20 | 100% |
| `news_article` | 16 | 20 | 80% |
| `presentation` | 17 | 20 | 85% |
| `questionnaire` | 16 | 19 | 84% |
| `resume` | 20 | 20 | 100% |
| `scientific_publication` | 18 | 20 | 90% |
| `scientific_report` | 14 | 20 | 70% |
| `specification` | 15 | 20 | 75% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_qwen3.7-flash_v18.1_high_320.md)
  - [Confusion matrix heatmap](confusion_matrix_qwen3.7-flash_v18.1_high_320.png)
- [Misclassification reasoning traces](misclassification_reasoning_qwen3.7-flash_v18.1_high_320.md)

### Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `letter` | `memo` | 5 |
| `scientific_report` | `form` | 5 |
| `specification` | `form` | 5 |
| `file_folder` | `presentation` | 3 |
| `invoice` | `form` | 3 |
| `advertisement` | `form` | 2 |
| `form` | `budget` | 2 |
| `invoice` | `budget` | 2 |
| `news_article` | `advertisement` | 2 |
| `news_article` | `file_folder` | 2 |
| `presentation` | `file_folder` | 2 |
| `scientific_publication` | `news_article` | 2 |
| `budget` | `form` | 1 |
| `budget` | `invoice` | 1 |
| `budget` | `scientific_report` | 1 |
| `file_folder` | `scientific_report` | 1 |
| `form` | `file_folder` | 1 |
| `handwritten` | `advertisement` | 1 |
| `handwritten` | `form` | 1 |
| `invoice` | `letter` | 1 |

## Results Interpretation

### Overall

`qwen3.7-flash` with prompt **v18.1** classifies **269/317 (84.9%)** of the 317-image `fixed_size_sampled_320` slice exactly.
There are **2 failed/empty rows** (failure rate 0.6%) — the retry loop exhausted its attempts on these (see 'Failed rows' below), and they count as misses.

**Near-miss analysis:** 33 of the 48 misses (68.8%) were near-misses — the model got the answer wrong but named the correct class as its runner-up in the reasoning trace. 295/317 rows had a parsable runner-up line. If runner-up confusion were fixed (e.g. sharpening the tie-break rules between the confused pairs below), accuracy would rise to approximately 95.3%.

### Strengths

- **`resume`**: 100% (20/20)
- **`memo`**: 100% (20/20)
- **`email`**: 100% (20/20)

### Weaknesses

- **`invoice`**: 70% (14/20)
- **`scientific_report`**: 70% (14/20)
- **`letter`**: 75% (15/20)

### Top Confusion Patterns

The most frequent misclassifications are:
- **`letter` → `memo`**: 5 images
- **`scientific_report` → `form`**: 5 images
- **`specification` → `form`**: 5 images
- **`file_folder` → `presentation`**: 3 images
- **`invoice` → `form`**: 3 images

The dominant failure mode is confusion between visually similar classes (`letter` ↔ `memo` `scientific_report` ↔ `form` `specification` ↔ `form` ); the single largest confused pair accounts for 10% of all misses.

### Cost

The run billed **$0.1972** actual vs **$0.1843** list-price expected (-7.0%), averaging $0.000622/image. The gap is mostly prompt caching — 7,634 of 11,891 avg prompt tokens/row were cache hits (cached input billed at ~10% of the input price). Extrapolated linearly: $0.50 for 800 images, $15.55 for 25,000, and $199.10 for a 320,000-image production sweep.

### Recommendations

1. Address the 33 near-misses by adding tie-break disambiguation rules between the top confused pairs — this is the highest-leverage prompt change (up to ~10.4pp of accuracy).
2. Add worked counter-examples for the dominant pairs (`letter`→`memo`, `scientific_report`→`form`, `specification`→`form`).
3. Inspect the 2 failed/empty rows; the retry loop already handles transient failures so any new errors point at persistent provider content filters.
4. Review the misclassification reasoning traces linked above before iterating on the prompt — the raw reasoning often exposes the exact rule the model misfired on.
