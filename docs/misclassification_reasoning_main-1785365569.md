# Misclassification Reasoning — main-1785365569

**Overall Accuracy:** 89.3% (142/159)  
**Total Errors:** 17  
**Unique Confused Pairs:** 15

---

## questionnaire → form (2 errors)

### `processed_balanced__questionnaire__questionnaire_2061828115_2061828117_page_0001.png`
**Expected:** `questionnaire` | **Predicted:** `form`

**Reasoning:**
> The document is a Business Reply Mail envelope or card for "MERIT NOVEMBER SURVEY". It has the standard BRM markings, address to PO BOX 8076, DOVER DE, and barcode.
questionnaire

The document is a Business Reply Mail envelope/card for the "MERIT NOVEMBER SURVEY," which is a survey response mechanism. Given the context of a survey mailing piece, it aligns with the questionnaire category as it's part of a survey data collection effort.

---
### `processed_balanced__questionnaire__questionnaire_2028715066_page_0001.png`
**Expected:** `questionnaire` | **Predicted:** `form`

**Reasoning:**
> The document is a form with blank fields to fill in, tables for personal and company data, Dutch language labels like "Naam", "Voornaam", etc. It's an application form for a mobile phone connection or...

---

## presentation → file_folder (2 errors)

### `processed_balanced__presentation__presentation_2071620949_0991_page_0001.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The image shows a mostly blank page with vertical text reading "COMPETITIVE BAR PROGRAMS" and a handwritten "A" and some number on the side. This looks like a file folder label or cover.
presentation

The vertical layout and handwritten elements suggest a folder tab, but "COMPETITIVE BAR PROGRAMS" functions as a clear program title, aligning it with presentation covers rather than a bare label. The guidelines prioritize meaningful titles over pure blankness, making this a presentation.

---
### `processed_balanced__presentation__presentation_0011840384_page_0001.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> (reasoning not exposed by model)

---

## memo → invoice (1 errors)

### `processed_balanced__memo__memo_71213540_page_0001.png`
**Expected:** `memo` | **Predicted:** `invoice`

**Reasoning:**
> The document is clearly an invoice. It has "INVOICE" in large letters, invoice number, date, billing details, amounts, etc.

---

## letter → memo (1 errors)

### `processed_balanced__letter__letter_518600431+-0431_page_0001.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The document has a header with:

---

## letter → budget (1 errors)

### `processed_balanced__letter__letter_40038317-8318_page_0001.png`
**Expected:** `letter` | **Predicted:** `budget`

**Reasoning:**
> The document is from "COUNCIL FOR TOBACCO RESEARCH - U.S.A., INC." It's addressed to "Research Foundation for SUNY" with details about a grantee, check amount, payment for second half, etc. It says "F...

---

## invoice → specification (1 errors)

### `processed_balanced__invoice__invoice_2024476471_page_0001.png`
**Expected:** `invoice` | **Predicted:** `specification`

**Reasoning:**
> The document is in German. It appears to be a rate sheet for hourly wages for assembly work.

---

## invoice → budget (1 errors)

### `processed_balanced__invoice__invoice_2021633316_page_0001.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The document is a "VOUCHER" from Philip Morris. It has a date, "TO DEPT. OF PHARMACOLOGY TRUST FUND", and describes "PROFESSIONAL SERVICES FOR ANALYSES OF COMPOUNDS (2d qtr., 1984) BALANCE. $7,260.00"...

---

## handwritten → advertisement (1 errors)

### `processed_balanced__handwritten__handwritten_517517307+-7310_page_0001.png`
**Expected:** `handwritten` | **Predicted:** `advertisement`

**Reasoning:**
> The image appears to be a scanned document, mostly blank or with heavy black bars (perhaps redacted or a poor scan), but there's a clear section in the bottom right that looks like a coupon or mail-in...advertisement

The document is a promotional mail-in response card for Winston cigarettes, featuring filled-in fields (name, address, checkboxes) and marketing text about tobacco aging.

---

## scientific_publication → news_article (1 errors)

### `processed_balanced__scientific_publication__scientific_publication_10202118_10202119_page_0001.png`
**Expected:** `scientific_publication` | **Predicted:** `news_article`

**Reasoning:**
> The document is from "Science" magazine, with the title "Theory explaining cancer partly retracted". It looks like a news article from C&EN (Chemical & Engineering News), dated Sept. 7, 1981.

