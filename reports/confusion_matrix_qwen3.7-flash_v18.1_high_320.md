# Confusion Matrix — qwen3.7-flash_v18.1_high_320

**Overall Accuracy:** 84.6% (270/319)  
**Dataset:** 2550×3300 padded PNGs, 50 per class  
**Model:** `google/gemini-2.5-flash`

![Confusion Matrix](confusion_matrix_qwen3.7-flash_v18.1_high_320.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **18** | . | . | . | 2 | . | . | . | . | . | . | . | . | . | . | . | 20 | 90% |
| `budget` | . | **17** | . | . | 1 | . | 1 | . | . | . | . | . | . | . | 1 | . | 20 | 85% |
| `email` | . | . | **20** | . | . | . | . | . | . | . | . | . | . | . | . | . | 20 | 100% |
| `file_folder` | . | . | . | **17** | . | . | . | . | . | . | 3 | . | . | . | . | . | 20 | 85% |
| `form` | . | 2 | . | 2 | **15** | . | . | . | . | . | . | . | . | . | . | . | 19 | 79% |
| `handwritten` | 1 | . | . | . | 1 | **18** | . | . | . | . | . | . | . | . | . | . | 20 | 90% |
| `invoice` | . | 2 | . | . | 3 | . | **14** | 1 | . | . | . | . | . | . | . | . | 20 | 70% |
| `letter` | . | . | . | . | . | . | . | **15** | 5 | . | . | . | . | . | . | . | 20 | 75% |
| `memo` | . | . | . | . | . | . | . | . | **20** | . | . | . | . | . | . | . | 20 | 100% |
| `news_article` | 2 | . | . | 2 | . | . | . | . | . | **16** | . | . | . | . | . | . | 20 | 80% |
| `presentation` | . | . | . | 2 | . | . | . | . | 1 | . | **17** | . | . | . | . | . | 20 | 85% |
| `questionnaire` | . | . | . | 1 | . | 1 | . | . | . | . | . | **16** | . | . | 1 | . | 19 | 84% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **20** | . | . | . | 20 | 100% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 2 | . | . | . | **18** | . | . | 20 | 90% |
| `scientific_report` | . | . | . | . | 5 | . | . | . | . | . | . | . | . | 1 | **14** | . | 20 | 70% |
| `specification` | . | . | . | . | 5 | . | . | . | . | . | . | . | . | . | . | **15** | 20 | 75% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `letter` | `memo` | 5 |
| `scientific_report` | `form` | 5 |
| `specification` | `form` | 5 |
| `file_folder` | `presentation` | 3 |
| `invoice` | `form` | 3 |
| `advertisement` | `form` | 2 |
| `form` | `budget` | 2 |
| `form` | `file_folder` | 2 |
| `invoice` | `budget` | 2 |
| `news_article` | `advertisement` | 2 |
| `news_article` | `file_folder` | 2 |
| `presentation` | `file_folder` | 2 |
| `scientific_publication` | `news_article` | 2 |
| `budget` | `form` | 1 |
| `budget` | `invoice` | 1 |
| `budget` | `scientific_report` | 1 |
| `handwritten` | `advertisement` | 1 |
| `handwritten` | `form` | 1 |
| `invoice` | `letter` | 1 |
| `presentation` | `memo` | 1 |
