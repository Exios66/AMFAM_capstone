# Confusion Matrix — main-1785272634

**Overall Accuracy:** 72.9% (583/800)  
**Dataset:** 2550×3300 padded PNGs, 50 per class  
**Model:** `google/gemini-2.5-flash`

![Confusion Matrix](confusion_matrix_main-1785272634.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **44** | . | . | . | 2 | . | . | 1 | . | 3 | . | . | . | . | . | . | 50 | 88% |
| `budget` | . | **25** | . | 2 | 4 | . | 12 | . | . | . | . | . | . | . | 6 | . | 49 | 51% |
| `email` | 1 | . | **46** | . | . | . | . | . | 1 | 1 | . | . | . | . | 1 | . | 50 | 92% |
| `file_folder` | . | . | . | **27** | 3 | 7 | . | 2 | 1 | . | . | . | . | . | 7 | 2 | 49 | 55% |
| `form` | . | 1 | 1 | 2 | **15** | . | . | 11 | 13 | . | . | . | . | . | 7 | . | 50 | 30% |
| `handwritten` | . | . | . | . | 3 | **33** | . | 4 | 3 | 1 | . | 2 | . | . | 4 | . | 50 | 66% |
| `invoice` | . | 1 | . | . | 3 | . | **43** | 1 | . | . | . | . | . | . | 1 | 1 | 50 | 86% |
| `letter` | 2 | . | 1 | . | . | . | . | **38** | 8 | . | . | . | . | . | 1 | . | 50 | 76% |
| `memo` | . | . | . | . | . | . | 1 | 1 | **48** | . | . | . | . | . | . | . | 50 | 96% |
| `news_article` | . | . | . | . | . | . | . | . | 2 | **47** | . | . | . | 1 | . | . | 50 | 94% |
| `presentation` | . | . | . | 2 | . | 1 | . | 5 | 1 | 11 | **18** | . | 1 | . | 11 | . | 50 | 36% |
| `questionnaire` | . | . | . | 1 | 1 | . | . | 2 | . | . | . | **42** | . | . | 4 | . | 50 | 84% |
| `resume` | . | . | . | . | . | . | . | 1 | . | . | . | . | **49** | . | . | . | 50 | 98% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 3 | . | . | . | **47** | . | . | 50 | 94% |
| `scientific_report` | . | . | . | . | . | 1 | . | 1 | . | 1 | 1 | . | . | 8 | **38** | . | 50 | 76% |
| `specification` | . | . | . | . | 1 | . | . | . | 1 | . | . | . | . | . | 25 | **23** | 50 | 46% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `specification` | `scientific_report` | 25 |
| `form` | `memo` | 13 |
| `budget` | `invoice` | 12 |
| `form` | `letter` | 11 |
| `presentation` | `news_article` | 11 |
| `presentation` | `scientific_report` | 11 |
| `letter` | `memo` | 8 |
| `scientific_report` | `scientific_publication` | 8 |
| `file_folder` | `handwritten` | 7 |
| `file_folder` | `scientific_report` | 7 |
| `form` | `scientific_report` | 7 |
| `budget` | `scientific_report` | 6 |
| `presentation` | `letter` | 5 |
| `budget` | `form` | 4 |
| `handwritten` | `letter` | 4 |
| `handwritten` | `scientific_report` | 4 |
| `questionnaire` | `scientific_report` | 4 |
| `advertisement` | `news_article` | 3 |
| `file_folder` | `form` | 3 |
| `handwritten` | `form` | 3 |
