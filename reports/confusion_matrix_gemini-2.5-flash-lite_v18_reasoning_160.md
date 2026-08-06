# Confusion Matrix — gemini-2.5-flash-lite_v18_reasoning_160

**Overall Accuracy:** 72.7% (112/154)  
**Dataset:** fixed_size_sampled  
**Model:** `google/gemini-2.5-flash-lite`

![Confusion Matrix](confusion_matrix_gemini-2.5-flash-lite_v18_reasoning_160.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `sci_pub` | `sci_rep` | `specif` | `__inv` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **5** | . | . | 1 | . | . | . | . | . | 3 | . | . | . | . | . | 1 | . | 10 | 50% |
| `budget` | . | **5** | . | . | . | 1 | 4 | . | . | . | . | . | . | . | . | . | . | 10 | 50% |
| `email` | . | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `file_folder` | . | . | . | **8** | 1 | . | . | . | . | . | . | . | . | . | . | . | . | 9 | 89% |
| `form` | . | 2 | 1 | 2 | **3** | . | . | . | . | . | . | . | . | . | . | 1 | . | 9 | 33% |
| `handwritten` | . | . | . | . | 1 | **8** | . | . | . | . | . | . | . | . | . | . | . | 9 | 89% |
| `invoice` | . | 4 | . | 1 | . | . | **5** | . | . | . | . | . | . | . | . | . | . | 10 | 50% |
| `letter` | 1 | . | . | 1 | . | . | . | **8** | . | . | . | . | . | . | . | . | . | 10 | 80% |
| `memo` | . | 1 | . | . | . | . | . | 1 | **6** | . | . | . | . | . | . | 2 | . | 10 | 60% |
| `news_article` | 1 | . | . | 2 | . | . | . | . | . | **5** | . | . | . | 1 | . | . | . | 9 | 56% |
| `presentation` | . | 1 | . | . | 2 | . | . | . | . | 1 | **5** | . | . | . | . | . | . | 9 | 56% |
| `questionnaire` | . | . | . | . | . | 1 | . | . | . | . | . | **8** | . | . | . | . | . | 9 | 89% |
| `resume` | . | . | . | 1 | . | . | . | . | . | . | . | . | **9** | . | . | . | . | 10 | 90% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | . | . | . | . | **11** | . | . | . | 11 | 100% |
| `scientific_report` | . | 1 | . | 1 | . | . | . | . | . | . | . | . | . | . | **7** | . | . | 9 | 78% |
| `specification` | 1 | . | . | . | . | . | . | . | . | . | . | . | . | . | . | **9** | . | 10 | 90% |
| `__invalid__` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |

## Top Confused Pairs

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
