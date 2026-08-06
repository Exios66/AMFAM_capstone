# Misclassification Reasoning — qwen3.7-flash_v18.1_high_320

**Overall Accuracy:** 84.6% (270/319)  
**Total Errors:** 49  
**Unique Confused Pairs:** 25

---

## specification → form (5 errors)

### `rvl_cdip__specification__0019.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the mandatory pre-scan and the 14 checks in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: None. There's a Bates number "398015304" at the bottom right. There are headers like "CS68XTOB CS68MAP CASING CROSS-REFERENCE 04/30/96 16:16". This looks like a computer printout or a system-generated report.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Content: Multiple tables with "CASING CROSS-REFERENCE", "BLEND CODE CROSS-REFERENCE", cut tobacco codes, status, change number, active date. Also handwritten signatures at the bottom. Not an identifier-only page.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Content: Mostly typed tables. Handwritten signatures at the bottom ("Wayne Sandefur 9/30/96", "JG Sneed 5/1/98"). Not majority handwritten.

Check 3: FAX TRANSMISSION SHEET -> form
- No fax header.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- No survey questions.

Check 5: PERSON'S CAREER HISTORY -> resume
- No.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- No journal masthead.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- No financial data, no payment demand.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- "CASING CROSS-REFERENCE", "BLEND CODE CROSS-REFERENCE". Lists cut tobacco (MT-019, MT-082, etc.), casing (C-407, C-428), blend (BW-2117, BW-2128), status, change number, active date.
- Is this a specification? "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table ... is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough".
- Wait, this is a cross-reference table for casing and blend codes. It maps cut tobacco to casing/blend and shows change numbers and active dates. It's a system-generated report or a data table.
- Let's check check 10: ADMINISTRATIVE FORM. "standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data". This is a cross-reference log.
- Let's re-read check 8: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table ... is a specification". This is a cross-reference table, not really a specification defining requirements. It's a log or a data table.
- Let's look at check 10 again: "A form does NOT have to be blank — a filled form recording data is still a form... This also covers: a standalone labeled data chart or table ... a records-management inventory or log table ... a QA/parameter review sheet."
- Wait, what about scientific_report? "Running narrative prose ... Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report." This page has no running prose. It's just tables and signatures.
- Let's reconsider specification (check 8): "test-analysis tables keyed to product/part codes ... is a specification". But this is a "Casing Cross-Reference" and "Blend Code Cross-Reference". It's a log of changes (Change Number, Active Date). It's essentially a database export or a log table.
- Is it a form? "administrative form ... filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data ... a records-management inventory or log table". This is a log table of casing/blend cross-references.
- Wait, look at the bottom: handwritten signatures "Wayne Sandefur 9/30/96", "JG Sneed 5/1/98". This looks like an approval or review sheet. "QA/parameter review sheet" is mentioned in check 10. But there are no QA parameters here, just cross-references.
- Let's re-read check 8: "manufacturing-change authorization ... followed by labeled approval/signature blocks ... is a specification, not a form. It defines the product's new composition/properties; the approval block is the sign-off on the change, not the page's function."
- This page has "Casing Cross-Reference" and "Blend Code Cross-Reference" with "Change Number" and "Active Date". It's a log of changes. Is it a specification? No, it doesn't define what the product *will be*, it just lists historical changes (HIST status, change numbers like 94-0049, active dates).
- So it's not a specification.
- Is it a form? "standalone labeled data chart or table ... holds generic administrative/log data". Yes, this is a log table. "records-management inventory or log table".
- Let's check if there's any other category.
- What about "scientific_report"? No prose.
- What about "presentation"? No.
- What about "email"? No.
- What about "memo"? No.
- What about "letter"? No.

Let's carefully evaluate Check 10 (form) vs Check 8 (specification).
Check 8: "test-analysis tables keyed to product/part codes ... is a specification". But this is a cross-reference log, not a test-analysis table. "A product-change authorization or review page ... is a specification ... It defines the product's new composition/properties". This page does not define new composition; it lists past changes (HIST status, change numbers, active dates). So it's not a specification.
Check 10: "standalone labeled data chart or table ... holds generic administrative/log data". This is a table of cross-references and change logs. It has columns: CUT TOBACCO, STATUS, CHANGE NUMBER, ACTIVE DATE. It's a log table. Therefore, it's a form.

Wait, is there any other check?
Check 1: file_folder. No, it has real content (tables).
Check 2: handwritten. No, mostly typed.
Check 3: fax. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial. No.
Check 8: specification. No, it's a log of changes, not a product specification or test-analysis table defining requirements.
Check 9: presentation. No.
Check 10: form. Yes, a standalone labeled data table/log table with administrative/log data (casing/blend cross-references, change numbers, active dates).
Check 11: correspondence. No.
Check 12: news_article. No.
Check 13: scientific_report. No, no running prose.
Check 14: advertisement. No.

Let's double check Check 8 vs Check 10.
"A labeled product/parameter rate-data chart — e.g. a statistical process-control chart titled with the product name ... plotting a measured property over time/subgroup against spec limits ... is a specification"
"But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
This table has product tie-in (Capri Menthol Export, Capri Lights Box, Kool XL). But it has no requirement language, no "shall/must", no spec limits. It's just a log of changes (Change Number, Active Date, Status = HIST). This is a log table. Log tables are forms (check 10: "a records-management inventory or log table").

Also, the handwritten signatures at the bottom ("Wayne Sandefur 9/30/96", "JG Sneed 5/1/98") indicate it's a document that was reviewed/approved, which is common for forms/reports. But since there's no narrative prose, it falls under form (check 10) as a filled/printed log table. Wait, check 10 says "a filled form recording data is still a form, including handwriting in its cells." Here the handwriting is signatures at the bottom, not filling cells. But the table itself is a printed log. "standalone labeled data chart or table ... holds generic administrative/log data". This fits perfectly.

Let's review the table content:
"CASING CROSS-REFERENCE"
Casing: C-407
Cut Tobacco | Status | Change Number | Active Date
MT-019 | Capri Menthol Export... | HIST | 94-0049 | 3/18/94
...
This is a system-generated report or log table. Since it's a standalone labeled data table holding log data (cross-references and change history), it is a form (check 10).

Wait, could it be scientific_report? "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report." This page has no running prose. So not scientific_report.

Could it be specification? "test-analysis tables keyed to product/part codes ... is a specification". But this is not a test-analysis table. It's a cross-reference log. "A product-change authorization or review page ... is a specification ... It defines the product's new composition/properties". This page does not define new composition; it just lists historical changes. So not specification.

Therefore, form is the correct label.

Let's check if there's any email/memo header. No.
Any financial data? No.
Any presentation elements? No.

The page is a printed log table (Casing Cross-Reference, Blend Code Cross-Reference) with handwritten signatures at the bottom.
Check 10: ADMINISTRATIVE FORM -> form.
Evidence: "standalone labeled data chart or table ... holds generic administrative/log data". The page contains multiple tables titled "CASING CROSS-REFERENCE" and "BLEND CODE CROSS-REFERENCE" with columns for Cut Tobacco, Status, Change Number, Active Date. This is a log table.

Runner-up: specification. Ruled out because the page is a historical log of changes (Status = HIST, Change Number, Active Date) rather than a document defining product composition, tolerances, or requirements (no "shall/must" language, no spec limits, no test-analysis data).

Let's confirm the exact strings:
"label>form</label>"
"confidence>85</confidence>"

Wait, is there any possibility this is a "scientific_report"? No, no prose.
Is there any possibility this is a "presentation"? No, it's a raw data printout.
Is there any possibility this is a "file_folder"? No, it has substantial table content.

I am confident in "form".

Let's quickly review the pre-scan and checks again.
Pre-scan: Bates number 398015304. No mail header. No masthead.
Check 1: file_folder. No, has tables.
Check 2: handwritten. No, mostly typed.
Check 3: fax. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial. No.
Check 8: specification. No, log table, not spec.
Check 9: presentation. No.
Check 10: form. Yes, log table.
Check 11: correspondence. No.
Check 12: news_article. No.
Check 13: scientific_report. No, no prose.
Check 14: advertisement. No.

Final label: form.
Confidence: 85.
Evidence for form: "CASING CROSS-REFERENCE" and "BLEND CODE CROSS-REFERENCE" tables with columns "CUT TOBACCO", "STATUS", "CHANGE NUMBER", "ACTIVE DATE". This is a standalone labeled data table holding administrative/log data.
Runner-up: specification. Ruled out because it's a historical change log (Status = HIST) without requirement language, tolerances, or test-analysis data.

---
### `rvl_cdip__specification__0017.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

**Pre-scan:**
- Mail-client header block: None.
- Masthead or running head: No newspaper/magazine masthead. No journal running head/volume/issue/page number on this specific page (just a Bates number "50623 9622" on the right side, and "Page 1 A:AL116.RPT 11/17/87 16:00:04.59" at the bottom).

**Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a lot of data: run date, filename, cigarette info, port #, puff count, mass, chamber conditions, analyte table, signature. Not identifier-only.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Mostly typed text and data tables. Only a signature "D. L. HEAVNER" and some handwritten-looking signature. Not majority handwritten.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions, rating scales, or commitment forms.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No biographical info.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, DOI, or copyright line belonging to a journal. The bottom says "ASYST Version 2.00 Page 1 A:AL116.RPT 11/17/87 16:00:04.59". This looks like a computer printout/report.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial data, no payment demand, no budget tracking. Data is about cigarette smoke analysis (CO, NOx, NO2, FID, CO2, PIEZO1, RAM-1, CNC).
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: The page shows test data ("TWO HOUR INTEGRATED AVERAGES(BACKGROUND SUBTRACTED)", "ANALYTE", "TOTAL", "/CIG"). It's a report of test results, not defining a product's requirements, tolerances, or "shall/must" language. It's a data output from a system ("ASYST Version 2.00").
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck, cover, or statement.
- Not this check.

**Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: Has fields like "RUN DATE:", "FILENAME:", "CIGARETTE:", "PORT #", "PUFF COUNT", etc. But it's a computer printout of data ("A:AL116.RPT"). Not an administrative form for capturing factual data manually.
- Not this check.

**Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: No TO/FROM/RE header, no salutation, no closing.
- Not this check.

**Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: No masthead, byline, dateline.
- Not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: "RUN DATE: 23 NOV 87 FILENAME: A:AL116.DAT CIGARETTE: 2 1R4F SEMS". Data tables of chamber conditions, analytes (CO, NOx, NO2, FID, CO2, PIEZO1, RAM-1, CNC). "NOTE: OK--SUBJ#1 = D. WINGATE , SUBJ #2 = B. HAMLIN". Signed by "D. L. HEAVNER". Bottom: "ASYST Version 2.00 Page 1 A:AL116.RPT 11/17/87 16:00:04.59". This is a technical/lab data report or scientific report output. Wait, is it a scientific_report? "Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
Wait, check 13 says: "Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
This page is mostly data tables and field-value entries. "RUN DATE: ... FILENAME: ... CIGARETTE: ... PORT # PUFF COUNT ... CHAMBER CONDITIONS: ... ANALYTE TOTAL /CIG ... NOTE: ... D. L. HEAVNER [signature]".
Is this a form or a scientific report?
Let's re-read check 10: "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) ... is a form". Wait, check 10 says: "a filled analytical or lab data sheet ... is a form".
Let's check check 10 again: "This also covers: ... a filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)".
This page is a computer printout of analytical data ("TWO HOUR INTEGRATED AVERAGES(BACKGROUND SUBTRACTED)", "ANALYTE", "TOTAL", "/CIG"). It has field-value entries ("RUN DATE:", "FILENAME:", "CIGARETTE:", "CHAMBER CONDITIONS:", "PRESSURE(TORR):", etc.).
Wait, what about check 13? "a hand-plotted experimental graph of test measurements ... is a research test result (check 13), not a form". But this is a typed printout, not hand-plotted.
Is there any other category?
Let's re-evaluate check 10 vs check 13.
Check 10: "Administrative Form ... A filled analytical or lab data sheet ... is a form".
Check 13: "Original Research Write-up ... Requires running prose ... a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
Since this page is ONLY labeled field-value entries and data tables (no running narrative prose), it falls under check 10 (form) according to the explicit exclusion in check 13 and the inclusion in check 10 ("filled analytical or lab data sheet").
Wait, is there any other check?
What about check 8: "Product-referenced test data is a specification. A titled product-analysis table ... is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough".
But this page doesn't have a title like "MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER". It's just a raw data printout from "ASYST Version 2.00".
Let's look at the data: "CIGARETTE: 2 1R4F SEMS". "ANALYTE ... CO(PPM) ... NOx(PPM) ...". This is lab data.
Check 10 explicitly mentions: "a filled analytical or lab data sheet ... is a form".
Wait, check 10 says: "It does NOT cover money records ... It does NOT cover product-change authorization pages ... A hand-plotted experimental GRAPH ... is a research test result (check 13), not a form".
This is a computer printout of lab data. Is it a form?
Let's re-read check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; ... A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) ... is a form".
This page has "RUN DATE:", "FILENAME:", "CIGARETTE:", "PORT #", "PUFF COUNT", "INITIAL MASS", "FINAL MASS", "MASS CONSUMED", "CHAMBER CONDITIONS:", "PRESSURE(TORR):", "TEMPERATURE(K):", "PIEZOI LPM:", "PIEZOI SLPM:", "ANALYTE", "TOTAL", "/CIG". These are labeled fields and data tables. It's a lab data sheet / printout. Thus, form.

Wait, is there any chance it's a scientific_report?
Check 13: "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
This page has NO running prose. It's just headers, data tables, a note, and a signature. So it cannot be scientific_report.

Could it be a specification?
Check 8: "Material Safety Data Sheet ... product formulation ... manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or "shall/must" requirement language. Product-referenced test data is a specification. A titled product-analysis table ... is a specification".
This page is not titled "product-analysis table". It's a raw data printout "A:AL116.RPT". It doesn't define requirements, tolerances, or "shall/must". It just reports measured values. So not specification.

Could it be a presentation?
Check 9: "Slide/overhead layouts ...". No.

So it must be form (check 10).
Let's double check check 10 evidence:
- "RUN DATE: 23 NOV 87"
- "FILENAME: A:AL116.DAT"
- "CIGARETTE: 2 1R4F SEMS"
- Table with "PORT #", "PUFF COUNT", "INITIAL MASS(mg)", "FINAL MASS(mg)", "MASS CONSUMED(mg)"
- "CHAMBER CONDITIONS: STATIC MODE/100% FANS 72F/50% RH"
- "PRESSURE(TORR): 743.3"
- "TEMPERATURE(K): 296.8"
- "ANALYTE", "TOTAL", "/CIG" table with CO, NOx, NO2, FID, CO2, PIEZO1, RAM-1, CNC.
- "NOTE: OK--SUBJ#1 = D. WINGATE , SUBJ #2 = B. HAMLIN"
- Signature "D. L. HEAVNER"
- "ASYST Version 2.00 Page 1 A:AL116.RPT 11/17/87 16:00:04.59"

This is a filled analytical or lab data sheet (computer printout). Check 10 explicitly includes "a filled analytical or lab data sheet".
Therefore, form is the correct label.

Let's review the scratchpad requirements:
- Walk checks 1-14 in order.
- State evidence or "not this check".
- Stop at first matching check.
- Add final line naming runner-up and evidence that ruled it out.

Check 1: file_folder. Evidence: page has extensive data tables and field entries. Not this check.
Check 2: handwritten. Evidence: mostly typed computer printout with one signature. Not this check.
Check 3: fax sheet. Evidence: no fax header. Not this check.
Check 4: questionnaire. Evidence: no survey questions. Not this check.
Check 5: resume. Evidence: no biographical info. Not this check.
Check 6: scientific_publication. Evidence: no journal masthead/volume/issue. Not this check.
Check 7: financial. Evidence: no financial data or payment demand. Not this check.
Check 8: specification. Evidence: no "shall/must" language, no product requirements, just raw test data printout. Not this check.
Check 9: presentation. Evidence: not a slide deck or cover. Not this check.
Check 10: form. Evidence: "filled analytical or lab data sheet" with labeled fields ("RUN DATE:", "FILENAME:", "CIGARETTE:", "CHAMBER CONDITIONS:", "ANALYTE" table) and data entries. Matches check 10.
Check 11: correspondence. Evidence: no TO/FROM/RE or salutation. Not this check.
Check 12: news_article. Evidence: no masthead or journalistic typography. Not this check.
Check 13: scientific_report. Evidence: requires running prose; this page is only labeled field-value entries and data tables, which check 13 explicitly excludes and routes to form (check 10). Not this check.
Check 14: advertisement. Evidence: no promotional material. Not this check.

Runner-up: scientific_report. Ruled out because check 13 requires running narrative prose, and the page contains only labeled field-value entries and data tables, which check 13 explicitly states is a filled form (check 10).

Let's refine the evidence for Check 10:
"RUN DATE:", "FILENAME:", "CIGARETTE:", "CHAMBER CONDITIONS:", "ANALYTE" table with "TOTAL" and "/CIG" columns. This is a filled analytical/lab data sheet (computer printout), which check 10 explicitly covers.

Wait, is there any possibility this is a specification?
Check 8: "test-analysis tables keyed to product/part codes, tolerances, or "shall/must" requirement language. Product-referenced test data is a specification. A titled product-analysis table ... is a specification".
The page has "CIGARETTE: 2 1R4F SEMS" and analyte data. But it's not a "titled product-analysis table" defining requirements. It's a raw data printout "A:AL116.RPT" from "ASYST Version 2.00". The absence of a defining title, tolerances, or "shall/must" language makes it not a specification. It's just lab data. Check 10 covers "filled analytical or lab data sheet".

I am confident in `form`.

Let's do a quick final review of the text:
"RUN DATE: 23 NOV 87 FILENAME: A:AL116.DAT CIGARETTE: 2 1R4F SEMS"
"PORT # PUFF COUNT INITIAL MASS(mg) FINAL MASS(mg) MASS CONSUMED(mg)"
"CHAMBER CONDITIONS: STATIC MODE/100% FANS 72F/50% RH"
"ANALYTE TOTAL /CIG"
"CO(PPM): 5.16 2.58"
"NOTE: OK--SUBJ#1 = D. WINGATE , SUBJ #2 = B. HAMLIN"
"D. L. HEAVNER [signature]"
"ASYST Version 2.00 Page 1 A:AL116.RPT 11/17/87 16:00:04.59"

This is clearly a lab data printout / analytical data sheet. Check 10 explicitly includes "a filled analytical or lab data sheet". Check 13 explicitly excludes pages with "only labeled field-value entries" from scientific_report and routes them to form.

Final label: form.
Confidence: 95.
Runner-up: scientific_report, ruled out by lack of running prose and explicit check 13 routing of field-value entries to form.

---
### `rvl_cdip__specification__0013.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: None. Just a Bates number "50512 3457" at the bottom right. "PAGE 1 OF 3" at top right.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Content: Has a lot of text, fields, instructions. Not identifier-only.
- Not this check.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Content: Typed text. No majority handwriting.
- Not this check.

Check 3: FAX TRANSMISSION SHEET -> form
- Header: "DATE . FRI, MAR 1, 1985, 8:21 AM", "PAGE 1 OF 3", "TEST NUMBER: PD00237", "CHARGE NUMBER: 1300". No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Content: "TEST PURPOSE: CONSUMER SATISFACTION PROGRAM", "TYPE OF PANEL TESTING: CLT". Instructions for tobacco processing, filter making, making & packing, testing. Not asking the reader to answer/rate/commit.
- Not this check.

Check 5: PERSON'S CAREER HISTORY -> resume
- Content: Not a resume.
- Not this check.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- Content: No journal masthead, volume, issue, page range.
- Not this check.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- Content: No line-item table, ledger, statement, payment demand. "CHARGE NUMBER: 1300" is present, but no financial data table or payment demand.
- Not this check.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- Content: "CLASSIFICATION: WINS KS", "TEST PURPOSE: CONSUMER SATISFACTION PROGRAM", "SPECIAL INSTRUCTIONS: TOBACCO PROCESSING: ... USE AS DESCRIBED IN BLEND FORMULATION. ANALYSE EACH BLEND COMPONENT FOR NICOTINE AND REDUCING SUGARS BEFORE MAKING PRODUCT. FILTER MAKING: PREPARE FILTERS AS DESCRIBED USING CURRENT WIN. KS CONFIGURATION AND SPECS. MAKING & PACKING: ... TESTING: STANDARD ANALYSES."
- Wait, is this a specification? It has instructions for making and testing a product (WINS KS). "USE AS DESCRIBED IN BLEND FORMULATION", "PREPARE FILTERS AS DESCRIBED USING CURRENT WIN. KS CONFIGURATION AND SPECS."
- Let's look at check 10: ADMINISTRATIVE FORM.
- Fields: "DATE", "TEST NUMBER", "CHARGE NUMBER", "PRIORITY", "REQUESTED BY", "DATE REQUESTED", "RELATED TEST NUMBER", "DIVISION", "CLASSIFICATION", "TEST PURPOSE", "MAKING AND PACKING DATE", "MAIL OUT DATE", "TYPE OF PANEL TESTING", "SPECIAL INSTRUCTIONS", "TOBACCO PROCESSING", "FILTER MAKING", "MAKING & PACKING", "TESTING".
- This looks like a test request form or a work order form. It captures factual data and provides instructions for a test.
- Let's re-read check 8: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all... is an administrative form (check 10), not a specification."
- Wait, check 8 says "product formulation or preparation/mixing instructions". This document has "SPECIAL INSTRUCTIONS" for "TOBACCO PROCESSING", "FILTER MAKING", "MAKING & PACKING", "TESTING". It is essentially a test request / work order form.
- Let's look at check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... a QA/parameter review sheet... internal authorization/approval forms with an approval signature/date block."
- This document has labeled fields: "DATE", "TEST NUMBER", "CHARGE NUMBER", "REQUESTED BY", "CLASSIFICATION", "TEST PURPOSE", "TYPE OF PANEL TESTING", "SPECIAL INSTRUCTIONS", etc. It is a form used to request a test and provide instructions.
- Is it a specification? "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language." This page doesn't have a table of test-analysis data, it has instructions. "product formulation or preparation/mixing instructions" - it says "USE AS DESCRIBED IN BLEND FORMULATION", "PREPARE FILTERS AS DESCRIBED USING CURRENT WIN. KS CONFIGURATION AND SPECS." It refers to other documents for the actual specs. This is a test request form / work order.
- Let's check check 10 again: "administrative form ... capturing factual data". This is a test request form.
- Let's check check 13: "ORIGINAL RESEARCH WRITE-UP -> scientific_report". Requires running narrative prose. This is not narrative prose.
- Let's check check 11: "CORRESPONDENCE -> email, memo, or letter". No TO/FROM/RE header block followed by prose. It's a form with fields.

Let's carefully evaluate Check 8 vs Check 10.
Check 8: "product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language."
The text says: "TOBACCO VARIETY CS3-44X IS STORED IN DAVIE COUNTY HHD #05326032-9; SHED #010529. USE AS DESCRIBED IN BLEND FORMULATION. ANALYSE EACH BLEND COMPONENT FOR NICOTINE AND REDUCING SUGARS BEFORE MAKING PRODUCT."
"FILTER MAKING: PREPARE FILTERS AS DESCRIBED USING CURRENT WIN. KS CONFIGURATION AND SPECS."
"MAKING & PACKING: NEED 20 CTNS. BANDED & 60 CTNS. NOT BANDED. MAKE PRODUCT TO FIRMNESS. DO NOT SAMPLE ON MAKING AND PACKING FLOOR. SAMPLES WILL BE PULLED LATER."
"TESTING: STANDARD ANALYSES."
This is a test request / work order form. It has fields like "TEST NUMBER", "CHARGE NUMBER", "REQUESTED BY", "CLASSIFICATION", "TEST PURPOSE", "SPECIAL INSTRUCTIONS". It is capturing data for a test request.
Check 10: "administrative form ... Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This page has labeled fields and filled-in text (or typed instructions) for a test request.
Wait, is there any other check?
What about check 10: "A QA/parameter review sheet." "internal authorization/approval forms".
This is a test request form. Test request forms are administrative forms.

Let's re-read Check 8 carefully: "Product-referenced test data is a specification. A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough; you don't need a code like 'PD 142A' specifically, just clear evidence the table's subject is a product's own composition or properties."
This page is NOT a product-analysis table. It's a test request with instructions.

Let's re-read Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application (research grant, employment, service request); a records-management inventory or log table... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: ... internal authorization/approval forms with an approval signature/date block."
A test request form is a service request / application for testing. It has fields: DATE, TEST NUMBER, CHARGE NUMBER, PRIORITY, REQUESTED BY, DATE REQUESTED, RELATED TEST NUMBER, DIVISION, CLASSIFICATION, TEST PURPOSE, MAKING AND PACKING DATE, MAIL OUT DATE, TYPE OF PANEL TESTING, SPECIAL INSTRUCTIONS, TOBACCO PROCESSING, FILTER MAKING, MAKING & PACKING, TESTING.
This is definitely a form.

Let's check if there's any other category.
Could it be a scientific_report? No narrative prose.
Could it be a specification? It has instructions, but it's not defining the product's composition/tolerances/requirements; it's instructing the lab/manufacturing on how to process a specific test request ("TEST NUMBER: PD00237", "CLASSIFICATION: WINS KS", "TEST PURPOSE: CONSUMER SATISFACTION PROGRAM"). It refers to "BLEND FORMULATION" and "WIN. KS CONFIGURATION AND SPECS" for the actual requirements. So it's not a specification itself.

Therefore, Check 10 (form) is the correct match.

Let's double check Check 1: file_folder. No, has real content.
Check 2: handwritten. No.
Check 3: fax. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial. No.
Check 8: specification. No, it's a test request form, not a product spec.
Check 9: presentation. No.
Check 10: form. Yes, labeled fields for capturing test request data and instructions.
Check 11: correspondence. No.
Check 12: news_article. No.
Check 13: scientific_report. No.
Check 14: advertisement. No.

Evidence for Check 10:
- Labeled fields: "DATE", "TEST NUMBER", "CHARGE NUMBER", "REQUESTED BY", "CLASSIFICATION", "TEST PURPOSE", "TYPE OF PANEL TESTING", "SPECIAL INSTRUCTIONS", "TOBACCO PROCESSING", "FILTER MAKING", "MAKING & PACKING", "TESTING".
- Capturing factual data for a test request (PD00237, WINS KS, Consumer Satisfaction Program).
- This is an administrative form (test request / work order).

Runner-up: specification (check 8). Ruled out because the page is a test request form with instructions referring to other documents ("USE AS DESCRIBED IN BLEND FORMULATION", "CURRENT WIN. KS CONFIGURATION AND SPECS"), rather than defining the product's composition, tolerances, or requirements itself. It lacks test-analysis tables or "shall/must" requirement language for the product's properties.

Let's confirm the confidence. The evidence for form is very clear (labeled fields, test request data). Confidence: 90.

Wait, is there any possibility it's a scientific_report? "TEST PURPOSE: CONSUMER SATISFACTION PROGRAM". No, it's just a form header.
Is it a memo? No TO/FROM/RE header.
Is it an invoice? No payment demand.