---

## questionnaire → letter (1 errors)

### `processed_balanced__questionnaire__questionnaire_522769191+-9192_page_0001.png`
**Expected:** `questionnaire` | **Predicted:** `letter`

**Reasoning:**
> The document is a formal letter from R.J. Reynolds Tobacco Company. It has a company letterhead, date, address to a customer, salutation "Dear Valued Customer:", body text, and a signature from Mark C...

---

## news_article → scientific_publication (1 errors)

### `processed_balanced__news_article__news_article_tob06202.11_tob06202.13_page_0001.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The document is from the "American Journal of Agricultural Economics" with pages 117-119, titled "Social Cost of the Tobacco Program Redux" by Paul R. Johnson and Daniel T. Norton. It has a copyright ...

---

## scientific_report → presentation (1 errors)

### `processed_balanced__scientific_report__scientific_report_2501568872_page_0001.png`
**Expected:** `scientific_report` | **Predicted:** `presentation`

**Reasoning:**
> The document is a cover page or title page for a proposal. It has:
presentation

The document is a formal proposal cover page with a clear title ("42 D-SMOKE INHALATION STUDY..."), organizational branding, and proposal number, which aligns directly with the presentation category for title/cover pages of presentations or slide decks. The scientific content suggests a research proposal, but the structural features (logo INBIFO, date, copy number, and proposal header) match the presentation cover definition more closely than a scientific_report, which is reserved for internal reports lacking journal attribution and is explicitly not used for grant applications or project status documents. The absence of a full letter format or memo headers further supports this classification. This choice prioritizes the explicit inclusion of title/cover pages in the presentation rules while avoiding over-application of scientific_report. The tobacco industry context reinforces the proposal nature but doesn't shift the category. This is a clean classification based on the provided visual and textual elements. The document's purpose as a proposal cover page makes it fit the presentation category 100%. The analysis approach confirms this through layout examination, text reading, and disambiguation rules. The final output is presentation. The image shows a professional cover with clear structure. This classification is accurate. The response is presentation. The user query is handled correctly. The output is only the class name.

---

## form → specification (1 errors)

### `processed_balanced__form__form_2028882198_2199_page_0001.png`
**Expected:** `form` | **Predicted:** `specification`

**Reasoning:**
> The document is from INBIFO Institut für biologische Forschung · Köln. It's titled "ÜBERPRÜFUNG VON P 0500 / 3222 DURCH QA" which means "Review of P 0500 / 3222 by QA".
scientific_report

The document is a QA verification report for a scientific study on cigarette smoke mutagenicity, including parameters checked and objections noted. It fits the scientific_report category as an internal technical study report with methodology and findings, rather than a published journal article or product specification. The title and content focus on research validation, aligning with the rules for scientific reports over other categories. The filled table and GLP reference confirm it's a completed report, not a blank form or presentation. This classification prioritizes the document's purpose as a QA review of scientific research findings. The output is the class name only. No additional text. The document is from INB 0500 / 3222 DURCH QA, which is a QA review of a scientific study on mutagenicity of cigarette smoke. It has a table with checked parameters and no objections. It mentions GLP principles. This is a QA inspection form for a scientific study, which according to the rules is NOT scientific_report.

---

## file_folder → form (1 errors)

### `processed_balanced__file_folder__file_folder_2026448946_page_0001.png`
**Expected:** `file_folder` | **Predicted:** `form`

**Reasoning:**
> The document is a patent-related form. It has fields like INVENTOR, City of, County of, State of, TITLE, FILED, SERIAL No., etc. It's filled out with handwritten information about an invention: "Impro...

---

## email → specification (1 errors)

### `processed_balanced__email__email_521210052+-0053_page_0001.png`
**Expected:** `email` | **Predicted:** `specification`

**Reasoning:**
> The document is a table titled "Trial 9-002 - CO Reduction Study". It has columns like Trial ID, Slot Pattern, Graphite %, Sub, WTPM, Nic, Gly, Water, CO, and then FTC with Tar, Nicotine, CO.
specification

The table presents smoke analysis data (CO reduction study with tar, nicotine, CO measurements) as a technical testing result, which aligns with specification classification per the rules. This is not a journal publication, internal research report, or other categories.

---