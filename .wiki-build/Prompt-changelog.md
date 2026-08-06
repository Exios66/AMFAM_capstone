This document tracks the changes between prompt iterations (v11 through v15) for the qwen3.7-flash document classifier.


## v11.5 — Extended Money-Only Records

**Extended clarification for money-only records and periodic customer statements.**

- **Check 7 (invoice):** Added landlord's rent/lease statement for a specific period as invoice (bills one-off service period, not ongoing account).
- **Check 7 (budget):** Clarified campaign-contribution/expenditure requests, contribution-request checklists, grant/contribution requests with recipient and amount as budget (internal money requests). Added campaign-contribution/expenditure statements/disclosures and financial/money-data tables (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures) as budget.
- **Check 10 (form):** Explicitly excluded campaign-contribution requests/checklists/statements and financial or money-data tables from form.

**Rationale:** The model was routing money-only records to form because they had approval blocks or field layouts. v11.5 made explicit that bare money requests (amount + recipient, or financial data tables) are budget, not form.


## v11.7 — Minimal Edit Set D + A + B

**Deliberately minimal 3-edit set (C and E skipped to reduce regression risk).**

- **Edit D (Check 7 voucher vs check-stub):** Voucher is a payment instrument that BILLS a named payee for named goods/services/charges (invoice). Check face/check stub is the DISBURSEMENT instrument (budget), even when stub columns are headed "INVOICE DATE/NO/AMOUNT".
- **Edit A (Check 8 rate-data chart):** A labeled product/parameter rate-data chart (e.g., statistical process-control chart titled with product name plotting measured property against spec limits) is specification even without "shall/must" text.
- **Edit B (Check 10 standalone-chart carve-out):** A standalone labeled chart is form only when it holds generic administrative/log data. A chart of a product's measured parameters against spec limits → specification (check 8). A financial/money chart → budget (check 7). A research-measurement chart → scientific_report (check 13).

**Rationale:** v11 had two 160-set misses: `jow70f00` (form → budget, ambiguous grant payment) and `tqi16e00` (budget → invoice, planning recap with estimate numbers). v11.7 targeted structural disambiguation (voucher vs check-stub) and chart-type routing (product/parameter charts, financial charts) with minimal changes to avoid regressions.

**Result:** 160-set: 156/159 (98.1%). Eval 56-set: 20/56 (35.7%) — best eval yet (v11.5 = 16/56, v11.6 = 17/56).


## v11.9 — Narrow Edit B's Financial-Chart→Budget Carve-Out

**Three edits that narrow Edit B so titled/designed deck charts no longer fall into budget.**

- **Edit 1 (Check 10 carve-out narrowed):** A product/parameter rate-data chart → specification. A research/measurement chart → scientific_report. A financial/money chart → budget ONLY when it is a standalone data table used for money planning or tracking (a ledger, budget-vs-actual, price/value table). A financial chart presented as a TITLED, DESIGNED DECK CHART (a chart page styled as a slide with its own title/caption, company logo/date, or chart-per-page deck look, e.g., a "brand shares" pie chart or "performance triggers" table page) → presentation (check 9), not budget.
- **Edit 2 (Check 9 hardened):** A titled/designed deck chart IS a presentation slide; don'*t* route it to budget. The check-10 carve-out routes money charts to budget only when they are standalone planning/tracking data tables, not when they are titled deck charts.
- **Edit 3 (Calibration):** Keep the deck-chart exception visible next to the general chart rule.

**Rationale:** v11.8's Edit B carve-out ("a financial/money chart is budget") was too broad — it routed titled designed deck charts to budget ahead of check 9. The eval set had two presentation→budget regressions (`presentation__0001`, `presentation__0011`) from v11.7 to v11.8. v11.9 narrows the carve-out to standalone planning/tracking tables only.