Final check of the text:
DATE . FRI, MAR 1, 1985, 8:21 AM
PAGE 1 OF 3
TEST NUMBER: PD00237
CHARGE NUMBER: 1300
PRIORITY:
REQUESTED BY: WILSON, JOHN (5979)
DATE REQUESTED: 840705
RELATED TEST NUMBER:
DIVISION: 775
CLASSIFICATION: WINS KS
TEST PURPOSE: CONSUMER SATISFACTION PROGRAM
MAKING AND PACKING DATE:
MAIL OUT DATE:
TYPE OF PANEL TESTING: CLT
SPECIAL INSTRUCTIONS:
TOBACCO PROCESSING: TOBACCO VARIETY CS3-44X IS STORED IN DAVIE COUNTY HHD #05326032-9; SHED #010529. USE AS DESCRIBED IN BLEND FORMULATION. ANALYSE EACH BLEND COMPONENT FOR NICOTINE AND REDUCING SUGARS BEFORE MAKING PRODUCT.
FILTER MAKING: PREPARE FILTERS AS DESCRIBED USING CURRENT WIN. KS CONFIGURATION AND SPECS.
MAKING & PACKING: NEED 20 CTNS. BANDED & 60 CTNS. NOT BANDED. MAKE PRODUCT TO FIRMNESS. DO NOT SAMPLE ON MAKING AND PACKING FLOOR. SAMPLES WILL BE PULLED LATER.
TESTING: STANDARD ANALYSES.

This is a test request form / work order. It has fields and filled-in text. It is a form.

Label: form
Confidence: 90

---
### `rvl_cdip__specification__0006.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: None. There's a Bates number "50052 7368" on the right edge. "RJR CLASS NO. PATENT" at the bottom. No journal masthead.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Content: The page has a lot of content: "Analytical information (detailed)", "Quantitative", "Qualitative", "Structural Formula", "Types of Tobacco", "Tox.-Pharm. Inform. and other Notes", "Reference", "Bibliography", patent info ("British American Tobacco Limited... MATERIAL FOR FILTERING TOBACCO SMOKE..."). Not an identifier-only page.
- Not this check.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Content: Mostly typed. There is a handwritten word "Goldshield" at the top. Not majority handwritten.
- Not this check.

Check 3: FAX TRANSMISSION SHEET -> form
- No fax header.
- Not this check.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Not a survey instrument.
- Not this check.

Check 5: PERSON'S CAREER HISTORY -> resume
- Not a resume.
- Not this check.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- No journal running head, volume, issue, page range, DOI.
- Not this check.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- No financial content, no payment demand.
- Not this check.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- "MATERIAL FOR FILTERING TOBACCO SMOKE - CONTAINING CARBON PARTICLES COATED INTERNALLY - EXTERNALLY WITH POROUS LAYER OF ORGANIC POLYMER."
- Wait, this is a patent abstract or index card? "RJR CLASS NO. PATENT". "British American Tobacco Limited...". "Bibliography: If there is not sufficient space available for any of the categories, use reverse side, identifying category(ies), and write "over" on this side. List all answerable information for each constituent and do so in index style."
- This looks like a form for capturing patent/technical information. Let's look at check 10.

Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
- Not a slide deck.
- Not this check.

Check 10: ADMINISTRATIVE FORM -> form
- "Analytical information (detailed)" with fields: "Smoke", "Green", "Cured", "Non-Leaf", "Itemize:".
- "Quantitative (all figures)", "Qualitative only", "Quotes or Semi-quant."
- "Structural Formula", "Mol. Form", "Mol. Weight", "M. P.", "B. P.", "Chem. Groups", "Derivatives".
- "Types of Tobacco (all details)"
- "Tox.-Pharm. Inform. and other Notes"
- "Reference"
- "RJR CLASS NO. PATENT"
- "British American Tobacco Limited, Gt. Brit. MATERIAL FOR FILTERING TOBACCO SMOKE..."
- "Bibliography: If there is not sufficient space available..."
- "*1976, No. 5, W 1957* *d* Tobacco manufactures:"
- This is a structured form for capturing analytical information, patent details, and bibliography. It has labeled fields, ruled entry lines (implied by the layout), and instructions ("If there is not sufficient space available..."). It's a form for recording data about a patent/material.
- Wait, is it a specification? Check 8: "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language... A titled product-analysis table... is a specification". This page is not defining a product's composition or requirements; it's recording information about a patent (British American Tobacco Limited material for filtering tobacco smoke). It's an index card or form for patent/technical data capture.
- Let's re-read Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; ... internal authorization/approval forms with an approval signature/date block." This page has fields for "Analytical information", "Quantitative", "Qualitative", "Structural Formula", "Mol. Form", "Mol. Weight", "Types of Tobacco", "Tox.-Pharm. Inform.", "Reference", "RJR CLASS NO. PATENT", "Bibliography". It's a form for capturing factual data about a patent/material.
- Let's check if there's any other category. Scientific report? No narrative prose. Specification? No "shall/must", not defining a product's requirements, just recording patent info.
- So it's a form.

Let's double check Check 8 vs Check 10.
Check 8: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
This page is a form for capturing patent and analytical information. It has fields like "Analytical information (detailed)", "Quantitative", "Qualitative", "Structural Formula", "Mol. Form", "Mol. Weight", "M. P.", "B. P.", "Chem. Groups", "Derivatives", "Types of Tobacco", "Tox.-Pharm. Inform.", "Reference", "RJR CLASS NO. PATENT", "Bibliography". It's a structured data capture form. The content filled in is a patent abstract. This is a form (check 10).

Let's review the whole page.
Top: handwritten "Goldshield"
Fields: Analytical information (detailed) Smoke Green Cured Non-Leaf Itemize:
Quantitative (all figures) Qualitative only Quotes or Semi-quant.
Structural Formula Mol. Form Mol. Weight M. P. B. P. Chem. Groups Derivatives
Types of Tobacco (all details)
Tox.-Pharm. Inform. and other Notes
Reference
RJR CLASS NO. PATENT
British American Tobacco Limited, Gt. Brit. MATERIAL FOR FILTERING TOBACCO SMOKE - CONTAINING CARBON PARTICLES COATED INTERNALLY - EXTERNALLY WITH POROUS LAYER OF ORGANIC POLYMER.
German Patent OLS 2,527,569...
Bibliography: If there is not sufficient space available...
*1976, No. 5, W 1957* *d* Tobacco manufactures:

This is clearly a form used to index or record patent and analytical information. It has labeled sections and fields for capturing factual data. It matches Check 10: ADMINISTRATIVE FORM -> form.

Let's check if it could be scientific_report.
Check 13: "Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
This page has labeled field-value entries (the patent abstract is in the "Reference" or "RJR CLASS NO. PATENT" field). It lacks running narrative prose with methods/results/discussion. So not scientific_report.

Could it be specification?
Check 8: "specification defines a product's REQUIREMENTS — it states what a product IS or must be. Signals: part numbers, ingredient/formulation lists, tolerance ranges, shall/must language. A quality-check sheet, lab measurement log, or product-test data table that merely RECORDS measurements about a product is a form, not specification — it captures data rather than defining requirements."
This page records patent information and analytical data fields. It doesn't define requirements for a product. So not specification.

Therefore, form is the correct label.

Let's do a quick pass of the checks again to be sure.
1. file_folder: No, has real content (fields, patent text).
2. handwritten: No, mostly typed.
3. fax: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No journal header.
7. financial: No.
8. specification: No requirement language, not defining a product.
9. presentation: No.
10. form: Yes, structured fields for capturing factual data (analytical info, patent details, bibliography).
11. correspondence: No.
12. news_article: No.
13. scientific_report: No narrative prose.
14. advertisement: No.

Final label: form.
Confidence: 85. The evidence for form is strong (labeled fields, structured data capture layout, instructions for filling it out like "If there is not sufficient space available..."). Runner-up was specification, ruled out because it's recording patent data rather than defining product requirements/tolerances.
Wait, let's look at the instruction text: "Bibliography: If there is not sufficient space available for any of the categories, use reverse side, identifying category(ies), and write "over" on this side. List all answerable information for each constituent and do so in index style." This is classic form instruction text.

I'm confident in `form`.

---
### `rvl_cdip__specification__0004.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: None. There is a Bates number "50918 4384" rotated on the right side. No journal masthead.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Evidence: The page has a table of data, not just an ID.
- Not this check.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Evidence: Typed text and a table. Handwritten scribble at top left, but not majority.
- Not this check.

Check 3: FAX TRANSMISSION SHEET -> form
- Evidence: No fax header.
- Not this check.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Evidence: Not a survey.
- Not this check.

Check 5: PERSON'S CAREER HISTORY -> resume
- Evidence: Not a resume.
- Not this check.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- Evidence: No journal masthead, volume, issue, DOI.
- Not this check.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- Evidence: No financial data, no payment demand.
- Not this check.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- Evidence: The page contains a table of product parameters for "MORE 120 Menthol", "ABC Menthol", "Va. Slim Lts. 120 M", "Eve Lts. 120 M". Parameters include Weight, Draft, Dilution, Size, Moisture, Puffed Tob., Filter Length, Total Cigt. Length, Puff Count, Nicotine, Nic./Puff, Tar, Tar/pf., Nicotine %, Menthol %, Menthol mg. cigt., ug/Puff.
- The footnote says: "* Data represents Control MORE 120 Menthol (smoke data represents product smoked on SED for 1st round testing of ABC), the ABC Menthol prototype using high porosity micro-laser, and VSLM 120's/Eve Lts. M. 120 (ordered in for physical/analytical testing)."
- This is a product analysis table / test-analysis tables keyed to product codes, or a labeled product/parameter rate-data chart. Wait, check 8 says: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough". Here, the columns are titled with product names ("MORE 120 Menthol", "ABC Menthol", etc.) and rows are product parameters (Weight, Draft, Dilution, Size, Moisture, Tar, Nicotine, etc.). This is a product analysis table / specification of product parameters.
- Let's check check 10 just in case. "A standalone labeled data chart or table ... is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8)". This table shows measured parameters for specific products. Is it a specification? "Specification defines a product's REQUIREMENTS — it states what a product IS or must be. Signals: part numbers, ingredient/formulation lists, MSDS headers, tolerance ranges, shall/must language. A quality-check sheet, lab measurement log, or product-test data table that merely RECORDS measurements about a product is a form, not specification — it captures data rather than defining requirements."
- Wait! The calibration says: "A research study's own experimental data tables, test measurements, and results belong to scientific_report, not specification. Specification requires the page's PRIMARY function to be defining a product's composition, tolerances, or requirements — a technical report that merely contains data tables or measurement charts is still a report."
- Also check 8: "But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
- And check 10: "A financial chart that is presented as a TITLED, DESIGNED DECK CHART ... is presentation ... A standalone labeled data chart or table ... is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a research-measurement chart is scientific_report (check 13)..."
- Wait, what is this page? It's a table of smoke data and physical data for cigarette products. "Data represents Control MORE 120 Menthol (smoke data represents product smoked on SED for 1st round testing of ABC), the ABC Menthol prototype using high porosity micro-laser, and VSLM 120's/Eve Lts. M. 120 (ordered in for physical/analytical testing)."
- This is a data table recording measurements about a product. "A quality-check sheet, lab measurement log, or product-test data table that merely RECORDS measurements about a product is a form, not specification".
- Is it scientific_report? "Original research write-up -> scientific_report. Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report." This page has NO running prose, only a table and a footnote. So it's not scientific_report.
- Is it a form? "A standalone labeled data chart or table ... is a form only when it holds generic administrative/log data". This holds product test data. Wait, check 10 says: "a chart of a product's measured parameters against spec limits is specification (check 8)". But this table doesn't have spec limits, it just has the measured values.
- Let's re-read check 8: "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table ... is a specification even without an explicit alphanumeric product/part code in the table itself".
- Wait, the calibration says: "A research study's own experimental data tables, test measurements, and results belong to scientific_report, not specification. Specification requires the page's PRIMARY function to be defining a product's composition, tolerances, or requirements — a technical report that merely contains data tables or measurement charts is still a report."
- But this page is ONLY a table. "Requires running prose ... is a filled form (check 10), not a scientific report." So if it's not scientific_report, and not specification (because it doesn't define requirements, it just records measurements), what is it? Form?
- Let's look at check 10 again: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a research-measurement chart is scientific_report (check 13), and a financial/money chart is budget (check 7) ONLY when it is a standalone data table used for money planning or tracking... It does NOT cover money records... It does NOT cover product-change authorization pages..."
- Wait, if it's a "product-test data table that merely RECORDS measurements about a product is a form, not specification", then this page is a form!
- Let's check the text again: "Data represents Control MORE 120 Menthol (smoke data represents product smoked on SED for 1st round testing of ABC), the ABC Menthol prototype using high porosity micro-laser, and VSLM 120's/Eve Lts. M. 120 (ordered in for physical/analytical testing)."
- This is a table of test results. "A quality-check sheet, lab measurement log, or product-test data table that merely RECORDS measurements about a product is a form, not specification — it captures data rather than defining requirements."
- So it's a form (check 10).

Let's carefully evaluate Check 8 vs Check 10.
Check 8: "Product-referenced test data is a specification. A titled product-analysis table ... is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough; you don't need a code like 'PD 142A' specifically, just clear evidence the table's subject is a product's own composition or properties."
Wait, "Product-referenced test data is a specification." This is in Check 8.
But the calibration says: "A research study's own experimental data tables, test measurements, and results belong to scientific_report, not specification. Specification requires the page's PRIMARY function to be defining a product's composition, tolerances, or requirements — a technical report that merely contains data tables or measurement charts is still a report."
And Check 10 says: "A quality-check sheet, lab measurement log, or product-test data table that merely RECORDS measurements about a product is a form, not specification — it captures data rather than defining requirements."

Which one applies here? The page is a table of measurements (Weight, Draft, Dilution, Size, Moisture, Tar, Nicotine, etc.) for different cigarette products. It does not define requirements, tolerances, or "shall/must" language. It merely records measurements. Therefore, it is a form (check 10), not a specification (check 8).

Wait, is there any other category?
Could it be presentation? "A standalone chart or table of values alone — an untitled data table or a bare chart with no deck styling — is NOT a slide; it is a form (check 10). BUT a TITLED, DESIGNED DECK CHART ... IS a presentation". This table is not a designed deck chart. It's a plain text table.

Could it be scientific_report? "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report." This page has no running prose, only a table and a footnote. So not scientific_report.

Therefore, the label must be `form`.

Let's double check Check 10: "Administrative Form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; ... A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a research-measurement chart is scientific_report (check 13)..."
Wait, if a chart of a product's measured parameters against spec limits is specification, and this table is NOT against spec limits, then it's not specification. What about "generic administrative/log data"? This is product test data. Is product test data "generic administrative/log data"?
Check 10 also says: "A quality-check sheet, lab measurement log, or product-test data table that merely RECORDS measurements about a product is a form, not specification — it captures data rather than defining requirements." This explicitly covers product-test data tables that merely record measurements. This page is exactly that: a product-test data table recording measurements (smoke data, physical/analytical testing). So it is a form.

Let's review the evidence for `form`:
- Table with rows (Weight, Draft, Dilution, Size, Moisture, Puffed Tob., Filter Length, Total Cigt. Length, Puff Count, Nicotine, Nic./Puff, Tar, Tar/pf., Nicotine %, Menthol %, Menthol mg. cigt., ug/Puff) and columns (MORE 120 Menthol, ABC Menthol, Va. Slim Lts. 120 M, Eve Lts. 120 M).
- Footnote: "* Data represents Control MORE 120 Menthol (smoke data represents product smoked on SED for 1st round testing of ABC), the ABC Menthol prototype using high porosity micro-laser, and VSLM 120's/Eve Lts. M. 120 (ordered in for physical/analytical testing)."
- Function: capturing/recording test measurements for products.
- Check 8 (specification) requires defining requirements, tolerances, or "shall/must" language. This page merely records measurements.
- Check 13 (scientific_report) requires running narrative prose. This page has no running prose.
- Check 10 (form) explicitly states: "A quality-check sheet, lab measurement log, or product-test data table that merely RECORDS measurements about a product is a form, not specification".

Therefore, `form` is the correct label.

Let's quickly check if there's any other evidence.
Bates number: 50918 4384.
Handwritten mark at top left.
No mail header, no fax header, no masthead.

Final check of the steps:
1. file_folder: No, has real content (table).
2. handwritten: No, mostly typed.
3. fax: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No.
7. financial: No.
8. specification: No, merely records measurements, does not define requirements/tolerances.
9. presentation: No, not a designed deck chart.
10. form: Yes, product-test data table recording measurements.
11. correspondence: No.
12. news_article: No.
13. scientific_report: No, no running prose.
14. advertisement: No.

Runner-up: specification. Ruled out because the page merely records product test measurements without defining requirements, tolerances, or "shall/must" language, which check 10 explicitly classifies as a form.

Confidence: 85. The evidence for form is clear based on the explicit exclusion in check 10 and the calibration notes.

---

## scientific_report → form (5 errors)

### `rvl_cdip__scientific_report__0016.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: None. Just a Bates number "2505336064" on the right side and "2197" at the top right.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Content: There is a table with handwritten entries, headers like "EFFECT", "1 R4F", "UR5J4S-35", "FACTOR", "N", "INTER-CEPT", "SLOPE", "N", "INTER-CEPT", "SLOPE". There's a table at the bottom: "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR5J4S-35 ... ENERGY, RATE RATS, 62-DAY INHALATION PERIOD".
- Not file_folder. Real content present.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Most of the content is handwritten text filling out a table or listing effects (nose, larynx, trachea, lung, AHH).
- Wait, is it freeform handwriting or filling a printed template?
- The page has printed headers: "EFFECT", "1 R4F", "UR5J4S-35", "FACTOR", "N", "INTER-CEPT", "SLOPE", "N", "INTER-CEPT", "SLOPE".
- The bottom has printed text: "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR5J4S-35 ... ENERGY, RATE RATS, 62-DAY INHALATION PERIOD".
- The main body is handwritten lists of effects: "nose Level 1 reserve cell hypoplasia squamous metaplasia Level 2 atrophy", "larynx base of epiglottis...", "trachea...", "lung...".
- Is this majority handwritten? Yes, the vast majority of the text is handwritten.
- Wait, check 2 says: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout. It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form (or the content's own category...)"
- Here, the handwriting is listing effects (nose, larynx, trachea, lung) and some crossed-out text. It's not really filling cells of a printed table; the printed table headers are at the top, but the handwritten text is a freeform list of anatomical effects.
- Wait, look at the bottom: "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR5J4S-35 ... ENERGY, RATE RATS, 62-DAY INHALATION PERIOD". This looks like a scientific data table or a page from a scientific report.
- Let's re-read check 2: "A log/diary sheet is freeform, not a form... Notes ABOUT a survey instrument are questionnaire, not handwritten... A respondent's freeform handwritten opinion/feedback card... IS handwritten, NOT questionnaire".
- Is this a scientific_report? Check 13: "Original research write-up -> scientific_report. Running narrative prose with objectives, methods, results, or discussion... Also scientific_report: a hand-plotted experimental graph... a technical-study title page...". This page is just a handwritten table/list of effects and a table caption. It doesn't have running narrative prose.
- Wait, what about check 10: "Administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)..."
- This page is a handwritten lab data sheet / table of effects. "EFFECT", "1 R4F", "UR5J4S-35", "FACTOR". The columns are N, INTER-CEPT, SLOPE. The rows are handwritten effects: "nose Level 1 reserve cell hypoplasia...", "larynx...", "trachea...", "lung...".
- Is it a form? "A filled analytical or lab data sheet ... is a form (check 10)". But wait, check 13 says "a hand-plotted experimental graph of test measurements ... is a research test result (check 13), not a form". This is a handwritten table of data.
- Let's look closely at check 2: "Most of the content is freeform handwriting ... NOT on a printed template. ... It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form (or the content's own category: a handwritten list of budget categories and dollar amounts ... is budget, not handwritten)."
- Here, the handwriting is filling a printed table structure (the columns N, INTER-CEPT, SLOPE are printed at the top, and the handwritten text is the row labels and data). Wait, the handwritten text is just a list on the left side: "nose Level 1...", "larynx...", "trachea...", "lung...". The right side (the columns N, INTER-CEPT, SLOPE) is mostly EMPTY. The handwriting is just listing the effects.
- Actually, this looks like a page from a scientific report or a lab notebook. But since it's just a handwritten table of data without narrative prose, it might be a form (lab data sheet) or scientific_report.
- Let's re-evaluate check 13: "Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
- This page has labeled field-value entries (the table headers EFFECT, N, INTER-CEPT, SLOPE) and handwritten entries. It lacks running prose. So it's not scientific_report.
- Is it a form? "A filled analytical or lab data sheet ... is a form (check 10)". Yes, a lab data sheet capturing experimental data is a form.
- Wait, what about check 2? "Most of the content is freeform handwriting ... NOT on a printed template." The template has printed headers "EFFECT", "1 R4F", "UR5J4S-35", "FACTOR", and the column sub-headers "N", "INTER-CEPT", "SLOPE". The bottom has a printed table caption "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS...". This is a printed template (a lab data sheet / table). The handwriting fills the rows. Therefore, it is NOT check 2 (handwritten). It is check 10 (form) or check 13 (scientific_report). Since check 13 requires running prose, and this is only labeled field-value entries (a table), it falls to check 10 (form).
- Let's check check 10 again: "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) ... is a form (check 10)". This page is a lab data sheet with effects and dose ratio calculation parameters. It's a filled form.
- Wait, is there any other check? Check 8: specification. "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table ... is a specification". This table is "DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR5J4S-35 ... ENERGY, RATE RATS, 62-DAY INHALATION PERIOD". This is test data / analysis table. But does it define a product's composition/tolerances? No, it's calculating dose ratios for biological effects. This is experimental data, not a specification.
- Check 13: "Original research write-up -> scientific_report. ... Requires running prose ... a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
- So this is a filled form (lab data sheet).

Let's double check check 2 vs check 10.
Check 2: "Most of the content is freeform handwriting ... NOT on a printed template. ... It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form ... A log/diary sheet is freeform, not a form: a minimal sheet with only ONE typed column header ... and blank ruled lines, filled with running narrative entries by hand ... is handwritten, not a filled form — a form needs multiple typed data-column headers defining cells for structured capture, not one date column plus free writing space."
Here, we have multiple typed data-column headers: "EFFECT", "1 R4F" (with subheaders "N", "INTER-CEPT", "SLOPE"), "UR5J4S-35" (with subheaders "N", "INTER-CEPT", "SLOPE"), "FACTOR". This is a structured table with multiple typed data-column headers defining cells. The handwriting fills the rows (the EFFECT column is filled with handwritten text, and presumably the other columns would be filled with data, though they are blank here). This is a printed structured table. Thus, it is NOT check 2. It is check 10 (form).

Let's review the bottom text:
"TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR5J4S-35 ... ENERGY, RATE RATS, 62-DAY INHALATION PERIOD"
This is a caption for a table. The page is essentially a blank table template with some handwritten notes listing the effects that will be measured or have been measured. It's a lab data sheet / form.

Is there any chance this is scientific_report?
Check 13: "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
This page has no running prose. It's just a table header and handwritten list of effects. So it's not scientific_report.

Is there any chance this is specification?
Check 8: "Material Safety Data Sheet ... product formulation ... manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. ... A labeled product/parameter rate-data chart ... is a specification".
This is a "DOSE RATIO CALCULATION" table. It's not defining a product's requirements, tolerances, or composition. It's a calculation for biological effects. So not specification.

Therefore, the label is `form`.

Let's do a quick pass of the checks:
1. file_folder: No, has real content (table, handwritten text).
2. handwritten: No, handwriting fills a printed structured table with multiple typed data-column headers ("EFFECT", "1 R4F", "UR5J4S-35", "FACTOR" and subheaders). Not freeform on blank/lined paper.
3. fax sheet: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No.
7. financial: No.
8. specification: No, not defining product requirements/tolerances.
9. presentation: No.
10. form: Yes, filled analytical or lab data sheet / structured table with typed headers and handwritten entries.
11. correspondence: No.
12. news_article: No.
13. scientific_report: No, requires running prose; this is only labeled field-value entries.
14. advertisement: No.

Runner-up: scientific_report. Ruled out because check 13 requires running narrative prose, and this page is only a labeled table/form with handwritten entries (a lab data sheet), which check 10 explicitly covers as a form.

Wait, is there any possibility it's a scientific_report because it's a page from a report?
"Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
This perfectly matches the page: it's a labeled table (field-value entries) with handwritten data, no running prose. So it's a form.

Let's confirm the evidence for form:
- Typed headers: "EFFECT", "1 R4F", "UR5J4S-35", "FACTOR", "N", "INTER-CEPT", "SLOPE".
- Typed table caption: "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR5J4S-35 ... ENERGY, RATE RATS, 62-DAY INHALATION PERIOD".
- Handwritten entries filling the rows: "nose Level 1 reserve cell hypoplasia...", "larynx...", "trachea...", "lung...".
- This is a structured table / lab data sheet. Check 10 covers "filled analytical or lab data sheet".

Confidence: 85. The evidence for form is clear (structured table with typed headers and handwritten entries, no running prose). The runner-up scientific_report is ruled out by the lack of running prose.

Final check of the text:
Top right: "2197"
Right side vertical: "2505336064" (Bates number)
Headers: "EFFECT", "1 R4F", "UR5J4S-35", "FACTOR"
Subheaders: "N", "INTER-CEPT", "SLOPE", "N", "INTER-CEPT", "SLOPE"
Handwritten text: "nose Level 1 reserve cell hypoplasia squamous metaplasia Level 2 atrophy", "larynx base of epiglottis squamous metaplasia hyperplasia...", "trachea reserve cell hypoplasia", "lung reserve cell hypoplasia goblet cell hyperplasia", "AHH 3-OH-B(a)P".
Bottom: "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR5J4S-35 ... ENERGY, RATE RATS, 62-DAY INHALATION PERIOD"

Everything aligns with a lab data sheet / form.
Label: form.
Confidence: 85.

---
### `rvl_cdip__scientific_report__0012.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

**Pre-scan:**
- Mail-client header block: None.
- Masthead or running head: None. There's a Bates number "2050056147" on the right side, but no journal masthead or newspaper masthead.

**Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a title "B L PLANT ANALYTICAL SUMMARY SHEET", multiple tables with data, handwritten entries, sections like "BURLEY", "PRODUCTION DUST", "SLURRY", "FINISHED PRODUCT CHEMICAL ANALYSIS", "FINISHED PRODUCT % OV TARGET", "HOGSHEAD REPORT".
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: The page has a printed template with tables and headers, and the cells are filled with handwritten data. However, the majority of the page's *structure* is printed, and the handwriting is just filling in the fields of a printed structured form. Wait, check 2 says: "It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form (or the content's own category...)"
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: Not a survey instrument.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: Not a resume.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal running head, volume, issue, etc.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial data, no payment demand, no budget tracking. It's plant analytical data (dryer stems, nitrates, production dust, slurry, chemical analysis).
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: This is an analytical summary sheet recording measurements (average/S.D.) for various plant processes (Burley, Production Dust, Slurry, Finished Product Chemical Analysis, Hogshead Report). It records data, it doesn't define requirements, tolerances, or "shall/must" language for a product's composition. Wait, there are targets: "TARGET: 2.8 +/- 0.5", "TARGET RANGE: .66 TO 1.46". But it's a data capture sheet recording actual vs target. Check 8 says: "A quality-check sheet, lab measurement log, or product-test data table that merely RECORDS measurements about a product is a form, not specification — it captures data rather than defining requirements." This is a lab/production measurement log.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck.
- Not this check.

**Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: "B L PLANT ANALYTICAL SUMMARY SHEET". Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data. Handwritten entries in cells. QA/parameter review sheet. This is a filled form recording production/analytical data.
- Let's check the caveats: "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)" -> form. This is a "PLANT ANALYTICAL SUMMARY SHEET" with tables for averages, S.D., targets, and actuals. It captures data.
- This matches check 10.

**Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: No correspondence structure.
- Not this check.

**Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: No.
- Not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: No running narrative prose. Just tables and data.
- Not this check.

**Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: No.
- Not this check.

