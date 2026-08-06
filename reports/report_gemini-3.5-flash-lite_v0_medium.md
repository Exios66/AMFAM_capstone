# Full Report — gemini-3.5-flash-lite_v0_medium

**Model:** `google/gemini-3.5-flash-lite`  
**Prompt version:** `v0`  
**Dataset:** `fixed_size_sampled_320` (19 per class × 16 classes = 319 images)  
**Image size:** 1024x1024  
**Reasoning:** enabled (effort=high), trace logged  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **72.73%** (232/319) |
| Scored rows | 319 |
| Failed/empty rows | 0 |
| Failure rate | 0.0% |
| **Near-miss** (correct answer was model's runner-up) | **0** (0.0% of rows; 0.0% of all misses) |
| Runner-up coverage | 0/319 completed rows |
| Prompt tokens (avg) | 1,296.0 |
| Prompt cached tokens (avg) | 0.0 |
| Completion tokens (avg) | 340.7 |
| Completion reasoning tokens (avg) | 334.9 |
| Total tokens (avg) | 1,636.8 |
| Time to first token (avg) | 2.73s |
| Duration (avg) | 0.00s |

## Cost — Expected vs Actual

**List pricing:** $0.3/M input tokens, $2.5/M output tokens (`google/gemini-3.5-flash-lite`, per OpenRouter model listing).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 413,425 |
| Total completion tokens (measured) | 108,699 |
| Total tokens (measured) | 522,124 |
| **Expected cost** (list price × measured tokens) | **$0.3958** |
| **Actual cost** (OpenRouter billed, all calls incl. retries) | **$0.3958** |
| Difference (expected − actual) | $+0.0000 (+0.0%) |
| Cost coverage | 319/319 rows with billed cost |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.99 | $0.99 |
| 25,000 | $31.02 | $31.02 |
| 320,000 | $397.02 | $397.02 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_gemini-3.5-flash-lite_v0_medium.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 18 | 20 | 90% |
| `budget` | 12 | 20 | 60% |
| `email` | 20 | 20 | 100% |
| `file_folder` | 13 | 20 | 65% |
| `form` | 13 | 19 | 68% |
| `handwritten` | 7 | 20 | 35% |
| `invoice` | 15 | 20 | 75% |
| `letter` | 15 | 20 | 75% |
| `memo` | 20 | 20 | 100% |
| `news_article` | 17 | 20 | 85% |
| `presentation` | 11 | 20 | 55% |
| `questionnaire` | 16 | 20 | 80% |
| `resume` | 12 | 20 | 60% |
| `scientific_publication` | 17 | 20 | 85% |
| `scientific_report` | 11 | 20 | 55% |
| `specification` | 15 | 20 | 75% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_gemini-3.5-flash-lite_v0_medium.md)
  - [Confusion matrix heatmap](confusion_matrix_gemini-3.5-flash-lite_v0_medium.png)
- [Misclassification reasoning traces](misclassification_reasoning_gemini-3.5-flash-lite_v0_medium.md)

### Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `handwritten` | `letter` | 10 |
| `resume` | `form` | 8 |
| `letter` | `memo` | 5 |
| `budget` | `form` | 4 |
| `file_folder` | `presentation` | 4 |
| `invoice` | `form` | 4 |
| `scientific_report` | `form` | 4 |
| `budget` | `invoice` | 3 |
| `form` | `memo` | 3 |
| `scientific_report` | `scientific_publication` | 3 |
| `specification` | `form` | 3 |
| `advertisement` | `form` | 2 |
| `news_article` | `advertisement` | 2 |
| `presentation` | `memo` | 2 |
| `presentation` | `news_article` | 2 |
| `scientific_publication` | `news_article` | 2 |
| `specification` | `scientific_report` | 2 |
| `budget` | `scientific_report` | 1 |
| `file_folder` | `handwritten` | 1 |
| `file_folder` | `memo` | 1 |

## Results Interpretation

### Overall

`gemini-3.5-flash-lite` with prompt **v0** classifies **232/319 (72.7%)** of the 319-image `fixed_size_sampled_320` slice exactly.
The resilient retry loop recovered every transient provider error, so accuracy is measured over the full slice.

**Near-miss analysis:** 0 of the 87 misses (0.0%) were near-misses — the model got the answer wrong but named the correct class as its runner-up in the reasoning trace. 0/319 rows had a parsable runner-up line. If runner-up confusion were fixed (e.g. sharpening the tie-break rules between the confused pairs below), accuracy would rise to approximately 72.7%.

### Strengths

- **`memo`**: 100% (20/20)
- **`email`**: 100% (20/20)
- **`advertisement`**: 90% (18/20)

### Weaknesses

- **`handwritten`**: 35% (7/20)
- **`presentation`**: 55% (11/20)
- **`scientific_report`**: 55% (11/20)

### Top Confusion Patterns

The most frequent misclassifications are:
- **`handwritten` → `letter`**: 10 images
- **`resume` → `form`**: 8 images
- **`letter` → `memo`**: 5 images
- **`budget` → `form`**: 4 images
- **`file_folder` → `presentation`**: 4 images

The dominant failure mode is confusion between visually similar classes (`handwritten` ↔ `letter` `resume` ↔ `form` `letter` ↔ `memo` ); the single largest confused pair accounts for 11% of all misses.

### Cost

The run billed **$0.3958** actual vs **$0.3958** list-price expected (+0.0%), averaging $0.001241/image. The gap is mostly prompt caching — 0 of 1,296 avg prompt tokens/row were cache hits (cached input billed at ~10% of the input price). Extrapolated linearly: $0.99 for 800 images, $31.02 for 25,000, and $397.02 for a 320,000-image production sweep.

### Recommendations

1. Add worked counter-examples for the dominant pairs (`handwritten`→`letter`, `resume`→`form`, `letter`→`memo`).
2. Review the misclassification reasoning traces linked above before iterating on the prompt — the raw reasoning often exposes the exact rule the model misfired on.
