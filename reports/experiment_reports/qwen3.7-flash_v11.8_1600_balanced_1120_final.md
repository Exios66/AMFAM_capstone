# Final Results: qwen3.7-flash_v11.8_reasoning_1600_balanced_1120

- **Dataset**: rvl_cdip_1600
- **Model**: qwen/qwen3.7-flash
- **Prompt**: v11.8
- **Max tokens**: 8192

## Overall

- **Rows**: 383
- **Completed**: 305
- **Errors**: 78
- **Empty**: 0
- **exact_match**: 254/383 (66.3%)

## Per-class accuracy

| Class | Correct | Total | Errors | Accuracy |
|---|---:|---:|---:|---:|
| advertisement | 20 | 27 | 3 | 74.1% |
| budget | 9 | 20 | 6 | 45.0% |
| email | 23 | 32 | 6 | 71.9% |
| file_folder | 18 | 29 | 9 | 62.1% |
| form | 19 | 24 | 1 | 79.2% |
| handwritten | 19 | 22 | 2 | 86.4% |
| invoice | 15 | 24 | 5 | 62.5% |
| letter | 17 | 29 | 6 | 58.6% |
| memo | 13 | 19 | 5 | 68.4% |
| news_article | 15 | 20 | 5 | 75.0% |
| presentation | 11 | 22 | 3 | 50.0% |
| questionnaire | 14 | 22 | 4 | 63.6% |
| resume | 18 | 20 | 2 | 90.0% |
| scientific_publication | 17 | 27 | 8 | 63.0% |
| scientific_report | 13 | 24 | 7 | 54.2% |
| specification | 13 | 22 | 6 | 59.1% |

## Failed (error) rows

- `rvl_cdip__advertisement__0011.png`
- `rvl_cdip__advertisement__0057.png`
- `rvl_cdip__advertisement__0087.png`
- `rvl_cdip__budget__0004.png`
- `rvl_cdip__budget__0027.png`
- `rvl_cdip__budget__0037.png`
- `rvl_cdip__budget__0047.png`
- `rvl_cdip__budget__0049.png`
- `rvl_cdip__budget__0100.png`
- `rvl_cdip__email__0021.png`
- `rvl_cdip__email__0032.png`
- `rvl_cdip__email__0059.png`
- `rvl_cdip__email__0065.png`
- `rvl_cdip__email__0084.png`
- `rvl_cdip__email__0092.png`
- `rvl_cdip__file_folder__0002.png`
- `rvl_cdip__file_folder__0022.png`
- `rvl_cdip__file_folder__0031.png`
- `rvl_cdip__file_folder__0066.png`
- `rvl_cdip__file_folder__0070.png`
- `rvl_cdip__file_folder__0075.png`
- `rvl_cdip__file_folder__0093.png`
- `rvl_cdip__file_folder__0094.png`
- `rvl_cdip__file_folder__0098.png`
- `rvl_cdip__form__0062.png`
- `rvl_cdip__handwritten__0001.png`
- `rvl_cdip__handwritten__0013.png`
- `rvl_cdip__invoice__0043.png`
- `rvl_cdip__invoice__0054.png`
- `rvl_cdip__invoice__0061.png`
- `rvl_cdip__invoice__0071.png`
- `rvl_cdip__invoice__0092.png`
- `rvl_cdip__letter__0024.png`
- `rvl_cdip__letter__0031.png`
- `rvl_cdip__letter__0060.png`
- `rvl_cdip__letter__0065.png`
- `rvl_cdip__letter__0080.png`
- `rvl_cdip__letter__0095.png`
- `rvl_cdip__memo__0014.png`
- `rvl_cdip__memo__0053.png`
- `rvl_cdip__memo__0078.png`
- `rvl_cdip__memo__0087.png`
- `rvl_cdip__memo__0100.png`
- `rvl_cdip__news_article__0048.png`
- `rvl_cdip__news_article__0062.png`
- `rvl_cdip__news_article__0078.png`
- `rvl_cdip__news_article__0084.png`
- `rvl_cdip__news_article__0100.png`
- `rvl_cdip__presentation__0054.png`
- `rvl_cdip__presentation__0055.png`
- `rvl_cdip__presentation__0097.png`
- `rvl_cdip__questionnaire__0011.png`
- `rvl_cdip__questionnaire__0022.png`
- `rvl_cdip__questionnaire__0046.png`
- `rvl_cdip__questionnaire__0063.png`
- `rvl_cdip__resume__0027.png`
- `rvl_cdip__resume__0041.png`
- `rvl_cdip__scientific_publication__0043.png`
- `rvl_cdip__scientific_publication__0049.png`
- `rvl_cdip__scientific_publication__0052.png`
- `rvl_cdip__scientific_publication__0060.png`
- `rvl_cdip__scientific_publication__0061.png`
- `rvl_cdip__scientific_publication__0069.png`
- `rvl_cdip__scientific_publication__0098.png`
- `rvl_cdip__scientific_publication__0100.png`
- `rvl_cdip__scientific_report__0018.png`
- `rvl_cdip__scientific_report__0042.png`
- `rvl_cdip__scientific_report__0047.png`
- `rvl_cdip__scientific_report__0048.png`
- `rvl_cdip__scientific_report__0082.png`
- `rvl_cdip__scientific_report__0083.png`
- `rvl_cdip__scientific_report__0095.png`
- `rvl_cdip__specification__0016.png`
- `rvl_cdip__specification__0026.png`
- `rvl_cdip__specification__0030.png`
- `rvl_cdip__specification__0067.png`
- `rvl_cdip__specification__0074.png`
- `rvl_cdip__specification__0096.png`