Let's double check Check 10 vs Check 8.
Check 8: specification. "Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
Also: "A quality-check sheet, lab measurement log, or product-test data table that merely RECORDS measurements about a product is a form, not specification — it captures data rather than defining requirements."
This page is a "B L PLANT ANALYTICAL SUMMARY SHEET" with sections for "BURLEY", "PRODUCTION DUST", "SLURRY", "FINISHED PRODUCT CHEMICAL ANALYSIS", "FINISHED PRODUCT % OV TARGET", "HOGSHEAD REPORT". It has tables with handwritten values for AVERAGE / S.D., TARGET, ACTUAL, OUT OF SPEC & REASON. This is clearly a lab/production measurement log capturing data. It is a form.

Let's double check Check 2.
"handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form"
Yes, this is a printed structured form with tables, filled by hand.

Therefore, the label is `form`.

Wait, could it be `scientific_report`? No, no narrative prose.
Could it be `specification`? No, it's recording data, not defining requirements. The targets are just reference values for the log.

Let's review the evidence for `form`:
- Title: "B L PLANT ANALYTICAL SUMMARY SHEET"
- Structure: Multiple tables with printed headers ("BURLEY", "PRODUCTION DUST", "SLURRY", "FINISHED PRODUCT CHEMICAL ANALYSIS", "HOGSHEAD REPORT") and ruled entry lines/cells.
- Content: Handwritten numerical data (averages, S.D., actuals, out of spec reasons) filling the cells.
- Function: Capturing factual production/analytical data. Matches check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A filled analytical or lab data sheet... is a form".

Runner-up: `specification`. Ruled out because the page merely records measurements and data (a lab measurement log) rather than defining a product's composition, tolerances, or requirements with "shall/must" language. The targets are reference values for the log, not requirement definitions.

Let's confirm there's no other check.
Check 1: file_folder - no, has real content.
Check 2: handwritten - no, handwriting fills printed form.
Check 3: fax - no.
Check 4: questionnaire - no.
Check 5: resume - no.
Check 6: scientific_publication - no.
Check 7: financial - no.
Check 8: specification - no, records data.
Check 9: presentation - no.
Check 10: form - yes.
Check 11: correspondence - no.
Check 12: news_article - no.
Check 13: scientific_report - no, no prose.
Check 14: advertisement - no.

Final label: form.
Confidence: 95.
Evidence is very clear: "B L PLANT ANALYTICAL SUMMARY SHEET", tables with handwritten data filling cells, "OUT OF SPEC & REASON" column. This is a classic filled analytical/lab data sheet form.

---
### `rvl_cdip__scientific_report__0008.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead/running head: "INBIFO Institut für biologische Forschung · Köln", "17.Okt.89 NDA/MWO QA3145.WM", "BLATT-NR.: 1 von 2". This looks like an internal institute document header, not a journal masthead or newspaper. No journal volume/issue/page number belonging to a published journal.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Content: Title "Biological Activity of Formaldehyde and Acrolein...", table with parameters and comments, signatures. Not identifier-only.
- Result: not this check.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Content: Mostly typed text, some handwritten signatures/dates ("21.Sep.89", "19.Okt.89"). Not majority handwritten.
- Result: not this check.

Check 3: FAX TRANSMISSION SHEET -> form
- No "FACSIMILE" or fax header.
- Result: not this check.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Not a survey instrument.
- Result: not this check.

Check 5: PERSON'S CAREER HISTORY -> resume
- Not a resume.
- Result: not this check.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- No journal running head, volume, issue, DOI. "INBIFO Institut für biologische Forschung" is an institute, not a journal.
- Result: not this check.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- No financial data, no payment demand.
- Result: not this check.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- Not an MSDS, product formulation, or test-analysis table keyed to product codes with tolerances. It's a QA review sheet.
- Result: not this check.

Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
- Not a slide deck or presentation.
- Result: not this check.

Check 10: ADMINISTRATIVE FORM -> form
- "ÜBERPRÜFUNG DURCH QA-UNIT" (Review by QA unit).
- Table with "ÜBERPRÜFTER PARAMETER" (Reviewed parameter) and "BEANSTANDUNG" (Objection/Comment).
- "STELLUNGNAHME" (Statement/Comment) box.
- "KENNTNISNAHME/STELLUNGNAHME DURCH PROJEKTLEITER: HHM" (Acknowledgment/Statement by project leader).
- "KENNTNISNAHME DURCH CM: UHA" (Acknowledgment by CM).
- "VERTEILER: UHA, HHM, QA, RM-BRT" (Distribution list).
- This is a QA/parameter review sheet or administrative form for capturing factual data (reviewed parameters, objections, acknowledgments).
- Let's check check 13 to see if it's a scientific_report.

Check 11: CORRESPONDENCE -> email, memo, or letter
- No TO:/FROM:/RE: header block followed by prose. It's a structured form.
- Result: not this check.

Check 12: PUBLISHED JOURNALISM -> news_article
- Not journalism.
- Result: not this check.

Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report
- "Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
- This page is exactly a QA parameter-review sheet's listed parameters/dates. It has a table of reviewed parameters and objections, and acknowledgment blocks. No running narrative prose.
- Result: not this check.

Check 14: PROMOTIONAL MATERIAL -> advertisement
- Not an ad.
- Result: not this check.

Wait, is there any other check?
Let's re-evaluate Check 10: ADMINISTRATIVE FORM -> form.
"A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: ... a QA/parameter review sheet."
Yes! "QA/parameter review sheet" is explicitly mentioned in Check 10.
The page has:
- "ÜBERPRÜFUNG DURCH QA-UNIT"
- Table with "ÜBERPRÜFTER PARAMETER" and "BEANSTANDUNG"
- "STELLUNGNAHME" box
- "KENNTNISNAHME" blocks with signatures/dates.
This is a QA/parameter review sheet. It captures data (parameters reviewed, objections, acknowledgments).
Therefore, it is a form.

Let's double check Check 8: specification.
"test-analysis tables keyed to product/part codes, tolerances, or "shall/must" requirement language. ... A labeled product/parameter rate-data chart ... is a specification"
But this is a QA review of a protocol ("Biological Activity of Formaldehyde and Acrolein... 90-Day Inhalation Study on Rats"). The table lists "Integrating/Subprotocols", "Subprotocol BC Method", "References", "allgemein" and the objections ("einige Unterschiede...", "Angabe 1 falschen Gruppenbezeichnung..."). This is a QA review sheet, not a specification defining product requirements. Check 10 explicitly covers "QA/parameter review sheet".

Let's double check Check 13: scientific_report.
"Requires running prose — a page that is only labeled field-value entries ... or a QA parameter-review sheet's listed parameters/dates is a filled form (check 10), not a scientific report."
This perfectly matches the page. It's a QA parameter-review sheet.

So the label is `form`.

Let's review the evidence for `form`:
- Header: "ÜBERPRÜFUNG DURCH QA-UNIT"
- Table columns: "ÜBERPRÜFTER PARAMETER", "BEANSTANDUNG"
- Rows: "Integrating/Subprotocols", "Subprotocol BC Method", etc.
- Bottom blocks: "STELLUNGNAHME", "KENNTNISNAHME/STELLUNGNAHME DURCH PROJEKTLEITER", "KENNTNISNAHME DURCH CM", "VERTEILER".
- Check 10 explicitly lists "a QA/parameter review sheet" as an example of an administrative form.
- Check 13 explicitly excludes "a QA parameter-review sheet's listed parameters/dates" from scientific_report, routing it to form (check 10).

Runner-up: scientific_report. Ruled out because the page lacks running narrative prose and is explicitly a QA parameter-review sheet, which Check 10 covers and Check 13 excludes.

Let's confirm there's no email/memo header.
"INBIFO Institut für biologische Forschung · Köln"
"17.Okt.89 NDA/MWO QA3145.WM"
"P 0500/3145"
"BLATT-NR.: 1 von 2"
This is just a document header, not a memo TO/FROM/RE block.

Final label: form.
Confidence: 95.
Evidence is very strong, explicit mentions in the prompt's check descriptions.
Check 10: "a QA/parameter review sheet"
Check 13: "a QA parameter-review sheet's listed parameters/dates is a filled form (check 10), not a scientific report."

I will output the scratchpad and the final label.

---
### `rvl_cdip__scientific_report__0003.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: None. Just a Bates number "81305509" on the right side.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Content: "A AND B COMPOUND RESULTS SUMMARY", "FILE NO: A310", "NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE", "NREC:", "SEAC:", "TESTING STATUS: ACTIVE 11-06-90", "DECISION TREE: II 11-21-90", "ISS: PENDING 11-06-90", "CHEM ABSTRACTS NUMBER: NA", "FEMA NUMBER: NA", "PH: 5.80 @ 28C", "MUTAGENICITY VEHICLE: DMSO", "IP VEHICLE:", "ORAL VEHICLE: EMUL 12MC; OIL", "IV VEHICLE: INSOLUBLE", "SPECIAL INSTRUCTIONS: FORMS EMULSION IN 12 MC AND IS SOLUBLE IN CORN OIL", "AWESI: PENDING 09-30-91", "ACUTDI R1: ORAL PENDING 09-30-91".
- This has real content (compound results summary, testing status, vehicles, etc.). Not file_folder.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Content is typed. Not handwritten.

Check 3: FAX TRANSMISSION SHEET -> form
- No fax header. Not this.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Not a survey instrument. Not this.

Check 5: PERSON'S CAREER HISTORY -> resume
- Not a resume. Not this.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- No journal masthead, volume, issue, DOI. Not this.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- No financial content, no payment demand. Not this.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- "A AND B COMPOUND RESULTS SUMMARY". Contains testing status, vehicles, special instructions. Is this a specification? Specification defines a product's requirements, tolerances, "shall/must". This looks like a summary of test results or a data sheet for a compound. Let's look at check 10 and 13.

Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
- Not a slide deck. Not this.

Check 10: ADMINISTRATIVE FORM -> form
- "filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This page has labeled fields (NAME:, NREC:, SEAC:, TESTING STATUS:, DECISION TREE:, ISS:, CHEM ABSTRACTS NUMBER:, FEMA NUMBER:, PH:, MUTAGENICITY VEHICLE:, IP VEHICLE:, ORAL VEHICLE:, IV VEHICLE:, SPECIAL INSTRUCTIONS:, AWESI:, ACUTDI R1:) and values filled in. It's a structured data capture sheet. "A AND B COMPOUND RESULTS SUMMARY". Wait, is it a form or a scientific report?
- Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report. "Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
- This page is exactly "labeled field-value entries" (NAME:, TESTING STATUS:, etc.). It is a filled form.

Let's re-evaluate Check 8 vs Check 10.
Check 8: specification. "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
This page is "A AND B COMPOUND RESULTS SUMMARY". It has field-value entries. No "shall/must". No tolerances. It's a summary of results/status for a compound. This matches the check 10 caveat: "a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report." Also check 10: "A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) ... [is a form]". This is exactly that: "A AND B COMPOUND RESULTS SUMMARY" with "NAME:", "PH:", "MUTAGENICITY VEHICLE:", etc.

Let's check Check 10 again:
"A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) ... is a form (check 10)"
This page is "A AND B COMPOUND RESULTS SUMMARY" with "NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE", "PH: 5.80 @ 28C", "MUTAGENICITY VEHICLE: DMSO", etc. This is a filled analytical/lab data sheet. Therefore, it is a form.

Let's double check Check 13:
"Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
This page has no running prose. It is only labeled field-value entries. So it is form.

Let's review the evidence for form:
- Title: "A AND B COMPOUND RESULTS SUMMARY"
- Fields: NAME:, NREC:, SEAC:, TESTING STATUS:, DECISION TREE:, ISS:, CHEM ABSTRACTS NUMBER:, FEMA NUMBER:, PH:, MUTAGENICITY VEHICLE:, IP VEHICLE:, ORAL VEHICLE:, IV VEHICLE:, SPECIAL INSTRUCTIONS:, AWESI:, ACUTDI R1:
- Values filled in: "BICYCLO[4.4.0]DEC-1-EN-3-ONE", "ACTIVE 11-06-90", "II 11-21-90", "PENDING 11-06-90", "5.80 @ 28C", "DMSO", "EMUL 12MC; OIL", "INSOLUBLE", "FORMS EMULSION IN 12 MC AND IS SOLUBLE IN CORN OIL", "PENDING 09-30-91".
- This is a filled analytical/lab data sheet. Check 10 explicitly includes "A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)" as a form.

Is there any other check?
Check 1: file_folder. No, has real content.
Check 2: handwritten. No.
Check 3: fax. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial. No.
Check 8: specification. No "shall/must", no tolerances, not an MSDS, not a product formulation. It's a results summary / data sheet.
Check 9: presentation. No.
Check 10: form. Yes, filled analytical data sheet with labeled field-value entries.
Check 11: correspondence. No.
Check 12: news_article. No.
Check 13: scientific_report. No running prose, only labeled field-value entries.
Check 14: advertisement. No.

Therefore, the label is `form`.

Let's quickly check if there's any chance it's scientific_report.
"Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
The page has absolutely no running prose. It's just a list of key-value pairs. So it's definitely form.

Runner-up: scientific_report. Ruled out because the page lacks running narrative prose and consists only of labeled field-value entries, which check 10 and check 13's caveats explicitly classify as a filled form.

Let's confirm the exact strings:
form

Confidence: 95. The evidence is very clear. Labeled field-value entries, no running prose, explicitly covered by the check 10 / check 13 caveats for analytical data sheets.

---
### `rvl_cdip__scientific_report__0002.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: "INBIFO Institut für biologische Forschung · Köln" at the top left, "INBIFO" logo at top right. This is a company letterhead, not a newspaper/magazine masthead or journal running head.
- Bates number: "2028875572" on the right side.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Content: "MONTHLY REPORT", "ANALYTICAL CHEMISTRY, JUNE 1984", "PROJECT A 0268/1215", responsibility/date/sign blocks, Study Director, Quality Assurance, Remarks, Distribution, footnote (a). This is not an identifier-only page. It has real content.
- Not this check.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Content: Mostly typed. Handwriting is just dates and signatures in the responsibility block.
- Not this check.

Check 3: FAX TRANSMISSION SHEET -> form
- No "FACSIMILE" or fax header.
- Not this check.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Not a survey instrument.
- Not this check.

Check 5: PERSON'S CAREER HISTORY -> resume
- Not a resume.
- Not this check.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- No journal running head, volume, issue, page range, DOI.
- Not this check.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- No financial content, no payment demand, no budget table.
- Not this check.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- Not an MSDS, product formulation, or test-analysis table keyed to product codes with tolerances.
- Not this check.

Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
- Not a slide deck, cover, or press release.
- Not this check.

Check 10: ADMINISTRATIVE FORM -> form
- Has fields like "RESPONSIBILITY (a)", "DATE", "SIGN", "PROJECT NO.", "Study Director:", "Quality Assurance:". But it's a cover page for a "MONTHLY REPORT". Wait, is it a form? Let's check check 13 first.

Check 11: CORRESPONDENCE -> email, memo, or letter
- Letterhead: "INBIFO Institut für biologische Forschung · Köln", "DR. W. FINK, PME RESEARCH LABORATORIES, CH-2003 NEUCHATEL".
- Date: "4.JUL.84".
- No "Dear..." salutation, no closing signature. It's a cover page for a report.
- Not this check.

Check 12: PUBLISHED JOURNALISM -> news_article
- Not news.
- Not this check.

Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report
- Title: "MONTHLY REPORT / ANALYTICAL CHEMISTRY, JUNE 1984 / PROJECT A 0268/1215".
- Footnote (a): "The responsibility includes, that in this report any information, that would be unexpected for the sponsor, is given with a special explanation or comment."
- This is a cover page for a "MONTHLY REPORT" from an institute (INBIFO) to a sponsor (PME Research Laboratories). It's a technical/project status report or scientific report cover page. Wait, check 13 says: "technical-study title page naming a specific experimental method/study is scientific_report (see check 9)". This is a "MONTHLY REPORT" for "ANALYTICAL CHEMISTRY, JUNE 1984". It's a report cover page.
- Let's re-read check 13: "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page with authors and an internal affiliation and no journal identifiers. Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
- Wait, this page is ONLY labeled field-value entries (Responsibility, Date, Sign, Study Director, Quality Assurance, Remarks, Distribution) and a title "MONTHLY REPORT". Does it have running prose? No.
- Let's re-read check 10: "administrative form... A QA/parameter review sheet... internal authorization/approval forms with an approval signature/date block."
- This page has an approval block: Responsibility, Date, Sign, Study Director, Quality Assurance. It's a cover page / approval sheet for a monthly report.
- Wait, check 13 says: "Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
- This page is exactly that: labeled field-value entries (Responsibility, Date, Sign, Study Director, Quality Assurance) for a "MONTHLY REPORT". It's an approval page / cover sheet for a report.
- Is it a form? Check 10: "internal authorization/approval forms with an approval signature/date block." Yes, this is an approval form for a monthly report.
- Let's check if there's any other category. "scientific_report" requires running prose. This page has no running prose, just fields and a title. So it's a form.
- Wait, what about check 9? "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation". This is a title page for a "MONTHLY REPORT". But check 13 says "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
- So this page, being only labeled field-value entries (approval block) for a report, is a form (check 10).

Let's carefully evaluate Check 10 vs Check 13.
Check 13: "Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
This page has:
- Title: MONTHLY REPORT / ANALYTICAL CHEMISTRY, JUNE 1984 / PROJECT A 0268/1215
- Table: RESPONSIBILITY (a) | DATE | SIGN | PROJECT NO. -/1215
- Study Director: [signature] [date]
- Quality Assurance: [date] [signature]
- Remarks: This page is not to be transmitted to the client.
- Distribution: Original into file of AC / Copies into files of GM and QA
- Footnote (a)

This is an approval page / cover sheet for a monthly report. It consists entirely of labeled fields, signatures, and distribution notes. No running prose. Therefore, it is a form (check 10).

Let's double check Check 11: Correspondence.
Letterhead: INBIFO ... DR. W. FINK ...
Date: 4.JUL.84
No salutation, no closing. Not a letter or memo.

Let's double check Check 1: file_folder.
Has real content (title, approval block, remarks, distribution). Not file_folder.

So the classification is form (check 10).

Wait, let's look at the label "scientific_report". Could it be a scientific_report?
Check 13: "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
This page has NO running prose. It's just the approval block and distribution info for a monthly report. So it's a form.

Let's review the evidence for form (check 10):
- "RESPONSIBILITY (a)", "DATE", "SIGN", "PROJECT NO."
- "Study Director:" with signature and date.
- "Quality Assurance:" with date and signature.
- "Remarks:", "Distribution:"
- This is an internal authorization/approval form with an approval signature/date block. Check 10 explicitly covers "internal authorization/approval forms with an approval signature/date block."

Runner-up: scientific_report. Ruled out because check 13 requires running prose, and this page is only labeled field-value entries (an approval block for a monthly report), which check 10 explicitly classifies as a form.

Let's confirm there's no other check.
Check 8: specification. No.
Check 9: presentation. No.

Final check of the text:
"MONTHLY REPORT
ANALYTICAL CHEMISTRY, JUNE 1984
PROJECT A 0268/1215"
"RESPONSIBILITY (a) DATE SIGN PROJECT NO. -/1215"
"Study Director: 4.Jul.84 [signature]"
"Quality Assurance: 04. JUNI 1984 [signature]"
"Remarks: This page is not to be transmitted to the client."
"Distribution: Original into file of AC Copies into files of GM and QA"

This is clearly an approval page / cover sheet for a report. It's a form.

I will output `form`.
Confidence: 85.
Evidence is clear: approval signature/date block, labeled fields, no running prose.
Runner-up: scientific_report (ruled out by lack of running prose, per check 13 caveat).

---

## letter → memo (5 errors)

### `rvl_cdip__letter__0010.png`
**Expected:** `letter` | **Predicted:** `memo`

*No reasoning text captured.*

---
### `rvl_cdip__letter__0009.png`
**Expected:** `letter` | **Predicted:** `memo`

*No reasoning text captured.*

---
### `rvl_cdip__letter__0008.png`
**Expected:** `letter` | **Predicted:** `memo`

*No reasoning text captured.*

---
### `rvl_cdip__letter__0007.png`
**Expected:** `letter` | **Predicted:** `memo`

*No reasoning text captured.*

---
### `rvl_cdip__letter__0002.png`
**Expected:** `letter` | **Predicted:** `memo`

*No reasoning text captured.*

---

## file_folder → presentation (3 errors)

### `rvl_cdip__file_folder__0008.png`
**Expected:** `file_folder` | **Predicted:** `presentation`

**Reasoning:**
> The page is mostly blank white space.
There is a vertical line on the left.
There is text rotated 90 degrees: "OVERHEADS" and "2046266350".
Wait, this looks like a folder tab or a section divider.
Let's check the rules for file_folder vs presentation.
Check 1: IDENTIFIER-ONLY PAGE -> file_folder.
"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
"A prominent topical heading always counts as real content, subtitle or not. EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB ... is a filing label, not a bold headline title, even when it is rotated."
Wait, the text is "OVERHEADS" and "2046266350".
Is "OVERHEADS" a folder tab label? Or is it a section divider for a presentation?
Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation.
"A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note ... a single-word/short-phrase heading with no subtitle at all (e.g. "RECOMMENDATIONS" centered on an otherwise blank page) ... is a presentation (this check), not file_folder (check 1)."
"A large heading rotated 90 degrees (e.g. "COMPETITIVE BAR PROGRAMS") is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab (product/collection/month/file name, e.g. "NEWTROL", "Litigation Content", "FEBRUARY") is a folder-tab label and stays file_folder (check 1)."

Wait, what is "OVERHEADS"? It's a single word. "2046266350" is a Bates number.
Is "OVERHEADS" a folder tab label or a section divider heading?
Usually, "OVERHEADS" in a tobacco archive could be a section divider in a presentation deck (e.g., a section about overheads).
Wait, "OVERHEADS" is a single word. Check 9 says: "a single-word/short-phrase heading with no subtitle at all (e.g. "RECOMMENDATIONS" centered on an otherwise blank page) ... is a presentation (this check), not file_folder (check 1)."
Also: "A large heading rotated 90 degrees (e.g. "COMPETITIVE BAR PROGRAMS") is a section divider ... is a presentation".
But wait, what about the exception: "but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab ... is a folder-tab label and stays file_folder".
Is "OVERHEADS" a folder's contents? "Overheads" could be a folder name (e.g., a folder containing overhead slides). But "OVERHEADS" is also a common section title in a presentation (e.g., "Overheads" meaning overhead projector slides).
Given the Bates number 2046266350, this is likely a scanned document from the tobacco archive.
If it's a section divider in a presentation, it's presentation.
Let's look at the layout: mostly empty space, vertical line on the left (maybe a margin line or artifact), "OVERHEADS" rotated 90 degrees, and "2046266350" rotated 90 degrees.
This looks exactly like a section divider page in a slide deck / presentation. "OVERHEADS" is the section title.
Check 9: "a single-word/short-phrase heading with no subtitle at all (e.g. "RECOMMENDATIONS" centered on an otherwise blank page) ... is a presentation (this check), not file_folder (check 1)."
"A large heading rotated 90 degrees ... is a section divider ... is a presentation".

Let's check Check 1: file_folder.
"A page is NOT file_folder if it carries any real content ... A prominent topical heading always counts as real content ... EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB ... is a filing label ... The black bar is the photographed folder body/tab edge ... it is NOT a slide-mount scan artifact".
Here, there is no black bar. There is a thin vertical line on the left, which might be a margin line or scan artifact. There is no photographed folder tab. The text "OVERHEADS" is a section divider heading.
Therefore, Check 9 (presentation) matches.

Let's verify Check 9 evidence:
- "OVERHEADS" is a single-word heading on an otherwise blank page.
- Rotated 90 degrees.
- Bates number "2046266350".
- This matches the description: "a single-word/short-phrase heading with no subtitle at all ... is a presentation (this check), not file_folder (check 1)." and "A large heading rotated 90 degrees ... is a section divider ... is a presentation".

Is there any other check?
Check 1: file_folder. No, because "OVERHEADS" is a prominent topical heading / section divider, not a folder tab label (no photographed folder tab, no black bar).
Check 9: presentation. Yes, section divider page.

Let's double check if "OVERHEADS" could be a folder tab. Folder tabs usually have a black bar (the folder body). Here, there's just a thin vertical line on the left, which is likely a scan artifact or margin line. The text is rotated 90 degrees, which is common for section dividers in presentations (to be read when the page is turned or as a vertical title).
Actually, in many tobacco archive presentations, section dividers are just the section name rotated 90 degrees on a blank page. "OVERHEADS" is a very common section name in a deck (e.g., "Overheads" meaning the overhead projector slides that follow).
So presentation is the correct label.

Let's review the scratchpad procedure:
Pre-scan:
- mail-client header: none
- masthead/running head: none

Check 1: file_folder. Evidence: "OVERHEADS" and Bates number. But "OVERHEADS" is a single-word heading on a blank page, which is a section divider (presentation), not a folder tab (no photographed folder tab, no black bar). Not file_folder.
Check 2: handwritten. None.
Check 3: fax sheet. None.
Check 4: questionnaire. None.
Check 5: resume. None.
Check 6: scientific_publication. None.
Check 7: financial. None.
Check 8: specification. None.
Check 9: presentation. Evidence: "OVERHEADS" is a single-word/short-phrase heading with no subtitle on an otherwise blank page, rotated 90 degrees. This matches the section divider / deck cover description in Check 9.
Check 10: form. None.
Check 11: correspondence. None.
Check 12: news_article. None.
Check 13: scientific_report. None.
Check 14: advertisement. None.

Runner-up: file_folder. Ruled out because the page lacks a photographed folder tab / black bar, and "OVERHEADS" functions as a section divider heading (single-word heading on blank page), which Check 9 explicitly classifies as presentation, not file_folder.

Final label: presentation.
Confidence: 95.
Evidence is clear: single-word heading "OVERHEADS" rotated 90 degrees on blank page with Bates number, matching Check 9's section divider / presentation cover definition.

---
### `rvl_cdip__file_folder__0006.png`
**Expected:** `file_folder` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.

Let's analyze the image:
- Top right: "Roger Whidden", "PM - Worldwide Regulatory Affairs", "Control #74"
- Center: "ISSUE MODULE", "PRODUCT INTEGRITY" (with some scan artifacts making it look like "PRODUC NTEGRITY")
- Bottom: "PHILIP MORRIS INTERNATIONAL"
- Right side vertical text: "2061695347" (Bates number)
- Background: A map-like graphic, possibly a world map or a stylized graphic with a PM logo.
- Overall layout: Looks like a presentation slide or a deck cover page. It has a title "ISSUE MODULE PRODUCT INTEGRITY", a company name "PHILIP MORRIS INTERNATIONAL", and a person's name/title "Roger Whidden, PM - Worldwide Regulatory Affairs".

Let's go through the checks:

1. IDENTIFIER-ONLY PAGE -> file_folder
- Not file_folder. It has a title "ISSUE MODULE PRODUCT INTEGRITY", company name, person's name. Real content.

2. MAJORITY-HANDWRITTEN PAGE -> handwritten
- Not handwritten. Typed text.

3. FAX TRANSMISSION SHEET -> form
- No fax header.

4. SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Not a survey.

5. PERSON'S CAREER HISTORY -> resume
- Not a resume.

6. PUBLISHED EVIDENCE -> scientific_publication
- No journal masthead, volume, issue, etc.

7. FINANCIAL DOCUMENT -> invoice or budget
- No financial data.

8. PRODUCT OR MATERIAL DOCUMENTATION -> specification
- Not an MSDS or product specification.

9. SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
- "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page..."
- This page has a title "ISSUE MODULE PRODUCT INTEGRITY", company name "PHILIP MORRIS INTERNATIONAL", and a speaker/author name "Roger Whidden, PM - Worldwide Regulatory Affairs". It looks exactly like a presentation cover slide or deck cover page.
- "Technical-study title pages: ... is scientific_report (check 13), not presentation ... The title names an experimental study, not a deck/program/section." - "ISSUE MODULE PRODUCT INTEGRITY" is not an experimental study title.
- "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note ... a deck cover ... is a presentation (this check)"
- This matches presentation perfectly. It's a deck cover / title page for a presentation module.

