# Structural Loops in Failed Reasoning Traces

- **Corpus rows (reasoning-covered)**: 3101
- **Differential bigram edges**: 400
- **Cycles found (length ≤ 6)**: 8

## Per-trace stuck-phrase rates

A trace is marked as looping when its token stream repeats a bi-gram back-to-back (`A B A B`) or a tri-gram back-to-back (`A B C A B C`) — the model re-running the same phrase instead of progressing. Plain `A -> B -> A` trigrams saturate (every v11.8 trace re-quotes evidence across the check cascade), so only consecutive duplication is counted.

| Group | Traces | Looping traces | Rate |
|---|---:|---:|---:|
| Failed | 658 | 335 | 50.9% |
| Correct | 2443 | 631 | 25.8% |

## Cycles in the differential bigram graph

| # | Cycle | Length | Edge weight (fail n / ok n) | Example trace excerpt |
|---|---:|---:|---|---|
| 1 | `dry` | 1 | dry→dry (102/0) | `The user wants me to classify a document from a tobacco industry archive.  **1. Analyze the document:** - **Header:** "MATERIAL SAFETY DATA SHEET", "NASHUA CORP", "44 FRANKLIN ST., NA". - **Top right:** Barcode, number "...` |
| 2 | `gs` | 1 | gs→gs (27/0) | `The user wants me to classify the provided document into one of 16 categories.  **1. Pre-scan:** - **Mail-client header block:** I see "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE" and "MO, RN : Rogers Law...` |
| 3 | `rel` | 1 | rel→rel (84/0) | `The user wants me to classify a document image into one of 16 categories.  **1. Analyze the document:** - **Header:** "BL HOGHEAD PRODUCTION MOISTURE REPORT" and a date "25-AUG-91". There's also a number "2055054854" at ...` |
| 4 | `change → gross` | 2 | change→gross (21/0) → gross→change (38/0) | `The user wants me to classify a document image into one of 16 categories.  **1. Analyze the document:** - **Header:** "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". This looks like a company le...` |
| 5 | `form → mol` | 2 | form→mol (51/0) → mol→form (78/0) | `The user wants me to classify a document from a tobacco industry archive.  **1. Analyze the document structure and content:** - **Top:** There's a handwritten name "Goldshield" (or similar, looks like "Goldshield"). - **...` |
| 6 | `nic → tar` | 2 | nic→tar (38/0) → tar→nic (44/0) | `The user wants me to classify a scanned document into one of 16 categories. I need to follow the scratchpad procedure, checking 1-14 in order.  **Pre-scan:** - Mail-client header block: None. - Masthead/running head: Non...` |
| 7 | `estimate → revised → marketing` | 3 | estimate→revised (17/0) → revised→marketing (22/0) → marketing→estimate (17/0) | `` |
| 8 | `all → answerable → information → detailed → quantitative` | 5 | all→answerable (44/0) → answerable→information (44/0) → information→detailed (67/0) → detailed→quantitative (18/0) → quantitative→all (27/0) | `` |

Cycle edges are highlighted in red on `phrase_net_differential.png`. Rotational duplicates are merged; direction is preserved (a reversed cycle is a different loop).
