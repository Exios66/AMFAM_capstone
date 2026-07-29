# Misclassification Reasoning — main-1785362441

**Overall Accuracy:** 85.0% (136/160)  
**Total Errors:** 24  
**Unique Confused Pairs:** 20

---

## presentation → file_folder (4 errors)

### `processed_balanced__presentation__presentation_tim00940.83_tim00941.10_page_0001.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The image shows a mostly blank page with only a few labels: "PAGE 1", "BOARD OF DIRECTORS WINTER MEETING", "SAMUEL D. CHILCOTE, JR.", a confidential stamp, and a document ID. This is essentially a cover/title page or file folder-like page with minimal content. Per instructions, nearly blank pages with only labels/ID/classification stamp should be file_folder. Output only class name.

---
### `processed_balanced__presentation__presentation_86237297_7310_page_0001.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The image is rotated. It shows minimal text: "KENT", "HEAVY-UP BUSINESS BUILDING PROGRAM", "YEAR II - BRAND PLAN", and a number "86237297". The page is mostly blank with just labels/title. According to rules, nearly blank pages with only a label/ID/classification should be file_folder. This looks like a file folder cover or index page. Output file_folder.

---
### `processed_balanced__presentation__presentation_2071620949_0991_page_0001.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The image shows a mostly blank page with a label "COMPETITIVE BAR PROGRAMS" rotated vertically, an ID number "2071620949", and a handwritten letter "A". This fits the file_folder category: nearly blank page with only a label/ID. Output only class name.

---
### `processed_balanced__presentation__presentation_0011840384_page_0001.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The image is mostly blank with just a heading "RECOMMENDATIONS", an ID-like label "cngl0212:11", and a number "465422487". This fits file_folder: nearly blank page with only a label/ID. Output only class name.

---

## resume → form (2 errors)

### `processed_balanced__resume__resume_87343995_3996_page_0001.png`
**Expected:** `resume` | **Predicted:** `form`

**Reasoning:**
> The image shows a "BIOGRAPHICAL SKETCH" form for a Principal Investigator/Program Director. It contains education history, research experience, publications. This is a PHS 398 form page (grant application biographical sketch). It's a structured form with fields. But it's filled out. It resembles a resume/CV too (biographical sketch). Categories: form vs resume vs scientific_report.

It's a PHS 398 Biographical Sketch page, which is part of a grant application. The document is a form (PHS 398) with structured fields: NAME, POSITION TITLE, EDUCATION table, etc. It has "Form Page 6" at bottom. This is a form. However, content is like a CV/resume. The classification guidelines: resume = CVs, resumes, job applications, professional profiles. A biographical sketch for grant is essentially a CV but on a standard form. Given it's a PHS form page with structured fields and "Form Page", I'd lean form. But biographical sketch is more like resume content. The document is an official form template filled in. The label in such datasets (e.g., RVL-CDIP / Tobacco) often classifies these as "resume" for biographical sketches? Actually in document classification, a biosketch is resume-like. But the presence of form fields and PHS 398 suggests form.

Given instructions: form = application forms, data entry forms, structured questionnaires. This is an application form (grant application biographical sketch). It has blank/structured fields. Output form.

Need only class name.

---
### `processed_balanced__resume__resume_40039741-9742_page_0001.png`
**Expected:** `resume` | **Predicted:** `form`

**Reasoning:**
> The image shows an NIH "Biographical Sketch" form for principal investigator Joseph Loscalzo. It is a structured grant application component with fields for name, position title, birthdate, education table, research/professional experience, awards, societies, publications. It has PHS 398 form identifiers. Classification among 16: It is a form (application/data entry structured) or resume? It is a biographical sketch/CV-like, but specifically an NIH grant form with structured fields. The prompt: resume includes CVs/resumes/job applications/professional profiles. form includes application forms/data entry forms structured questionnaires. NIH biosketch is a form (PHS 398) used in grant applications, has structured fields and instructions "Give the following information... Photocopy this page". It resembles CV but is a standard form. In these document classification tasks, NIH biographical sketch pages are often classified as form due to PHS 398 template and fill-in structure, not resume. Need output only class name. Choose form. Ensure no explanation.

---

## memo → invoice (1 errors)

### `processed_balanced__memo__memo_71213540_page_0001.png`
**Expected:** `memo` | **Predicted:** `invoice`

**Reasoning:**
> The image clearly shows an "INVOICE" header from Gaskell Associates, with invoice number, date, terms, billing details, amounts, and total. This matches the invoice class criteria exactly.

---

## letter → email (1 errors)

### `processed_balanced__letter__letter_518600431+-0431_page_0001.png`
**Expected:** `letter` | **Predicted:** `email`