10. ADMINISTRATIVE FORM -> form
- Not a form with fill-in fields.

11. CORRESPONDENCE -> email, memo, or letter
- No mail header, no TO/FROM/RE memo header, no letter structure.

12. PUBLISHED JOURNALISM -> news_article
- No newspaper/magazine masthead.

13. ORIGINAL RESEARCH WRITE-UP -> scientific_report
- No narrative prose.

14. PROMOTIONAL MATERIAL -> advertisement
- Not an ad.

Let's double check check 9 vs check 1.
Check 1: file_folder. "A page titled 'RECOMMENDATIONS' ... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
This page has a bold title "ISSUE MODULE PRODUCT INTEGRITY", company name, and person's name. It is a presentation cover.

Check 9: presentation. "a deck title or section-divider page ... a meeting/program/speaker cover page ... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note ... is a presentation (this check), not file_folder (check 1)."
The page has "ISSUE MODULE PRODUCT INTEGRITY" as the main title, "PHILIP MORRIS INTERNATIONAL" at the bottom, and "Roger Whidden / PM - Worldwide Regulatory Affairs" at the top right. This is a classic presentation cover slide / deck cover.

Let's check the runner-up.
Runner-up: file_folder. Ruled out because the page has a bold headline title ("ISSUE MODULE PRODUCT INTEGRITY"), company name, and author name, which constitutes real content and a designed title page, not just filing metadata.

Wait, is there any other possibility?
Could it be a scientific_report? No narrative prose.
Could it be a specification? No.

The layout is sparse, large type, company logo/name, title. This is a presentation cover.

Evidence for check 9:
- Title: "ISSUE MODULE PRODUCT INTEGRITY"
- Company: "PHILIP MORRIS INTERNATIONAL"
- Author/Speaker: "Roger Whidden / PM - Worldwide Regulatory Affairs"
- Layout: Deck cover / title page style with large sparse type and graphic background.

Let's confirm the exact strings:
"label": "presentation"
"confidence": 95

Scratchpad:
- pre-scan: no mail-client header, no masthead.
- check 1 (file_folder): no — page has real content: bold title "ISSUE MODULE PRODUCT INTEGRITY", company name "PHILIP MORRIS INTERNATIONAL", and author "Roger Whidden". Not just filing metadata.
- check 2 (handwritten): no — typed text.
- check 3 (fax): no.
- check 4 (questionnaire): no.
- check 5 (resume): no.
- check 6 (scientific_publication): no journal identifiers.
- check 7 (financial): no.
- check 8 (specification): no.
- check 9 (presentation): yes — deck cover / title page layout with bold headline title "ISSUE MODULE PRODUCT INTEGRITY", company name "PHILIP MORRIS INTERNATIONAL", and speaker/author name "Roger Whidden, PM - Worldwide Regulatory Affairs". Sparse type, designed background. Matches check 9 definition of a deck cover or section-divider page.
- check 10 (form): no fill-in fields.
- check 11 (correspondence): no memo/letter headers or structure.
- check 12 (news_article): no masthead.
- check 13 (scientific_report): no narrative prose.
- check 14 (advertisement): no promotional product imagery/slogans.

Runner-up: file_folder. Ruled out because the page contains a bold topical title ("ISSUE MODULE PRODUCT INTEGRITY"), company name, and author attribution, which makes it a designed presentation cover/title page rather than a pure filing identifier.

Confidence: 95.
The evidence is very clear for presentation (deck cover).
I will output the result.

---
### `rvl_cdip__file_folder__0004.png`
**Expected:** `file_folder` | **Predicted:** `presentation`

**Reasoning:**
> The page is mostly blank with some text rotated 90 degrees.
Text: "PRODUCT INTEGRITY - TDA - PRESENTATION" and "2065213892".
There is a black bar at the bottom (scan artifact for slide/folder tab?).
Wait, the text is rotated 90 degrees. "PRODUCT INTEGRITY - TDA - PRESENTATION".
Let's check the rules for file_folder vs presentation.
Check 1: file_folder. "A prominent topical heading always counts as real content... EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is a filing label, not a bold headline title... The black bar is the photographed folder body/tab edge — it is NOT a slide-mount scan artifact (check 9), and a rotated filing label on a folder tab is NOT a section-divider heading."
Wait, the text is "PRODUCT INTEGRITY - TDA - PRESENTATION". Is this a folder tab label?
The page has a black bar at the bottom (scan artifact). The text is rotated 90 degrees.
Wait, "PRODUCT INTEGRITY - TDA - PRESENTATION" sounds like a section divider or a presentation title.
But check 9: "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab (product/collection/month/file name, e.g. 'NEWTROL', 'Litigation Content', 'FEBRUARY') is a folder-tab label and stays file_folder (check 1)."
Wait, what about the black bar? "Scan-artifact signal: a solid black bar along one edge of the page ... combined with sparse text placed off-center ... points to a photographed slide/overhead — presentation ... BUT this signal applies only to a photographic image ... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label ... and a Bates number is file_folder"
Wait, is "PRODUCT INTEGRITY - TDA - PRESENTATION" a folder tab label or a section divider?
"PRODUCT INTEGRITY - TDA - PRESENTATION"
TDA = Tobacco Development Association? or something.
If it's a section divider in a presentation, it's presentation (check 9).
Let's re-read check 9: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note ... a single-word/short-phrase heading with no subtitle at all ... a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."
"A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider ... is a presentation (this check), not file_folder (check 1)."
Wait, what if it's a folder tab? "a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab (product/collection/month/file name, e.g. 'NEWTROL', 'Litigation Content', 'FEBRUARY') is a folder-tab label and stays file_folder (check 1)."
Is "PRODUCT INTEGRITY - TDA - PRESENTATION" a folder tab label? It names a presentation. "PRESENTATION" is in the text.
Wait, if it says "PRESENTATION", it's likely a section divider for a presentation.
Let's look at the text again: "PRODUCT INTEGRITY - TDA - PRESENTATION".
Bates number: 2065213892.
There's a black bar at the bottom.
If it's a section divider for a presentation, it's check 9 -> presentation.
Let's consider file_folder (check 1): "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only. ... A prominent topical heading always counts as real content, subtitle or not. EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB ... is a filing label, not a bold headline title ... The black bar is the photographed folder body/tab edge ... and a rotated filing label on a folder tab is NOT a section-divider heading."
If the black bar is a slide-mount scan artifact, then it's presentation.
"Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title; don't let a technical-sounding phrase pull this toward scientific_report when the layout itself is sparse and slide-like rather than a prose page. BUT this signal applies only to a photographic image ... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label ... and a Bates number is file_folder"
How to distinguish? "PRODUCT INTEGRITY - TDA - PRESENTATION". This looks like a title page or section divider for a presentation. "PRESENTATION" is explicitly in the text. A folder tab wouldn't typically say "PRESENTATION" as part of the folder name, unless the folder is named "PRESENTATION". But "PRODUCT INTEGRITY - TDA - PRESENTATION" sounds like a section title in a deck: "Product Integrity - TDA - Presentation".
Wait, check 9: "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab ... is a folder-tab label and stays file_folder (check 1)."
If the text is "PRODUCT INTEGRITY - TDA - PRESENTATION", it's a section divider. Section dividers are presentation (check 9).
Let's check if there's any other evidence.
Bates number: 2065213892.
Text: "PRODUCT INTEGRITY - TDA - PRESENTATION" rotated 90 degrees.
This is a section divider page in a presentation deck.
Therefore, presentation.

Let's double check check 1: "A page is NOT file_folder if it carries any real content ... A prominent topical heading always counts as real content ... EXCEPTION — folder tabs ... a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB ... is a filing label ... The black bar is the photographed folder body/tab edge ... and a rotated filing label on a folder tab is NOT a section-divider heading."
If the black bar is a slide-mount scan artifact, then it's presentation. The prompt says: "Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center ... points to a photographed slide/overhead — presentation ... BUT this signal applies only to ... a designed deck page — it does NOT apply to a photographed file-folder TAB".
Since the text is "PRODUCT INTEGRITY - TDA - PRESENTATION", it's a designed deck page / section divider. The word "PRESENTATION" strongly indicates it's a deck section. Folder tabs don't usually have "PRESENTATION" in the label unless the folder is literally named that, but even then, "PRODUCT INTEGRITY - TDA - PRESENTATION" reads like a slide title or section divider.
Also, the text is placed off-center (lower-right when rotated, or right side when upright). "sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation".
So check 9 matches: presentation.

Let's review the scratchpad steps:
1. file_folder: no, "PRODUCT INTEGRITY - TDA - PRESENTATION" is a prominent topical heading / section divider, not just filing metadata. The black bar is a slide scan artifact, not a folder tab edge, given the text content.
2. handwritten: no.
3. fax sheet: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial: no.
8. specification: no.
9. presentation: yes. Sparse text, rotated heading "PRODUCT INTEGRITY - TDA - PRESENTATION", black bar scan artifact indicating slide/overhead, section divider in a deck.
10. form: no.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no.
14. advertisement: no.

Runner-up: file_folder. Ruled out because the text "PRODUCT INTEGRITY - TDA - PRESENTATION" is a section divider heading for a presentation deck, not a short filing label on a physical folder tab. The black bar is a slide-mount scan artifact, not a folder body edge.

Wait, is there any possibility it's a scientific_report? No, no prose.
Is it a specification? No.

Let's confirm the text: "PRODUCT INTEGRITY - TDA - PRESENTATION"
Bates: 2065213892
This is definitely a section divider in a presentation.

Final label: presentation.
Confidence: 90.
Evidence: "PRODUCT INTEGRITY - TDA - PRESENTATION" rotated 90 degrees, sparse text, black bar scan artifact. Matches check 9 section divider / slide deck layout.
Runner-up: file_folder. Ruled out because the heading is a section divider for a presentation, not a folder-tab filing label.

---

## invoice → form (3 errors)

### `rvl_cdip__invoice__0006.png`
**Expected:** `invoice` | **Predicted:** `form`

*No reasoning text captured.*

---
### `rvl_cdip__invoice__0015.png`
**Expected:** `invoice` | **Predicted:** `form`

*No reasoning text captured.*

---
### `rvl_cdip__invoice__0014.png`
**Expected:** `invoice` | **Predicted:** `form`

*No reasoning text captured.*

---

## presentation → file_folder (2 errors)

### `rvl_cdip__presentation__0018.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The page is almost entirely blank.
There is a vertical black bar on the right side.
There is handwritten text "1991-84" and "foundation" rotated 90 degrees near the top right.
There is a Bates number "465246617" at the bottom right.
This looks like a photographed file folder tab or a blank page with a folder tab edge.
Wait, let's look at the black bar. "a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". BUT "this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label (product/collection/month/file name), and a Bates number is file_folder even though the folder body photographs as a solid black bar and the label may be rotated."
The text "1991-84 foundation" is a short filing label. "foundation" could be the folder name, "1991-84" the date range.
Let's check check 1: file_folder.
"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
"A folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB — a protruding tab-shaped piece of cardboard... bearing a short filing label that names the folder's contents... usually with a Bates number stamped on the folder body. The label IS filing metadata... so it is NOT a 'topical title' for this check. The page stays file_folder even when the label is rotated 90 degrees, even when the folder body photographs as a solid black bar/border along one or more edges..."
Here we have a solid black bar on the right edge. Rotated text "1991-84 foundation". Bates number "465246617".
This perfectly matches the folder-tab page description in check 1.
Let's verify:
- Black bar on right edge: yes.
- Rotated short filing label: "1991-84 foundation" (rotated 90 degrees).
- Bates number: "465246617".
- No other content: yes, the rest is blank.
Therefore, check 1 matches: file_folder.

Let's double check check 9 (presentation):
"Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation... BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label (product/collection/month/file name), and a Bates number is file_folder even though the folder body photographs as a solid black bar and the label may be rotated."
The text "1991-84 foundation" is a short filing label (date range + folder name). So it's file_folder.

Let's do the scratchpad walk:
1. file_folder: yes — page is almost entirely blank, contains only a rotated short filing label "1991-84 foundation", a solid black bar on the right edge (photographed folder body/tab edge), and a Bates number "465246617". Matches folder-tab page description in check 1.
2. handwritten: no — only a short rotated label is handwritten/typed, not majority content.
3. fax sheet: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial: no.
8. specification: no.
9. presentation: no — check 1 exception applies; black bar + rotated label + Bates number = folder tab, not presentation.
10. form: no.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no.
14. advertisement: no.

Runner-up: presentation, ruled out because check 1 explicitly excludes folder-tab pages with black bar artifacts and rotated filing labels from presentation classification.

Final label: file_folder.
Confidence: 95.
Evidence is very clear: black bar, rotated label "1991-84 foundation", Bates number. Matches check 1 folder-tab bullet perfectly.

---
### `rvl_cdip__presentation__0017.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The image is a scanned document. Let's analyze its content.
Top right: "F" or some symbol.
Bottom right: "2071969205" (Bates number).
Left side: There is a large vertical band of noise/static, possibly a scanned artifact or a very degraded image. It looks like a solid black bar or heavy noise on the left edge, maybe a photographed folder tab or a slide artifact. Wait, looking closely at the left side, there's a vertical band of noise, and at the bottom left, a darker block. This looks like a scanned folder tab or a slide mount artifact.
Wait, let's look at the instructions for file_folder:
"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
"Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB — a protruding tab-shaped piece of cardboard (often with a cutout/notch shape at the folder's edge) bearing a short filing label that names the folder's contents... The black bar is the photographed folder body/tab edge — it is NOT a slide-mount scan artifact (check 9), and a rotated filing label on a folder tab is NOT a section-divider heading."
"Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title; don't let a technical-sounding phrase pull this toward scientific_report when the layout itself is sparse and slide-like rather than a prose page. BUT this signal applies only to a photographic image... it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label (product/collection/month/file name), and a Bates number is file_folder even though the folder body photographs as a solid black bar and the label may be rotated."

Let's look at the image again.
Left side: vertical band of noise, bottom left has a darker block. This looks like the edge of a folder or a scanned artifact.
Bottom right: "2071969205" rotated 90 degrees. This is a Bates number.
Top right: "F" or a symbol.
Is there any real content? No sentences, no topical title, no data table. Just a Bates number and some scan noise/artifact on the left.
Wait, check 1: "IDENTIFIER-ONLY PAGE -> file_folder. Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title. A page is NOT file_folder if it carries any real content... Pure filing metadata only."
The page has a Bates number "2071969205". The left side is just noise/artifact. There is no real content.
Therefore, it's file_folder.

Let's double check.
Is there a folder tab? The left side has a vertical band that could be the folder body/tab edge. The text "2071969205" is rotated.
There is no other text. No header, no body, no form fields.
This is a classic file_folder page (Bates number only, with scan artifacts).

Let's review the checks:
1. file_folder: Yes, only Bates number "2071969205" and scan noise/artifact. No sentences, no topical title.
2. handwritten: No.
3. fax sheet: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No.
7. financial: No.
8. specification: No.
9. presentation: No. (Scan artifact signal points to presentation, BUT the rule says "it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label... and a Bates number is file_folder". Here, there's no filing label, just a Bates number and noise. Still, it's identifier-only.)
10. form: No.
11. correspondence: No.
12. news_article: No.
13. scientific_report: No.
14. advertisement: No.

The page is essentially blank except for a Bates number and some scanning noise on the left edge. This perfectly matches "file_folder" (identifier-only page).

Wait, the prompt says: "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image (people, a scene, a slide) or with a bold headline title... carries real content — it is a cover/title page... not file_folder."
Here, there is no photographic image, no bold headline title. Just noise on the left. The noise is likely a scanning artifact from the folder body or edge.
So it is file_folder.

Let's confirm the noise on the left. It's a vertical band of static, with a darker block at the bottom. This is typical of a scanned blank page or a page with just a Bates number where the scanner picked up the edge of the folder or a previous page's bleed-through, or it's a folder tab scan. Either way, no real content.

Final label: file_folder.
Confidence: 95.
Runner-up: presentation (due to scan-artifact signal of black bar on left), but ruled out because there's no photographic image or designed deck page, just noise and a Bates number, which falls under file_folder identifier-only page.
Actually, the rule says: "a page whose content is a physical folder tab, a short filing label... and a Bates number is file_folder even though the folder body photographs as a solid black bar". Here we have a Bates number and a black bar/noise. So file_folder is correct.
I'll output file_folder.

---

## news_article → advertisement (2 errors)

### `rvl_cdip__news_article__0020.png`
**Expected:** `news_article` | **Predicted:** `advertisement`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: Top of the page has "THE NEW YORK TIMES, MONDAY, SEPTEMBER 11, 1989". This is a newspaper masthead. Wait, let's look closer. "THE NEW YORK TIMES, MONDAY, SEPTEMBER 11, 1989". This is a newspaper masthead. But wait, check 12 says "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement even if printed inside a newspaper/magazine with a running masthead and some surrounding text; news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
Let's look at the content.
Headline: "All Advertising Should Be Truthful"
Subtext: "Reprinted with permission from November 10, 1969, Advertising Age"
Article: "The Truth Seems a Little Twisted" - discusses cigarette advertising, American Cancer Society, American Heart Association.
Bottom section: "What is Advertising Age? The national newspaper of the advertising and marketing industry... A constant champion of truth in advertising... Not a defender of smoking"
Footer: "the tobacco institute 1776 K Street, N.W., Washington, D.C. 20006" and a Bates number "901216053".

This is clearly an advertisement placed in a newspaper (The New York Times). It's a full-page ad by the Tobacco Institute, reprinted from Advertising Age, defending their advertising practices.
Let's check the checks.

Check 1: file_folder. No, lots of content.
Check 2: handwritten. No.
Check 3: fax sheet. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial. No.
Check 8: specification. No.
Check 9: presentation. No.
Check 10: form. No.
Check 11: correspondence. No.
Check 12: news_article. Masthead is present ("THE NEW YORK TIMES"), but check 12 caveat says: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement (product imagery, slogans, a Surgeon General warning, brand styling) is an advertisement (check 14) even if printed inside a newspaper/magazine with a running masthead and some surrounding text; news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
Wait, does this page present primarily as editorial/multi-story news content? No, it's a single promotional layout by "the tobacco institute". It's an ad.
Check 13: scientific_report. No.
Check 14: advertisement. "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content... a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page with a running masthead and some surrounding text."
This page is an ad by the Tobacco Institute. It has a slogan ("All Advertising Should Be Truthful"), brand styling, and is clearly a promotional piece by "the tobacco institute".

Let's double check check 12 vs 14.
The page has a newspaper masthead at the top: "THE NEW YORK TIMES, MONDAY, SEPTEMBER 11, 1989".
But the content is entirely an advertisement by the Tobacco Institute.
"Reprinted with permission from November 10, 1969, Advertising Age"
"The Truth Seems a Little Twisted"
"What is Advertising Age?"
"the tobacco institute 1776 K Street, N.W., Washington, D.C. 20006"
This is an advertisement. The dominant content is a single promotional layout.

Let's review the scratchpad rules for advertisement:
"Judge by DOMINANT content (see check 12): a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page with a running masthead and some surrounding text."
Here, the page is a single promotional layout by the Tobacco Institute. It's an ad.

Let's do the scratchpad:
- pre-scan: newspaper masthead at top ("THE NEW YORK TIMES, MONDAY, SEPTEMBER 11, 1989"). But dominant content is an ad.
- file_folder: no.
- handwritten: no.
- fax sheet: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no.
- financial: no.
- specification: no.
- presentation: no.
- form: no.
- correspondence: no.
- news_article: masthead present, but dominant content is a single promotional layout by the Tobacco Institute, not multi-story editorial news content. Ruled out by check 12 caveat.
- scientific_report: no.
- advertisement: yes — single brand promotional layout by "the tobacco institute", slogan "All Advertising Should Be Truthful", reprinted from Advertising Age, with contact info and Bates number. Check 14 and check 12 caveat apply.

Runner-up: news_article, ruled out because the page's dominant content is a single promotional advertisement by the Tobacco Institute, not editorial news content, despite the newspaper masthead at the top.

Confidence: 95. The evidence for advertisement is very strong (Tobacco Institute branding, slogan, promotional text, reprinted ad layout). The newspaper masthead is a red herring per the calibration rules.

Let's refine the scratchpad:
<scratchpad>
pre-scan: newspaper masthead at top ("THE NEW YORK TIMES, MONDAY, SEPTEMBER 11, 1989"), but dominant content is an ad.
file_folder: no — full page of text and layout.
handwritten: no — typed throughout.
fax sheet: no.
questionnaire: no.
resume: no.
scientific_publication: no.
financial: no.
specification: no.
presentation: no.
form: no.
correspondence: no.
news_article: no — although a newspaper masthead ("THE NEW YORK TIMES") is present at the top, check 12's caveat states that a page whose dominant layout is a single brand advertisement is an advertisement, not a news_article. This page is entirely a promotional layout by the Tobacco Institute, not multi-story editorial content.
scientific_report: no.
advertisement: yes — the page is a single promotional layout by "the tobacco institute" with a slogan ("All Advertising Should Be Truthful"), reprinted from "Advertising Age", and includes the institute's address. Check 14 and the check 12 caveat explicitly route single-brand ads in newspapers to advertisement.
Runner-up: news_article, ruled out because the dominant content is a single promotional advertisement by the Tobacco Institute, not editorial news content, per the check 12 caveat.
</scratchpad>
<label>advertisement</label>
<confidence>95</confidence>

---
### `rvl_cdip__news_article__0018.png`
**Expected:** `news_article` | **Predicted:** `advertisement`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the mandatory pre-scan and the 14 checks in order.

**Pre-scan:**
- Mail-client header: None.
- Fax transmission header: "JUN 24 '94 10:53AM PHILIP MORRIS P. 6/9" at the top left. This is a FAX machine transmission header, NOT a mail-client header. Ignore for email classification.
- Masthead/running head: No newspaper/magazine masthead. No journal running head.

**Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Content: There is a full page of text, a large headline "HOW SCIENCE AND POLITICS COLLIDED AND BALANCED REPORTING WAS THE CASUALTY.", columns of text, a logo at the bottom "PHILIP MORRIS", and a tagline "IN ANY CONTROVERSY, FACTS MUST MATTER."
- Not file_folder.

**Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Content: Typed text throughout. Some handwritten annotations (circles, underlines) but majority is typed.
- Not handwritten.

**Check 3: FAX TRANSMISSION SHEET -> form**
- No "FACSIMILE TRANSMISSION" header. The top left is just a fax machine stamp.
- Not fax sheet.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Not a survey instrument.

**Check 5: PERSON'S CAREER HISTORY -> resume**
- Not a resume.

**Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- No journal name, volume, issue, page range, DOI on this page itself. The text mentions "EPA's 1992 report", "Am J Epidemiol" maybe in text? Let's check the text. "Many of these questions are addressed in this Forbes MediaGuide article..." Wait, it looks like an article or a press release or a statement.
- Let's look at the bottom: "PHILIP MORRIS" logo, "IN ANY CONTROVERSY, FACTS MUST MATTER." This looks like a corporate statement or advertisement or news article.
- Wait, check 12: PUBLISHED JOURNALISM -> news_article.
- Let's look at the layout. It has a headline, subheadings, columns of text. It looks like a newspaper or magazine article, or a press release.
- "How Science and Politics Collided and Balanced Reporting Was The Casualty."
- "The press confidently played up the EPA's side of the story."
- "Stories about the EPA's report 'exaggerated evidence and minimized children.'"
- "The complicated presentation of the EPA's report discouraged scrutiny."
- Bottom text: "For a free reprint of this article, or more information, please call 1 800 823-5725."
- "PHILIP MORRIS" logo.
- This is a corporate statement or an advertisement disguised as an article, or a news article. Wait, "For a free reprint of this article..." implies it's an article. But it's from Philip Morris. "IN ANY CONTROVERSY, FACTS MUST MATTER." is a slogan.
- Let's check check 14: PROMOTIONAL MATERIAL -> advertisement.
- "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content... a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page..."
- Wait, is this an advertisement? It has the Philip Morris logo, a slogan "IN ANY CONTROVERSY, FACTS MUST MATTER.", and offers a "free reprint of this article". This is a classic "advertorial" or corporate advertisement.
- Let's check check 12: PUBLISHED JOURNALISM -> news_article. "Newspaper or magazine masthead, byline, dateline, multi-column news typography...". There is no masthead. The top left is a fax stamp. The text is an article, but it's published by Philip Morris as a corporate statement/advertisement.
- Let's re-read check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation. "corporate press release / issued statement ("FOR IMMEDIATE RELEASE", media contact)..." This doesn't have "FOR IMMEDIATE RELEASE".
- Let's re-read check 14: PROMOTIONAL MATERIAL -> advertisement. "Marketing layout: product imagery, slogans, brand styling... Judge by DOMINANT content... a single brand ad with product imagery, slogans... is advertisement". The bottom has "IN ANY CONTROVERSY, FACTS MUST MATTER." and the Philip Morris logo. The text is an article about how Philip Morris is being unfairly portrayed. This is a corporate advertisement / advertorial.
- Wait, could it be a news_article? "Many of these questions are addressed in this Forbes MediaGuide article... This week, Philip Morris is bringing you this article in its entirety..." This is a reprinted article from Forbes MediaGuide, brought to you by Philip Morris. This is an advertisement (advertorial).
- Let's check the labels again. advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
- Is it an advertisement? Yes, it's a corporate ad / advertorial. "Philip Morris is bringing you this article in its entirety... For a free reprint of this article... please call..." This is a paid placement / advertisement.
- Let's check check 12 again: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement (product imagery, slogans, a Surgeon General warning, brand styling) is an advertisement (check 14) even when printed inside a newspaper/magazine with a running masthead and some surrounding text; news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
- This page is a single promotional layout from Philip Morris. It has the Philip Morris logo, their slogan, and offers a free reprint. It is an advertisement.

Let's carefully evaluate if it's `news_article` or `advertisement`.
The text says: "Many of these questions are addressed in this Forbes MediaGuide article. But only barely have they begun to be answered... This week, Philip Morris is bringing you this article in its entirety... For a free reprint of this article, or more information, please call 1 800 823-5725."
Bottom: Philip Morris logo, "IN ANY CONTROVERSY, FACTS MUST MATTER."
This is clearly a corporate advertisement (advertorial). The dominant content is a promotional layout from a brand (Philip Morris) with their slogan and contact info for a reprint. It is not a news article from a general-audience outlet; it's a reprinted article placed as an ad by Philip Morris.

Let's check if there's any other category.
Could it be `presentation`? "corporate press release / issued statement". No "FOR IMMEDIATE RELEASE".
Could it be `scientific_report`? No, it's an article about reporting.
Could it be `specification`? No.

Let's review the definition of `advertisement`:
"Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content (see check 12): a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page with a running masthead and some surrounding text."
Here we have brand styling (Philip Morris logo), slogans ("IN ANY CONTROVERSY, FACTS MUST MATTER."), and it's a single promotional layout (an advertorial). The text is an article, but the page's function is to advertise Philip Morris's perspective and offer a free reprint. This is an advertisement.

Wait, is there any chance it's `news_article`?
"news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
This page is one promotional layout (a single article reprinted by Philip Morris with their branding and slogan at the bottom). It is an advertisement.

Let's double check check 12: "Also a magazine feature or an encyclopedia entry/excerpt... or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet". This is from Philip Morris, not a general-audience outlet. It's a corporate publication/ad.

Therefore, `advertisement` is the correct label.

