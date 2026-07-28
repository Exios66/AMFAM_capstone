# Confusion Matrix — main-1785270444

**Overall Accuracy:** 73.8% (118/160)  
**Dataset:** 2550×3300 padded PNGs, 50 per class  
**Model:** `google/gemini-2.5-flash`

![Confusion Matrix](confusion_matrix_main-1785270444.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `budget` | . | **6** | . | . | . | . | 3 | . | . | . | . | . | . | . | 1 | . | 10 | 60% |
| `email` | . | . | **9** | . | . | . | . | . | . | . | . | . | . | . | 1 | . | 10 | 90% |
| `file_folder` | . | . | . | **4** | 2 | 2 | . | . | . | . | . | . | . | . | 2 | . | 10 | 40% |
| `form` | . | . | . | 1 | **1** | . | . | 2 | 4 | . | . | . | . | . | 2 | . | 10 | 10% |
| `handwritten` | . | . | . | . | . | **7** | . | 1 | 1 | . | . | 1 | . | . | . | . | 10 | 70% |
| `invoice` | . | . | . | . | . | . | **9** | . | . | . | . | . | . | . | . | 1 | 10 | 90% |
| `letter` | . | . | 1 | . | . | . | . | **9** | . | . | . | . | . | . | . | . | 10 | 90% |
| `memo` | . | . | . | . | . | . | 1 | . | **9** | . | . | . | . | . | . | . | 10 | 90% |
| `news_article` | . | . | . | . | . | . | . | . | . | **9** | . | . | . | 1 | . | . | 10 | 90% |
| `presentation` | . | . | . | . | . | . | . | 1 | . | 2 | **5** | . | . | . | 2 | . | 10 | 50% |
| `questionnaire` | . | . | . | . | 1 | . | . | 1 | . | . | . | **8** | . | . | . | . | 10 | 80% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **10** | . | . | . | 10 | 100% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | . | . | . | . | **10** | . | . | 10 | 100% |
| `scientific_report` | . | . | . | . | . | . | . | . | . | . | . | . | . | 3 | **7** | . | 10 | 70% |
| `specification` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 5 | **5** | 10 | 50% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `specification` | `scientific_report` | 5 |
| `form` | `memo` | 4 |
| `budget` | `invoice` | 3 |
| `scientific_report` | `scientific_publication` | 3 |
| `file_folder` | `form` | 2 |
| `file_folder` | `handwritten` | 2 |
| `file_folder` | `scientific_report` | 2 |
| `form` | `letter` | 2 |
| `form` | `scientific_report` | 2 |
| `presentation` | `news_article` | 2 |
| `presentation` | `scientific_report` | 2 |
| `budget` | `scientific_report` | 1 |
| `email` | `scientific_report` | 1 |
| `form` | `file_folder` | 1 |
| `handwritten` | `letter` | 1 |
| `handwritten` | `memo` | 1 |
| `handwritten` | `questionnaire` | 1 |
| `invoice` | `specification` | 1 |
| `letter` | `email` | 1 |
| `memo` | `invoice` | 1 |
