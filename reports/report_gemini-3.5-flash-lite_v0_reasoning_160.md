# Full Report — gemini-3.5-flash-lite_v0_reasoning_160

**Model:** `google/gemini-3.5-flash-lite`  
**Prompt version:** `v0`  
**Dataset:** `fixed_size_sampled` (10 per class × 16 classes = 160 images)  
**Image size:** 1024x1024  
**Reasoning:** enabled (effort=high), trace logged  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **72.50%** (116/160) |
| Scored rows | 160 |
| Failed/empty rows | 0 |
| Failure rate | 0.0% |
| **Near-miss** (correct answer was model's runner-up) | **0** (0.0% of rows; 0.0% of all misses) |
| Runner-up coverage | 0/160 completed rows |
| Prompt tokens (avg) | 0.0 |
| Prompt cached tokens (avg) | 0.0 |
| Completion tokens (avg) | 0.0 |
| Completion reasoning tokens (avg) | 0.0 |
| Total tokens (avg) | 0.0 |
| Time to first token (avg) | 0.00s |
| Duration (avg) | 0.00s |

## Cost — Expected vs Actual

**List pricing:** $0.3/M input tokens, $2.5/M output tokens (`google/gemini-3.5-flash-lite`, per OpenRouter model listing).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 0 |
| Total completion tokens (measured) | 0 |
| Total tokens (measured) | 0 |
| **Expected cost** (list price × measured tokens) | **$0.0000** |
| **Actual cost** (OpenRouter billed, all calls incl. retries) | **$0.3406** |
| Difference (expected − actual) | $-0.3406 (+0.0%) |
| Cost coverage | 160/160 rows with billed cost |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.00 | $1.70 |
| 25,000 | $0.00 | $53.22 |
| 320,000 | $0.00 | $681.25 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_gemini-3.5-flash-lite_v0_reasoning_160.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 10 | 10 | 100% |
| `budget` | 3 | 10 | 30% |
| `email` | 10 | 10 | 100% |
| `file_folder` | 9 | 10 | 90% |
| `form` | 7 | 10 | 70% |
| `handwritten` | 3 | 10 | 30% |
| `invoice` | 7 | 10 | 70% |
| `letter` | 10 | 10 | 100% |
| `memo` | 9 | 10 | 90% |
| `news_article` | 8 | 9 | 89% |
| `presentation` | 5 | 10 | 50% |
| `questionnaire` | 6 | 10 | 60% |
| `resume` | 5 | 10 | 50% |
| `scientific_publication` | 11 | 11 | 100% |
| `scientific_report` | 6 | 10 | 60% |
| `specification` | 7 | 10 | 70% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_gemini-3.5-flash-lite_v0_reasoning_160.md)
  - [Confusion matrix heatmap](confusion_matrix_gemini-3.5-flash-lite_v0_reasoning_160.png)
- [Misclassification reasoning traces](misclassification_reasoning_gemini-3.5-flash-lite_v0_reasoning_160.md)

### Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `handwritten` | `letter` | 5 |
| `resume` | `form` | 4 |
| `budget` | `invoice` | 3 |
| `invoice` | `form` | 3 |
| `specification` | `form` | 3 |
| `budget` | `form` | 2 |
| `budget` | `handwritten` | 2 |
| `presentation` | `news_article` | 2 |
| `questionnaire` | `scientific_report` | 2 |
| `scientific_report` | `form` | 2 |
| `file_folder` | `budget` | 1 |
| `form` | `invoice` | 1 |
| `form` | `memo` | 1 |
| `form` | `scientific_report` | 1 |
| `handwritten` | `memo` | 1 |
| `handwritten` | `questionnaire` | 1 |
| `memo` | `letter` | 1 |
| `news_article` | `scientific_publication` | 1 |
| `presentation` | `advertisement` | 1 |
| `presentation` | `form` | 1 |

## Results Interpretation

### Overall

`gemini-3.5-flash-lite` with prompt **v0** classifies **116/160 (72.5%)** of the 160-image `fixed_size_sampled` slice exactly.
The resilient retry loop recovered every transient provider error, so accuracy is measured over the full slice.

**Near-miss analysis:** 0 of the 44 misses (0.0%) were near-misses — the model got the answer wrong but named the correct class as its runner-up in the reasoning trace. 0/160 rows had a parsable runner-up line. If runner-up confusion were fixed (e.g. sharpening the tie-break rules between the confused pairs below), accuracy would rise to approximately 72.5%.

### Strengths

- **`scientific_publication`**: 100% (11/11)
- **`letter`**: 100% (10/10)
- **`email`**: 100% (10/10)

### Weaknesses

- **`budget`**: 30% (3/10)
- **`handwritten`**: 30% (3/10)
- **`presentation`**: 50% (5/10)

### Top Confusion Patterns

The most frequent misclassifications are:
- **`handwritten` → `letter`**: 5 images
- **`resume` → `form`**: 4 images
- **`budget` → `invoice`**: 3 images
- **`invoice` → `form`**: 3 images
- **`specification` → `form`**: 3 images

The dominant failure mode is confusion between visually similar classes (`handwritten` ↔ `letter` `resume` ↔ `form` `budget` ↔ `invoice` ); the single largest confused pair accounts for 11% of all misses.

### Cost

The run billed **$0.3406** actual vs **$0.0000** list-price expected (+0.0%), averaging $0.002129/image. Extrapolated linearly: $1.70 for 800 images, $53.22 for 25,000, and $681.25 for a 320,000-image production sweep.

### Recommendations

1. Add worked counter-examples for the dominant pairs (`handwritten`→`letter`, `resume`→`form`, `budget`→`invoice`).
2. Review the misclassification reasoning traces linked above before iterating on the prompt — the raw reasoning often exposes the exact rule the model misfired on.