Let's trace the checks:
1. file_folder: no, has real content.
2. handwritten: no, typed.
3. fax sheet: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no journal identifier on this page.
7. financial: no.
8. specification: no.
9. presentation: no, not a slide deck or press release with "FOR IMMEDIATE RELEASE".
10. form: no.
11. correspondence: no.
12. news_article: no, not from a general-audience outlet, it's a corporate promotional layout.
13. scientific_report: no.
14. advertisement: yes, brand styling (Philip Morris logo), slogan ("IN ANY CONTROVERSY, FACTS MUST MATTER."), promotional layout offering a free reprint.

Wait, is there a Surgeon General warning? I don't see it explicitly in the text, but the definition says "product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content... a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement". The presence of the slogan and brand logo and the "free reprint" offer strongly indicates advertisement.

Let's re-read the bottom text:
"PHILIP MORRIS"
"IN ANY CONTROVERSY, FACTS MUST MATTER."
This is a classic tobacco industry advertisement / advertorial.

Final check of the text:
"How Science and Politics Collided And Balanced Reporting Was The Casualty."
"The press confidently played up the EPA's side of the story."
...
"For a free reprint of this article, or more information, please call 1 800 823-5725."
"PHILIP MORRIS"
"IN ANY CONTROVERSY, FACTS MUST MATTER."

This is definitely an advertisement (advertorial).

Confidence: 95. The evidence for advertisement is strong (brand logo, slogan, "free reprint" offer, corporate perspective). The runner-up is news_article, ruled out because it's not from a general-audience outlet and is a single promotional layout from Philip Morris.

---

## news_article → file_folder (2 errors)

### `rvl_cdip__news_article__0014.png`
**Expected:** `news_article` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: "...DAILY BULLETIN...DAILY BULLETIN...DAILY BULLETIN... / ...PUBLIC AFFAIRS DIVISION...THE TOBACCO INSTITUTE...". This looks like a newsletter or bulletin header, but not a newspaper/magazine masthead or journal running head. It's an internal bulletin.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Evidence: There is a lot of body content (bulletin text). Not file_folder.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Evidence: Typed text throughout. Not handwritten.

Check 3: FAX TRANSMISSION SHEET -> form
- Evidence: No fax header. Not fax.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Evidence: Not a survey. Not questionnaire.

Check 5: PERSON'S CAREER HISTORY -> resume
- Evidence: Not a resume.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- Evidence: No journal running head, volume, issue, DOI. Not scientific_publication.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- Evidence: No financial data, no payment demand. Not financial.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- Evidence: No product formulation, MSDS, or "shall/must" language. Not specification.

Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
- Evidence: Not a slide deck or presentation.

Check 10: ADMINISTRATIVE FORM -> form
- Evidence: Not a form with fill-in fields.

Check 11: CORRESPONDENCE -> email, memo, or letter
- Evidence: No TO:/FROM:/RE: memo header, no letterhead with external address, no salutation. Not correspondence.

Check 12: PUBLISHED JOURNALISM -> news_article
- Evidence: "...DAILY BULLETIN...DAILY BULLETIN...DAILY BULLETIN... / ...PUBLIC AFFAIRS DIVISION...THE TOBACCO INSTITUTE...". This is an internal bulletin, not published journalism from a general-audience outlet. Wait, is it a news_article? "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content". This is an internal daily bulletin from the Public Affairs Division of The Tobacco Institute. It's not a newspaper or magazine. Let's look at the remaining categories.

Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report
- Evidence: Running narrative prose about legislative updates (smoking bans, tobacco control initiatives). It's a summary of news/legislative events, not original research. Wait, is it a scientific_report? No, it's a daily bulletin summarizing legislative actions.

Check 14: PROMOTIONAL MATERIAL -> advertisement
- Evidence: Not an ad.

Wait, if none of 1-14 match perfectly, what is it?
Let's re-read the categories.
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

Is it a memo?
"internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose"
This page has:
"...DAILY BULLETIN...DAILY BULLETIN...DAILY BULLETIN...
...PUBLIC AFFAIRS DIVISION...THE TOBACCO INSTITUTE...
Monday
January 24, 1994
...IN REVIEW...IN REVIEW...IN REVIEW..."
Then paragraphs of text.
Then "...For further information...call Public Affairs..."
This is an internal bulletin. Does it fit memo?
Memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block...
This doesn't have TO/FROM/RE.

Could it be news_article?
"Newspaper or magazine masthead, byline, dateline, multi-column news typography, '- more-' continuation, or wire-service credit. Also a magazine feature or an encyclopedia entry/excerpt... or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet"
This is from "THE TOBACCO INSTITUTE", an internal division ("PUBLIC AFFAIRS DIVISION"). Not a general-audience outlet.

Could it be scientific_report?
"Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page... Requires running prose"
This is running prose, but it's a daily bulletin about legislative updates, not a research write-up.

Wait, look at check 12 again: "news_article ... any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet". This is not general-audience.

What about check 9: presentation?
"Slide/overhead layouts... a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement ("FOR IMMEDIATE RELEASE", media contact), or a photographic slide image... A near-blank cover or title page... a deck cover, or a section divider"
Not a presentation.

Let's re-evaluate check 11: memo.
"A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo even without literal "TO:/FROM:" labels"
This is a daily bulletin. Is it a memo?

Let's re-evaluate check 13: scientific_report.
Is a daily legislative bulletin considered a scientific_report? No.

Wait, is there any other category?
What about "news_article"? Sometimes internal bulletins that summarize news are classified as news_article if they look like news. But the instructions say: "news_article requires the page to present primarily as editorial/multi-story news content... from a GENERAL-AUDIENCE outlet".

Let's look at the document again.
"...DAILY BULLETIN...DAILY BULLETIN...DAILY BULLETIN...
...PUBLIC AFFAIRS DIVISION...THE TOBACCO INSTITUTE...
Monday
January 24, 1994
...IN REVIEW...IN REVIEW...IN REVIEW..."

This is an internal memo/bulletin. If I have to choose between memo and news_article...
Actually, could it be a memo?
"A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. "Mr. R. J. Smith, Manager - Hanmer Division" from "T. P. Pettigrew, Manufacturing Services Manager - Research and Development") with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo even without literal "TO:/FROM:" labels"
This document doesn't have a named person. It's a bulletin.

Wait, is there a category I missed?
"advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification"

If it's an internal bulletin summarizing news, maybe it's `news_article`? No, "from a GENERAL-AUDIENCE outlet".
Maybe `scientific_report`? "Running narrative prose with objectives, methods, results, or discussion...". No.

Let's reconsider `memo`.
Memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose.
This has a date: "Monday January 24, 1994".
It is from "PUBLIC AFFAIRS DIVISION...THE TOBACCO INSTITUTE".
It is an internal document.
If it doesn't have TO/FROM/RE, but is an internal dated note with prose, could it be memo?
The rule says: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... IS a memo even without literal TO:/FROM: labels". This is addressed to no one specific, it's a bulletin.

What if it's `news_article`?
"Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content"
This page presents as a daily bulletin with news content (legislative updates). Even if it's from The Tobacco Institute, it's news content. But the rule says "from a GENERAL-AUDIENCE outlet". The Tobacco Institute is not a general-audience outlet.

Wait! What about `scientific_report`?
Sometimes internal reports/bulletins are classified as scientific_report if they contain running prose. But this is clearly a legislative news bulletin.

Let's look at the labels again.
Is there an "internal bulletin" category? No.
Could it be `memo`?
Often, internal newsletters/bulletins are classified as `memo` if they are internal communications.
Let's check the memo definition again: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation). Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels"

This document has:
Header: "...DAILY BULLETIN... / ...PUBLIC AFFAIRS DIVISION...THE TOBACCO INSTITUTE..."
Date: "Monday January 24, 1994"
Body: prose paragraphs about legislative updates.
Footer: "...For further information...call Public Affairs..."

This is an internal communication. If I must choose, `memo` is the closest for internal correspondence that isn't a letter.
Wait, what if it's `news_article`?
"any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet" -> No.

What if it's `presentation`?
No.

Let's think if this could be `scientific_report`.
"Original research write-up -> scientific_report. Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page... Requires running prose"
This is not original research.

Could it be `form`?
No.

Could it be `file_folder`?
No.

Let's reconsider `news_article`.
Is The Tobacco Institute a general-audience outlet? No, it's a trade association.
But the content is news. "Proposal from working group of NATL ASSN OF ATTORNEYS GENERAL... Statewide 'Uniform Tobacco Control' initiative... SOUTH DAKOTA H1267... WISCONSIN Assembly... INDIANA House... WASHINGTON House... VIRGINIA H249... FT. SMITH AR... RICHMOND COUNTY GA... AUSTIN TX..."
This is a news bulletin.
If the categories don't have "newsletter" or "bulletin", what is the best fit?
Maybe `memo`? Internal memo/bulletin.
"A dated internal note addressed to a named person... IS a memo even without literal TO:/FROM: labels"
This is a dated internal note. Even if not addressed to a named person, it's an internal memo/bulletin.

Wait, look at check 12 again:
"Newspaper or magazine masthead, byline, dateline, multi-column news typography, '- more-' continuation, or wire-service credit. Also a magazine feature or an encyclopedia entry/excerpt (e.g. a 'TOBACCO ENCYCLOPEDIA' page with a titled, authored article), or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet — even when the topic is scientific and journal citations appear within the text as references to other work."
This page has a dateline: "Monday January 24, 1994".
It has multi-column? No, it's single column.
It has "...DAILY BULLETIN..." which is like a masthead.
But it's from "THE TOBACCO INSTITUTE", not a general-audience outlet.

What about `scientific_report`?
Sometimes, industry internal reports that summarize legislative or scientific news are classified as `scientific_report` if they are technical. But this is purely legislative news.

Let's reconsider `memo`.
Memo is for internal correspondence. A daily bulletin from the Public Affairs Division is internal correspondence.
I will classify this as `memo`.

Wait! Is there any chance this is `news_article`?
If the classifier considers any page with news content as `news_article`... but the prompt specifically says: "news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout... from a GENERAL-AUDIENCE outlet". The Tobacco Institute is not a general-audience outlet.

Let's check `presentation`.
No.

Let's check `letter`.
No external address, no salutation.

I'll go with `memo`. It's an internal document from The Tobacco Institute, Public Affairs Division, dated January 24, 1994, containing internal news/bulletin prose. Internal dated notes with prose are memos.

Wait, is there any possibility it's `scientific_report`?
"Running narrative prose with objectives, methods, results, or discussion... Requires running prose"
This has running prose. But it's not a research write-up.

Let's review the memo definition:
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation). Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."

This document has:
- Internal division: "PUBLIC AFFAIRS DIVISION...THE TOBACCO INSTITUTE"
- Date: "Monday January 24, 1994"
- Prose: paragraphs of legislative updates.
- No external address, no salutation, no closing signature.
This fits the "dated internal note... with memo-style prose" pattern, even if it's a bulletin format. The function is internal communication/memo.

Let's double check if there's any other label.
"advertisement" - no.
"budget" - no.
"email" - no.
"file_folder" - no.
"form" - no.
"handwritten" - no.
"invoice" - no.
"letter" - no.
"questionnaire" - no.
"resume" - no.
"scientific_publication" - no.
"specification" - no.

So `memo` is the most appropriate.

Wait, could it be `news_article` because it's a "DAILY BULLETIN"?
"Newspaper or magazine masthead... or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet"
A "DAILY BULLETIN" from an institute is not from a general-audience outlet. It's an internal bulletin. Internal bulletins are memos.

I will output `memo`.

Evidence for memo:
- Internal header: "...PUBLIC AFFAIRS DIVISION...THE TOBACCO INSTITUTE..."
- Date: "Monday January 24, 1994"
- Prose body summarizing internal/legislative news.
- No external address, no salutation, no closing signature.
- Fits "dated internal note... with memo-style prose".

Runner-up: news_article. Ruled out because the page is from "THE TOBACCO INSTITUTE" (a trade association), not a "GENERAL-AUDIENCE outlet" as required for news_article.

Let's refine the scratchpad.
pre-scan: mail-client header none; "...DAILY BULLETIN... / ...PUBLIC AFFAIRS DIVISION...THE TOBACCO INSTITUTE..." is an internal bulletin header, not a general-audience masthead.
file_folder: no — full body content.
handwritten: no — typed.
fax sheet: no. questionnaire: no. resume: no. scientific_publication: no.
financial: no. specification: no. presentation: no. form: no.
correspondence: yes — internal header ("PUBLIC AFFAIRS DIVISION...THE TOBACCO INSTITUTE"), date ("Monday January 24, 1994"), prose body, no external address/salutation/closing.
memo: yes — dated internal note with memo-style prose, no salutation or closing signature.
news_article: no — not from a general-audience outlet.
Runner-up: news_article, ruled out because The Tobacco Institute is not a general-audience outlet; this is an internal bulletin/memo.

Final label: memo.
Confidence: 85.

---
### `rvl_cdip__news_article__0008.png`
**Expected:** `news_article` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the mandatory pre-scan and the 14 checks in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: "HILL AND KNOWLTON International Public Relations Counsel", "Press Clipping", "Client: Tobacco Institute of Hong Kong Limited". "Subject Publication: Oriental Daily News", "Date: March 4, 1987", "Circulation: 650,000". There is a clipping of a Chinese newspaper article. No journal running head.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Evidence: There is a lot of content: "Press Clipping", a Chinese newspaper clipping, and a paragraph of English text summarizing a seminar. Not file_folder.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Evidence: Typed text throughout. Not handwritten.

Check 3: FAX TRANSMISSION SHEET -> form
- Evidence: No fax header. Not fax.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Evidence: Not a survey.

Check 5: PERSON'S CAREER HISTORY -> resume
- Evidence: Not a resume.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- Evidence: No journal running head, volume, issue, DOI. Not a scientific publication.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- Evidence: No financial data, no payment demand. Not financial.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- Evidence: No product specs, MSDS, etc. Not specification.

Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
- Evidence: Not a slide deck.

Check 10: ADMINISTRATIVE FORM -> form
- Evidence: Not a form with fill-in fields.

Check 11: CORRESPONDENCE -> email, memo, or letter
- Evidence: "HILL AND KNOWLTON", "Press Clipping", "Client: Tobacco Institute...", "Subject Publication: Oriental Daily News", "Date: March 4, 1987", "Circulation: 650,000". This is a press clipping transmittal or cover sheet from a PR firm. Wait, is it a letter or memo? It has "Subject", "Date", "Client", "Publication". It's a cover sheet for a press clipping. Let's look at the content. It's a press clipping from "Oriental Daily News" with a summary paragraph.
Wait, let's look at check 12: PUBLISHED JOURNALISM -> news_article.
The page contains a "Press Clipping" from "Oriental Daily News". The main content is a newspaper clipping (Chinese text) and a summary paragraph about a "passive smoking" seminar.
Is it a news_article? "Newspaper or magazine masthead, byline, dateline, multi-column news typography... Also a magazine feature or an encyclopedia entry... or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet". This page is a PR firm's press clipping report. It's not the newspaper itself.
Wait, what about check 11? "memo: internal TO:/FROM:/RE:/SUBJECT:/DATE: header block followed directly by memo-style prose". This has "Subject", "Date", "Client", "Publication". It's a cover page for a press clipping.
Let's re-read check 12: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout." This page is a press clipping summary.
Wait, is there any other category?
Let's check the labels: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

Could it be `news_article`? The page contains a clipping from a newspaper ("Oriental Daily News") and a summary. But the page itself is a "Press Clipping" cover sheet from Hill and Knowlton.
Wait, look at the text: "In a 'passive smoking' seminar held yesterday, Mr Steve Kroos, Chairman of the Tobacco Institute of Hong Kong, called for rational debate..." This is a news summary or a press release summary.
Is it a `memo`? "Subject Publication: Oriental Daily News Date: March 4, 1987 Circulation: 650,000 Leadership:"
It looks like a cover sheet for a press clipping.
What about `letter`? No salutation, no closing.
What about `presentation`? No.
What about `scientific_report`? No.

Let's rethink: Is this a `news_article`? The document is a press clipping. Often, press clippings are classified as `news_article` if they are just the article, but this is a PR firm's cover sheet.
Wait, look at the content: it's a clipping from a newspaper. The text below is a summary of the article.
Could it be `form`? No.
Could it be `memo`? Hill and Knowlton is a PR firm. They send press clippings to clients. This is a cover sheet. "Client: Tobacco Institute of Hong Kong Limited". "Subject Publication: Oriental Daily News". "Date: March 4, 1987". "Circulation: 650,000". "Leadership:" (blank).
This is a transmittal cover sheet for a press clipping.
Is there a category for this?
Maybe `news_article`? The page contains a newspaper clipping. But the dominant content is the PR cover sheet and the summary.
Wait, what if it's `news_article` because it's a clipping from a newspaper? "Newspaper or magazine masthead... multi-column news typography...". The Chinese text is a newspaper clipping.
But the page itself is a PR report.
Let's check the categories again:
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

If I have to choose between `news_article` and `memo` or `letter`.
Actually, a press clipping summary from a PR firm is often just classified as `news_article` if the main content is the news article, or maybe `memo` if it's an internal memo. But this is sent to a client ("Client: Tobacco Institute...").
Wait, could it be `letter`? No salutation.
Could it be `memo`? "Subject", "Date", "Client". Not a standard memo.
What about `presentation`? No.

Let's look at the text again:
"HILL AND KNOWLTON International Public Relations Counsel"
"Press Clipping"
"Client: Tobacco Institute of Hong Kong Limited"
"Subject Publication: Oriental Daily News"
"Date: March 4, 1987"
"Circulation: 650,000"
"Leadership:"
[Chinese newspaper clipping]
"In a 'passive smoking' seminar held yesterday, Mr Steve Kroos, Chairman of the Tobacco Institute of Hong Kong, called for rational debate on the issue that smoking is hazardous to health. He said that discussion by the public on the issue has apparently become sensational and politicalized. Two US scholars pointed out that, although a number of researchs have been conducted throughout the world, no association between passive smoking and health hazards has been established."

This is a press clipping report. The document itself is a summary of a news article.
Is it `news_article`? "any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet". This page does not present as published periodical editorial content; it presents as a PR firm's press clipping cover sheet.
Wait! What if the category is `news_article` because it's a clipping from a newspaper? The instructions say: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content". This page does not present as editorial news content; it's a PR cover sheet.

Could it be `form`? "A records-management inventory or log table...". No.
Could it be `file_folder`? No.

Let's reconsider `news_article`. Sometimes, press clippings are classified as `news_article` because they contain the news article. But here, the news article is just a small Chinese clipping, and the main text is a summary paragraph.
Wait, is there any other category?
What about `scientific_report`? No.

Let's look at the checks again.
Check 11: CORRESPONDENCE -> email, memo, or letter.
"memo: internal TO:/FROM:/RE:/SUBJECT:/DATE: header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... is a memo".
This is not internal; it's sent to a client ("Client: Tobacco Institute...").
"letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature". No salutation, no signature.

What about `presentation`? "a meeting/program/speaker cover page". No.

What about `news_article`? If the page is a press clipping, maybe it's considered `news_article`?
"Newspaper or magazine masthead, byline, dateline, multi-column news typography, '- more-' continuation, or wire-service credit. Also a magazine feature or an encyclopedia entry/excerpt... or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet".
The Chinese text is a newspaper clipping. But the page is a PR cover sheet.

Wait, is there a category for "press clipping"? No.
Could it be `form`? A "Press Clipping" cover sheet with fields "Client", "Subject Publication", "Date", "Circulation", "Leadership". It's a template used by PR firms to log press clippings.
Check 10: "Administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... a records-management inventory or log table".
This page has fields: "Client: [filled]", "Subject Publication: [filled]", "Date: [filled]", "Circulation: [filled]", "Leadership: [blank]". It's a cover sheet for a press clipping. Is it a form?
"A form does NOT have to be blank — a filled form recording data is still a form... This also covers: a standalone labeled data chart or table... internal authorization/approval forms with an approval signature/date block."
This is a cover sheet for a press clipping. It captures factual data (Client, Publication, Date, Circulation). It could be classified as `form`.

Wait, what if it's `news_article`? The summary paragraph is about a news event. But it's not published journalism.
What if it's `scientific_report`? No.

Let's think about `news_article`. The document is a "Press Clipping". The content is a clipping from "Oriental Daily News". The text below is a summary of the article. In many document classification tasks, a press clipping is classified as `news_article` because it contains news content. But the instructions say: "Judge by DOMINANT content... news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout." This page does not present as editorial news content. It presents as a PR firm's cover sheet.

Could it be `memo`? "Subject Publication: Oriental Daily News Date: March 4, 1987". It has a "Subject" and "Date" field. But it's not a memo.

Let's look at the label list again:
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

If I have to choose the best fit:
The page is a "Press Clipping" cover sheet from Hill and Knowlton. It has fields for Client, Subject Publication, Date, Circulation, Leadership. It contains a newspaper clipping and a summary.
Is it a `form`? Yes, it's a cover sheet with fields capturing data about a press clipping. "Filled or blank fields... for capturing factual data". The fields are "Client", "Subject Publication", "Date", "Circulation", "Leadership". The data is filled in (Client, Publication, Date, Circulation). This is a filled form.
Wait, is there a stronger category?
What about `news_article`? The page contains a newspaper clipping. But the page itself is not the newspaper.
What about `letter`? No.

Let's check the rules for `form`:
"A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: a standalone labeled data chart or table... internal authorization/approval forms with an approval signature/date block."
This page is a cover sheet for a press clipping. It has labeled fields: "Client:", "Subject Publication:", "Date:", "Circulation:", "Leadership:". The fields are filled with data. This is a filled form.

Is there any evidence for `news_article`?
"Newspaper or magazine masthead, byline, dateline, multi-column news typography..."
The Chinese text is a newspaper clipping, but it's not the dominant layout. The dominant layout is the PR cover sheet and the summary paragraph.

Is there any evidence for `scientific_report`?
"In a 'passive smoking' seminar held yesterday..." This is a summary of a news event, not a scientific report.

Is there any evidence for `presentation`?
No.

I will classify this as `form`. It is a press clipping cover sheet with fields for client, publication, date, circulation, and leadership. It captures factual data about a press clipping.

Wait, let's re-read the `news_article` check:
"Newspaper or magazine masthead, byline, dateline, multi-column news typography, '- more-' continuation, or wire-service credit. Also a magazine feature or an encyclopedia entry/excerpt (e.g. a 'TOBACCO ENCYCLOPEDIA' page with a titled, authored article), or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet — even when the topic is scientific and journal citations appear within the text as references to other work."
This page does not present as published periodical editorial content. It's a PR firm's cover sheet.

What about `letter`?
"letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature"
No salutation, no signature.

What about `memo`?
"internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose"
This has "Subject" and "Date", but not "TO:/FROM:". And it's not internal; it's sent to a client.

So `form` is the most appropriate label. The page is a press clipping cover sheet (a form used by PR firms to log and transmit press clippings to clients). It has labeled fields (Client, Subject Publication, Date, Circulation, Leadership) that are filled with data.

Let's double check if there's any other category.
"Press Clipping" is the title.
Fields:
Client: Tobacco Institute of Hong Kong Limited
Subject Publication: Oriental Daily News
Date: March 4, 1987
Circulation: 650,000
Leadership: [blank]

This is a structured data capture page. It's a form.

Wait, could it be `file_folder`?
"A page titled 'RECORDS MANAGEMENT INVENTORY'... is a form (check 10), not file_folder — it's tabulating an inventory of many items as structured data, not identifying a single filed document."
This page identifies a single press clipping. But it has a lot of content (the clipping and the summary paragraph). "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
This page has a newspaper clipping and a summary paragraph. So it's not file_folder.

Could it be `news_article` because it contains a news article?
"Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
The dominant content is the PR cover sheet and the summary. The newspaper clipping is just an attachment. So not `news_article`.

Therefore, `form` is the correct label. The page is a filled form (press clipping cover sheet) capturing data about a press clipping.

Let's review the evidence for `form`:
- Labeled fields: "Client:", "Subject Publication:", "Date:", "Circulation:", "Leadership:".
- Filled data: "Tobacco Institute of Hong Kong Limited", "Oriental Daily News", "March 4, 1987", "650,000".
- Function: capturing factual data about a press clipping for a client.
- Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... a filled form recording data is still a form".

Runner-up: `news_article`. Ruled out because the page does not present primarily as editorial/multi-story news content; it is a PR firm's cover sheet with a newspaper clipping attached and a summary paragraph. The dominant layout is the cover sheet, not the newspaper.

Another runner-up: `memo`. Ruled out because it lacks a TO:/FROM:/RE: header block and is not internal correspondence; it's a client cover sheet.

Final label: `form`.
Confidence: 85.

---

## form → budget (2 errors)

### `rvl_cdip__form__0018.png`
**Expected:** `form` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow the scratchpad procedure, walking through checks 1-14 in order.

Let's look at the document.
It's a table/chart.
Title: "1976 ADVERTISING PLAN CHART"
"BRUNO & WILLIAMSON TOBACCO CORPORATION"
"METRO SUNDAY SUPPLEMENT"
"MILWAUKEE JOURNAL"
Columns: Jan, Feb, March, April, May, June, July, Aug, Sept, Oct, Nov, Dec.
Rows: SUNDAY DATES, KOOL, RALEIGH, FACT, VICEROY, TOTAL, MATERIAL CLOSING, SPACE CLOSING (6 weeks).
There are numbers and 'X' marks in the grid.
Bottom right: "670163842" (Bates number).
Bottom left: "Circulation: 587,612 as of 3-31-75"
Top right: "Dated: 12/21/75 Revised: 3/28/76"
Bottom text: "REVISION: KOOL - Cancel 12/5 insertion."
"EG MEDIA DEPARTMENT"
"XS = 2 page spread (* = centerspread)"
"c = coupon ad"
"t = full page ad"
"1 = 3 color"

Let's evaluate the checks:

Check 1: file_folder. No, it has a full table with real content.
Check 2: handwritten. No, mostly typed with some handwritten 'X's and numbers. Wait, is it mostly handwritten? No, it's a printed grid filled in with typed/printed numbers and some 'X's. Actually, looking closely, the numbers and X's might be typed or handwritten, but it's a filled form/table. Wait, check 2 says "Most of the content is freeform handwriting... NOT on a printed template." This is on a printed template. So not handwritten.
Check 3: FAX TRANSMISSION SHEET. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial document (invoice or budget). It's an advertising plan chart. Advertising plan, circulation, space closing. Is it a budget? "internal money planning, tracking, or disbursement... financial/money-data table". An advertising plan with space closing and circulation might be budget. Let's check check 7: "budget: internal money planning, tracking, or disbursement WITHOUT demanding payment. Budget includes: ... a financial/money-data table ... A document titled 'ESTIMATE' is budget". Wait, is this a budget? It's an "ADVERTISING PLAN CHART". It tracks ad placements (KOOL, RALEIGH, FACT, VICEROY) across months. It has "SPACE CLOSING (6 weeks)". This looks like an advertising media plan or budget tracking. Let's see if there's a better fit.
Check 8: specification. No.
Check 9: presentation. "A standalone chart or table of values alone — an untitled data table or a bare chart with no deck styling — is NOT a slide; it is a form (check 10). BUT a TITLED, DESIGNED DECK CHART ... IS a presentation". This is a titled table/chart: "1976 ADVERTISING PLAN CHART". Is it a designed deck chart? It looks like a printed spreadsheet or planning chart, not a slide deck. "EG MEDIA DEPARTMENT". It's a media planning chart.
Check 10: administrative form. "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) ... is a form only when it holds generic administrative/log data". This is an advertising plan chart. Wait, check 10 says: "a financial/money chart is budget (check 7) ONLY when it is a standalone data table used for money planning or tracking". Is this a financial/money chart? It's an advertising plan. Advertising plans track media buys, which is a budget.
Let's re-read check 7: "budget: internal money planning, tracking, or disbursement ... financial/money-data table". An advertising plan chart tracking ad insertions (KOOL, RALEIGH, etc.) across months is definitely internal money planning/tracking for advertising. It's a media budget or advertising plan.
Wait, let's look at the labels again. Is there an "advertising_plan" label? No. The labels are: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
Could it be `form`? "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A standalone labeled data chart or table ... is a form only when it holds generic administrative/log data". This is an advertising plan, which is a specific business document.
Could it be `budget`? "budget: internal money planning, tracking, or disbursement ... financial/money-data table". An advertising plan tracks where money is spent (ad space).
Let's check if there's any other category.
What about `presentation`? "A standalone chart or table of values alone ... is NOT a slide; it is a form (check 10). BUT a TITLED, DESIGNED DECK CHART ... IS a presentation". This doesn't look like a deck chart. It looks like a printed planning sheet.
What about `specification`? No.
What about `scientific_report`? No.

