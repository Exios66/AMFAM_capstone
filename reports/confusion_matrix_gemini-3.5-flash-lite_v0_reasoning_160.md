# Confusion Matrix — gemini-3.5-flash-lite_v0_reasoning_160

**Overall Accuracy:** 72.5% (116/160)  
**Dataset:** 2550×3300 padded PNGs, 50 per class  
**Model:** `google/gemini-2.5-flash`

![Confusion Matrix](confusion_matrix_gemini-3.5-flash-lite_v0_reasoning_160.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `budget` | . | **3** | . | . | 2 | 2 | 3 | . | . | . | . | . | . | . | . | . | 10 | 30% |
| `email` | . | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `file_folder` | . | 1 | . | **9** | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 90% |
| `form` | . | . | . | . | **7** | . | 1 | . | 1 | . | . | . | . | . | 1 | . | 10 | 70% |
| `handwritten` | . | . | . | . | . | **3** | . | 5 | 1 | . | . | 1 | . | . | . | . | 10 | 30% |
| `invoice` | . | . | . | . | 3 | . | **7** | . | . | . | . | . | . | . | . | . | 10 | 70% |
| `letter` | . | . | . | . | . | . | . | **10** | . | . | . | . | . | . | . | . | 10 | 100% |
| `memo` | . | . | . | . | . | . | . | 1 | **9** | . | . | . | . | . | . | . | 10 | 90% |
| `news_article` | . | . | . | . | . | . | . | . | . | **8** | . | . | . | 1 | . | . | 9 | 89% |
| `presentation` | 1 | . | . | . | 1 | . | . | . | . | 2 | **5** | . | . | . | . | 1 | 10 | 50% |
| `questionnaire` | . | . | . | . | . | 1 | . | 1 | . | . | . | **6** | . | . | 2 | . | 10 | 60% |
| `resume` | . | . | . | . | 4 | . | . | . | . | . | . | . | **5** | 1 | . | . | 10 | 50% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | . | . | . | . | **11** | . | . | 11 | 100% |
| `scientific_report` | . | . | . | . | 2 | . | . | . | 1 | . | 1 | . | . | . | **6** | . | 10 | 60% |
| `specification` | . | . | . | . | 3 | . | . | . | . | . | . | . | . | . | . | **7** | 10 | 70% |

## Top Confused Pairs

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
