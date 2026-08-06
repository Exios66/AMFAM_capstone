# Final Results: gemini-2.5-flash-lite_v18_reasoning_160

- **Dataset**: fixed_size_sampled
- **Model**: google/gemini-2.5-flash-lite
- **Prompt**: v18
- **Max tokens**: 4096

## Overall

- **Rows**: 160
- **Completed**: 154
- **Errors**: 6
- **Empty**: 0
- **exact_match**: 112/160 (70.0%)
- **failure rate**: 6/160 (3.8%)
- **near_miss** (correct answer was the model's runner-up): 1/160 (0.6% of rows; 2.4% of all misses)
- **runner_up coverage**: 3/154 completed rows had a parsable runner-up
- **Total cost**: $0.2855 across 154 rows with billed cost (avg $0.001854/image)

## Per-class accuracy

| Class | Correct | Total | Errors | Accuracy |
|---|---:|---:|---:|---:|
| advertisement | 5 | 10 | 0 | 50.0% |
| budget | 5 | 10 | 0 | 50.0% |
| email | 10 | 10 | 0 | 100.0% |
| file_folder | 8 | 10 | 1 | 80.0% |
| form | 3 | 10 | 1 | 30.0% |
| handwritten | 8 | 10 | 1 | 80.0% |
| invoice | 5 | 10 | 0 | 50.0% |
| letter | 8 | 10 | 0 | 80.0% |
| memo | 6 | 10 | 0 | 60.0% |
| news_article | 5 | 9 | 0 | 55.6% |
| presentation | 5 | 10 | 1 | 50.0% |
| questionnaire | 8 | 10 | 1 | 80.0% |
| resume | 9 | 10 | 0 | 90.0% |
| scientific_publication | 11 | 11 | 0 | 100.0% |
| scientific_report | 7 | 10 | 1 | 70.0% |
| specification | 9 | 10 | 0 | 90.0% |

## Failed (error) rows

- `test_imagesw_w_a_v_wav33e00_2045715585.tif.png`
- `test_imagesn_n_o_z_noz90d00_521820980_-0985.tif.png`
- `test_imagesu_u_j_f_ujf01d00_517728084_-8084.tif.png`
- `test_imagesd_d_t_n_dtn93f00_0000539310.tif.png`
- `test_imagesl_l_i_p_lip18c00_503907505_-7542.tif.png`
- `test_imagesa_a_a_s_aas73e00_2029145115.tif.png`

## Near-miss rows (correct answer was the model's runner-up)

These rows were misclassified but the model named the correct class as its
second choice in the reasoning trace — the closest possible misses.

- `test_imagesz_z_b_z_zbz01c00_660202.tif.png`