Let's carefully consider `budget` vs `form`.
The document is "1976 ADVERTISING PLAN CHART". It has rows for brands (KOOL, RALEIGH, FACT, VICEROY) and columns for months. It tracks "SUNDAY DATES", "MATERIAL CLOSING", "SPACE CLOSING". This is a media planning/budgeting chart. It tracks ad placements, which is part of the advertising budget.
Check 7: "budget: internal money planning, tracking, or disbursement WITHOUT demanding payment. Budget includes: ... a financial/money-data table ...". An advertising plan is a financial planning document for media buys.
Wait, is there any explicit money amount? "Circulation: 587,612". "XS = 2 page spread", "c = coupon ad", "t = full page ad", "1 = 3 color". These are ad specs, not dollar amounts. But it's a plan for advertising space, which is a budget item.
Is it a `form`? "administrative form -> form. ... A standalone labeled data chart or table ... is a form only when it holds generic administrative/log data". This is a specific advertising plan, not generic administrative data.
Actually, let's look at check 10 again: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7) ... including ... financial or money-data tables (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures), which are budget, not a generic labeled-data form."
This chart is tracking advertising space (media plan). Is it a budget? Yes, media planning is a subset of budgeting.
Wait, could it be `form`? "A QA/parameter review sheet ... stays form". This is not a QA sheet.
Let's consider if it's `presentation`. "A chart-per-page deck look is explicitly part of this check's definition." This is not a deck. It's a printed spreadsheet-like chart.

Let's re-evaluate `budget`.
"budget: internal money planning, tracking, or disbursement ... financial/money-data table".
Is an advertising plan a financial/money-data table? It tracks ad insertions, which directly relates to the advertising budget. The "SPACE CLOSING" and "MATERIAL CLOSING" are budget tracking terms in media planning.
I will classify this as `budget`.

Wait, could it be `form`?
Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a research-measurement chart is scientific_report (check 13), and a financial/money chart is budget (check 7) ONLY when it is a standalone data table used for money planning or tracking".
This chart is used for money planning/tracking (advertising budget). So it falls under budget (check 7) rather than form (check 10).

Let's check if there's any other evidence.
"1976 ADVERTISING PLAN CHART"
"BRUNO & WILLIAMSON TOBACCO CORPORATION"
"METRO SUNDAY SUPPLEMENT"
"MILWAUKEE JOURNAL"
This is clearly an advertising media plan. Advertising plans are budget documents.
I'll go with `budget`.

Wait, is there any possibility it's `advertisement`?
Check 14: "PROMOTIONAL MATERIAL -> advertisement. Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures." This is an internal planning chart, not a promotional layout.

Is there any possibility it's `specification`?
Check 8: "specification. ... test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table ... is a specification". This is not a product analysis table; it's an advertising plan chart.

So `budget` is the best fit.

Let's double check check 7:
"budget: internal money planning, tracking, or disbursement WITHOUT demanding payment. Budget includes: expense reports, forecast-vs-actual, a statement of account, a check face/check stub, a check register, a financial/money-data table, a handwritten list of expenses, a campaign-contribution/expenditure statement, or a money-only REQUEST/CHECKLIST/STATEMENT."
An advertising plan chart tracking ad insertions across months is a financial/money-data table used for money planning (advertising budget).

Let's review the scratchpad requirements:
- Walk checks 1-14 in order.
- State evidence for each check or "not this check".
- Stop at the first matching check.

Check 1: file_folder. Evidence: none. (Has full table content).
Check 2: handwritten. Evidence: none. (Printed template with some filled entries).
Check 3: fax sheet. Evidence: none.
Check 4: questionnaire. Evidence: none.
Check 5: resume. Evidence: none.
Check 6: scientific_publication. Evidence: none.
Check 7: financial document (invoice or budget). Evidence: "1976 ADVERTISING PLAN CHART", tracking ad insertions (KOOL, RALEIGH, FACT, VICEROY) across months for "METRO SUNDAY SUPPLEMENT". This is an internal money planning/tracking document (advertising budget/media plan). Budget matches.
Check 8: specification. Evidence: none.
Check 9: presentation. Evidence: none. (Not a deck chart).
Check 10: form. Evidence: none. (Check 7 overrides for financial/money planning charts).
Check 11: correspondence. Evidence: none.
Check 12: news_article. Evidence: none.
Check 13: scientific_report. Evidence: none.
Check 14: advertisement. Evidence: none.

Final label: budget.

Wait, is there any chance this is `form`?
"A standalone labeled data chart or table ... is a form only when it holds generic administrative/log data". This is a specific advertising plan, not generic. And check 7 says "financial/money chart is budget (check 7) ONLY when it is a standalone data table used for money planning or tracking". An advertising plan is exactly that.

I'm confident in `budget`.
Let's quickly check the runner-up. `form` is the most likely runner-up because it's a grid with filled cells. But the content is an advertising plan, which is a budget document. I will note `form` as the runner-up.

Let's refine the evidence for Check 7:
"1976 ADVERTISING PLAN CHART" with rows for brands (KOOL, RALEIGH, FACT, VICEROY) and columns for months (Jan-Dec), tracking "SUNDAY DATES", "MATERIAL CLOSING", "SPACE CLOSING". This is an internal media planning/budgeting chart used for tracking advertising spend and placements, which falls under budget (internal money planning/tracking).

Runner-up: form. Ruled out because check 7 explicitly routes financial/money planning charts (like an advertising plan tracking space/closing) to budget, overriding the form layout.

Confidence: 85.
Evidence is clear: "1976 ADVERTISING PLAN CHART", media tracking across months. Budget is the correct category for internal money planning/tracking documents like media plans.

---
### `rvl_cdip__form__0001.png`
**Expected:** `form` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead/running head: "Ted Bates new york/advertising" is a letterhead/agency name, not a newspaper/magazine masthead. "BROWN & WILLIAMSON TOBACCO CORPORATION" is a company name. No journal running head.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Content: "PRINT PRODUCTION ESTIMATE", tables, line items, fees. Not identifier-only.
- Not this check.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Content: Mostly typed, with some handwritten numbers in the cost columns (e.g., "3,144", "4,125", "548 + 312"). Not majority handwritten.
- Not this check.

Check 3: FAX TRANSMISSION SHEET -> form
- No fax header.
- Not this check.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Not a survey.
- Not this check.

Check 5: PERSON'S CAREER HISTORY -> resume
- Not a resume.
- Not this check.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- No journal identifier.
- Not this check.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- Content: "PRINT PRODUCTION ESTIMATE" from "Ted Bates new york/advertising" for "BROWN & WILLIAMSON TOBACCO CORPORATION".
- Lists items like "Photographer's Fee", "Model Fee", "Dye Transfer", "C-Prints", with "Cost Per Ad/Item", "No. of Ads/Items", "Estimated Total Cost", "Actual Total Cost".
- Title is "PRINT PRODUCTION ESTIMATE".
- Check 7 says: "A document titled 'ESTIMATE' is budget — it PLANS spending, even when it compares previous/current amounts, has revision columns, or lists project costs. Only an explicit payment demand makes it invoice; the word 'estimate' itself signals planning, not billing."
- There is no "Amount Due", "Pay This Amount", or payment demand. It's an estimate of costs for print production.
- This is budget.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- Not an MSDS or product specification.
- Not this check.

Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
- Not a slide deck.
- Not this check.

Check 10: ADMINISTRATIVE FORM -> form
- Has fields and a table, but check 7 (financial/budget) overrides form layout when money function is primary. Wait, check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "A document titled 'ESTIMATE' is budget".
- Let's re-read check 7: "budget: internal money planning, tracking, or disbursement WITHOUT demanding payment. Budget includes: expense reports, forecast-vs-actual, a statement of account, a check face/check stub, a check register, a financial/money-data table, a handwritten list of expenses... A document titled 'ESTIMATE' is budget — it PLANS spending..."
- This is an estimate of costs for an advertisement production. It's a financial/money-data table / estimate. So budget.

Check 11: CORRESPONDENCE -> email, memo, or letter
- Not correspondence.
- Not this check.

Check 12: PUBLISHED JOURNALISM -> news_article
- Not news.
- Not this check.

Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report
- Not research.
- Not this check.

Check 14: PROMOTIONAL MATERIAL -> advertisement
- Not an ad itself, it's an estimate for an ad.
- Not this check.

Let's double check Check 7 vs Check 10.
The page is a "PRINT PRODUCTION ESTIMATE". It has fields (Brand, Caption, Subject, Photographer/Artist, etc.) and a table of costs.
Check 7: "financial/money-data table ... is budget, not a generic labeled-data form." "A document titled 'ESTIMATE' is budget".
Check 10: "administrative form ... does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)".
So budget is the correct label.

