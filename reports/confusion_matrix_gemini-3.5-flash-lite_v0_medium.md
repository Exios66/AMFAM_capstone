# Confusion Matrix — gemini-3.5-flash-lite_v0_medium

**Overall Accuracy:** 72.7% (232/319)  
**Dataset:** 2550×3300 padded PNGs, 50 per class  
**Model:** `google/gemini-2.5-flash`

![Confusion Matrix](confusion_matrix_gemini-3.5-flash-lite_v0_medium.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **18** | . | . | . | 2 | . | . | . | . | . | . | . | . | . | . | . | 20 | 90% |
| `budget` | . | **12** | . | . | 4 | . | 3 | . | . | . | . | . | . | . | 1 | . | 20 | 60% |
| `email` | . | . | **20** | . | . | . | . | . | . | . | . | . | . | . | . | . | 20 | 100% |
| `file_folder` | . | . | . | **13** | . | 1 | . | . | 1 | . | 4 | . | . | . | 1 | . | 20 | 65% |
| `form` | . | . | . | 1 | **13** | . | 1 | . | 3 | . | . | . | . | . | 1 | . | 19 | 68% |
| `handwritten` | 1 | . | . | . | 1 | **7** | . | 10 | 1 | . | . | . | . | . | . | . | 20 | 35% |
| `invoice` | . | . | . | . | 4 | . | **15** | . | 1 | . | . | . | . | . | . | . | 20 | 75% |
| `letter` | . | . | . | . | . | . | . | **15** | 5 | . | . | . | . | . | . | . | 20 | 75% |
| `memo` | . | . | . | . | . | . | . | . | **20** | . | . | . | . | . | . | . | 20 | 100% |
| `news_article` | 2 | . | . | . | . | . | . | . | . | **17** | . | . | . | . | . | . | 19 | 89% |
| `presentation` | 1 | . | . | 1 | . | . | . | 1 | 2 | 2 | **11** | . | . | . | 1 | 1 | 20 | 55% |
| `questionnaire` | . | . | . | . | 1 | 1 | . | 1 | . | . | . | **16** | . | . | 1 | . | 20 | 80% |
| `resume` | . | . | . | . | 8 | . | . | . | . | . | . | . | **12** | . | . | . | 20 | 60% |
| `scientific_publication` | . | . | . | . | . | . | . | . | 1 | 2 | . | . | . | **17** | . | . | 20 | 85% |
| `scientific_report` | . | . | . | . | 4 | . | . | . | 1 | . | . | . | . | 3 | **11** | 1 | 20 | 55% |
| `specification` | . | . | . | . | 3 | . | . | . | . | . | . | . | . | . | 2 | **15** | 20 | 75% |

## Top Confused Pairs

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