**Result:** Eval 56-set: 20/56 (35.7%) — ties v11.7's best, +2 over v11.8's 18/56. Both presentation→budget regressions recovered, plus bonus fix of `jed71e00` (form → presentation, also v11.8's 160-set miss). Cost: `form__0005` (a v11.8 Fix-1 success) regressed to invoice; new `news_article__0008` → memo miss.


## v13 — Specialist Periodicals + Scientific Research Records

**Built from v11.9. Extends scientific_publication to specialist periodicals and scientific_report to research records.**

- **Check 6 (Published evidence):** Include a dated, titled science, medical, engineering, or technical periodical page whose own masthead identifies that specialist publication (e.g., a science magazine or medical trade paper), even when it lacks volume/issue/DOI.
- **Check 12 (News article caveat):** Don'*t* use general-news caveat for specialist science, medical, engineering, or technical periodicals. A specialist periodical with its own dated masthead is scientific_publication, not news_article, even if its page uses magazine/news typography or a section title such as "Monitor" or "World Wide Report".
- **Check 10 (Form carve-out):** Generic administrative forms remain form, but a page whose fields, tables, signatures, or handwritten entries document a scientific experiment, laboratory result, compound test, analytical measurement, protocol review, or technical research report → scientific_report (check 13), not form.
- **Check 10 (additional):** It does NOT cover scientific/laboratory research records merely because they use fields, tables, QA sign-offs, or a report cover.

**Rationale:** The model was routing specialist science/medical/technical periodicals (with their own mastheads) to news_article because they used magazine/news typography. It was also routing scientific research records (experiments, lab results, compound tests) to form because they used structured fields/tables. v13 extends scientific_publication to specialist periodicals and scientific_report to research records.

**Result:** v2 160-set: 137/159 (86.2%).


## v15 — Function-First Regression Repair

**Built from the validated v13 base after analyzing the v14 reasoning traces.**

- **Financial boundary:** Requires positive billing evidence for `invoice`; estimate numbers, revisions, agency letterhead, projected periods, and quoted totals alone remain `budget` when the page plans future spend. Purchase orders and authorization requests remain `form` when their function is approval.
- **Letter boundary:** Recognizes recipient-directed prose with a salutation or closing as `letter` without requiring letterhead or a complete street address. Complete handwritten letters remain `letter`; freeform notes and cards remain `handwritten`.
- **Email boundary:** Preserves genuine mail-client evidence requirements so phone-message logs, voicemail records, fax metadata, and generic From/To forms do not become email.
- **Form/questionnaire boundary:** Requires a respondent-facing survey instrument for `questionnaire`; retains `form` for administrative capture and QC sheets.
- **Technical boundary:** Separates normative product requirements (`specification`), filled QC/data-capture sheets (`form`), and study findings/results (`scientific_report`).
- **Presentation/news boundary:** Requires explicit deck or promotional function instead of relying on rotation, scan borders, sparse tables, or isolated mastheads.
- **Output contract:** Requires exactly one parser-safe `<label>...</label>` result.

**Rationale:** v14 fell to 85.0% on `fixed_size_sampled_v2`, with repeated budget/invoice and form-boundary errors. Its final precedence rules over-weighted weak visual or lexical cues and contradicted function-based evidence in the traces.

**Validation assets:** Adds two disjoint 160-image Braintrust slices, `fixed_size_sampled_v3` and `fixed_size_sampled_v4`, sampled primarily from the full Hugging Face `chainyo/rvl-cdip` test split and using the Kaggle test checkout only as a fallback when the Hugging Face source cannot satisfy disjoint quotas.


## Best Results by Dataset

| Dataset | Best Version | Accuracy |
|---------|--------------|----------|
| 160-image (original) | v11.8 | 157/158 (99.4%) |
| 320-image | v11.8 | 279/320 (87.2%) |
| 480-image | v11.8 | 424/476 (89.1%) |
| Eval 56 | v11.7 / v11.9 | 20/56 (35.7%) |
| 160-image v2 | v11.9 | 137/159 (86.2%) |

**Note:** v11.8 generalizes best to larger, noisier datasets (320, 480). v11.7 and v11.9 tie on the eval 56-set. v13 and v14 target specialist periodicals and scientific research records but show lower accuracy on the v2 dataset.


## v17 — Simplified Financial Rules + Handwritten → Letter Override

**Data-driven rebuild of the v11.9 check-7 (financial) rules, eliminating the agency-estimate sub-protocol that caused v11.9–v16's budget→invoice errors. Adds explicit LETTER/MEMO OVERRIDE in check-2 (handwritten) to enforce ordered-checklist precedence.**

Driven by three root causes identified in the v16 multispect evaluation (`reports/v16_multislice_evaluation_report.md`):

1. **Provider failures (16 rows / 3.3%)** — 13 finish_reason=length (qwen3.7-flash exhausts reasoning tokens on the bloated check-7 section) → **Fix:** Trim check-7 from 6,284 chars to ~1,100 chars (simplified invoice=payment-demand, budget=planning, estimate=budget). Reduced reasoning effort to `medium`. Raised MAX_TOKENS_CAP to 32,768. Added 300s HTTP timeout.

2. **Slice source quality gap (~15 ***pp***)** — v2/v3 (HF mirror) images are inherently harder than v1 (test_images) → **Mitigation:** Stronger rules should be more robust across sources.

3. **Prompt regression from v11.8's 99.4%** — the agency-estimate sub-protocol caused the model to misclassify budgets (planning estimates) as invoices when "PREVIOUS/CURRENT ESTIMATE" revision columns were present. → **Fix:** Removed the entire agency-estimate sub-protocol. The rule is now simple: "A document titled ESTIMATE is budget — it PLANS spending. Only an explicit payment demand (Amount Due, Pay, Invoice header) makes it invoice."

**Key changes from v11.9/v16:**
- **Check-7 (invoice):** Replaced 2,450-char agency-estimate maze with a 250-char clean rule: payment demand = invoice.
- **Check-7 (budget):** Replaced 3,030-char budget section (including the planning-recap vs agency-bill sub-protocol) with a 700-char clean rule: estimate = budget.
- **Check-2 (handwritten):** Added "LETTER/MEMO OVERRIDE" bullet: if most of the page is handwritten, it IS handwritten — even with complete letter structure (salutation, body, closing) or memo layout (To/From/Re/Date headers). Check 2 fires before check 11; do not evaluate letter/memo for handwritten pages.
- **Prompt length:** 46,277 chars — 3,977 shorter than v11.9, 5,476 shorter than v16.

**Infrastructure:**
- Reasoning effort reduced to `medium` for qwen models (was `high`).
- MAX_TOKENS_CAP raised to 32,768 (was 16,384).
- Failed rows now return ERROR: sentinel output and are scored as a tracked `failed` metric in Braintrust.
- HTTP timeout (300s) on OpenAI client.
- All eval runs now use `--manifest` for resumability.


## v17.1 — Surgical Calibration + Counter-Examples (Aug 2026)

**Data-driven corrections from v16 v2+v3 multi-slice failure analysis (320 images, 81.6% accuracy).**

- **Worked example — handwritten letter → handwritten.** v16's worked example #2 taught the model that "a complete handwritten letter remains letter." This caused 7/44 misclassifications across both slices (35% of the handwritten class). The new worked example applies the LETTER/MEMO OVERRIDE: handwriting wins regardless of letter formatting.
- **Worked example — agency estimate → budget.** v16's worked example #1 failed to prevent budget→invoice confusion (6/44 misclassifications). The new worked example reinforces the simplified check-7 rule: no payment demand = budget.
- **Calibration — scientific_report vs specification.** 2 scientific_report→specification errors and a budget→scientific_report outlier traced to the model misreading technical data tables as product specs. New sentence: "A research study's own experimental data tables belong to scientific_report, not specification — specification requires the page's PRIMARY function to be defining a product's composition."
- **Calibration — news_article vs advertisement.** 3 news_article→advertisement errors where the model fixated on embedded ad imagery. New sentence: "Judge newspaper/magazine pages by editorial intent, not embedded ads — a page with masthead, columns, and bylines is news_article even when it CONTAINS a branded advertisement."

**Token profile:** +2,177 chars (+4.7%). v17.1 total: 48,462 chars vs v16: 51,753 chars. Still significantly lighter than v16 while carrying 2 more worked examples (6 total vs v16's 6, but v16's were actively harmful).


## v17.2 — Three-Slice Generalization (Aug 2026)

**Data-driven corrections from v17.1 v1+v2+v3 combined analysis (480 images, 53 failures, ~89% accuracy).**

v17.1 successfully eliminated handwritten→letter (0 misses across all 3 slices) and length errors (4 vs v16's 15). Five clusters survived the v17.1 fix:

- **invoice→budget (6) + budget→invoice (3) + invoice→form (4):** 13 financial document failures in 480 images. The simplified check-7 reduced v16's 20 financial failures but the form-override rule ("money function overrides form layout") wasn'*t* consistently applied when invoices had form-like layouts.
- **news_article→advertisement (3):** The v17.1 calibration sentence wasn'*t* sufficient — the model still fixated on embedded ad imagery within newspaper pages.
- **Form over-prediction (8 instances of form as predicted class):** invoice→form (4), budget→form (2), specification→form (2), scientific_report→form (2), advertisement→form (1). The model defaulted to form when unsure.
- **scientific_publication→scientific_report (3):** Journal reprint boundary still fuzzy.
- **Presentation confusion (4):** presentation→memo (2), →handwritten (1), →budget (1) — the model read slide-style layouts as prose memos.

**Changes:**
- **Calibration — form-is-never-a-default.** "If you are choosing form because no other check clearly matched, you have missed a check — go back through checks 1-14." Addresses the 8 form-overprediction instances.
- **Calibration — presentation vs memo.** "A presentation with slide-style layout is presentation, not memo — memo requires internal organizational context and prose body, not slide typography." Addresses the 2 presentation→memo cases.
- **Worked example — invoice with form layout → invoice.** Shows a vendor bill with labeled fields, amount boxes, and approval blocks being classified as invoice because "money function overrides form layout." Addresses the 4 invoice→form cases.
- **Worked example — newspaper page with embedded ad → news_article.** Shows a newspaper page with masthead, columns, bylines, and an embedded brand ad being classified as news_article because "the page's dominant function is newspaper editorial content." Addresses the 3 news→ad cases.

**Token profile:** +2,216 chars (+4.6% vs v17.1). v17.2 total: 50,678 chars. 8 worked examples total. Still 1,075 chars lighter than v16.

---

## v0 — Function-Not-Subject Baseline (Aug 2026)

**Minimal baseline prompt (915 chars) with no check structure — added to benchmark the value of the check-driven iterations (v11+).**

- **Content:** Only the "judge by FUNCTION, not subject matter" preamble (commit to the first check with concrete on-page evidence; later checks don'*t* override) plus the 16 exact label strings. No checks, no worked examples, no calibration sentences.
- **Purpose:** Isolated control to measure how much of the v17.x accuracy comes from prompt engineering vs. the model's prior knowledge of document types.

**Result:** `fixed_size_sampled_480` slice (30/class × 16 = 480), `qwen/qwen3.7-flash`, reasoning high, max_tokens 8192: **332/480 (69.2%)**, 0 failed rows. Memo 100%; advertisement/email/scientific_publication 93%; file_folder/news_article 80%; form 73%; letter 70%; resume/scientific_report 60%; invoice/questionnaire/specification 57%; handwritten 53%; budget 43%; presentation 37%.

---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