Evidence for budget:
- Title: "PRINT PRODUCTION ESTIMATE"
- Content: Financial table listing fees (Photographer's Fee, Model Fee, Dye Transfer, etc.) with columns for "Cost Per Ad/Item", "No. of Ads/Items", "Estimated Total Cost", "Actual Total Cost".
- No payment demand (not invoice).
- Check 7 explicitly states: "A document titled 'ESTIMATE' is budget — it PLANS spending... financial/money-data table ... is budget, not a generic labeled-data form."

Runner-up: form. Ruled out because check 7 explicitly routes money-only forms and estimates to budget, overriding the form layout.

Let's review the scratchpad requirements:
- Walk checks 1-14 in order.
- State evidence or "not this check".
- Stop at first matching check.
- Add final line naming runner-up and evidence that ruled it out.

Scratchpad:
pre-scan: mail-client header none; "Ted Bates" and "BROWN & WILLIAMSON" are company names/letterheads, not a journal masthead or newspaper masthead.
file_folder: no — full document with title, fields, and cost table.
handwritten: no — mostly typed, only some handwritten numbers in cost columns.
fax sheet: no. questionnaire: no. resume: no. scientific_publication: no.
financial: yes — page is a "PRINT PRODUCTION ESTIMATE" with a financial table of fees (Photographer's Fee, Model Fee, Dye Transfer, etc.) and cost columns.
invoice: no — no "Amount Due", "Pay This Amount", or payment demand; it is an estimate.
budget: yes — titled "PRINT PRODUCTION ESTIMATE", lists planned costs/fees for ad production, no payment demand. Check 7 explicitly states "A document titled 'ESTIMATE' is budget" and money-only forms/tables are budget.
specification: no. presentation: no.
form: no — check 7 overrides form layout for financial documents; "money-only forms are budget (check 7)".
Runner-up: form, ruled out because check 7 explicitly routes estimates and money-data tables to budget, overriding the form-like layout.

Final label: budget.
Confidence: 95.
Evidence is very clear: "PRINT PRODUCTION ESTIMATE", cost table, no payment demand. Check 7 explicitly covers this.

---

## form → file_folder (2 errors)

### `rvl_cdip__form__0006.png`
**Expected:** `form` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the mandatory pre-scan and the 14 checks in order.

**Pre-scan:**
- Mail-client header block: None.
- Fax transmission header: None. (There is a "FAX #:" field in the To/From block, but it's part of a cover sheet layout, not a machine-stamped "SENT BY:" header).
- Masthead/running head: None. "LORILLARD TOBACCO COMPANY Market Planning and Information Department" is a letterhead/department header, not a newspaper/magazine masthead or journal running head.

**Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a full letter body, header block, etc. Not identifier-only.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Typed text, with a handwritten signature "Sus" and maybe some minor marks. Not majority handwritten.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: The page has a box with "To:", "Firm:", "FAX #:", "From:", "FAX #:", "Phone #:", "Date:", "# Pages:". This looks like a fax cover sheet. Wait, check 3 says: 'A "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", or "TELEFAX MESSAGE NO." header with To/From/company/phone/page-count fields. Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels.'
- Does this page have a "FACSIMILE", "FAX COVER SHEET", etc. header? The header is "LORILLARD TOBACCO COMPANY / Market Planning and Information Department". It doesn't explicitly say "FAX COVER SHEET" or "FACSIMILE TRANSMISSION". It just has a To/From block with FAX # fields. Let's look closely at the text. It's a memo/letter with a fax routing block at the top. Wait, is it a fax cover sheet? The text says "# Pages: 3 (including this cover page)". This implies it's a cover page for a fax. But does it have the specific headers required for check 3? "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", or "TELEFAX MESSAGE NO." header. It doesn't have those exact words. Let's keep reading. Wait, check 11 covers correspondence. Let's evaluate check 11 first.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal masthead.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No line-item table, no payment demand. Mentions "Store Count Database", "market importance". No money.
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: No.
- Not this check.

**Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: Has a box with fields, but the main content is a short memo/letter. Check 10 says "A form does NOT have to be blank...". But is the primary structure a form? The primary structure is a memo/letter with a fax routing block. Let's check 11.

**Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence:
  - Header: "LORILLARD TOBACCO COMPANY / Market Planning and Information Department"
  - Routing block: To: Mike Mozina, Firm: MSA, FAX #: Autodial, From: Susan Smith, FAX #: 335-7733, Phone #: 335-7150, Date: 8/31/98, # Pages: 3 (including this cover page).
  - Body: "Mike, As promised, here are: -- Approval for AWS Quarterly Store Count Database to begin 3rd Quarter 1998 -- Table showing significant jump in Convenience Store market importance in 2nd Quarter 1998 Talk to you soon! Sus"
  - This is a memo or letter. It has an internal "To:" (Mike Mozina) and "From:" (Susan Smith). Wait, the firm is "MSA", which is external. "Mike Mozina / MSA". This makes it addressed to an external person.
  - Let's check the memo vs letter rules in Check 11:
    - "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo"
    - "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."
    - Here, the recipient is "Mike Mozina" at "Firm: MSA". MSA is an external firm. The salutation is "Mike,". The closing is "Talk to you soon! Sus" (handwritten signature).
    - Is it a letter or a memo? The routing block has "To:", "From:", "Date:", "# Pages:". It doesn't have "RE:" or "SUBJECT:". But it has "To:" and "From:".
    - Wait, the rule for memo says: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block". This doesn't have RE/SUBJECT.
    - The rule for letter says: "letterhead with an external recipient address... OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block." But this HAS a TO:/FROM: block.
    - Let's re-read carefully: "A dated note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels"
    - What about external? "A dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block. ... If the page still has an external addressee, a 'Dear ...' salutation, a prose body, and a closing signature, it stays letter"
    - Here we have: external addressee (Mike Mozina, MSA), no "Dear ..." salutation (just "Mike,"), prose body, closing signature ("Sus").
    - Wait, is "Mike," a salutation? Yes. Is it "Dear Mike,"? No, just "Mike,".
    - Let's look at the routing block again. It's a fax cover sheet layout. "FAX #: Autodial", "# Pages: 3 (including this cover page)". This is a fax cover sheet.
    - Check 3: "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header with To/From/company/phone/page-count fields. Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels."
    - Does this page have one of those headers? The header is "LORILLARD TOBACCO COMPANY / Market Planning and Information Department". It does NOT have "FAX COVER SHEET" or "FACSIMILE TRANSMISSION".
    - However, the block itself is a fax routing block. "# Pages: 3 (including this cover page)" strongly implies it's a cover page for a fax.
    - If it's not check 3, what is it? It's a memo/letter.
    - Let's re-evaluate check 11: "email: mail-client header block... memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block... letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."
    - Wait, if it has a TO:/FROM: block AND an external addressee, what is it?
    - "Routing/distribution fields added on top of a full letter (e.g. a mailroom stamp with 'To:'/'From:'/'Posted:'/'Subject:' fields) do NOT turn a letter into a memo: if the page still has an external addressee, a 'Dear ...' salutation, a prose body, and a closing signature, it stays letter — memo requires the TO/FROM/RE header to be immediately followed by memo-style prose with no salutation or external address, not just the presence of routing-style field labels somewhere on the page."
    - Here, the TO/FROM block is followed by "Mike," (salutation), prose body, and "Sus" (closing signature). And it has an external address ("Firm: MSA"). So it stays a LETTER.
    - Wait, is "Mike," a salutation? Yes. Is there a closing signature? Yes, "Sus".
    - So it's a letter.

Let's double check Check 3: "FAX TRANSMISSION SHEET -> form".
"A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header with To/From/company/phone/page-count fields. Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels."
The page does NOT have "FAX COVER SHEET" or similar as a header. The header is "LORILLARD TOBACCO COMPANY". So Check 3 does not fire.

Let's double check Check 11: "CORRESPONDENCE -> email, memo, or letter".
- email: no mail-client header.
- memo: requires internal TO/FROM/RE/SUBJECT/DATE. This has external firm "MSA". Also requires no salutation or external address. This has external address and salutation "Mike,". So not memo.
- letter: "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."
Wait, the rule says: "if the page still has an external addressee, a 'Dear ...' salutation, a prose body, and a closing signature, it stays letter". Here we have "Mike," instead of "Dear Mike,". Is "Mike," considered a salutation? Yes, addressing someone by their first name is a salutation. And it has a closing signature "Sus". And it has an external addressee (MSA). So it's a letter.

Wait, is there any other check?
What about Check 10: "ADMINISTRATIVE FORM -> form".
"A form does NOT have to be blank — a filled form recording data is still a form... This also covers: ... internal authorization/approval forms with an approval signature/date block."
But the primary structure is correspondence. "A page whose primary structure is a memo header + prose, but whose prose merely discusses, forwards, or requests approval of an invoice/bill... stays memo". Here, the primary structure is a letter/memo with a fax routing block. The fax routing block is just routing metadata. The content is a short letter. "Mike, As promised, here are: ... Talk to you soon! Sus". This is clearly a letter/memo. Since it's external, it's a letter.

Let's review the exact text of Check 11:
"letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."
Wait, if it has a TO:/FROM: block, but is addressed to an external person, and has a salutation and closing signature, the routing rule says: "Routing/distribution fields added on top of a full letter ... do NOT turn a letter into a memo: if the page still has an external addressee, a 'Dear ...' salutation, a prose body, and a closing signature, it stays letter".
Here we have:
- External addressee: Mike Mozina, MSA
- Salutation: "Mike,"
- Prose body: "As promised, here are: ..."
- Closing signature: "Sus"
Therefore, it is a letter.

Let's check if there's any other evidence.
"LORILLARD TOBACCO COMPANY / Market Planning and Information Department" -> letterhead.
"To: Mike Mozina / Firm: MSA" -> external recipient address.
"Date: 8/31/98" -> date.
"Mike," -> salutation.
"Talk to you soon! Sus" -> closing with signature.
This perfectly matches the letter definition, with the fax routing block acting as the "routing/distribution fields added on top of a full letter".

Wait, could it be a memo?
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."
This has an external address ("Firm: MSA") and a salutation ("Mike,"). So it's not a memo.

Could it be a fax transmission sheet (form)?
Check 3 requires a "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", or "TELEFAX MESSAGE NO." header. The header here is "LORILLARD TOBACCO COMPANY". It does not match the required header strings for Check 3. The presence of "FAX #:" and "# Pages:" fields is typical of a fax cover sheet, but without the explicit header label, Check 3 does not fire. The instructions say: "A FAX machine transmission header is NOT a mail-client header... but a FAX machine transmission header is NOT a mail-client header: machine-stamped 'SENT BY:'... is fax transmission metadata... you must classify the underlying document by its own content". Here, the underlying document is a letter with a fax routing block. Since the routing block doesn't have the exact "FAX COVER SHEET" header, we fall back to the underlying document's content, which is a letter.

Wait, is there any possibility this is a "form"?
Check 10: "Administrative form... Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". The top box has fields, but the bottom half is a letter. The primary function is correspondence, not data capture. The form rule says "A form does NOT have to be blank...". But correspondence overrides form if the primary structure is correspondence. "A page whose primary structure is a memo header + prose... stays memo". Similarly, a page whose primary structure is a letter header + prose stays letter.

Let's confirm the label: `letter`.

Evidence for letter:
- Letterhead: "LORILLARD TOBACCO COMPANY Market Planning and Information Department"
- External recipient: "To: Mike Mozina / Firm: MSA"
- Date: "8/31/98"
- Salutation: "Mike,"
- Prose body: "As promised, here are: ..."
- Closing signature: "Talk to you soon! Sus"
- Routing fields (fax block) are added on top, but don't override the letter structure because it has external addressee, salutation, and closing signature.

Runner-up: memo. Ruled out because the document has an external recipient address ("Firm: MSA"), a salutation ("Mike,"), and a closing signature ("Sus"), which are characteristic of a letter, not an internal memo.
Another runner-up: form (fax cover sheet). Ruled out because Check 3 requires specific headers like "FAX COVER SHEET" or "FACSIMILE TRANSMISSION", which are absent; the underlying document is a letter.

Let's do a final check of the text:
"LORILLARD TOBACCO COMPANY
Market Planning and Information Department

To: Mike Mozina
Firm: MSA
FAX #: Autodial

From: Susan Smith
FAX #: 335-7733
Phone #: 335-7150

Date: 8/31/98
# Pages: 3 (including this cover page)

Mike,

As promised, here are:

-- Approval for AWS Quarterly Store Count Database to begin 3rd Quarter 1998

-- Table showing significant jump in Convenience Store market importance in 2nd Quarter 1998

Talk to you soon! Sus"

Bates number: 86220420 (vertical on the right).

Everything aligns with `letter`.
Confidence: 95.
The evidence is very clear. The routing block is just a fax cover block, but without the explicit "FAX COVER SHEET" header, it doesn't trigger check 3. The content is a letter to an external party (MSA).
I will output `letter`.

---
### `rvl_cdip__form__0004.png`
**Expected:** `form` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned business document.
I will follow the scratchpad procedure and walk through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: None. Just "Insecticides" at the top right (rotated) and "51303 2938" at the bottom right (rotated). Wait, let's look at the image.
The image is mostly blank white space.
On the right edge, there is a vertical black line (maybe a border or scan artifact).
Text at top right (rotated 90 degrees clockwise): "Insecticides"
Text at bottom right (rotated 90 degrees clockwise): "51303 2938"
This looks like a folder tab or a section divider, or maybe a file folder page.
Wait, let's re-read check 1: IDENTIFIER-ONLY PAGE -> file_folder.
"Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."
"A prominent topical heading always counts as real content, subtitle or not. EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB ... is a filing label, not a bold headline title, even when it is rotated."
Wait, the text "Insecticides" is rotated 90 degrees. Is it a folder tab?
The right edge has a black line, maybe the edge of a folder tab.
Let's look at the text: "Insecticides" and "51303 2938".
"51303 2938" looks like a Bates number or archive number.
"Insecticides" is a short label.
Is there any other content? No. The page is almost entirely blank white space.
This perfectly matches check 1: file_folder.
"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
Here, we have "Insecticides" (short label) and "51303 2938" (Bates/archive number).
This is a folder tab page. The black line on the right is the photographed folder body/tab edge.
Let's check check 9: presentation. "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab (product/collection/month/file name, e.g. 'NEWTROL', 'Litigation Content', 'FEBRUARY') is a folder-tab label and stays file_folder (check 1)."
"Insecticides" is a short filing label naming a folder's contents.
"51303 2938" is the Bates number.
So this is file_folder.

Let's double check.
Check 1: IDENTIFIER-ONLY PAGE -> file_folder.
Evidence: "Insecticides" (rotated short label) and "51303 2938" (Bates number). Almost no body content. The right edge has a black line indicating a photographed folder tab/body.
Matches file_folder.

Check 2: handwritten -> no.
Check 3: fax -> no.
Check 4: questionnaire -> no.
Check 5: resume -> no.
Check 6: scientific_publication -> no.
Check 7: financial -> no.
Check 8: specification -> no.
Check 9: presentation -> no. "a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab ... is a folder-tab label and stays file_folder (check 1)."
Check 10: form -> no.
Check 11: correspondence -> no.
Check 12: news_article -> no.
Check 13: scientific_report -> no.
Check 14: advertisement -> no.

Runner-up: presentation (check 9). Ruled out because the rotated label "Insecticides" on a page with a black bar on the edge is a folder-tab label, not a section divider or presentation cover. The page is file_folder.

Let's confirm the visual elements:
- Top right (rotated): "Insecticides"
- Bottom right (rotated): "51303 2938"
- Right edge: a vertical black line, likely the edge of the folder tab or the scanned folder body.
- Rest of the page: blank white space.

This is a classic file_folder page (folder tab scan).

Final label: file_folder.
Confidence: 95.
Evidence is clear: Bates number, short rotated label, folder tab edge artifact, no body content.

---

## advertisement → form (2 errors)

### `rvl_cdip__advertisement__0015.png`
**Expected:** `advertisement` | **Predicted:** `form`

*No reasoning text captured.*

---
### `rvl_cdip__advertisement__0003.png`
**Expected:** `advertisement` | **Predicted:** `form`

*No reasoning text captured.*

---

## invoice → budget (2 errors)

### `rvl_cdip__invoice__0017.png`
**Expected:** `invoice` | **Predicted:** `budget`

*No reasoning text captured.*

---
### `rvl_cdip__invoice__0008.png`
**Expected:** `invoice` | **Predicted:** `budget`

*No reasoning text captured.*

---

## scientific_publication → news_article (2 errors)

### `rvl_cdip__scientific_publication__0016.png`
**Expected:** `scientific_publication` | **Predicted:** `news_article`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the mandatory pre-scan and the 14 checks in order.

**Pre-scan:**
- Mail-client header block: None.
- Masthead or running head: "HOSPITAL-TRADE" at the top center, "Monday, February 2, 1970" at the top right. Page number "16" at top left. This looks like a newspaper or magazine page. "HOSPITAL-TRADE" could be a section of a newspaper or a trade magazine. Let's look closer. "Theory of Emphysema Cause Raises Questions" is a headline. "Surgeon General" is another headline. "Clinic at U. of Va. Offers Health Care to Families" is another. "Antitrypsin Lack Might Increase Fertility" is another. This is clearly a newspaper or magazine page with multiple articles. Wait, "HOSPITAL-TRADE" might be the name of the publication or section. Let's check check 12.

**Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: Multiple articles, headlines, body text. Not an identifier-only page.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Typed text throughout. There is a handwritten number "00622624" at the bottom right, but it's not the majority content.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No fax header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No biographical sketch.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: "HOSPITAL-TRADE" at the top. Is this a journal? "Monday, February 2, 1970". Looks like a newspaper or trade publication. Check 6 requires a named journal with volume/issue/page range, DOI, or copyright line belonging to a journal. "HOSPITAL-TRADE" might be a section of a newspaper (like Hospital Trade News). Let's check check 12.

**Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial tables or payment demands.
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No MSDS or product specs.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck.
- Not this check.

**Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: Not a form.
- Not this check.

**Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: No correspondence headers.
- Not this check.

**Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: "HOSPITAL-TRADE" at the top center, "Monday, February 2, 1970" at the top right. Page number "16". Multiple headlines: "Theory of Emphysema Cause Raises Questions", "Surgeon General", "Clinic at U. of Va. Offers Health Care to Families", "Antitrypsin Lack Might Increase Fertility". Multi-column news typography. Bylines/datelines (e.g., "HOSPITAL-TRADE World Wide Report", "Charlotteville, Va.—", "BOSTON—"). This is clearly a newspaper or trade magazine page with editorial content.
- Matches check 12.

**Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: The content is journalistic reporting on scientific topics (emphysema, antitrypsin), not an original research write-up with methods/results narrative from a single study. It's news articles.
- Not this check.

**Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: Not an advertisement.
- Not this check.

**Conclusion:**
The page is a newspaper/magazine page with multiple articles, headlines, bylines, and multi-column typography. The header "HOSPITAL-TRADE" and date "Monday, February 2, 1970" indicate it's a published periodical. This fits `news_article`.

Let's double check check 6 vs check 12.
Check 6: "a named journal on the page plus a publication identifier... OR a formal paper or abstract in published conference proceedings". "HOSPITAL-TRADE" is likely a trade newspaper or section of a newspaper (Hospital Trade News is a known trade publication for hospital procurement). The layout is multi-column news typography with headlines and bylines. Check 12 explicitly covers "Newspaper or magazine masthead, byline, dateline, multi-column news typography...". The page has "HOSPITAL-TRADE" (masthead/section title), "Monday, February 2, 1970" (date), page number "16", and multiple news articles with datelines ("Charlotteville, Va.—", "BOSTON—"). This is definitively `news_article`.

Runner-up: scientific_publication. Ruled out because the layout is newspaper/magazine journalism (multi-column, headlines, datelines, date) rather than a formal scientific journal article with volume/issue/DOI. The content is news reporting on science, not a primary research publication.

Final label: news_article.
Confidence: 95.

---
### `rvl_cdip__scientific_publication__0006.png`
**Expected:** `scientific_publication` | **Predicted:** `news_article`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: "New Scientist 17 June 1982" is at the top. "M O N I T O R" is a large heading. Page number "772" is at the top left. "Sfoo1058" (Bates number?) at top right. This looks like a page from a magazine/newspaper. "New Scientist" is a magazine/journal. Wait, "New Scientist" is a general-audience science magazine. Let's see if it's news_article or scientific_publication.
Check 6: scientific_publication. "New Scientist" is a general news outlet/magazine, not a research journal. Wait, check 12: news_article. "New Scientist" is a magazine. Let's look at the content. "All routes are leading to the same few cancer genes". Multi-column news typography. Byline? No obvious byline, but it's an article from New Scientist.
Let's trace carefully.

Check 1: file_folder. No, lots of text.
Check 2: handwritten. No, typed.
Check 3: fax sheet. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. Does this page carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings? "New Scientist 17 June 1982". New Scientist is a magazine. Check 6 caveat: "general news outlets: a page that presents itself as a newspaper, general-magazine, or encyclopedia piece ... is news_article (check 12), not a publication". New Scientist is a general-magazine. So check 6 is not scientific_publication.
Check 7: financial document. No.
Check 8: specification. No.
Check 9: presentation. No.
Check 10: form. No.
Check 11: correspondence. No.
Check 12: news_article. "New Scientist 17 June 1982" masthead. Multi-column news typography. Article title "All routes are leading to the same few cancer genes". This is a magazine article. Check 12: "Newspaper or magazine masthead, byline, dateline, multi-column news typography... Also a magazine feature or an encyclopedia entry... from a GENERAL-AUDIENCE outlet". New Scientist is a general-audience magazine. So news_article.
Check 13: scientific_report. No, it's a magazine article.
Check 14: advertisement. No.

Let's double check Check 6 vs Check 12.
Check 6: "First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings? ... Caveat — general news outlets: a page that presents itself as a newspaper, general-magazine, or encyclopedia piece ... is news_article (check 12), not a publication".
New Scientist is a general-magazine. The page has "New Scientist 17 June 1982" and "772" (page number). This is a magazine page.
Therefore, news_article.

Let's review the evidence for news_article:
- Masthead: "New Scientist 17 June 1982"
- Page number: "772"
- Multi-column typography (3 columns)
- Article headline: "All routes are leading to the same few cancer genes"
- Section headline: "Carcinogens act on irritated tissues"
This perfectly matches Check 12: "Newspaper or magazine masthead, byline, dateline, multi-column news typography... magazine feature... from a GENERAL-AUDIENCE outlet".

Runner-up: scientific_publication. Ruled out because New Scientist is a general-audience magazine, not a research journal, and the caveat in check 6 explicitly routes general-magazine pages to news_article (check 12).

Let's confirm there's no mail header. No.
No fax header.
No form fields.
No financial data.

Final label: news_article.
Confidence: 95.
Evidence is very clear: "New Scientist 17 June 1982", page 772, 3-column layout, article text.

---

## questionnaire → scientific_report (1 errors)

### `rvl_cdip__questionnaire__0005.png`
**Expected:** `questionnaire` | **Predicted:** `scientific_report`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure and walk through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: "Bellomy Research" logo at top. "AROMA MINI GROUPS" in the middle. "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991" at bottom right. Address at bottom. Bates number "50918 7883" on the right edge. Handwritten "File Props" at top right. No newspaper/magazine masthead, no journal running head.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Content: "Bellomy Research" logo, "AROMA MINI GROUPS", "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991", address at bottom. This is a title page / cover page for a document. Not an identifier-only page.
- Not this check.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Content: Mostly typed. Handwritten "File Props" at top right. Not majority handwritten.
- Not this check.

Check 3: FAX TRANSMISSION SHEET -> form
- No fax header.
- Not this check.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- No survey questions.
- Not this check.

Check 5: PERSON'S CAREER HISTORY -> resume
- No biographical info.
- Not this check.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- No journal identifier, volume, issue, page range.
- Not this check.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- No financial data, line items, payment demand.
- Not this check.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- No MSDS, product formulation, test-analysis tables keyed to product codes, "shall/must" language.
- Not this check.

Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
- "Bellomy Research" logo, "AROMA MINI GROUPS" centered, "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991". This looks like a title page / cover page for a report or presentation. Wait, is it a presentation cover? Or a scientific_report title page?
- Let's check check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report. "A technical-study title page naming a specific experimental method/study is scientific_report (check 13)". "AROMA MINI GROUPS" sounds like a study title. "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991". Bellomy Research is an external consulting/research firm. This is likely the title page of a scientific report or technical report prepared for RJR.
- Let's re-read check 9: "Technical-study title pages: a title page naming a specific study or methodology with a date — e.g. "TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter... / November 28, 1966" — is scientific_report (check 13), not presentation, even when it is sparse or printed slide-style on a dark background".
- Here we have "AROMA MINI GROUPS" (study title), "Prepared For: R. J. REYNOLDS TOBACCO COMPANY", "November 1991" (date), "Bellomy Research" (author/affiliation). This matches the technical-study title page pattern -> scientific_report.
- Let's check check 13: "lab or technical study title page with authors and an internal affiliation and no journal identifiers." Bellomy Research is the author/affiliation. R.J. Reynolds is the client. No journal identifiers. This is a scientific_report.

Let's double check check 9 vs 13.
Check 9: "Slide/overhead layouts... a deck title or section-divider page... a near-blank cover or title page... is a presentation... EXCEPTIONS: ... a technical-study title page naming a specific experimental method/study is scientific_report (check 13)".
"AROMA MINI GROUPS" is the title of the study. "Bellomy Research" is the author. "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991". This is a title page for a technical study/report. Therefore, scientific_report.

Let's check if there's any other category.
Could it be a form? No.
Letter/memo? No.

Let's review the evidence for scientific_report (check 13):
- Title page of a technical study: "AROMA MINI GROUPS"
- Author/affiliation: "Bellomy Research"
- Client: "Prepared For: R. J. REYNOLDS TOBACCO COMPANY"
- Date: "November 1991"
- No journal identifiers.
This perfectly matches "lab or technical study title page with authors and an internal affiliation and no journal identifiers" (though Bellomy is external, it's the authoring research firm). Wait, check 13 says "internal affiliation" but also "lab or technical study title page with authors and an internal affiliation and no journal identifiers". Bellomy Research is the author. The document is a report prepared for RJR. Title pages of such reports are scientific_report.

Let's check check 9 again: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".
Yes, "AROMA MINI GROUPS" is the specific study. "November 1991" is the date. "Bellomy Research" is the author. This is a scientific_report.

Let's confirm there is no other match.
Check 1: file_folder - no, has real content (title page).
Check 2: handwritten - no.
Check 3: fax - no.
Check 4: questionnaire - no.
Check 5: resume - no.
Check 6: scientific_publication - no journal ID.
Check 7: financial - no.
Check 8: specification - no.
Check 9: presentation - exception for technical-study title page.
Check 10: form - no.
Check 11: correspondence - no.
Check 12: news_article - no.
Check 13: scientific_report - yes, technical-study title page.
Check 14: advertisement - no.

Runner-up: presentation. Ruled out because check 9 explicitly states that a technical-study title page naming a specific study or methodology with a date is scientific_report (check 13), not presentation. "AROMA MINI GROUPS" is the study title, "November 1991" is the date, "Bellomy Research" is the authoring firm.

Wait, is "AROMA MINI GROUPS" a study title? Yes, in the context of tobacco research, "mini groups" are focus groups (mini-groups). "Aroma mini groups" is a study about aroma in mini-groups. This is definitely a technical study title page.

Final label: scientific_report.
Confidence: 90.
Evidence: Title page of a technical study ("AROMA MINI GROUPS"), authoring firm ("Bellomy Research"), client ("R. J. REYNOLDS TOBACCO COMPANY"), date ("November 1991"). Check 9 exception routes technical-study title pages to check 13 (scientific_report).

---

## scientific_report → scientific_publication (1 errors)

### `rvl_cdip__scientific_report__0009.png`
**Expected:** `scientific_report` | **Predicted:** `scientific_publication`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the mandatory pre-scan and the 14 checks in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: There is a header "HR3651-239" and "CARB" at the top right. There is a section header "MONDAY AFTERNOON - GENERAL (CONTINUED) - C. RAINER P. READING". This looks like a conference program or abstract book. Let's look closer.
Wait, "HR3651-239" and "CARB" might be Bates numbers or archive IDs.
The text contains numbered abstracts: "7. A SHORT SYNTHESIS OF 1-DEOXYFUJIMYCIN...", "8. SYNTHESIS OF 3-O-(2-ACETINO-3,4,6-TRI-O-ACETYL-2-DEOXY-B-D-GLUCOPYRANOSYL)-2,4,6-TRI-O-ACETYL-B-D-GALACTOPYRANOSYL BROMIDE...", "9. SYNTHESIS OF A CLOSE ANALOG OF THE REPEATING UNIT OF THE ANTHRACELL GLYCOPROTEINS OF ANTARCTIC FISH...".
These are scientific abstracts from a conference or symposium.
Let's check the checks.

Check 1: file_folder. No, there is real content (abstracts).
Check 2: handwritten. No, typed.
Check 3: fax sheet. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. Does this page carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings?
"HR3651-239" and "CARB" at the top right. "MONDAY AFTERNOON - GENERAL (CONTINUED) - C. RAINER P. READING".
This looks like a page from a conference proceedings or abstract book (e.g., ACS meetings, or similar chemical society meeting). "CARB" might be a section code (Carbohydrate Chemistry?).
Wait, check 6: "First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings? If yes... Evidence for this check: a named journal on the page plus a publication identifier... OR a formal paper or abstract in published conference proceedings: a named conference/symposium/tagungsband with a year, a titled, authored paper or abstract with an affiliation, and (usually) a page number."
Here we have abstracts with titles, authors, and affiliations:
"7. A SHORT SYNTHESIS OF 1-DEOXYFUJIMYCIN WITH A FLUORINE OXIDATION AS THE CRITICAL REACTION STEP. S. Franz, W. Kobernigg, P. Szakal, Dr. Alexander P. Studer, Bayer AG, Post-TASCH, 6350 Mainaustrasse 1, Germany."
"8. SYNTHESIS OF ... Saeed A. Abbas and Khushi L. Mitter, Department of Carbohydrate Chemistry, Roswell Park Memorial Institute, 200 Elm St., Buffalo, New York 14263."
"9. SYNTHESIS OF A CLOSE ANALOG ... M. Laurence Anderson and A. K. M. Abulazizan, Department of Biochemistry, University of Wisconsin, Madison, WI 53706."
This is a page from published conference proceedings (abstracts). It has a named conference/symposium section ("MONDAY AFTERNOON - GENERAL (CONTINUED) - C. RAINER P. READING"), titled authored papers/abstracts with affiliations.
Wait, is this scientific_publication or scientific_report?
Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report. "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... A lab or technical study title page with authors and an internal affiliation and no journal identifiers."
These are abstracts from a conference. Conference abstracts in proceedings are scientific_publication (check 6: "a formal paper or abstract in published conference proceedings: a named conference/symposium/tagungsband with a year, a titled, authored paper or abstract with an affiliation, and (usually) a page number.").
Wait, what about the header "HR3651-239" and "CARB"? "CARB" could be the section (Carbohydrates). "HR3651-239" is likely a Bates number or internal archive ID.
Let's re-read check 6: "a formal paper or abstract in published conference proceedings: a named conference/symposium/tagungsband with a year, a titled, authored paper or abstract with an affiliation, and (usually) a page number."
The page has abstracts 7, 8, 9. They have titles, authors, affiliations. This is typical of a conference abstract book (e.g., ACS National Meeting abstracts).
Is there a journal name? No. But check 6 says: "OR a formal paper or abstract in published conference proceedings: a named conference/symposium/tagungsband with a year, a titled, authored paper or abstract with an affiliation, and (usually) a page number."
Wait, does it have a named conference? "MONDAY AFTERNOON - GENERAL (CONTINUED) - C. RAINER P. READING". This is a session heading.
Let's consider scientific_report (check 13). "A lab or technical study title page with authors and an internal affiliation and no journal identifiers." But these are abstracts, not a full report.
Actually, abstract books from conferences are considered scientific_publication if they are published proceedings.
Wait, let's look at the content. It's a list of abstracts.
Is there any other check?
Check 13: "Original research write-up -> scientific_report. Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries ... is a filled form ... not a scientific report." These are abstracts, which are short narrative prose. But they are abstracts from a conference.
Let's re-read check 6 carefully: "Evidence for this check: a named journal on the page plus a publication identifier ... OR a formal paper or abstract in published conference proceedings: a named conference/symposium/tagungsband with a year, a titled, authored paper or abstract with an affiliation, and (usually) a page number."
Do we have a named conference? The text doesn't explicitly name the conference in the visible part, except maybe "CARB" (Carbohydrate Chemistry symposium?). "HR3651-239" is probably a Bates number.
Wait, what if it's scientific_report? "A lab or technical study title page with authors and an internal affiliation and no journal identifiers." These are not title pages, they are abstracts.
Let's look at the structure. It's a page from a conference program/abstract book.
Often, these are classified as scientific_publication if they are from published proceedings.
Wait, what if the document is just a scientific_report because it's a collection of abstracts from an internal meeting? "C. RAINER P. READING" - Rainer P. Studer? No, "C. RAINER P. READING" might be the session chair.
Actually, let's look at the text: "MONDAY AFTERNOON - GENERAL (CONTINUED) - C. RAINER P. READING"
This is definitely a conference session.
Is it scientific_publication or scientific_report?
If it's an internal meeting abstract book, it might be scientific_report. But check 6 says "published conference proceedings".
Let's check if there's any other category.
Could it be presentation? No.
Could it be form? No.

Let's re-evaluate check 6 vs 13.
Check 6: "a formal paper or abstract in published conference proceedings: a named conference/symposium/tagungsband with a year, a titled, authored paper or abstract with an affiliation, and (usually) a page number."
Check 13: "Original research write-up -> scientific_report. Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... A lab or technical study title page with authors and an internal affiliation and no journal identifiers."

If this is a page from a published conference abstract book (like ACS meetings), it's scientific_publication. The header "CARB" likely stands for the Carbohydrate Chemistry symposium. "HR3651-239" is a Bates number from the tobacco archive (HR = Health Research? or similar).
Wait, "CARB" is at the top right, next to "HR3651-239". This is typical of Bates-numbered pages from a large archive, where "CARB" might be a document type or section code, or it's part of the original document's header.
Actually, in tobacco archives, "CARB" could be a file folder or section name, but here it's in the header.
Wait, look at the first paragraph: "is used to collect three spectra,* the intensities and phases of which are dependent on the number of protons attached to each 13C nucleus. Linear combinations of these spectra then yield three subspectra in which the 13C signals of different nitrogen types are isolated. For example, separate MR, NH2, and NH subspectra have been obtained for the antibiotic lipostreptin, produced in trifluoroacetic acid solution. *The spectra were recorded at the High Field NMR Facility of the National Measurement Laboratory, National Bureau of Standards."
This is the continuation of abstract 6 (not shown).
Then abstract 7, 8, 9.
This is a page from a conference abstract book. Conference abstracts are published in proceedings. Thus, scientific_publication.
Wait, is there any chance it's scientific_report? "A technical/project status report whose content is primarily technical...". No, this is abstracts.
What about "scientific_publication"? "a formal paper or abstract in published conference proceedings: a named conference/symposium/tagungsband with a year, a titled, authored paper or abstract with an affiliation, and (usually) a page number."
We have titled, authored papers/abstracts with affiliations. We have a session heading "MONDAY AFTERNOON - GENERAL (CONTINUED) - C. RAINER P. READING". This implies a conference schedule.
I will classify this as scientific_publication.

Wait, let's look at the label options:
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification

If I'm not sure about the conference name, could it be scientific_report?
"Requires running prose — a page that is only labeled field-value entries ... is a filled form ... not a scientific report."
These abstracts have running prose (methods, results). But they are abstracts.
Usually, abstract books from conferences are considered scientific_publication if they are published proceedings. If it's an internal document, it might be scientific_report. But the format (numbered abstracts, session headings, author affiliations) is exactly that of a published conference abstract book (e.g., ACS National Meeting).
I'll go with scientific_publication.

Let's double check check 6 evidence:
- "a formal paper or abstract in published conference proceedings: a named conference/symposium/tagungsband with a year, a titled, authored paper or abstract with an affiliation, and (usually) a page number."
Evidence: Numbered abstracts (7, 8, 9) with titles ("A SHORT SYNTHESIS OF...", "SYNTHESIS OF...", "SYNTHESIS OF A CLOSE ANALOG..."), authors (S. Franz et al., Saeed A. Abbas et al., M. Laurence Anderson et al.), and affiliations (Bayer AG, Roswell Park Memorial Institute, University of Wisconsin). Session heading "MONDAY AFTERNOON - GENERAL (CONTINUED) - C. RAINER P. READING". This is a page from published conference proceedings (abstract book).

Is there any journal identifier? "HR3651-239" and "CARB". "CARB" might be the symposium name (Carbohydrate Chemistry).
I'm confident in scientific_publication.

Wait, what if it's scientific_report because it's just a collection of abstracts without a clear conference name?
Check 13: "Original research write-up -> scientific_report. Running narrative prose with objectives, methods, results, or discussion... A lab or technical study title page with authors and an internal affiliation and no journal identifiers."
These are not title pages, they are abstracts. Abstracts are not full research write-ups. They are published in proceedings. Check 6 explicitly covers "a formal paper or abstract in published conference proceedings".
I will use scientific_publication.

Let's review the scratchpad requirements:
- Walk checks 1-14 in order.
- State evidence or "not this check".
- Stop at first matching check.
- Add final line naming runner-up and evidence that ruled it out.

Check 1: file_folder. Evidence: none. (has real content)
Check 2: handwritten. Evidence: none. (typed)
Check 3: fax sheet. Evidence: none.
Check 4: questionnaire. Evidence: none.
Check 5: resume. Evidence: none.
Check 6: scientific_publication. Evidence: "a formal paper or abstract in published conference proceedings: a named conference/symposium/tagungsband with a year, a titled, authored paper or abstract with an affiliation, and (usually) a page number." Page contains numbered abstracts (7, 8, 9) with titles, authors, and affiliations (e.g., "S. Franz, W. Kobernigg... Bayer AG", "Saeed A. Abbas... Roswell Park Memorial Institute"), under a session heading "MONDAY AFTERNOON - GENERAL (CONTINUED) - C. RAINER P. READING". This matches the definition of abstracts in published conference proceedings.
Stop here.

Runner-up: scientific_report. Ruled out because the page contains formal abstracts from a conference session (indicated by the session heading and numbered abstracts with author affiliations), which falls under published conference proceedings (check 6), rather than being an original research write-up or internal technical report (check 13).

Let's refine the evidence for check 6:
"MONDAY AFTERNOON - GENERAL (CONTINUED) - C. RAINER P. READING" indicates a conference session. Abstracts 7, 8, 9 have titles, authors, and institutional affiliations (Bayer AG, Roswell Park Memorial Institute, University of Wisconsin). This matches "a formal paper or abstract in published conference proceedings... a titled, authored paper or abstract with an affiliation".

Confidence: 85. (Strong evidence for conference abstracts, but the exact conference name isn't fully explicit beyond "CARB" and the session heading, though the format is unmistakably a published abstract book).

Wait, I should check if there's any other possibility.
Could it be a specification? No.
Could it be a form? No.

Let's write the scratchpad.
<scratchpad>
file_folder: no — page contains multiple numbered abstracts with full text, titles, authors, and affiliations.
handwritten: no — typed throughout.
fax sheet: no.
questionnaire: no.
resume: no.
scientific_publication: yes — page contains numbered abstracts (7, 8, 9) with titles, authors, and institutional affiliations (e.g., "S. Franz... Bayer AG", "Saeed A. Abbas... Roswell Park Memorial Institute") under a session heading "MONDAY AFTERNOON - GENERAL (CONTINUED) - C. RAINER P. READING". This matches the check 6 definition for "a formal paper or abstract in published conference proceedings... a titled, authored paper or abstract with an affiliation".
Runner-up: scientific_report, ruled out because the content is a set of formal conference abstracts with a session heading and author affiliations, which fits published conference proceedings (check 6) rather than an original research write-up or internal technical report (check 13).
</scratchpad>
<label>scientific_publication</label>
<confidence>85</confidence>

---

## handwritten → form (1 errors)

### `rvl_cdip__handwritten__0006.png`
**Expected:** `handwritten` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: None. Just a Bates number "50935 3477" on the right edge.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Content: "BLEND COMBINATIONS BY G13 TYPE", "G13-22", "G4-KDN", "Card No. NAME", "150 84 VANTAGE UL M 100", "KDN ONLY", "132 231 NEW BS 100*", "G13-14", "G4-KDN", "214 26 WINSTON LT BS", "G13-5", "KDN ONLY", "167 8 NOT LISTED", "INTERNATIONAL - NO G13", "KDN ONLY", "G4-KDN", "NO KDN/G4 M2".
- This has real content, a title "BLEND COMBINATIONS BY G13 TYPE", and tabular data. Not file_folder.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Content: The page has a printed ruled table/template with column headers like "Card No.", "NAME", and rows filled with handwritten text ("G13-22", "G4-KDN", "150", "84", "VANTAGE UL M 100", "KDN ONLY", "132", "231", "NEW BS 100*", etc.).
- Wait, is it majority handwritten? The text is handwritten, but it's filling in a printed structured form (ruled lines, column headers "Card No.", "NAME").
- Check 2 says: "It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form (or the content's own category...)"
- So this is not handwritten. It's a filled form.

Check 3: FAX TRANSMISSION SHEET -> form
- No fax header.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Not a survey instrument.

Check 5: PERSON'S CAREER HISTORY -> resume
- Not a resume.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- No journal masthead or running head.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- No financial content, no payment demand, no budget table.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- "BLEND COMBINATIONS BY G13 TYPE". G13 is a cigarette testing machine (Gardner or similar? Actually G13 is a cigarette smoking machine or blend testing).
- Wait, is this a specification? "test-analysis tables keyed to product/part codes... A labeled product/parameter rate-data chart... is a specification".
- But this is a handwritten log of blend combinations. Let's look at check 10.

Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
- Not a slide deck.

Check 10: ADMINISTRATIVE FORM -> form
- "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
- The page has a printed ruled table with headers ("Card No.", "NAME") and handwritten entries filling the cells. This is a filled form capturing factual data (blend combinations by G13 type).
- Let's check if there's a stronger category.
- Is it a scientific_report? "Requires running narrative prose... a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report." This page has no running narrative prose, just a table filled with handwritten data.
- Is it a specification? "A quality-check sheet, lab measurement log, or product-test data table that merely RECORDS measurements about a product is a form, not specification — it captures data rather than defining requirements." This page records blend combinations (data), it doesn't define requirements/tolerances. So it's a form.

Check 11: CORRESPONDENCE -> email, memo, or letter
- No correspondence structure.

Check 12: PUBLISHED JOURNALISM -> news_article
- No.

Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report
- No running narrative prose.

Check 14: PROMOTIONAL MATERIAL -> advertisement
- No.

Let's re-evaluate Check 2 vs Check 10.
Check 2: "handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form". The page has printed ruled lines, column headers ("Card No.", "NAME"), and handwritten entries. This is a filled form.
Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
This perfectly matches Check 10.

Let's double check if there's any other category.
"BLEND COMBINATIONS BY G13 TYPE"
"G13-22", "G4-KDN", "Card No. NAME", "150 84 VANTAGE UL M 100"
"KDN ONLY", "132 231 NEW BS 100*"
"G13-14", "G4-KDN", "214 26 WINSTON LT BS"
"G13-5", "KDN ONLY", "167 8 NOT LISTED"
"INTERNATIONAL - NO G13", "KDN ONLY", "G4-KDN", "NO KDN/G4 M2"
This is a log/table of blend combinations. It's a form used to record data.

Could it be scientific_report? "A technical/project status report whose content is primarily technical... even when it embeds a budget-vs-actual cost section". But this is just a data table. "Requires running narrative prose... a page that is only labeled field-value entries... is a filled form". No narrative prose here.

Could it be specification? "A product-referenced test data table... is a specification." But the calibration says: "A quality-check sheet, lab measurement log, or product-test data table that merely RECORDS measurements about a product is a form, not specification — it captures data rather than defining requirements." This page records blend combinations (data), not defining requirements. So form is correct.

Let's review the evidence for form:
- Printed ruled lines and column headers ("Card No.", "NAME").
- Handwritten entries filling the cells ("G13-22", "G4-KDN", "150", "84", "VANTAGE UL M 100", etc.).
- Title "BLEND COMBINATIONS BY G13 TYPE".
- Captures factual data in a structured table.

Runner-up: scientific_report (ruled out because there is no running narrative prose, only labeled field-value entries in a table).
Another runner-up: specification (ruled out because it records data rather than defining product requirements/tolerances).

Let's confirm the label: form.
Evidence: printed ruled table with headers "Card No.", "NAME", filled with handwritten data recording "BLEND COMBINATIONS BY G13 TYPE". Check 10 explicitly covers filled forms with handwriting in cells.

Final check of the scratchpad steps:
1. file_folder: no, has real content and table.
2. handwritten: no, handwriting fills printed structured form.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial: no.
8. specification: no, records data, doesn't define requirements.
9. presentation: no.
10. form: yes, filled ruled table with headers and handwritten data.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no, no narrative prose.
14. advertisement: no.

Label: form.
Confidence: 95.
Evidence is clear: printed ruled lines, column headers, handwritten data filling the cells. Check 10 explicitly states "a filled form recording data is still a form, including handwriting in its cells."

---

## handwritten → advertisement (1 errors)

### `rvl_cdip__handwritten__0003.png`
**Expected:** `handwritten` | **Predicted:** `advertisement`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

**Pre-scan:**
- Mail-client header block: None.
- Masthead or running head: None. There's a 7-Eleven logo, Camel Winston ad, and a check/payment stub. No newspaper/magazine masthead, no journal running head.

**Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a lot of content: an ad, a check, handwritten notes. Not identifier-only.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: There is some handwritten text ("Please remove, Addressee is deceased. Died of smoking-related illness on 11/15/98."), but the majority of the page is blank white space, with a printed ad and a printed check/payment stub in the bottom right quadrant. Not majority handwritten.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey instrument.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No resume content.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal masthead, volume, issue, etc.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: There is a check/payment stub. "P.O. Box 834039", "52273 9120", "PAID", "Change Service Requested". It's a check stub or a payment remittance advice. Wait, let's look closer.
- The bottom right has a check-like element: "P.O. Box 834039", "52273 9120", "PAID", "Change Service Requested".
- There is also a 7-Eleven / Camel Winston coupon/ad: "$3.50 off a carton, 35¢ off a pack".
- Wait, is this an invoice? No payment demand.
- Is it a budget? No.
- Let's look at the remaining checks.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No MSDS, no product formulation.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: No slide deck.
- Not this check.

**Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: Not a form.

**Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: No.

**Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: No.

**Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: No.

**Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: The dominant printed content in the bottom right is a 7-Eleven / Camel Winston advertisement/coupon. "$3.50 off a carton", "35¢ off a pack", "CAMEL WINSTON", "7-ELEVEN". There's also a check stub attached to it, and handwritten notes about the addressee being deceased.
- Wait, the page is mostly blank white space. The content is an advertisement (coupon) and a check stub.
- Let's re-read Check 14: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content... a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page..."
- The printed content is a coupon/advertisement for Camel Winston cigarettes at 7-Eleven. It has the Surgeon General warning ("THIS IS NOT A COUPON See other side for details", "WARNING: CIGARETTE SMOKING DANGEROUS TO HEALTH...").
- The handwritten note is about the addressee.
- The check stub is a payment remittance.
- Is the dominant content an advertisement? Yes, the printed graphic is a coupon/advertisement.
- Wait, what about the check? A check is a financial document. But the check is just a stub attached to the ad? "P.O. Box 834039", "52273 9120", "PAID". It looks like a mail-order coupon response or a check sent with a coupon.
- Actually, look at the text: "#BANKSUD AUTO ************ S-DIGIT 94550", "#2032000456-211374#", "NANCY EVERITT", "2705 SUPERIOR DR", "LIVERMORE CA 94550-6615". This is a check stub / remittance advice.
- But the top part is a 7-Eleven / Camel Winston coupon.
- Is this an advertisement? "coupons, flyers, brochures". Yes, a coupon is an advertisement.
- Let's check if there's any other category.
- What about "form"? No.
- What about "invoice"? No payment demand for goods provided by the sender; it's a coupon for a discount.
- What about "budget"? No.

Let's look closely at the image.
The image is rotated 90 degrees counter-clockwise.
If I rotate it 90 degrees clockwise:
Top right (now top left): 7-Eleven logo, "$3.50 off a carton", "35¢ off a pack", "CAMEL WINSTON", "THIS IS NOT A COUPON See other side for details".
Bottom right (now bottom left): Check stub / remittance advice. "P.O. Box 834039", "52273 9120", "PAID", "Change Service Requested". Address: "NANCY EVERITT", "2705 SUPERIOR DR", "LIVERMORE CA 94550-6615". Handwritten note: "Please remove, Addressee is deceased. Died of smoking-related illness on 11/15/98."

The page is essentially a scanned coupon/advertisement with a check stub attached and a handwritten note.
The dominant printed content is the advertisement/coupon.
Check 14: "PROMOTIONAL MATERIAL -> advertisement. Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."
The page contains a coupon for Camel Winston cigarettes. It has brand styling, slogans ("$3.50 off a carton"), and a Surgeon General warning.
Therefore, it is an advertisement.

Wait, is there any other check?
Check 7: "invoice: a bill for goods or services provided... A payment voucher naming a payee with 'AMOUNT'/'PAY THIS AMOUNT' is invoice."
The check stub doesn't have an amount due or payment demand. It's a remittance advice or check stub. "PAID" is stamped on it. It's not an invoice.

Check 14 is the best fit. The page is a coupon/advertisement (with a check stub and handwritten note). The dominant printed layout is the advertisement.

Let's double check Check 14 definition:
"Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content (see check 12): a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page with a running masthead and some surrounding text."

The page has a 7-Eleven / Camel Winston coupon. It is an advertisement.

Let's review the scratchpad steps:
1. file_folder: no, has content.
2. handwritten: no, mostly blank with printed ad and check.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial: no, check stub is not an invoice or budget. No payment demand.
8. specification: no.
9. presentation: no.
10. form: no.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no.
14. advertisement: yes, coupon with brand styling, slogans, Surgeon General warning.

Runner-up: form (because of the check stub fields), ruled out because check 14 explicitly covers coupons and the dominant printed content is the advertisement.
Another runner-up: invoice, ruled out because there is no payment demand, just a "PAID" check stub and a coupon.

Final label: advertisement.
Confidence: 85.
The page is clearly a scanned coupon/advertisement (Camel Winston at 7-Eleven) with a check stub and a handwritten note. The dominant printed content is the advertisement.

---

## budget → invoice (1 errors)

### `rvl_cdip__budget__0014.png`
**Expected:** `budget` | **Predicted:** `invoice`

*No reasoning text captured.*

---

## budget → form (1 errors)

### `rvl_cdip__budget__0013.png`
**Expected:** `budget` | **Predicted:** `form`

*No reasoning text captured.*

---

## budget → scientific_report (1 errors)

### `rvl_cdip__budget__0007.png`
**Expected:** `budget` | **Predicted:** `scientific_report`

*No reasoning text captured.*

---

## invoice → letter (1 errors)

### `rvl_cdip__invoice__0003.png`
**Expected:** `invoice` | **Predicted:** `letter`

*No reasoning text captured.*

---

## questionnaire → handwritten (1 errors)

### `rvl_cdip__questionnaire__0016.png`
**Expected:** `questionnaire` | **Predicted:** `handwritten`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.

Let's look at the document:
- Top: "79-0414" (handwritten)
- Middle: "Lab plan & Questionnaire" (handwritten)
- Bottom right: "50130 8150" (printed, vertical) and a handwritten "1" or "S".
- The page is mostly blank with handwritten text.

Let's go through the checks:

1. IDENTIFIER-ONLY PAGE -> file_folder
- Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card.
- Wait, the text is "79-0414", "Lab plan & Questionnaire". This is a short label. Is it a folder tab? No, it's handwritten on a blank page.
- Wait, check 1 says: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
- Is this a note? "Lab plan & Questionnaire". It's a handwritten note.
- Let's check check 2: HANDWRITTEN PAGE.

2. MAJORITY-HANDWRITTEN PAGE -> handwritten
- Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template.
- The page has "79-0414", "Lab plan & Questionnaire" handwritten.
- Is it a filled form? No printed template.
- Is it a note? Yes, a handwritten note.
- Check 2: "Most of the content is freeform handwriting... NOT on a printed template."
- "The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
- This page is freeform handwriting on blank paper.
- So it matches handwritten.

Wait, is there any other check?
- Check 4: questionnaire. "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing (e.g. "Revised questionnaire to be used VIII-IV. Revisions highlighted in VIII file. CPP questionnaire was not changed.") is a transmittal note for the instrument — questionnaire (check 4), even though it is freeform handwriting on blank paper."
- Wait! "Lab plan & Questionnaire" is a note ABOUT a questionnaire? Or is it the title of a document?
- Let's re-read check 4: "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing ... is a transmittal note for the instrument — questionnaire (check 4), even though it is freeform handwriting on blank paper."
- "Lab plan & Questionnaire" sounds like a title or a note indicating the contents of a folder or a section. "79-0414" is an ID. "Lab plan & Questionnaire" is a label.
- Wait, if it's a folder tab or a section divider?
- Check 1: file_folder. "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB ... bearing a short filing label that names the folder's contents ... The label IS filing metadata — its only job is to identify the folder — so it is NOT a 'topical title' for this check. The page stays file_folder even when the label is rotated 90 degrees..."
- But this is handwritten on a blank page, not a photograph of a folder tab.
- Wait, what about check 9: presentation. "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note ... is a presentation (this check), not file_folder (check 1)." But this is handwritten.
- Check 2 says: "Most of the content is freeform handwriting ... This wins over a typed letter or memo layout. ... A typed page with only a signature, stamp, or margin note is not handwritten."
- Here, the page IS handwritten. "79-0414", "Lab plan & Questionnaire".
- Is it a handwritten note? Yes.
- Let's re-read check 2 carefully: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout. ... A log/diary sheet is freeform, not a form: ... A handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
- What about "Notes ABOUT a survey instrument are questionnaire, not handwritten"? "a handwritten note about a questionnaire's revision, distribution, or routing ... is a transmittal note for the instrument — questionnaire (check 4)".
- "Lab plan & Questionnaire" is not really a note about a questionnaire's revision, distribution, or routing. It's just a label: "Lab plan & Questionnaire". It's likely a cover page or a note indicating what's inside a file.
- If it's just a handwritten label on a blank page, it's handwritten.
- Wait, could it be file_folder? "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only." A handwritten note "Lab plan & Questionnaire" is a note. So it's not file_folder.
- Is it a questionnaire? No, it doesn't ask the reader to answer.
- Is it a form? No.
- Is it a memo/letter? No.

Let's look at the text again:
"79-0414"
"Lab plan &"
"Questionnaire"
"50130 8150" (printed, vertical, bottom right)
"1" (handwritten, bottom right)

This looks like a handwritten note or label on a blank page, possibly a cover sheet or a note indicating the contents of a file (Lab plan & Questionnaire, ID 79-0414).
Since it's freeform handwriting on blank paper with no printed template, it falls under check 2: handwritten.

Wait, is there any possibility it's a form? No printed fields.
Is it a file_folder? "Pure filing metadata only." But it has a handwritten note "Lab plan & Questionnaire". Check 1 says: "A page is NOT file_folder if it carries any real content — ... or a note." So a handwritten note makes it NOT file_folder.
Thus, check 2 (handwritten) is the correct match.

Let's double check check 4: "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing (e.g. "Revised questionnaire to be used VIII-IV. Revisions highlighted in VIII file. CPP questionnaire was not changed.") is a transmittal note for the instrument — questionnaire (check 4), even though it is freeform handwriting on blank paper."
"Lab plan & Questionnaire" is not a note about a questionnaire's revision, distribution, or routing. It's just a title/label. So check 4 does not apply.

Therefore, the document is handwritten.

Evidence for check 2: The page consists almost entirely of freeform handwriting ("79-0414", "Lab plan & Questionnaire") on blank paper with no printed template, fields, or boxes.
Evidence against check 1: The page contains a handwritten note ("Lab plan & Questionnaire"), which is real content, so it is not pure filing metadata (file_folder).
Evidence against check 4: The text is a simple label/title, not a note about a questionnaire's revision, distribution, or routing.

Final label: handwritten.
Confidence: 95.

---

## questionnaire → file_folder (1 errors)

### `rvl_cdip__questionnaire__0010.png`
**Expected:** `questionnaire` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.

Pre-scan:
- Mail-client header block: None.
- Masthead or running head: None. Just a title "GMR MARKETING QUESTIONS REGARDING BID RESPONSE" and a Bates number "2083156178" rotated on the right side.

Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Evidence: The page has a title "GMR MARKETING QUESTIONS REGARDING BID RESPONSE" and multiple sections with bullet points (Region Managers, Event Staffing, Training, Talent Salaries, Floating Clubs, Vehicle Rental, Agency Travel). It has real content, not just an ID.
- Not this check.

Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- Evidence: The page is typed. No majority handwriting.
- Not this check.

Check 3: FAX TRANSMISSION SHEET -> form
- Evidence: No "FACSIMILE" or fax header. The rotated text "2083156178" is a Bates number.
- Not this check.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
- Evidence: The title is "GMR MARKETING QUESTIONS REGARDING BID RESPONSE". It asks questions to Region Managers about a bid response (estimates, staffing, training, etc.). Wait, is this a questionnaire? "questions regarding bid response" - it's a list of questions/comments about a bid. Let's look at check 11 (correspondence) or check 10 (form) or check 13 (scientific_report - no).
- Actually, this looks like a memo or a letter with questions. Let's check 11.

Check 5: PERSON'S CAREER HISTORY -> resume
- Evidence: No.

Check 6: PUBLISHED EVIDENCE -> scientific_publication
- Evidence: No journal masthead.

Check 7: FINANCIAL DOCUMENT -> invoice or budget
- Evidence: Mentions "$4,000 weekly fee", "15.95%", "Agency travel estimate is very high". But it's not a line-item table, ledger, or payment demand. It's a document asking questions about a bid response.
- Not this check.

Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification
- Evidence: No.

Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
- Evidence: Not a slide deck.

Check 10: ADMINISTRATIVE FORM -> form
- Evidence: No fill-in fields, checkboxes, or ruled entry lines. It's a typed list of questions/bullet points.

Check 11: CORRESPONDENCE -> email, memo, or letter
- Evidence: The document is titled "GMR MARKETING QUESTIONS REGARDING BID RESPONSE". It has sections like "Region Managers", "Event Staffing", etc., with bullet points containing questions and comments (e.g., "You have proposed 5 Region Managers. How do you envision dividing their responsibilities?", "Estimates are well above expectations. Please reevaluate need for talent coordinators...").
- Is it a memo? It lacks a TO:/FROM:/RE:/DATE: header block. Wait, check 11 says: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
- "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person..."
- This page has none of those. It's just a list of questions.
- Wait, what about check 4? "questionnaire: The page asks the reader to answer, rate, choose, or commit... A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument... Also counts: instructions or directions given to product-test/consumer-test participants..."
- This is "QUESTIONS REGARDING BID RESPONSE". It's a list of questions sent to someone (likely a vendor or agency) regarding their bid. Is it a questionnaire? No, a questionnaire is a survey instrument. This is a transmittal or a set of questions for a bid response.
- Let's re-read check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels"
- This page has no TO/FROM/RE header, no salutation, no closing. It's just a list of bullet points under headings.
- Could it be a form? "A form does NOT have to be blank — a filled form recording data is still a form... This also covers: a standalone labeled data chart or table... internal authorization/approval forms..." No, it's not a form.
- Let's look at the labels again: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
- What if it's a memo? Sometimes memos don't have the strict header if it's just a list of questions. But the rules say: "Without that header-then-prose structure it is not a memo."
- Wait! Look at the content: "GMR MARKETING QUESTIONS REGARDING BID RESPONSE". It's a document asking questions. Is it a questionnaire? "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey." This is asking for answers to questions about a bid. But it's not a survey instrument.
- Let's reconsider check 10: form. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank... internal authorization/approval forms with an approval signature/date block." Not a form.
- What about check 13: scientific_report? "Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries... is a filled form". This is bullet points, not narrative prose.
- Let's re-evaluate check 11 (memo). Is there a TO/FROM/RE header? No.
- Is there a letter structure? No.
- Is there an email header? No.
- Could it be a presentation? "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page..." This has bullet lists under headings. "GMR MARKETING QUESTIONS REGARDING BID RESPONSE" is a title. Sections: Region Managers, Event Staffing, Training, Talent Salaries, Floating Clubs, Vehicle Rental, Agency Travel. This looks like a slide deck or a presentation document! "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page...". But it's a single page with text.
- Wait, what about "questionnaire"? "The page asks the reader to answer...". This page asks questions: "How do you envision dividing their responsibilities?", "Are Region Mangers third party staff?", "Please provide a total cost...", "Will surveyors... be trained together?", "How long is the surveyor training?", "What does $4,000 in talent cover?", "Please verify what is included...", "Why do we have a driver...", "What is the purpose of additional vehicle rental...", "Please rethink number of trips...". These are questions directed at the bidder. Is this a questionnaire? "A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument... Also counts: instructions or directions given to product-test/consumer-test participants". This is not a survey instrument. It's a list of questions for a bid response.
- Let's look at check 7: budget. "budget: internal money planning, tracking, or disbursement WITHOUT demanding payment. Budget includes: expense reports, forecast-vs-actual, a statement of account, a check face/check stub, a check register, a financial/money-data table, a handwritten list of expenses, a campaign-contribution/expenditure statement, or a money-only REQUEST/CHECKLIST/STATEMENT." This document is a "REQUEST/CHECKLIST/STATEMENT" about money? "Agency travel estimate is very high. Please rethink number of trips..." It's questioning a bid. Not really a budget.
- Let's look at check 10 again: form. "administrative form... capturing factual data". Not really.
- What about memo? "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels". This page has no date, no named person, no internal title.
- Is it a letter? No.
- Is it a file_folder? No.
- Let's reconsider the content. It's a list of questions and comments regarding a bid response from GMR Marketing. This is likely a memo or a letter. But strictly, it lacks the headers.
- Wait! Look at the prompt: "A page whose primary structure is a memo header + prose, but whose prose merely discusses, forwards, or requests approval of an invoice/bill... stays memo". This doesn't have a memo header.
- What if it's a "questionnaire"? "The page asks the reader to answer, rate, choose, or commit... open-response lines". The page has open-response lines (the bullet points are essentially open-response questions). But it's not a survey instrument.
- Let's re-read check 4: "questionnaire: The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey. A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument (e.g. 'APPENDIX 1' of a questionnaire, a handwritten note about a revised questionnaire) is still questionnaire, not file_folder."
- This is a list of questions. Is it a questionnaire? "QUESTIONS REGARDING BID RESPONSE". It's asking the vendor to answer these questions. This fits "asks the reader to answer... open-response lines". But is it a "survey instrument"? Usually, a questionnaire is a survey. This is a bid response questionnaire. Yes! A document asking a vendor to answer questions regarding a bid is a questionnaire (or bid response form). "The page asks the reader to answer... open-response lines". The bullet points are open-response lines.
- Let's check if there's any other category. "form": "administrative form... capturing factual data". A bid response form is a form. But check 4 says "questionnaire... asks the reader to answer... open-response lines". A bid response with questions is a questionnaire.
- Wait, what about "memo"? Often, internal documents with bullet points like this are memos. But without TO/FROM/RE, it's hard to classify as memo.
- Let's look at the title: "GMR MARKETING QUESTIONS REGARDING BID RESPONSE". This is a document sent to GMR Marketing (or from GMR Marketing) with questions. If it's sent to GMR Marketing, it's a questionnaire asking them to answer. "You have proposed 5 Region Managers. How do you envision dividing their responsibilities?" -> asking GMR to answer. "Please reevaluate need for talent coordinators..." -> asking GMR to respond. This is a questionnaire (a set of questions for the bidder to answer).
- Let's check check 4 again: "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines...". The bullet points are open-response lines. "How do you envision...", "Are Region Mangers third party staff?", "Please provide a total cost...", "Will surveyors... be trained together?", "How long is the surveyor training?", "What does $4,000 in talent cover?", "Please verify what is included...", "Why do we have a driver...", "What is the purpose...", "Please rethink number of trips...". These are all questions or requests for information directed at the reader (the bidder). This perfectly matches "asks the reader to answer... open-response lines".
- Is it a form? "A form does NOT have to be blank — a filled form recording data is still a form...". But check 4 precedes check 10. "questionnaire (this check), not a form". So if it's a questionnaire, it's not a form.
- Is it a memo? A memo requires a TO:/FROM:/RE:/SUBJECT: header block or a dated internal note addressed to a named person. This page has neither. So it's not a memo by the strict rules.
- Therefore, questionnaire is the best fit. The document is a set of questions for the bidder to answer (open-response lines).

Let's double check check 4 vs check 10.
Check 4: questionnaire. "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines...". The page is literally titled "QUESTIONS REGARDING BID RESPONSE" and contains a list of questions. The reader (the bidder) is expected to answer these questions. This is a questionnaire.
Check 10: form. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This page has bullet points, not ruled entry lines or boxes. It's a list of questions.

Let's double check check 11: memo.
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
"A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels"
This page has no date, no named person, no TO/FROM/RE. So it fails the memo check.

Let's double check check 7: budget.
"budget: internal money planning... or a money-only REQUEST/CHECKLIST/STATEMENT."
This document is a request/checklist about a bid, but it's primarily a set of questions (questionnaire). The financial content is just part of the questions ("Estimates are well above expectations", "What does $4,000 in talent cover?"). It's not a budget document itself.

So questionnaire is the strongest match. The page asks the reader to answer open-response questions regarding a bid.

Wait, is there any possibility it's a "specification"? No.
"scientific_report"? No.

Let's review the evidence for questionnaire:
- Title: "GMR MARKETING QUESTIONS REGARDING BID RESPONSE"
- Content: A list of questions and comments directed at the bidder, requiring answers (open-response lines). Examples: "How do you envision dividing their responsibilities?", "Are Region Mangers third party staff?", "Please provide a total cost...", "How long is the surveyor training?", "What does $4,000 in talent cover?", "Why do we have a driver...", "What is the purpose of additional vehicle rental...".
- Function: Asking the reader to answer questions / provide information. This matches "asks the reader to answer... open-response lines" in check 4.

Runner-up: form. Ruled out because check 4 (questionnaire) fires before check 10 (form), and the page is a set of questions for the reader to answer, not a structured data-capture form with fields/boxes/ruled lines. Also, memo is ruled out because it lacks the required header block or dated internal note structure.

Let's confirm there's no hidden memo header.
Top of page: "GMR MARKETING QUESTIONS REGARDING BID RESPONSE"
Bottom right: "2083156178" (Bates number)
No TO/FROM/DATE/RE.

Conclusion: questionnaire.
Evidence: Title "QUESTIONS REGARDING BID RESPONSE", followed by bulleted open-response questions asking the reader to provide information and answers (e.g., "How do you envision dividing their responsibilities?", "Please provide a total cost...", "What does $4,000 in talent cover?"). Check 4 explicitly covers pages that ask the reader to answer open-response lines.

Final check of the label: questionnaire.
Confidence: 85. (Clear evidence for questionnaire, memo ruled out by lack of headers, form ruled out by check 4 precedence and lack of form fields).

---

## questionnaire → error: rvl_cdip__questionnaire__0003.png: model returned no usable content (finish_reason=length) (1 errors)

### `rvl_cdip__questionnaire__0003.png`
**Expected:** `questionnaire` | **Predicted:** `error: rvl_cdip__questionnaire__0003.png: model returned no usable content (finish_reason=length)`

*No reasoning text captured.*

---

## presentation → memo (1 errors)

### `rvl_cdip__presentation__0013.png`
**Expected:** `presentation` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.

Let's analyze the image:
- Top center: handwritten "DLG", "xJNJ"
- Typed text: "First draft for April 29. Please add."
- Typed text: "Lance"
- Bottom right: vertical text "526001380" (Bates number)
- Bottom: some black bars/artifacts.

Let's go through the checks:

1. IDENTIFIER-ONLY PAGE -> file_folder
   - Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card.
   - Wait, there is text: "First draft for April 29. Please add." and "Lance". This is a note. Is it file_folder? No, it has real content (a note). Wait, check 1 says "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note." So not file_folder.

2. MAJORITY-HANDWRITTEN PAGE -> handwritten
   - Most of the content is freeform handwriting. Here, there is "DLG", "xJNJ" handwritten, and the rest is typed ("First draft for April 29. Please add.", "Lance"). Not majority handwritten.

3. FAX TRANSMISSION SHEET -> form
   - No fax header.

4. SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
   - No.

5. PERSON'S CAREER HISTORY -> resume
   - No.

6. PUBLISHED EVIDENCE -> scientific_publication
   - No.

7. FINANCIAL DOCUMENT -> invoice or budget
   - No.

8. PRODUCT OR MATERIAL DOCUMENTATION -> specification
   - No.

9. SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
   - No.

10. ADMINISTRATIVE FORM -> form
    - No fields, boxes, checkboxes.

11. CORRESPONDENCE -> email, memo, or letter
    - "First draft for April 29. Please add."
    - "Lance"
    - Handwritten "DLG", "xJNJ"
    - This looks like a memo or a note. Let's check memo definition: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
    - Here we have "Lance" (name), "First draft for April 29. Please add." (prose/note), date "April 29". Handwritten initials "DLG", "xJNJ".
    - This is a memo! Or a handwritten note? Wait, check 2: "A typed page with only a signature, stamp, or margin note is not handwritten." The main text is typed: "First draft for April 29. Please add." and "Lance". The handwriting is just "DLG" and "xJNJ". So it's not majority handwritten.
    - Is it a memo? "Lance" could be the addressee. "First draft for April 29. Please add." is the message. "DLG" could be the sender (initials). This is a classic internal memo/note format.
    - Let's re-read check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division') from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
    - Here we have "Lance" (name), "April 29" (date), "First draft for April 29. Please add." (prose), "DLG" (sender initials). This fits the memo definition perfectly: internal names + date + prose, no salutation or closing.

Wait, is there any other category?
- email: no mail-client header.
- letter: no external address, no salutation, no closing signature.
- handwritten: not majority handwritten.

Let's check the scratchpad rules for memo:
"A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
Here: "Lance" (name), "April 29" (date), "First draft for April 29. Please add." (prose). "DLG" (sender). This is a memo.

Wait, is it just a handwritten note? "DLG" and "xJNJ" are handwritten. But the typed text is "First draft for April 29. Please add." and "Lance". The typed text is the main content. Check 2 says: "A typed page with only a signature, stamp, or margin note is not handwritten." So it's not handwritten.

Let's review the whole page:
- Top: handwritten "DLG", "xJNJ"
- Typed: "First draft for April 29. Please add."
- Typed: "Lance"
- Bottom right: "526001380" (Bates number)
- Bottom: black bars (scan artifacts)

This is a typed internal note/memo with handwritten initials.
Category: memo.

Let's double check check 11:
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation). Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."

Evidence:
- "Lance" (named person)
- "April 29" (date)
- "First draft for April 29. Please add." (memo-style prose)
- "DLG" (sender initials)
- No external address, no "Dear ..." salutation, no closing signature.
This matches the memo definition.

Is there any other possibility?
- file_folder: no, has real content (note).
- handwritten: no, mostly typed.
- form: no.
- letter: no, no external address, no salutation, no closing.

Therefore, memo is the correct label.

Let's write the scratchpad:
pre-scan: mail-client header none; Bates number 526001380 present.
file_folder: no — page carries real content ("First draft for April 29. Please add.", "Lance"), not just filing metadata.
handwritten: no — majority of content is typed ("First draft for April 29. Please add.", "Lance"); only small handwritten annotations ("DLG", "xJNJ"). Check 2 says typed page with margin notes is not handwritten.
fax sheet: no.
questionnaire: no.
resume: no.
scientific_publication: no.
financial: no.
specification: no.
presentation: no.
form: no — no fill-in fields, boxes, or ruled lines.
correspondence: yes — internal note addressed to "Lance" with date "April 29", prose "First draft for April 29. Please add.", and sender initials "DLG". No external address, no salutation, no closing signature. Matches memo definition: "internal names + date + prose, with no salutation or closing, is a memo header."
memo: yes — fits the dated internal note addressed to a named person with memo-style prose and no salutation/closing.
Runner-up: letter, ruled out because there is no external address, no "Dear ..." salutation, and no closing signature; it's an internal note.

Wait, is "Lance" an internal name? Yes, in the context of tobacco industry archives, "Lance" is likely an internal employee (e.g., Lance R. or similar). The rule says: "A dated internal note addressed to a named person by NAME ... with memo-style prose ... IS a memo even without literal 'TO:/FROM:' labels".

Let's confirm the confidence. The evidence is clear: typed internal note with name, date, prose, and initials. Memo is the correct label. Confidence: 95.

Wait, looking closely at the image:
"DLG"
"xJNJ"
"First draft for April 29. Please add."
"Lance"
"526001380"

This is a classic internal routing slip or memo note.
Label: memo.
Confidence: 95.

---