**Reasoning:**
> The document has To:/From:/Posted:/Subject: header block, "Ladies & Gentlemen" salutation, formal closing. It looks like an internal memo/email. The header with To/From/Posted/Subject resembles email or memo. It's electronic correspondence? "Posted:" suggests email. But categories include email and memo. The document uses To/From/Subject, CC, and distribution; likely an email message. However it says Ladies & Gentlemen and sincerely, like letter. Critical: memos have TO/FROM/RE/DATE header blocks; this has To/From/Posted/Subject and CC, typical email. Output email.

---

## letter → budget (1 errors)

### `processed_balanced__letter__letter_40038317-8318_page_0001.png`
**Expected:** `letter` | **Predicted:** `budget`

**Reasoning:**
> The document shows Council for Tobacco Research header, addressed To Research Foundation for SUNY, with Grant No., Grantee, Check Amount $38,982, For: Second Half Payment. This is a payment record/check-related document. According to rules, checks/check stubs/payment records are budget, not invoice. It has check amount and payment purpose. So classify as budget.

---

## invoice → specification (1 errors)

### `processed_balanced__invoice__invoice_2024476471_page_0001.png`
**Expected:** `invoice` | **Predicted:** `specification`

**Reasoning:**
> Hourly wage rates for montage work — a rate sheet defining prices/rates. Rules say specification includes rate sheets.

---

## invoice → budget (1 errors)

### `processed_balanced__invoice__invoice_2021633316_page_0001.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The document is a Philip Morris voucher/payment record with amount $7,260, check return instructions, fields like voucher number, account code. It's a payment record/check voucher, classified as budget (payment records, checks/statements) rather than invoice (no invoice header/amount due from vendor). Need output only class.

---

## handwritten → form (1 errors)

### `processed_balanced__handwritten__handwritten_517517307+-7310_page_0001.png`
**Expected:** `handwritten` | **Predicted:** `form`

**Reasoning:**
> The image is rotated. It appears to be a promotional offer/form for Winston Select Tobaccos. It has fields for name, address, signature, birthdate, gender checkboxes, and an offer restricted to smokers 21+. It says "Complete this form and send it to" - it's a marketing form/questionnaire-ish. It has blank fields to fill in (name, address, signature). This is a form (application/data entry form with blank fields). It also has promotional content but the structure is a fill-in form. Given rules: form has blank fields to fill in. Output form.

---

## scientific_publication → news_article (1 errors)

### `processed_balanced__scientific_publication__scientific_publication_10202118_10202119_page_0001.png`
**Expected:** `scientific_publication` | **Predicted:** `news_article`

**Reasoning:**
> The image shows a newspaper/magazine page with "Science" header, headline "Theory explaining cancer partly retracted", byline "Jeffrey L. Fox, C&EN, Washington", multi-column layout, publication date "Sept. 7, 1981 C&EN". This is published journalism with byline, columns, publication name (C&EN - Chemical & Engineering News). Classify as news_article.

---

## questionnaire → letter (1 errors)

### `processed_balanced__questionnaire__questionnaire_522769191+-9192_page_0001.png`
**Expected:** `questionnaire` | **Predicted:** `letter`

**Reasoning:**
> Formal letter with addresses, date, salutation.

---

## questionnaire → form (1 errors)

### `processed_balanced__questionnaire__questionnaire_2028715066_page_0001.png`
**Expected:** `questionnaire` | **Predicted:** `form`

**Reasoning:**
> The document is a Belgian "REGIE VAN TELEGRAFIE EN TELEFONIE" form for "VERBINTENIS VOOR EEN MOBILOFOONTOESTEL" (subscription for a mobile phone device). It has many blank fields with dotted lines to fill in: name, address, ID card number, etc. This is clearly a form with blank fields. Classify as form.

---

## presentation → memo (1 errors)

### `processed_balanced__presentation__presentation_2040742530_2040742574_page_0001.png`
**Expected:** `presentation` | **Predicted:** `memo`

**Reasoning:**
> Speech/remarks text. No letter format, no memo header. Likely presentation? It's a typed speech... Best fit: letter? No addresses. Probably "presentation"? Hmm. Speech text pages often classified as memo/letter... I'd pick memo? No headers. Closest: letter? Actually typed remarks — I'd go with memo? No. Choose "letter" seems wrong. Tobacco docs speech often labeled "memo"? I'll pick memo.

---

## presentation → scientific_report (1 errors)

### `processed_balanced__presentation__presentation_0000128701_page_0001.png`
**Expected:** `presentation` | **Predicted:** `scientific_report`

**Reasoning:**
> The image shows a cover/title page with "VRL COPY RESEARCH", "PHASE I: COPY CONCEPT STUDY", "McCann-Erickson, Inc. Research Department", "August 28, 1980", and an ID number stamped vertically. It's mostly a title/cover page for a research study. It presents research findings? It's a cover page of a copy concept study by an ad agency research department. This is an internal research report, not published journal. Classify scientific_report. Ensure not file_folder: it has more than just label, title and org/date. It is a report cover. Final only class name.

