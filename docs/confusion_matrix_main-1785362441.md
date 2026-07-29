# Confusion Matrix — main-1785362441

**Overall Accuracy:** 85.0% (136/160)  
**Dataset:** 2550×3300 padded PNGs, 50 per class  
**Model:** `google/gemini-2.5-flash`

![Confusion Matrix](confusion_matrix_main-1785362441.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `budget` | . | **9** | . | . | . | . | . | . | . | . | . | . | . | . | 1 | . | 10 | 90% |
| `email` | . | . | **9** | . | . | . | . | . | . | . | . | . | . | . | 1 | . | 10 | 90% |
| `file_folder` | . | . | . | **8** | 1 | . | . | . | . | . | . | . | . | 1 | . | . | 10 | 80% |
| `form` | . | . | . | . | **9** | . | . | . | . | . | . | . | . | . | 1 | . | 10 | 90% |
| `handwritten` | . | . | . | . | 1 | **9** | . | . | . | . | . | . | . | . | . | . | 10 | 90% |
| `invoice` | . | 1 | . | . | . | . | **8** | . | . | . | . | . | . | . | . | 1 | 10 | 80% |
| `letter` | . | 1 | 1 | . | . | . | . | **8** | . | . | . | . | . | . | . | . | 10 | 80% |
| `memo` | . | . | . | . | . | . | 1 | . | **9** | . | . | . | . | . | . | . | 10 | 90% |
| `news_article` | . | . | . | . | . | . | . | . | . | **9** | . | . | . | 1 | . | . | 10 | 90% |
| `presentation` | . | . | . | 4 | . | . | . | . | 1 | . | **4** | . | . | . | 1 | . | 10 | 40% |
| `questionnaire` | . | . | . | . | 1 | . | . | 1 | . | . | . | **8** | . | . | . | . | 10 | 80% |
| `resume` | . | . | . | . | 2 | . | . | . | . | . | . | . | **8** | . | . | . | 10 | 80% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 1 | . | . | . | **9** | . | . | 10 | 90% |
| `scientific_report` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | **10** | . | 10 | 100% |
| `specification` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 1 | **9** | 10 | 90% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `presentation` | `file_folder` | 4 |
| `resume` | `form` | 2 |
| `budget` | `scientific_report` | 1 |
| `email` | `scientific_report` | 1 |
| `file_folder` | `form` | 1 |
| `file_folder` | `scientific_publication` | 1 |
| `form` | `scientific_report` | 1 |
| `handwritten` | `form` | 1 |
| `invoice` | `budget` | 1 |
| `invoice` | `specification` | 1 |
| `letter` | `budget` | 1 |
| `letter` | `email` | 1 |
| `memo` | `invoice` | 1 |
| `news_article` | `scientific_publication` | 1 |
| `presentation` | `memo` | 1 |
| `presentation` | `scientific_report` | 1 |
| `questionnaire` | `form` | 1 |
| `questionnaire` | `letter` | 1 |
| `scientific_publication` | `news_article` | 1 |
| `specification` | `scientific_report` | 1 |
