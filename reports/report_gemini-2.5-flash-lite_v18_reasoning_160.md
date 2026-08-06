# Full Report — gemini-2.5-flash-lite_v18_reasoning_160

**Model:** `google/gemini-2.5-flash-lite`  
**Prompt version:** `v18`  
**Dataset:** `fixed_size_sampled` (10 per class × 16 classes = 154 images)  
**Image size:** 1024x1024  
**Reasoning:** enabled (effort=high), trace logged  
**Max concurrency:** 8  

## Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **72.73%** (112/154) |
| Scored rows | 154 |
| Failed/empty rows | 6 |
| Failure rate | 3.8% |
| **Near-miss** (correct answer was model's runner-up) | **1** (0.6% of rows; 2.4% of all misses) |
| Runner-up coverage | 3/154 completed rows |
| Prompt tokens (avg) | 0.0 |
| Prompt cached tokens (avg) | 0.0 |
| Completion tokens (avg) | 0.0 |
| Completion reasoning tokens (avg) | 0.0 |
| Total tokens (avg) | 0.0 |
| Time to first token (avg) | 0.00s |
| Duration (avg) | 0.00s |

## Cost — Expected vs Actual

**List pricing:** $0.1/M input tokens, $0.4/M output tokens (`google/gemini-2.5-flash-lite`, per OpenRouter model listing).

| Metric | Value |
|--------|------:|
| Total prompt tokens (measured) | 0 |
| Total completion tokens (measured) | 0 |
| Total tokens (measured) | 0 |
| **Expected cost** (list price × measured tokens) | **$0.0000** |
| **Actual cost** (OpenRouter billed, all calls incl. retries) | **$0.2855** |
| Difference (expected − actual) | $-0.2855 (+0.0%) |
| Cost coverage | 154/154 rows with billed cost |

### Scale-up projections (list-price expected vs extrapolated actual)

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.00 | $1.48 |
| 25,000 | $0.00 | $46.35 |
| 320,000 | $0.00 | $593.34 |

## Per-Class Accuracy

![Per-Class Accuracy](per_class_accuracy_gemini-2.5-flash-lite_v18_reasoning_160.png)

| Class | Correct | Total | Accuracy |
|-------|--------:|------:|---------:|
| `advertisement` | 5 | 10 | 50% |
| `budget` | 5 | 10 | 50% |
| `email` | 10 | 10 | 100% |
| `file_folder` | 8 | 9 | 89% |
| `form` | 3 | 9 | 33% |
| `handwritten` | 8 | 9 | 89% |
| `invoice` | 5 | 10 | 50% |
| `letter` | 8 | 10 | 80% |
| `memo` | 6 | 10 | 60% |
| `news_article` | 5 | 9 | 56% |
| `presentation` | 5 | 9 | 56% |
| `questionnaire` | 8 | 9 | 89% |
| `resume` | 9 | 10 | 90% |
| `scientific_publication` | 11 | 11 | 100% |
| `scientific_report` | 7 | 9 | 78% |
| `specification` | 9 | 10 | 90% |

## Confusion Matrix & Misclassification Analysis

- [Confusion matrix markdown](confusion_matrix_gemini-2.5-flash-lite_v18_reasoning_160.md)
  - [Confusion matrix heatmap](confusion_matrix_gemini-2.5-flash-lite_v18_reasoning_160.png)
- [Misclassification reasoning traces](misclassification_reasoning_gemini-2.5-flash-lite_v18_reasoning_160.md)

### Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `budget` | `invoice` | 4 |
| `invoice` | `budget` | 4 |
| `advertisement` | `news_article` | 3 |
| `form` | `budget` | 2 |
| `form` | `file_folder` | 2 |
| `memo` | `specification` | 2 |
| `news_article` | `file_folder` | 2 |
| `presentation` | `form` | 2 |
| `advertisement` | `file_folder` | 1 |
| `advertisement` | `specification` | 1 |
| `budget` | `handwritten` | 1 |
| `file_folder` | `form` | 1 |
| `form` | `email` | 1 |
| `form` | `specification` | 1 |
| `handwritten` | `form` | 1 |
| `invoice` | `file_folder` | 1 |
| `letter` | `advertisement` | 1 |
| `letter` | `file_folder` | 1 |
| `memo` | `budget` | 1 |
| `memo` | `letter` | 1 |

## Results Interpretation

### Overall

`gemini-2.5-flash-lite` with prompt **v18** classifies **112/154 (72.7%)** of the 154-image `fixed_size_sampled` slice exactly.
There are **6 failed/empty rows** (failure rate 3.8%) — the retry loop exhausted its attempts on these (see 'Failed rows' below), and they count as misses.

**Near-miss analysis:** 1 of the 42 misses (2.4%) were near-misses — the model got the answer wrong but named the correct class as its runner-up in the reasoning trace. 3/154 rows had a parsable runner-up line. If runner-up confusion were fixed (e.g. sharpening the tie-break rules between the confused pairs below), accuracy would rise to approximately 73.4%.

### Strengths

- **`scientific_publication`**: 100% (11/11)
- **`email`**: 100% (10/10)
- **`specification`**: 90% (9/10)

### Weaknesses

- **`form`**: 33% (3/9)
- **`advertisement`**: 50% (5/10)
- **`budget`**: 50% (5/10)

### Top Confusion Patterns

The most frequent misclassifications are:
- **`budget` → `invoice`**: 4 images
- **`invoice` → `budget`**: 4 images
- **`advertisement` → `news_article`**: 3 images
- **`form` → `budget`**: 2 images
- **`form` → `file_folder`**: 2 images

The dominant failure mode is confusion between visually similar classes (`budget` ↔ `invoice` `invoice` ↔ `budget` `advertisement` ↔ `news_article` ); the single largest confused pair accounts for 10% of all misses.

### Cost

The run billed **$0.2855** actual vs **$0.0000** list-price expected (+0.0%), averaging $0.001854/image. Extrapolated linearly: $1.48 for 800 images, $46.35 for 25,000, and $593.34 for a 320,000-image production sweep.

### Recommendations

1. Address the 1 near-misses by adding tie-break disambiguation rules between the top confused pairs — this is the highest-leverage prompt change (up to ~0.6pp of accuracy).
2. Add worked counter-examples for the dominant pairs (`budget`→`invoice`, `invoice`→`budget`, `advertisement`→`news_article`).
3. Inspect the 6 failed/empty rows; the retry loop already handles transient failures so any new errors point at persistent provider content filters.
4. Review the misclassification reasoning traces linked above before iterating on the prompt — the raw reasoning often exposes the exact rule the model misfired on.