---

## news_article → scientific_publication (1 errors)

### `processed_balanced__news_article__news_article_tob06202.11_tob06202.13_page_0001.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The image shows a journal page header "American Journal of Agricultural Economics", article title, authors, published journal evidence, copyright 1983. Classify scientific_publication. Need output only class name.

---

## specification → scientific_report (1 errors)

### `processed_balanced__specification__specification_504660910_page_0001.png`
**Expected:** `specification` | **Predicted:** `scientific_report`

**Reasoning:**
> The document shows "MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER" with a table of chemical analysis data (puff count, TPM, nicotine, etc.) for different product codes PD 142A-D. This is a technical/scientific data table presenting research findings on smoke analysis. No journal header, so not scientific_publication. It presents original research/analysis findings without journal attribution → scientific_report. Not a specification (not defining product requirements). Output only class.

---

## form → scientific_report (1 errors)

### `processed_balanced__form__form_2028882198_2199_page_0001.png`
**Expected:** `form` | **Predicted:** `scientific_report`

**Reasoning:**
> This is a QA inspection document from INBIFO (Institute for Biological Research) regarding mutagenicity of cigarette smoke condensate. It's a research/lab QA report, internal document, not published. Classify as scientific_report.

---

## file_folder → scientific_publication (1 errors)

### `processed_balanced__file_folder__file_folder_2048267049_page_0001.png`
**Expected:** `file_folder` | **Predicted:** `scientific_publication`

**Reasoning:**
> The image appears to be a scanned document page, very degraded/noisy grayscale. It looks like dense text, possibly a published article or scientific text. There is a handwritten note at top right rotated: "Reduced D... judgment actions" maybe. A number 2048267049 at right edge. The page itself has two columns? Hard to tell. Need classify among 16. We must output only class name.

Need infer from visual: The image is mostly a full page of printed text with justified paragraphs, maybe from a book/article. No obvious letterhead, invoice, form fields. It has a handwritten annotation but majority is typed, so not handwritten. There are no journal headers visible due quality, no title. It resembles a page from a scientific publication? Dense typeset text, possibly journal page. But explicit evidence required for scientific_publication (journal name, volume etc). Not visible. Scientific_report should be last choice. Could be news_article? Published journalism with columns and publication names; image shows maybe newspaper-like dense columns? It is a single page portrait with article text in columns? Top right handwriting marginal note. It might be a scanned news article (old newspaper) with columns; degraded text, narrow column layout. But no visible publication name/byline. 

Given classification dataset likely RVL-CDIP samples; this noisy page with stamped number and handwriting could be "scientific_publication"? Let's choose based on layout: multi-column dense text page, no forms/tables. If published journal not evident, but visual of typeset article suggests scientific_publication over report. Need only label.

Final one word.

---

## file_folder → form (1 errors)

### `processed_balanced__file_folder__file_folder_2026448946_page_0001.png`
**Expected:** `file_folder` | **Predicted:** `form`

**Reasoning:**
> The image shows a document that appears to be a patent-related form. It has structured fields: INVENTOR, City of, County of, State of, Assignor of, TITLE, FILED, SERIAL No., etc. It has pre-printed labels with handwritten entries filled in. This is a form with blank fields being filled in. The layout is a structured data entry form (patent cover/file wrapper). According to rules, forms have blank fields to fill in. This is a printed form with handwritten entries. Majority is printed form fields, not purely handwritten. Classify as form.

---

## email → scientific_report (1 errors)

### `processed_balanced__email__email_521210052+-0053_page_0001.png`
**Expected:** `email` | **Predicted:** `scientific_report`

**Reasoning:**
> The document shows "Trial 9-002 - CO Reduction Study" with a data table containing trial IDs, graphite percentages, substrate types, WTPM, Nic, Gly, Water, CO, Tar, Nicotine, CO columns. This is research data, internal study. It's a scientific_report - internal research study presenting findings/data. Not published journal. Table of experimental results. Output scientific_report.

---

## budget → scientific_report (1 errors)

### `processed_balanced__budget__budget_01410567_page_0001.png`
**Expected:** `budget` | **Predicted:** `scientific_report`

**Reasoning:**
> The image shows a "MONTHLY MANAGEMENT STATUS REPORT" with project title "SOCIALLY ACCEPTABLE CIGARETTE", budget $13,054, project description, a budget vs actual chart, project components, and prepared by Warren Kelley. This is an internal research/project status report. It presents project status, budget tracking, and research findings (sample preparation, flavor evaluation). It's not published in a journal. It has budget elements but the overall document is a status report. Among categories, scientific_report fits best as an internal research report/technical study not published in a journal. It could be budget due to budget vs actual, but the document is a management status report for a research project. The critical rule says scientific_report last choice only when clearly presents research findings with methodology. This does present project description and sample evaluation. Output scientific_report.

---