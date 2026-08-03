# Misclassification Reasoning — smoke_v10_full

**Overall Accuracy:** 82.9% (180/217)  
**Total Errors:** 37  
**Unique Confused Pairs:** 5

## invoice → budget (20 errors)

### `test_imagesy_y_n_j_ynj47c00_2084022615.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> Document analysis:
> - Header: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING"
> - Title: "NEWSPAPER ESTIMATE RECAP - PN05"
> - Period: "01/01/96 TO 12/31/96"
> - Date: "03/14/97"
> - Client: "P.M. INC."
> - Est No: "6089 REVISES EST DTD 02/14/97"
> - Desc: "760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS"
> - Table: "TOTALS BY MRKT/S ZON /PRODUCT/MONTH"
> - Columns: PRODUCT, PERIOD, EST AMT AMOUNT, EST AMT CHANGE, EST AMT LESS C/D
> - Row: "10-MARLBORO", "JAN 1996", "136.80-", "115.74-"
> - Bottom left: "FORM M01A REV 04-14-83"
> - Bottom right: Bates number "2084022615"
> 
> Let's go through the checks.
> 
> Pre-scan:
> - Mail-client header: None.
> - Masthead/running head: None.
> 
> Check 1: file_folder
> - Almost no body content? No, it has a table, headers, data. Not file_folder.
> 
> Check 2: handwritten
> - Most content handwritten? No, it's typed.
> 
> Check 3: FAX TRANSMISSION SHEET
> - No fax header.
> 
> Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL
> - Not a survey.
> 
> Check 5: PERSON'S CAREER HISTORY
> - Not a resume.
> 
> Check 6: PUBLISHED EVIDENCE
> - No journal identifier.
> 
> Check 7: FINANCIAL DOCUMENT -> invoice or budget
> - "ESTIMATE RECAP"
> - "PROJECTS upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - Wait, the text says: "DESC: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS", "REVISES EST DTD 02/14/97".
> - "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D".
> - This is an estimate recap. It's planning projected spend or tracking budget.
> - Let's check the budget definition: "budget: internal money planning, tracking, or disbursement... ALSO a provider's periodic customer statement... Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical... is scientific_report... But an agency/vendor document that lists actual charges and totals owed is an invoice... Wait. "an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - This is an "ESTIMATE RECAP" from Leo Burnett (an advertising agency) for P.M. Inc. (client). It shows "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". This is an estimate/budget tracking document.
> - Therefore, Check 7 matches: budget.
> 
> Let's double check Check 10: ADMINISTRATIVE FORM -> form
> - "FORM M01A REV 04-14-83" is at the bottom.
> - But Check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> - And "budget: ... an agency/vendor estimate or recap that projects upcoming placements/periods ... is budget, not invoice."
> - So budget overrides form.
> 
> Let's review the evidence for budget:
> - Title: "NEWSPAPER ESTIMATE RECAP"
> - Columns: "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D"
> - Content: Advertising estimate recap for Marlboro, Jan 1996.
> - This is money planning/tracking (estimate recap).
> 
> Let's check if it's an invoice: "invoice: ... an agency/vendor document that lists actual charges and totals owed is an invoice". But this is an "ESTIMATE RECAP", which plans projected spend. The text explicitly says: "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report... an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> This matches "ESTIMATE RECAP" perfectly.
> 
> So Check 7 is the match. Label: budget.
> 
> Let's quickly check other checks just in case.
> Check 8: specification. No.
> Check 9: presentation. No.
> Check 10: form. "FORM M01A" is present, but Check 7 (financial) overrides form layout when money function is primary. "Money function overrides form layout...". Also, "an agency/vendor estimate or recap... is budget, not invoice."
> Check 11: correspondence. No.
> Check 12: news_article. No.
> Check 13: scientific_report. No.
> Check 14: advertisement. No.
> 
> Final label: budget.
> 
> Wait, is there any chance it's a form?
> Check 10: "administrative form... A form does NOT have to be blank... It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
> Since this is an estimate recap (money record), it falls under Check 7.
> 
> Evidence for Check 7:
> - "NEWSPAPER ESTIMATE RECAP" header.
> - "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D" columns.
> - Client "P.M. INC.", product "MARLBORO", period "JAN 1996".
> - This is an estimate recap tracking projected spend/budget for advertising.
> 
> Runner-up: form, ruled out because the page is an estimate recap tracking money/planned spend (budget, check 7), which overrides the generic form layout (check 10).
> 
> Let's write the scratchpad.
> file_folder: no — page has substantial body content including headers, a data table, and financial figures.
> handwritten: no — content is entirely typed.
> fax: no — no fax transmission header.
> questionnaire: no — not a survey instrument.
> resume: no — not a career history.
> scientific_publication: no — no journal running head or publication identifier.
> financial_document: yes — titled "NEWSPAPER ESTIMATE RECAP", contains columns for "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D" for client "P.M. INC." and product "MARLBORO"; this is an agency/vendor estimate recap tracking projected spend/budget, which falls under budget (check 7).
> presentation: no — not a slide deck or cover.
> form: no — although "FORM M01A" is printed at the bottom, check 7 (financial document) overrides form layout when the primary content is money planning/tracking (an estimate recap).
> correspondence: no — no memo/letter header or prose.
> news_article: no — no masthead or journalistic layout.
> scientific_report: no — no running narrative prose or research methodology.
> advertisement: no — not a promotional layout.
> 
> Runner-up: form, ruled out because the page's primary structure is an "ESTIMATE RECAP" tracking advertising spend (budget, check 7), which overrides the generic form layout indicated by the "FORM M01A" footer (check 10).
> 
> Looks solid.

---

### `test_imagesd_d_a_v_dav40c00_ti16801308.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: No newspaper/magazine masthead. No journal running head. There's a Bates number "T11680-1308" at the bottom right.
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: The page has a lot of content: "ESTIMATE CHANGE ORDER", tables with financial data, descriptions, approvals. Not just an identifier/stamp.
>     *   Result: not this check.
> 
> *   **Check 2: handwritten**
>     *   Evidence: Mostly typed text. There are signatures and a date "2/12/96" in handwriting, but the majority is typed.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: No survey questions.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
>     *   Evidence: No CV/resume content.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
>     *   Evidence: No journal name, volume, issue, page range, DOI.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: Title is "ESTIMATE CHANGE ORDER". It has a table with "Estimate", "Change Order", "New Estimate" columns. It lists charges: "800 Number - Fax Contacts Total", "Management 800 Number - Operator Telephone Operators Total". Total is $100,000.00.
>     *   Wait, let's look at the definition of invoice vs budget.
>     *   Invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
>     *   Budget: "money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice."
>     *   The document is titled "ESTIMATE CHANGE ORDER".
>     *   Description: "Receive 'We Card' orders via 800#. includes operator training and time, scripting, report interpretations evaluating proper allocation of resources. *2/8/95 change order: TO REFLECT INCREASE IN 800 NUMBER-OPERATOR REQUESTS FROM 10,000 TO 25,000."
>     *   Table: "800 Number - Fax Contacts Total", "Management 800 Number - Operator Telephone Operators Total".
>     *   "Estimate is based on estimated personnel and production costs prior to receipt of all final bids, assuming no changes to the job specifications. Final invoice to reflect total actual personnel and production costs."
>     *   This is an "estimate change order". The text says "Final invoice to reflect total actual...". This implies it's not the final invoice yet, but an estimate/change order for future work or a change to an estimate.
>     *   Wait, check 7 says: "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... It does not have to be titled 'INVOICE' — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
>     *   BUT: "budget: ... an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an 'ESTIMATE RECAP' of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
>     *   Let's re-read carefully: "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> This lists "estimate change order" as potentially an invoice if it lists ACTUAL billable charges.
>     *   "budget: ... an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
>     *   The document has columns "Estimate", "Change Order", "New Estimate". The "New Estimate" is 100,000.00. The text says "Final invoice to reflect total actual personnel and production costs." This strongly suggests it is a budget/estimate for future work, not a bill for completed work. It's an "ESTIMATE CHANGE ORDER" adjusting the estimate.
>     *   Wait, is it an invoice? "a production estimate report, estimate change order... listing ACTUAL billable charges". Here, the charges are estimates (6,900.00, 21,600.00, 23,760.00). The total is 100,000.00. It's an estimate.
>     *   Let's look at the budget definition again: "budget: internal money planning, tracking, or disbursement... ALSO a provider's periodic customer statement... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice."
>     *   This is an "ESTIMATE CHANGE ORDER" from "Walt Klein & Associates, Inc." to "The Tobacco Institute". It's a vendor (WKA) providing an estimate/change order to a client (Tobacco Institute). It projects spend ("New Estimate" 100,000.00). It says "Final invoice to reflect total actual...". So this is a budget/estimate document, not an invoice for completed work.
>     *   Therefore, Check 7 matches "budget".
> 
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
>     *   Evidence: Not a material safety data sheet or product formulation.
>     *   Result: not this check.
> 
> *   **Check 9: SLIDE DECK... -> presentation**
>     *   Evidence: Not a slide deck.
>     *   Result: not this check.
> 
> *   **Check 10: ADMINISTRATIVE FORM -> form**
>     *   Evidence: It has fields and an approval block. But check 7 (Financial Document) takes precedence if it's financial. Wait, the instructions say: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
>     *   So if it's budget, it's budget, not form.
> 
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
>     *   Evidence: No TO/FROM/RE header followed by prose. It's a structured document with a table.
>     *   Result: not this check.
> 
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
>     *   Evidence: No masthead.
>     *   Result: not this check.
> 
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
>     *   Evidence: No running narrative prose about research.
>     *   Result: not this check.
> 
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
>     *   Evidence: Not an ad.
>     *   Result: not this check.
> 
> Let's re-evaluate Check 7.
> The document is an "ESTIMATE CHANGE ORDER".
> Text: "Estimate is based on estimated personnel and production costs prior to receipt of all final bids... Final invoice to reflect total actual personnel and production costs."
> This is clearly a budget/estimate document. It plans projected spend.
> Label: budget.
> 
> Wait, is there any other check?
> Check 10: Administrative form. "internal authorization/approval forms with an approval signature/date block." But "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)." This is a financial document (estimate/change order with dollar amounts). So it falls under Check 7.
> 
> Is it an invoice?
> "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> The text says "listing ACTUAL billable charges". This document lists ESTIMATES (6,900.00, 21,600.00, etc.). The "New Estimate" is 100,000.00. It is not listing actual charges. It is an estimate.
> "budget: ... an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> This fits perfectly. It's an estimate change order projecting spend (New Estimate 100,000.00).
> 
> So the label is `budget`.
> 
> Let's double check.
> Title: ESTIMATE CHANGE ORDER
> Vendor: Walt Klein & Associates, Inc.
> Client: The Tobacco Institute
> Content: Table with Estimate, Change Order, New Estimate columns. Dollar amounts.
> Footer note: "Final invoice to reflect total actual personnel and production costs."
> This confirms it's not the final invoice, but an estimate/budget document.
> 
> Therefore, Check 7 -> budget.
> 
> Final check of the scratchpad steps:
> 1. file_folder: No, has content.
> 2. handwritten: No, mostly typed.
> 3. fax: No.
> 4. questionnaire: No.
> 5. resume: No.
> 6. scientific_publication: No.
> 7. financial document: Yes. It's an estimate change order. Is it invoice or budget?
>    - Invoice: "listing ACTUAL billable charges". This lists estimates. "Final invoice to reflect..." implies this is not the invoice.
>    - Budget: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice."
>    - This is an estimate change order projecting the new total estimate (100,000.00). It is budget.
> 8. specification: No.
> 9. presentation: No.
> 10. form: No, money records are budget/invoice.
> 11. correspondence: No.
> 12. news_article: No.
> 13. scientific_report: No.
> 14. advertisement: No.
> 
> Runner-up: invoice. Ruled out because the document is an estimate change order projecting future spend ("New Estimate", "Final invoice to reflect total actual"), not billing completed work with actual charges. Or runner-up: form. Ruled out because money function overrides form layout (Check 7).
> 
> The label is `budget`.

---

### `test_imagesw_w_c_e_wce83f00_0001140924.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: No newspaper/magazine masthead. No journal running head.
> 
> **Check 1: file_folder**
> - Content: "Ted Bates & company, inc./advertising", "PRODUCTION ESTIMATE REPORT AC14", table with "WORK CODE", "COMMISSION RATE", "ORIGINAL ESTIMATE", "PRESENT ESTIMATE", totals, notes, contact/client signature lines. Bates number at bottom: 66602 9852.
> - Not file_folder. Has real content (table, headers, text).
> 
> **Check 2: handwritten**
> - Mostly typed. Some handwritten signatures/names in "CONTACT" and "CLIENT" lines. Not majority handwritten.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - No fax header.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - Not a survey.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - Not a resume.
> 
> **Check 6: PUBLISHED EVIDENCE**
> - No journal identifier.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - "PRODUCTION ESTIMATE REPORT AC14"
> - "BILLING TYPE PROGRESSIVE"
> - "RUN ON OCT24/79 AT 16.27 PAGE 1"
> - Table: "WORK CODE", "COMMISSION RATE", "ORIGINAL ESTIMATE", "PRESENT ESTIMATE". Values: 6500.00.
> - "TOTALS (NET)", "COMMISSIONS", "TOTALS (GROSS)".
> - Note: "ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES IN DESIGN, TYPOGRAPHY, ILLUSTRATION, PLATES NEEDED, ETC MAY ALTER FINAL CHARGES."
> - This is an estimate/recap projecting future work or a production estimate report.
> - Let's check the rules for invoice vs budget.
> - "invoice: ... an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, the rule says: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... is an invoice." BUT then: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - The document is titled "PRODUCTION ESTIMATE REPORT AC14". It has "ORIGINAL ESTIMATE" and "PRESENT ESTIMATE". The note says "ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES... MAY ALTER FINAL CHARGES." This is an estimate for future/completed work? "BILLING TYPE PROGRESSIVE". "RUN ON OCT24/79".
> - Wait, is it an invoice or budget?
> - Let's re-read check 7 carefully:
>   - "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> Wait, if it lists ACTUAL billable charges, it's an invoice. But this is an "ESTIMATE REPORT".
>   - "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> - The document is an "ESTIMATE REPORT". It has "ORIGINAL ESTIMATE" and "PRESENT ESTIMATE". It says "MAY ALTER FINAL CHARGES". This is an estimate, which is money planning for future work (or at least, not a final bill for completed work with actual charges). Thus, it's a budget.
> - Let's check if there's any other category.
> - Is it a form? Check 10: "internal authorization/approval forms with an approval signature/date block." It has "CONTACT... DATE...", "CLIENT... DATE...". But the primary content is the financial estimate table. Check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." So Check 7 wins over Check 10.
> - Is it an invoice? "an agency/vendor billing document for COMPLETED work: a production estimate report... listing ACTUAL billable charges". This document is an *estimate*, not actual charges. "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES." So it's not actual charges. It's an estimate. Therefore, budget.
> 
> Let's double check Check 7 text:
> "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed. It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
> "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> 
> This document is a "PRODUCTION ESTIMATE REPORT". It shows "ORIGINAL ESTIMATE" and "PRESENT ESTIMATE". It is an estimate, not a bill for completed work with actual charges. So it is budget.
> 
> Wait, is there any other check?
> Check 8: specification. No.
> Check 9: presentation. No.
> Check 10: form. It has fields, but Check 7 overrides: "Money function overrides form layout...".
> Check 11: correspondence. No.
> Check 12: news_article. No.
> Check 13: scientific_report. No.
> Check 14: advertisement. No.
> 
> So the label is budget.
> 
> Let's review the evidence for budget:
> - Title: "PRODUCTION ESTIMATE REPORT AC14"
> - Fields: "ORIGINAL ESTIMATE", "PRESENT ESTIMATE", "TOTALS (NET)", "TOTALS (GROSS)" with dollar amounts (6500.00).
> - Note: "ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES IN DESIGN... MAY ALTER FINAL CHARGES."
> - This is an agency/vendor estimate projecting spend/charges, not a final invoice for completed work with actual charges. Thus, budget.
> 
> Let's check if it could be invoice. "a production estimate report... listing ACTUAL billable charges". This report does NOT list actual billable charges; it lists estimates. The note explicitly says it "MAY ALTER FINAL CHARGES". So it's an estimate, which falls under budget ("an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice").
> 
> Therefore, budget is the correct label.
> 
> Scratchpad:
> - file_folder: no — page has detailed financial table, headers, and text.
> - handwritten: no — mostly typed, only small handwritten signatures.
> - fax: no — no fax header.
> - questionnaire: no — not a survey.
> - resume: no.
> - scientific_publication: no — no journal header.
> - financial_document: yes — "PRODUCTION ESTIMATE REPORT", table with "ORIGINAL ESTIMATE", "PRESENT ESTIMATE", dollar amounts, note "MAY ALTER FINAL CHARGES". This is an agency/vendor estimate projecting spend, not a final invoice for actual charges. Matches budget.
> - specification: no.
> - presentation: no.
> - form: no — Check 7 overrides form layout for financial documents.
> - correspondence: no.
> - news_article: no.
> - scientific_report: no.
> - advertisement: no.
> 
> Runner-up: invoice, ruled out because the document is an "ESTIMATE REPORT" with "ORIGINAL ESTIMATE" and "PRESENT ESTIMATE" that "MAY ALTER FINAL CHARGES", meaning it plans projected spend rather than billing actual completed work charges.
> 
> Final label: budget.

---

### `test_imagesy_y_n_j_ynj47c00_2084022615.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING" is a company logo/header, not a newspaper/magazine masthead or journal running head.
> 
> **Check 1: file_folder**
> - Evidence: The page has a table with "PRODUCT", "PERIOD", "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". It has a title "NEWSPAPER ESTIMATE RECAP - PNO5". It has real content, not just an identifier.
> - Not this check.
> 
> **Check 2: handwritten**
> - Evidence: Mostly typed text, a Bates number "208402615". No majority handwriting.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No "FACSIMILE" or fax cover sheet header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - Evidence: No survey questions or transmittal note.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - Evidence: No resume/CV content.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE**
> - Evidence: No journal name, volume, issue, page range, DOI.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: "NEWSPAPER ESTIMATE RECAP - PNO5". "EST NO: 6089 REVISES EST DTD 02/14/97". "DESC: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS". "TOTALS BY MRKT/S ZON /PRODUCT/MONTH". Table with "PRODUCT", "PERIOD", "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". "10-MARLBORO JAN 1996 136.80- 115.74-".
> - This is an "ESTIMATE RECAP". According to the instructions: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - Also: "A provider's periodic customer statement... is budget, not invoice". But this is an "ESTIMATE RECAP" from an advertising agency (Leo Burnett) to a client (P.M. Inc.). It's an estimate/recap of planned spend or adjustments. "EST NO: 6089 REVISES EST DTD 02/14/97". "DESC: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS". This is an estimate/recap, which falls under budget.
> - Let's re-read check 7: "budget: internal money planning, tracking, or disbursement... ALSO a provider's periodic customer statement... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice."
> - This is an "ESTIMATE RECAP" from an advertising agency. It's budget.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Evidence: No material safety data sheet, product formulation, or "shall/must" language.
> - Not this check.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Evidence: Not a slide deck, cover, or press release.
> - Not this check.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - Evidence: It has a form layout ("FORM M01A REV 04-14-83" at the bottom left). But check 7 (financial document) takes precedence if the primary structure is financial. Wait, let's check the order. Check 7 is before Check 10.
> - "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> - "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
> - So if it's budget, it's budget, not form.
> 
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
> - Evidence: No TO/FROM/RE header followed by prose, no letterhead with external address and salutation.
> - Not this check.
> 
> **Check 12: PUBLISHED JOURNALISM -> news_article**
> - Evidence: No newspaper/magazine masthead, byline, dateline.
> - Not this check.
> 
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
> - Evidence: No running narrative prose with objectives, methods, results.
> - Not this check.
> 
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
> - Evidence: Not a marketing layout, product imagery, slogans. It's an estimate recap.
> - Not this check.
> 
> Let's double check Check 7 vs Check 10.
> The document is an "ESTIMATE RECAP" from Leo Burnett U.S.A. (an advertising agency) for P.M. Inc. (client).
> It shows "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D".
> This is an estimate/recap of advertising placements (newspaper, ROP - Run of Paper).
> According to Check 7: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> This perfectly matches "ESTIMATE RECAP". It is budget.
> 
> Let's review the evidence for budget:
> - Header: "NEWSPAPER ESTIMATE RECAP - PNO5"
> - Client: "P.M. INC."
> - Description: "760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS"
> - Table columns: "PRODUCT", "PERIOD", "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D"
> - Row: "10-MARLBORO", "JAN 1996", "136.80-", "115.74-"
> - Footer: "FORM M01A REV 04-14-83"
> 
> This is an estimate/recap of projected spend (advertising placements). Therefore, it is budget.
> 
> Runner-up: form. Ruled out because the page's primary structure is financial (an estimate recap of projected ad spend), which falls under check 7 (budget) before check 10 (form). The instructions explicitly state: "Money function overrides form layout... money-only forms are budget (check 7)." and "an agency/vendor estimate or recap... is budget, not invoice."
> 
> Let's confirm there's no email header. No From/To/Sent/Subject.
> Let's confirm no fax header. No "SENT BY:" or "# N/N".
> 
> Final label: budget.

---

### `test_imagesd_d_a_v_dav40c00_ti16801308.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. "wka Walt Klein & Associates, Inc." is a company logo/header, not a newspaper/magazine masthead or journal running head. "ESTIMATE CHANGE ORDER" is a document title. Bates number "T11680-1308" at the bottom right.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of content: title "ESTIMATE CHANGE ORDER", description, table with financial data, approvals. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed text, with some handwritten signatures and dates in the "Approvals" section. Not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax cover sheet header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions or transmittal.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No CV/resume content.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal name, volume, issue, page range, DOI.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: Title is "ESTIMATE CHANGE ORDER". It has a table with "Estimate", "Change Order", "New Estimate" columns, showing dollar amounts (6,900.00, 21,600.00, 47,740.00, 100,000.00).
> - Let's look at the definition of invoice vs budget.
> - Invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, the text says: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... is an invoice."
> - Budget: "an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - Let's read the document carefully.
> - Title: "ESTIMATE CHANGE ORDER"
> - Description: "Receive 'We Card' orders via 800#. includes operator training and time, scripting, report interpretations evaluating proper allocation of resources. *2/8/95 change order: TO REFLECT INCREASE IN 800 NUMBER-OPERATOR REQUESTS FROM 10,000 TO 25,000."
> - Table:
>   - 800 Number - Fax Contacts Total: Estimate 6,900.00, New Estimate 6,900.00
>   - Management 800 Number - Operator: Estimate 23,760.00, Change Order 47,740.00, New Estimate 71,500.00
>   - Telephone Operators Total: Estimate 45,360.00, Change Order 47,740.00, New Estimate 93,100.00
>   - TOTAL: Estimate $52,260.00, Change Order 47,740.00, New Estimate 100,000.00
> - Note at bottom: "Estimate is based on estimated personnel and production costs prior to receipt of all final bids, assuming no changes to the job specifications. Final invoice to reflect total actual personnel and production costs."
> - This is an "ESTIMATE CHANGE ORDER". It is adjusting an estimate. It says "Final invoice to reflect total actual...". This means it is NOT billing completed work yet; it's an estimate change order for projected spend / planning.
> - Wait, check 7 says: "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." But this is an *estimate* change order. "Estimate is based on estimated personnel... Final invoice to reflect..."
> - Let's re-read check 7 budget definition: "budget: internal money planning, tracking, or disbursement... ALSO a provider's periodic customer statement... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - This is an "ESTIMATE CHANGE ORDER" adjusting an estimate for future work (800 number operator requests). It is money planning for future work. So it's a budget.
> - Wait, is it a form? Check 10: "internal authorization/approval forms with an approval signature/date block." But check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "an agency/vendor document that lists actual charges and totals owed is an invoice... never a form." But this is an estimate, not actual charges.
> - Let's look at the invoice definition again: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, the text says: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... is an invoice." This implies an estimate change order *can* be an invoice if it lists actual billable charges. But this one says "Final invoice to reflect total actual...". So it's not listing actual charges. It's an estimate change order for projected spend. Thus, budget.
> - Let's re-read carefully: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> - This document is an "ESTIMATE CHANGE ORDER" that increases the estimate from 52,260 to 100,000 for "800 NUMBER-OPERATOR REQUESTS". It explicitly states "Final invoice to reflect total actual personnel and production costs." Therefore, it is planning projected spend, not billing completed work. It is a budget.
> 
> Let's double check if it could be a form (check 10).
> Check 10: "internal authorization/approval forms with an approval signature/date block."
> But check 7: "Money function overrides form layout... Money PLANNING for future work is budget... an agency/vendor estimate... plans projected spend... budget, not invoice."
> Also, check 7 caveat: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget". This document HAS billable charges (line items with dollar amounts), so it's not just an authorization form. It's a financial document (budget).
> 
> Let's review the invoice definition in check 7: "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> The key is "listing ACTUAL billable charges". This document lists "Estimate", "Change Order", "New Estimate". It does not list actual charges. The footnote says "Final invoice to reflect total actual...". So it's not an invoice. It's a budget (estimate change order for projected spend).
> 
> Let's check if there's any other category.
> - advertisement: no
> - email: no
> - file_folder: no
> - form: no (financial overrides)
> - handwritten: no
> - invoice: no (not actual charges)
> - letter: no
> - memo: no
> - news_article: no
> - presentation: no
> - questionnaire: no
> - resume: no
> - scientific_publication: no
> - scientific_report: no
> - specification: no
> 
> So the label is `budget`.
> 
> Wait, could it be `invoice`? "ESTIMATE CHANGE ORDER" is explicitly mentioned in the invoice definition: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... is an invoice." But the condition is "listing ACTUAL billable charges". This document does not list actual charges; it lists estimates. The budget definition says: "an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice." This matches perfectly. It's an estimate change order that plans projected spend.
> 
> Let's confirm the evidence for budget:
> - Title: "ESTIMATE CHANGE ORDER"
> - Table with "Estimate", "Change Order", "New Estimate" columns and dollar amounts.
> - Text: "Estimate is based on estimated personnel and production costs prior to receipt of all final bids... Final invoice to reflect total actual..."
> - This is money planning for future work (projected spend), not billing completed work.
> 
> Runner-up: invoice. Ruled out because the document is an estimate change order for projected spend ("Final invoice to reflect total actual..."), not a bill for completed goods/services with actual charges.
> 
> Let's do a quick pass of the scratchpad rules.
> Check 1: file_folder - no, has content.
> Check 2: handwritten - no, mostly typed.
> Check 3: fax - no.
> Check 4: questionnaire - no.
> Check 5: resume - no.
> Check 6: scientific_publication - no.
> Check 7: invoice or budget - yes, budget. Evidence: "ESTIMATE CHANGE ORDER" title, table with Estimate/Change Order/New Estimate columns, footnote "Final invoice to reflect total actual...". This is money planning for future work (budget), not invoice.
> Check 8: specification - no.
> Check 9: presentation - no.
> Check 10: form - no, financial overrides.
> Check 11: correspondence - no.
> Check 12: news_article - no.
> Check 13: scientific_report - no.
> Check 14: advertisement - no.
> 
> Final label: budget.
> Evidence: "ESTIMATE CHANGE ORDER" header, line-item table with "Estimate", "Change Order", "New Estimate" columns showing projected costs, and footnote stating "Final invoice to reflect total actual...". This indicates money planning for future work (budget) rather than billing for completed work (invoice).
> Runner-up: invoice, ruled out because the document is an estimate change order for projected spend, not an actual bill for completed work.
> Runner-up: form, ruled out because financial content (money planning) overrides form layout per check 7.
> 
> Looks solid.
> I will write the scratchpad and output.

---

### `test_imagesw_w_c_e_wce83f00_0001140924.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I need to follow a specific scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a company header "Ted Bates & company, inc./advertising", but it's a letterhead/company header, not a newspaper/magazine masthead or journal running head.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of content: company header, client info, a table with financial data (Original Estimate, Present Estimate), totals, notes, contact/client signature lines. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed text and a table. There are some handwritten signatures/names in the contact/client/date lines, but it's not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions or transmittal for a survey.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No CV/resume content.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal name, volume, issue, page range, DOI.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: "PRODUCTION ESTIMATE REPORT AC14". "BILLING TYPE PROGRESSIVE". "ORIGINAL ESTIMATE 6500.00", "PRESENT ESTIMATE 6500.00". "TOTALS (NET)", "COMMISSIONS", "TOTALS (GROSS)". Note: "ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES IN DESIGN, TYPOGRAPHY, ILLUSTRATION, PLATES NEEDED, ETC MAY ALTER FINAL CHARGES."
> - This is an estimate/recap projecting future work or a production estimate report.
> - Let's look at the definition of budget vs invoice in Check 7.
> - "invoice: ... an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, the text says: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... is an invoice." BUT later it says: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - Let's re-read carefully: "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, is this an invoice or budget?
> - The document is titled "PRODUCTION ESTIMATE REPORT AC14". It has "ORIGINAL ESTIMATE" and "PRESENT ESTIMATE". It says "ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES... MAY ALTER FINAL CHARGES." This is an estimate, planning projected spend.
> - "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> - This is an estimate report from an advertising agency (Ted Bates) to a client (Brown & Williamson Tobacco Corp) for a job (Hispanic World's Fair). It's an estimate of costs/commissions. This is budget (internal money planning/tracking or vendor estimate of projected spend).
> - Wait, is it a form? "A form does NOT have to be blank... internal authorization/approval forms with an approval signature/date block." But check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." But this is an *estimate*, not actual charges owed. "plans projected spend rather than billing completed work — budget, not invoice."
> - So it's budget.
> 
> Let's double check Check 10: ADMINISTRATIVE FORM.
> - "A form does NOT have to be blank... internal authorization/approval forms with an approval signature/date block."
> - But Check 7 says: "Money function overrides form layout... an agency/vendor document that lists actual charges and totals owed is an invoice... never a form." What about an estimate? "Money PLANNING for future work is budget: an agency/vendor estimate or recap... plans projected spend rather than billing completed work — budget, not invoice."
> - So it falls under budget.
> 
> Let's re-read Check 7 carefully:
> "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> This implies if it lists ACTUAL charges, it's an invoice.
> "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> The document is a "PRODUCTION ESTIMATE REPORT". It has "ORIGINAL ESTIMATE" and "PRESENT ESTIMATE". It does not list actual billable charges for completed work, but rather estimates for a job. The note says "MAY ALTER FINAL CHARGES". This is a projected spend / estimate. Therefore, it is budget.
> 
> Wait, is there any other check?
> Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification. No.
> Check 9: SLIDE DECK... -> presentation. No.
> Check 10: ADMINISTRATIVE FORM -> form. The page has a table, signature lines. But Check 7 overrides for financial documents. "Money function overrides form layout...". Is an estimate a financial document? Yes, it's about money (estimates, commissions, totals). "an agency/vendor estimate or recap ... is budget, not invoice." So it's budget.
> 
> Let's review the evidence for budget:
> - "PRODUCTION ESTIMATE REPORT"
> - "ORIGINAL ESTIMATE 6500.00", "PRESENT ESTIMATE 6500.00"
> - "TOTALS (NET) 6500.00", "COMMISSIONS", "TOTALS (GROSS) 6500.00"
> - "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES."
> This is an agency/vendor estimate projecting spend/commissions. Matches budget.
> 
> Let's check if it could be invoice. "invoice: ... a production estimate report ... listing ACTUAL billable charges". This report does NOT list actual billable charges, it lists estimates. The note explicitly says it "MAY ALTER FINAL CHARGES". So it's not an invoice for completed work. It's a budget (projected spend).
> 
> Wait, the prompt says: "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." This document lists estimates, not actual charges. So it's budget.
> 
> Let's confirm the label: budget.
> 
> Scratchpad:
> - file_folder: no — page has substantial content (header, table, financial data, notes).
> - handwritten: no — mostly typed, only minor handwritten signatures.
> - fax: no — no fax header.
> - questionnaire: no — no survey items.
> - resume: no — no career history.
> - scientific_publication: no — no journal identifier.
> - invoice/budget: yes — "PRODUCTION ESTIMATE REPORT", "ORIGINAL ESTIMATE", "PRESENT ESTIMATE", "TOTALS (GROSS) 6500.00", note "MAY ALTER FINAL CHARGES". This is an agency/vendor estimate projecting spend/commissions, which falls under budget (money planning for future work, not billing completed work).
> - specification: no — not a material/product spec.
> - presentation: no — not a slide deck.
> - form: no — financial content (estimate) overrides form layout per check 7.
> - correspondence: no — no TO/FROM/RE memo header or letter structure.
> - news_article: no — no masthead.
> - scientific_report: no — no running narrative prose of research.
> - advertisement: no — not a promotional layout.
> 
> Runner-up: invoice, ruled out because the document is an estimate projecting future charges ("MAY ALTER FINAL CHARGES", "ESTIMATE REPORT") rather than billing for completed work with actual charges owed.
> Or runner-up: form, ruled out because check 7 (financial document) overrides form layout when money is the primary structure.
> 
> Final label: budget.

---

### `test_imagesy_y_n_j_ynj47c00_2084022615.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> Document analysis:
> - Header: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING"
> - Title: "NEWSPAPER ESTIMATE RECAP - PN05"
> - Period: "01/01/96 TO 12/31/96"
> - Date: "03/14/97"
> - Client: "P.M. INC."
> - Est No: "6089 REVISES EST DTD 02/14/97"
> - Desc: "760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS"
> - Table: "TOTALS BY MRKT/S ZON /PRODUCT/MONTH"
> - Columns: PRODUCT, PERIOD, EST AMT AMOUNT, EST AMT CHANGE, EST AMT LESS C/D
> - Row: "10-MARLBORO", "JAN 1996", "136.80-", "115.74-"
> - Bottom left: "FORM M01A REV 04-14-83"
> - Bottom right: Bates number "208402615"
> 
> Let's go through the checks.
> 
> Pre-scan:
> - Mail-client header: None.
> - Masthead/running head: None.
> 
> Check 1: file_folder
> - Has body content (table, headers, data). Not file_folder.
> 
> Check 2: handwritten
> - Typed throughout. Not handwritten.
> 
> Check 3: FAX TRANSMISSION SHEET
> - No fax header. Not this.
> 
> Check 4: questionnaire
> - Not a survey. Not this.
> 
> Check 5: resume
> - Not a resume. Not this.
> 
> Check 6: scientific_publication
> - No journal identifier. Not this.
> 
> Check 7: FINANCIAL DOCUMENT -> invoice or budget
> - "ESTIMATE RECAP"
> - "PROJECTED spend rather than billing completed work — budget, not invoice."
> - "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
> - Wait, is this an estimate recap (planning) or an invoice (completed work)?
> - "ESTIMATE RECAP - PN05"
> - "DESC: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS"
> - "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D"
> - "PLAN money for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - This is an "ESTIMATE RECAP" from Leo Burnett (advertising agency) for P.M. Inc. (Philip Morris). It's an estimate of ad buys.
> - Therefore, it's a budget.
> 
> Let's double check check 7 definition:
> "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category (amounts need not be legible). ALSO a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold. Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> 
> Yes, "ESTIMATE RECAP" is explicitly mentioned as budget.
> 
> Check 8: specification
> - Not a material safety data sheet or product formulation.
> 
> Check 9: presentation
> - Not a slide deck.
> 
> Check 10: form
> - It has a form number at the bottom left "FORM M01A REV 04-14-83".
> - But check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> - And "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
> - Wait, is this an invoice or budget? It's an estimate recap, so budget. Budget overrides form.
> 
> Check 11: correspondence
> - Not a letter/memo/email.
> 
> Check 12: news_article
> - Not news.
> 
> Check 13: scientific_report
> - Not scientific.
> 
> Check 14: advertisement
> - Not an ad itself, it's an estimate recap for an ad campaign.
> 
> So the label is budget.
> 
> Let's review the scratchpad steps:
> 1. file_folder: no — has table data, headers, financial content.
> 2. handwritten: no — typed text.
> 3. fax: no — no fax header.
> 4. questionnaire: no — not a survey.
> 5. resume: no — not a career history.
> 6. scientific_publication: no — no journal header.
> 7. financial document (budget): yes — "ESTIMATE RECAP" from advertising agency Leo Burnett for client P.M. Inc., showing projected spend ("EST AMT AMOUNT", "EST AMT LESS C/D") for newspaper placements. Check 7 explicitly states an "ESTIMATE RECAP" that projects upcoming placements is budget, not invoice.
> 8. specification: no — not a product spec.
> 9. presentation: no — not a slide deck.
> 10. form: no — although it has "FORM M01A" at the bottom, check 7 (financial document) overrides form layout when the primary content is financial tracking/planning.
> 11. correspondence: no — no TO/FROM/RE or letter structure.
> 12. news_article: no — no masthead.
> 13. scientific_report: no — no running prose.
> 14. advertisement: no — not a promotional layout.
> 
> Runner-up: form, ruled out because check 7 (financial document) explicitly overrides form layout for money planning/tracking documents like an "ESTIMATE RECAP".
> Another runner-up: invoice, ruled out because the document is an "ESTIMATE RECAP" projecting spend (budget), not billing for completed goods/services (invoice).
> 
> Final label: budget.

---

### `test_imagesd_d_a_v_dav40c00_ti16801308.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. "wka Walt Klein & Associates, Inc." is a company logo/header, not a newspaper/magazine masthead or journal running head. "ESTIMATE CHANGE ORDER" is a document title.
> 
> **Check 1: file_folder**
> - Evidence: The page has a title "ESTIMATE CHANGE ORDER", a table with financial data, descriptions, and an approval block. It has real content.
> - Not this check.
> 
> **Check 2: handwritten**
> - Evidence: Mostly typed text, with a signature and date in the approval block. Not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - Evidence: No survey questions or transmittal note.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - Evidence: No resume/CV content.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE**
> - Evidence: No journal name, volume, issue, page range, DOI.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: Title is "ESTIMATE CHANGE ORDER". It has a table with "Estimate", "Change Order", "New Estimate" columns. Line items: "800 Number - Fax Contacts Total", "Management 800 Number - Operator Telephone Operators Total". Total: $52,260.00, 47,740.00, 100,000.00.
> - Text at bottom: "Estimate is based on estimated personnel and production costs prior to receipt of all final bids, assuming no changes to the job specifications. Final invoice to reflect total actual personnel and production costs."
> - This is an estimate change order. It projects upcoming charges/changes to an estimate.
> - Let's check the rules for invoice vs budget.
> - "invoice: ... an agency/vendor document that lists actual charges and totals owed is an invoice ... A production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, the rule says: "A production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." is an invoice. BUT it also says: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - Let's re-read carefully: "invoice: ... an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> - Wait, the text says: "Estimate is based on estimated personnel and production costs prior to receipt of all final bids... Final invoice to reflect total actual personnel and production costs." This implies the work is not yet completed or billed as final. It's an estimate change order.
> - Let's look at the budget definition: "budget: internal money planning, tracking, or disbursement ... ALSO a provider's periodic customer statement ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> - The document is an "ESTIMATE CHANGE ORDER". It shows "Estimate", "Change Order", "New Estimate". The "New Estimate" is 100,000.00. The text says "Final invoice to reflect total actual...". This means it's not billing completed work yet, it's adjusting the estimate. Thus, it's budget (planning/projected spend).
> - Wait, is it an invoice? "an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges..." If it lists ACTUAL billable charges, it's an invoice. But this lists "Estimate" and "New Estimate", and says "Final invoice to reflect...". So it's not billing actual charges yet. It's an estimate change order for projected spend. Therefore, budget.
> - Let's re-read check 7: "invoice: ... an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." This phrasing is slightly ambiguous. Does "estimate change order" always mean invoice? No, only if it lists ACTUAL billable charges. Here it lists estimates.
> - "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> - This document is an "ESTIMATE CHANGE ORDER" that changes the estimate from 52,260 to 100,000. It's planning/projecting spend. So it's budget.
> 
> Let's check if there's any other category.
> - Check 8: specification. No.
> - Check 9: presentation. No.
> - Check 10: form. It has an approval block, but the primary content is a financial table (estimate change order). Check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." So it's financial (invoice or budget). Since it's an estimate change order for projected spend, it's budget.
> - Check 11: correspondence. No.
> - Check 12: news_article. No.
> - Check 13: scientific_report. No.
> - Check 14: advertisement. No.
> 
> Let's double check Check 7:
> "invoice: ... an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed. It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
> "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> 
> The document is titled "ESTIMATE CHANGE ORDER".
> Columns: "Estimate", "Change Order", "New Estimate".
> Values: 6,900.00, 21,600.00, 23,760.00 -> Total 52,260.00. Change order 47,740.00. New Estimate 100,000.00.
> Text: "Estimate is based on estimated personnel and production costs prior to receipt of all final bids... Final invoice to reflect total actual personnel and production costs."
> This clearly indicates it is NOT billing completed work (no actual charges yet, just estimates and a change order to the estimate). It is planning/projecting spend. Thus, it is a budget.
> 
> Wait, is there any possibility it's a form?
> Check 10: "internal authorization/approval forms with an approval signature/date block." But Check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "an internal expenditure-authorization form ... is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money. But an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
> Here, it's an agency/vendor document (Walt Klein & Associates) listing estimates and a change order to the estimate. It's financial. Since it's an estimate (planning), it's budget.
> 
> Let's confirm the label: `budget`.
> 
> Let's review the scratchpad steps:
> 1. file_folder: no — has title, table, descriptions, approvals.
> 2. handwritten: no — mostly typed, only signature/date.
> 3. FAX: no — no fax header.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. financial (invoice/budget): yes — "ESTIMATE CHANGE ORDER" with Estimate/Change Order/New Estimate columns, totaling projected spend. Text says "Final invoice to reflect total actual...", meaning this is not a final invoice for completed work, but an estimate change order (planning/projected spend). Matches budget.
> 8. specification: no.
> 9. presentation: no.
> 10. form: no — money function overrides form layout (check 7).
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no.
> 14. advertisement: no.
> 
> Runner-up: invoice. Ruled out because the document is an "ESTIMATE CHANGE ORDER" that projects a "New Estimate" of 100,000.00 and explicitly states "Final invoice to reflect total actual personnel and production costs," meaning it is planning projected spend (budget) rather than billing for completed work (invoice).
> 
> Final label: budget.

---

### `test_imagesj_j_o_w_jow70f00_0011930077.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header block:** No "From:", "To:", "Sent:", "Subject:" headers. There is a "VOUCHER" header. No email headers.
> - **Masthead/Running head:** No newspaper/magazine masthead. No journal running head with volume/issue/page number. There is a header "VOUCHER" and "BROWN & WILLIAMSON TOBACCO CORPORATION".
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
>     *   Evidence: The page has a lot of content: a voucher form with fields, dates, amounts, descriptions. It's not just an ID or stamp.
>     *   Result: not this check.
> 
> *   **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
>     *   Evidence: Most of the content is typed (form fields, printed text). There is some handwriting ("November 1989", maybe a signature or initials), but it's filling a form.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET -> form**
>     *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. Just a "VOUCHER".
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: No survey questions.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
>     *   Evidence: No CV/resume content.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
>     *   Evidence: No journal name, volume, issue, page range.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: The page is titled "VOUCHER" (Brown & Williamson Tobacco Corporation).
>     *   Fields: Date (11/20/89), Vendor No (218119), Vendor (The Franklin Institute), Address (Benjamin Franklin Parkway, Philadelphia, PA 19108), Due Date (12/1/89).
>     *   Item Description: "Final contribution for grant to above institute for basic research".
>     *   Item Amount: $278,000.00.
>     *   Pay this amount: $278,000.00.
>     *   Account Name: Gen, Corp, Contributions - Medical - Other.
>     *   This is a payment voucher / check stub / payment request.
>     *   Let's look at the definitions in Check 7.
>     *   "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..." -> Wait, "payment voucher" is listed under invoice? Let's re-read carefully.
>     *   "invoice: an outside vendor, supplier, or agency states charges owed... a payment voucher... a receipt, a payment request..."
>     *   "budget: ... a check face or check stub, a check/payment register..."
>     *   Wait, let's look closer. "A hotel/motel guest bill... is an invoice". "A running 'BALANCE DUE' column does not make a bill a budget".
>     *   "budget: ... internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking."
>     *   The document is a "VOUCHER". A voucher is a document authorizing payment.
>     *   Let's check the invoice definition again: "a payment voucher... is an invoice". Wait. "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work".
>     *   Let's check the budget definition: "budget: ... a check face or check stub...".
>     *   This document looks like a voucher for a grant contribution. "Final contribution for grant to above institute for basic research". Amount $278,000.00.
>     *   Is it an invoice or a budget?
>     *   The item description says "Final contribution for grant...". This is a payment for a grant.
>     *   Let's look at the "invoice" definition: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD". The Franklin Institute is receiving a grant. Is this a bill?
>     *   "budget: ... internal money planning, tracking, or disbursement... a check face or check stub...". A voucher is often part of the internal accounting process (check stub/voucher).
>     *   However, the text says "payment voucher" is under invoice? Let's re-read: "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request...".
>     *   Wait, let's look at the text: "Final contribution for grant to above institute for basic research". This is a disbursement.
>     *   Let's look at the "budget" definition again: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register...".
>     *   A voucher is a document used to authorize payment. It's often a check stub or part of the accounting record.
>     *   Let's look at the specific text: "VOUCHER BROWN & WILLIAMSON TOBACCO CORPORATION".
>     *   It has fields for Vendor, Amount, Account Name ("Gen, Corp, Contributions - Medical - Other").
>     *   This looks like an internal accounting document authorizing a payment (a grant contribution).
>     *   Is it an invoice? An invoice is usually from a vendor stating charges owed. Here, Brown & Williamson is paying The Franklin Institute. The Franklin Institute isn't billing them for goods/services in the traditional sense, it's a grant contribution. But the document itself is a "VOUCHER" from Brown & Williamson.
>     *   Let's re-read the invoice definition carefully: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an 'INVOICE' header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work...".
>     *   Wait, "a payment voucher" is explicitly listed under invoice? "an 'INVOICE' header with line items and amount due, a payment voucher, a vendor's price...". Yes.
>     *   BUT, let's look at the budget definition: "budget: ... a check face or check stub...".
>     *   This document is a voucher. Is a voucher an invoice or a budget?
>     *   Let's look at the content: "Final contribution for grant to above institute for basic research". $278,000.00.
>     *   Account: "Gen, Corp, Contributions - Medical - Other".
>     *   This is a disbursement record.
>     *   Let's look at the "invoice" definition again. "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
>     *   "invoice: ... a payment voucher...". This suggests a payment voucher is an invoice.
>     *   However, usually a voucher is internal. "Brown & Williamson Tobacco Corporation Voucher". This is an internal document authorizing payment.
>     *   Let's look at the "budget" definition: "budget: internal money planning, tracking, or disbursement...". A voucher tracks disbursement.
>     *   Let's look at the "form" check (Check 10). "internal authorization/approval forms with an approval signature/date block". This has approval blocks? "Pay this amount", "Duplicate", "Not to be paid". It has account codes.
>     *   But Check 7 says: "Money function overrides form layout... a billing or payment page stays financial".
>     *   Is this a billing page? "Final contribution for grant...". It's a payment.
>     *   Let's distinguish between invoice and budget.
>     *   Invoice: "charges owed for goods or services SOLD". "agency/vendor billing document for COMPLETED work".
>     *   Budget: "internal money planning, tracking, or disbursement". "check face or check stub".
>     *   This is a "VOUCHER". A voucher is a document supporting a payment. It's like a check stub or payment record.
>     *   The definition for budget includes "a check face or check stub". A voucher is very similar to a check stub/accounting record.
>     *   The definition for invoice includes "a payment voucher". This is confusing. Let's read carefully: "invoice: ... an 'INVOICE' header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request...".
>     *   Wait, if "payment voucher" is under invoice, then this is an invoice.
>     *   BUT, the context is "an outside vendor... states charges owed". Here, Brown & Williamson is the one issuing the voucher. They are paying. The Franklin Institute is the vendor (sort of).
>     *   Actually, usually a "Voucher" in accounting is the internal document that authorizes the check. The check itself is the payment.
>     *   Let's look at the text: "VOUCHER BROWN & WILLIAMSON TOBACCO CORPORATION". This is the payer's document.
>     *   If it's the payer's document authorizing payment, it's a disbursement record.
>     *   Budget definition: "internal money planning, tracking, or disbursement". This fits perfectly. It's tracking a disbursement ($278,000 grant).
>     *   Invoice definition: "an outside vendor... states charges owed". The Franklin Institute (vendor) would send an invoice. This document is from Brown & Williamson (the payer). It says "Final contribution for grant...". It's not a bill from the institute; it's Brown & Williamson's record of payment/authorization.
>     *   So it's likely a budget document (tracking disbursement) or a form.
>     *   Wait, Check 7 says: "Money function overrides form layout... a billing or payment page stays financial".
>     *   Is this a "payment page"? Yes.
>     *   Is it an invoice or budget?
>     *   Invoice: "billing document for COMPLETED work". A grant contribution isn't really "goods or services sold" in the commercial sense, but it's a payment.
>     *   Budget: "internal money... disbursement". This is an internal voucher from Brown & Williamson.
>     *   Let's look at the "form" check (Check 10). "internal authorization/approval forms with an approval signature/date block". This has "Pay this amount", account codes.
>     *   But Check 7 is higher priority if it's financial. "Check 7 applies only when financial content IS the page's primary structure". Yes, it's a financial form.
>     *   So it's either invoice or budget.
>     *   Let's re-evaluate "payment voucher" in the invoice definition. "invoice: ... a payment voucher...". This might refer to a vendor's payment voucher (a bill). But here the header is "VOUCHER BROWN & WILLIAMSON...". This is the payer's voucher.
>     *   Let's look at the budget definition: "budget: ... a check face or check stub...". A voucher is essentially a check stub or the accounting record preceding the check.
>     *   Also, "Gen, Corp, Contributions - Medical - Other" is an account code for tracking.
>     *   The description is "Final contribution for grant...". This is a disbursement.
>     *   I lean towards **budget** because it's an internal disbursement record (voucher) from the corporation, tracking a grant contribution. It's not a bill from an outside vendor (invoice). The outside vendor is The Franklin Institute, but this document is issued by Brown & Williamson ("VOUCHER BROWN & WILLIAMSON..."). An invoice would be from The Franklin Institute to Brown & Williamson. This is Brown & Williamson's internal accounting document (voucher) to pay them.
>     *   Wait, is a "voucher" an invoice? In accounting, a voucher is the document that authorizes payment. It's internal.
>     *   So it fits "internal money... disbursement" -> budget.
>     *   Let's check if it could be a **form** (Check 10). "internal authorization/approval forms with an approval signature/date block". It has fields, but the content is financial (money, account codes). Check 7 says "Money function overrides form layout". So it's financial.
>     *   So it's budget.
> 
>     Let's refine the "invoice" vs "budget" distinction.
>     - Invoice: "an outside vendor... states charges owed". Example: "production estimate report... listing ACTUAL billable charges".
>     - Budget: "internal money planning, tracking, or disbursement". Example: "check face or check stub".
>     - This document is a "VOUCHER" from "BROWN & WILLIAMSON TOBACCO CORPORATION". It is an internal document. It records a payment of $278,000 to "The Franklin Institute".
>     - It is a record of disbursement. Therefore, **budget**.
> 
>     Wait, let's look at the invoice definition again: "a payment voucher".
>     "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
>     If the text explicitly says "a payment voucher" is an invoice, maybe I should classify it as invoice?
>     But the context is "an outside vendor... states charges owed... a payment voucher [from the vendor?]".
>     Usually, a "Payment Voucher" is the document the *payer* creates to authorize payment. A "Vendor Invoice" is what the vendor sends.
>     If the label is "VOUCHER" and the company is "BROWN & WILLIAMSON", this is the payer's document.
>     The budget definition includes "check face or check stub". A voucher is very close to a check stub/accounting record.
>     Also, "internal money... disbursement". This is definitely internal disbursement tracking.
>     The item is "Final contribution for grant". Grants are often tracked in budgets/expenditure reports.
>     Account: "Gen, Corp, Contributions - Medical - Other". This is an internal account code.
>     This strongly points to **budget** (internal tracking/disbursement).
> 
>     Let's check if it's a **form** (Check 10).
>     "internal authorization/approval forms with an approval signature/date block".
>     Check 7: "Money function overrides form layout... a billing or payment page stays financial".
>     Is this a "billing or payment page"? Yes, it's a payment authorization (voucher).
>     So it falls under Check 7.
>     Under Check 7, is it invoice or budget?
>     - Invoice: charges owed for goods/services SOLD. (Grant contribution is not really goods/services sold, it's a contribution/grant).
>     - Budget: internal money... disbursement. (This fits perfectly. It's a disbursement of a grant).
>     - Also, "budget: ... a check face or check stub". A voucher is the accounting equivalent.
> 
>     Let's look at the "invoice" example: "a hotel/motel guest bill... is an invoice". "A running 'BALANCE DUE' column does not make a bill a budget 'statement of account'".
>     "budget: ... a provider's periodic customer statement... is budget, not invoice".
>     Here, Brown & Williamson is paying. The Franklin Institute is the recipient.
>     If this were a bill from Franklin Institute, it would be an invoice. But it's a "VOUCHER" from Brown & Williamson.
>     So it's Brown & Williamson's internal record. -> Budget.
> 
>     Wait, is there any other category?
>     Check 10: "administrative form".
>     "internal authorization/approval forms with an approval signature/date block".
>     But Check 7 says money overrides form.
>     "Check 7 applies only when financial content IS the page's primary structure". Yes, it's a financial voucher.
> 
>     So, **budget**.
> 
>     Let's double check the "payment voucher" in invoice definition.
>     "invoice: ... a payment voucher..."
>     Maybe it means a voucher *from* a payment? Or a voucher *for* payment?
>     If I have to choose between invoice and budget:
>     - Invoice is for "goods or services SOLD". A grant is a contribution.
>     - Budget is for "internal money... disbursement". A grant payment is a disbursement.
>     - The document is from the payer (Brown & Williamson), not the payee (Franklin Institute). An invoice comes from the payee. A voucher/check stub comes from the payer.
>     - Therefore, it's a budget document (internal disbursement record).
> 
>     Let's look at the label "budget".
>     "budget: internal money planning, tracking, or disbursement... a check face or check stub...".
>     This is a voucher (accounting document for disbursement).
> 
>     Final decision: **budget**.
> 
>     Wait, let's look at the text again.
>     "VOUCHER"
>     "BROWN & WILLIAMSON TOBACCO CORPORATION"
>     "DATE: 11/20/89"
>     "VENDOR NO: 218119"
>     "VENDOR: The Franklin Institute"
>     "AMOUNT: $278,000.00"
>     "ITEM DESCRIPTION: Final contribution for grant to above institute for basic research"
>     "ACCOUNT NAME: Gen, Corp, Contributions - Medical - Other"
> 
>     This is a payment voucher / check authorization.
>     In the tobacco archive context, these are often part of the financial records (budget/expenditure tracking).
>     The definition of budget includes "internal money... disbursement".
>     The definition of invoice includes "an outside vendor... states charges owed". The Franklin Institute is not stating charges owed here; Brown & Williamson is stating they are paying a contribution.
> 
>     So **budget** is the correct label.
> 
>     Wait, could it be **form**?
>     Check 10: "internal authorization/approval forms...".
>     Check 7: "Money function overrides form layout... a billing or payment page stays financial".
>     Is this a "payment page"? Yes.
>     Is it financial content as primary structure? Yes.
>     So Check 7 applies.
>     Check 7 splits into invoice or budget.
>     As argued, it's budget (internal disbursement, not vendor invoice).
> 
>     One more check: "invoice: ... a payment voucher...".
>     If the text explicitly lists "payment voucher" under invoice, maybe I should be careful.
>     "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an 'INVOICE' header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
>     This list seems to describe documents *from* a vendor or *for* a vendor's goods.
>     "a payment voucher" might mean a voucher *issued by* a vendor? Or a voucher *for* payment?
>     Usually, a "Payment Voucher" is the internal document.
>     If the label is "VOUCHER" and it's from the corporation, it's internal.
>     Internal financial tracking -> budget.
> 
>     Let's consider **invoice** again.
>     "a payment voucher" is listed under invoice.
>     But the context is "an outside vendor... states charges owed".
>     Here, the document is from Brown & Williamson.
>     So it's not an invoice from an outside vendor.
>     It's an internal document.
>     Internal financial document -> budget.
> 
>     Final check: **form**.
>     If I ignore the financial override (which I shouldn't), it's a form.
>     But the override is mandatory. "Money function overrides form layout".
> 
>     So **budget**.

---

### `test_imagesw_w_c_e_wce83f00_0001140924.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header block:** None. No From/To/Sent/Subject.
> - **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a company header "Ted Bates & company, inc./advertising".
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
>     *   Evidence: The page has a lot of content: a header "Ted Bates & company, inc./advertising", client info, a table with "WORK CODE", "COMMISSION RATE", "ORIGINAL ESTIMATE", "PRESENT ESTIMATE", totals, notes, signature lines. It's not just an ID.
>     *   Result: not this check.
> 
> *   **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
>     *   Evidence: Mostly typed text and a table. There are some handwritten signatures/names ("Contact...", "Client..."), but it's not majority handwritten.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET -> form**
>     *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: No survey questions.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
>     *   Evidence: No biographical info.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
>     *   Evidence: No journal name, volume, issue, page range.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: The document is a "PRODUCTION ESTIMATE REPORT AC14".
>     *   Header: "Ted Bates & company, inc./advertising". Client: "BROWN & WILLIAMSON TOBACCO CORP". Product: "KOOL KIDS". Job: "PC7501 HISPANIC WORLD'S FAIR".
>     *   Table columns: "WORK CODE", "COMMISSION RATE", "ORIGINAL ESTIMATE", "PRESENT ESTIMATE".
>     *   Values: "6500.00".
>     *   Totals: "TOTALS (NET)", "COMMISSIONS", "TOTALS (GROSS)".
>     *   Note: "***NOTE*** ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES IN DESIGN, TYPOGRAPHY, ILLUSTRATION, PLATES NEEDED, ETC. MAY ALTER FINAL CHARGES."
>     *   Analysis: This is an estimate/report for an advertising job. It's a "PRODUCTION ESTIMATE REPORT".
>     *   Check 7 details:
>         *   "invoice": outside vendor states charges owed for goods/services SOLD. "production estimate report, estimate change order, estimate recap... listing ACTUAL billable charges". Wait, let's look closer. "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES." This suggests it's a projection/estimate, not a final bill for completed work.
>         *   "budget": internal money planning, tracking... "agency/vendor document that lists actual charges and totals owed is an invoice". "A provider's periodic customer statement... is budget". "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice."
>     *   This is a "PRODUCTION ESTIMATE REPORT". It's an estimate from an agency (Ted Bates) to a client (Brown & Williamson). It projects costs ("ORIGINAL ESTIMATE", "PRESENT ESTIMATE"). The note says it "MAY ALTER FINAL CHARGES". This fits "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice."
>     *   Wait, let's re-read Check 7 carefully.
>     *   "invoice": "...a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> This page lists estimates, not actual charges. "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES." So it's not billing completed work.
>     *   "budget": "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
>     *   This document is a "PRODUCTION ESTIMATE REPORT". It shows "ORIGINAL ESTIMATE" and "PRESENT ESTIMATE" of $6500.00. It's an estimate for a job ("HISPANIC WORLD'S FAIR"). This is a budget/estimate document.
>     *   Wait, is it a form? Check 10 covers forms. But Check 7 is "FINANCIAL DOCUMENT -> invoice or budget". Check 7 comes before Check 10.
>     *   Let's check the hierarchy. Check 7 is before Check 10.
>     *   Is it an invoice? "an outside vendor... states charges owed... for COMPLETED work". This is an estimate. "ESTIMATE... MAY ALTER FINAL CHARGES". So it's not an invoice for completed work.
>     *   Is it a budget? "Money PLANNING for future work is budget: an agency/vendor estimate or recap... plans projected spend". Yes, this is an estimate report.
>     *   So Check 7 matches "budget".
> 
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
>     *   Evidence: Not an MSDS, not product formulation.
>     *   Result: not this check.
> 
> *   **Check 9: SLIDE DECK... -> presentation**
>     *   Evidence: Not a slide deck.
>     *   Result: not this check.
> 
> *   **Check 10: ADMINISTRATIVE FORM -> form**
>     *   Evidence: It has fields (Client, Product, Job, Work Code table, Contact/Client signature lines). It looks like a form.
>     *   However, Check 7 (Financial Document) takes precedence if it's financial.
>     *   "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
>     *   Since this is a financial estimate report (budget), Check 7 applies.
> 
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
>     *   Evidence: No TO/FROM/RE header followed by prose. No letterhead with external address + salutation.
>     *   Result: not this check.
> 
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
>     *   Evidence: No masthead.
>     *   Result: not this check.
> 
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
>     *   Evidence: No running narrative prose about research.
>     *   Result: not this check.
> 
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
>     *   Evidence: Not an ad. It's an internal/agency document.
>     *   Result: not this check.
> 
> **Re-evaluating Check 7 vs Check 10:**
> The document is a "PRODUCTION ESTIMATE REPORT".
> Check 7: "FINANCIAL DOCUMENT -> invoice or budget".
> - "invoice": ... "a production estimate report... listing ACTUAL billable charges". This report lists estimates, not actual charges. The note says "MAY ALTER FINAL CHARGES". So it's not an invoice for completed work.
> - "budget": "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice."
> This fits "budget" perfectly. It's an estimate from an advertising agency (Ted Bates) for a job (Hispanic World's Fair). It projects spend ($6500).
> 
> Wait, let's look at the structure.
> It has a header block: CLIENT, PRODUCT, MEDIA, JOB, EST NO.
> Then a table: WORK CODE, COMMISSION RATE, ORIGINAL ESTIMATE, PRESENT ESTIMATE.
> Then totals.
> Then a note.
> Then signature lines (Contact, Client, Date).
> 
> Is this a form? Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
> But Check 7 says: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
> And "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
> Here, it lists estimates. "Money PLANNING for future work is budget".
> So it falls under Check 7 -> budget.
> 
> Let's check the labels again.
> Labels: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> 
> The document is a "PRODUCTION ESTIMATE REPORT".
> Is it an invoice? "invoice: ... a production estimate report ... listing ACTUAL billable charges". This lists estimates. "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES." So it's not final charges.
> Is it a budget? "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> Yes, this is an estimate/report projecting spend. So it is a **budget**.
> 
> Wait, is there any other category?
> What about "form"?
> Check 10: "administrative form".
> But Check 7 is higher priority (7 comes before 10).
> Check 7: "Check 7 applies only when financial content IS the page's primary structure... If the page is otherwise formatted as correspondence... and a dollar figure... is merely mentioned... classify it as correspondence".
> Here, the primary structure IS financial (a table of estimates and totals).
> So Check 7 applies.
> Under Check 7, is it invoice or budget?
> - Invoice: "states charges owed for goods or services SOLD... listing ACTUAL billable charges". This is an estimate, not actual charges.
> - Budget: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work".
> This is an estimate for a job ("HISPANIC WORLD'S FAIR", "RUN ON OCT24/79"). It's planning the cost. So it's **budget**.
> 
> Let's double check the "invoice" definition in Check 7.
> "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> The text says "PRODUCTION ESTIMATE REPORT AC14".
> But the content is "ORIGINAL ESTIMATE 6500.00", "PRESENT ESTIMATE 6500.00".
> And the note: "ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES... MAY ALTER FINAL CHARGES."
> This confirms it is NOT listing actual billable charges for completed work. It is an estimate.
> Therefore, it fits the "budget" definition: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice."
> 
> So the label is **budget**.
> 
> Let's check if it could be a **form**.
> Check 10: "administrative form".
> "A hand-plotted experimental GRAPH... is a research test result (check 13), not a form: the form rule covers labeled charts/tables with values in rows/columns/cells, not plotted experimental data. It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
> This is a money record (estimate). So it's Check 7.
> 
> Final decision: **budget**.
> 
> Wait, let's look at the "invoice" definition again.
> "invoice: ... an outside vendor, supplier, or agency states charges owed for goods or services SOLD ... a production estimate report ... listing ACTUAL billable charges".
> If the report is titled "PRODUCTION ESTIMATE REPORT", but it's used to bill?
> The note says "MAY ALTER FINAL CHARGES". This implies it's not the final bill.
> The "PRESENT ESTIMATE" is 6500.00.
> This is a budget/estimate document.
> 
> One detail: "A provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
> This is a one-off job estimate ("HISPANIC WORLD'S FAIR").
> "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> This fits perfectly. It's an estimate for a specific job (Hispanic World's Fair), projecting the cost ($6500).
> 
> So, **budget**.
> 
> Let's check the scratchpad requirements.
> - Walk checks 1-14 in order.
> - State evidence or "none".
> - Stop at first match.
> - Final line: runner-up label and evidence ruling it out.
> 
> Check 1: file_folder. Evidence: Page has header, table, totals, notes. Not identifier-only. -> not this check.
> Check 2: handwritten. Evidence: Mostly typed, some signatures. -> not this check.
> Check 3: fax. Evidence: No fax header. -> not this check.
> Check 4: questionnaire. Evidence: No survey questions. -> not this check.
> Check 5: resume. Evidence: No bio info. -> not this check.
> Check 6: scientific_publication. Evidence: No journal header. -> not this check.
> Check 7: financial document (invoice/budget). Evidence: "PRODUCTION ESTIMATE REPORT", table with "ORIGINAL ESTIMATE", "PRESENT ESTIMATE", totals ($6500.00), note "MAY ALTER FINAL CHARGES". This is an agency/vendor estimate projecting spend, not billing completed work. Fits "budget". -> STOP.
> 
> Runner-up: invoice. Ruled out because the document is an estimate ("PRODUCTION ESTIMATE REPORT", "MAY ALTER FINAL CHARGES") projecting future spend/planned cost, not a bill for completed goods/services with actual charges owed.
> Runner-up: form. Ruled out because Check 7 (financial document) takes precedence for money records/tables, and this is a budget/estimate.
> 
> Wait, is "PRODUCTION ESTIMATE REPORT" a form?
> Check 10 says "internal authorization/approval forms with an approval signature/date block". This has signature lines.
> But Check 7 says "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
> And "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
> Here it lists estimates. "Money PLANNING for future work is budget".
> So Check 7 wins.
> 
> The label is **budget**.
> 
> One final check: Could it be **invoice**?
> "invoice: ... a production estimate report ... listing ACTUAL billable charges".
> The title is "PRODUCTION ESTIMATE REPORT".
> But the content is estimates.
> The definition of invoice includes "listing ACTUAL billable charges". This lists estimates.
> The definition of budget includes "agency/vendor estimate or recap that projects upcoming placements... plans projected spend rather than billing completed work".
> This matches perfectly.
> 
> Final label: budget.

---

### `test_imagesy_y_n_j_ynj47c00_2084022615.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". This is a company logo/header, not a newspaper/magazine masthead or journal running head.
> 
> **Check 1: file_folder**
> - Evidence: There is a Bates number "2084022615" and a form footer "FORM M01A REV 04-14-83". But there is actual content: an "ESTIMATE RECAP" table. Not file_folder.
> 
> **Check 2: handwritten**
> - Evidence: No handwriting. Typed text throughout.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No fax header.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - Evidence: No survey questions.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - Evidence: No resume/CV.
> 
> **Check 6: PUBLISHED EVIDENCE**
> - Evidence: No journal name/volume/issue/page number.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: "NEWSPAPER ESTIMATE RECAP - PN05". "PERIOD 01/01/96 TO 12/31/96", "DATE 03/14/97". "CLIENT: P.M. INC.", "DESC: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS". "TOTALS BY MRKT/S ZON /PRODUCT/MONTH". Table with "PRODUCT", "PERIOD", "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". "10-MARLBORO", "JAN 1996", "136.80-", "115.74-".
> - This is an "ESTIMATE RECAP". According to the instructions: "Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical... is scientific_report... But an agency/vendor document that lists actual charges and totals owed is an invoice... ALSO a provider's periodic customer statement... is budget, not invoice... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - Wait, the text says: "ESTIMATE RECAP". "DESC: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS". "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". This is an estimate recap, which is budget planning.
> - Let's re-read check 7: "budget: internal money planning, tracking, or disbursement... an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - This document is an "ESTIMATE RECAP" from Leo Burnett (an advertising agency) for P.M. Inc. (Philip Morris). It shows "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". It's an estimate recap, which is budget.
> - Let's check if it's an invoice. "invoice: an outside vendor... states charges owed... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, the text says: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... is an invoice." BUT later it says: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - How to distinguish? "EST AMT AMOUNT" (Estimated Amount), "EST AMT CHANGE", "EST AMT LESS C/D". The word "EST" means estimated. It's projecting spend, not billing completed work with actual charges. The description says "760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS". The period is "01/01/96 TO 12/31/96", date is "03/14/97". This is an estimate recap for a period, likely tracking estimated spend vs actual or prior adjustments. Given the explicit example in the prompt: "(e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice", this is almost certainly budget.
> - Let's look closely at the table: "PRODUCT", "PERIOD", "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". "10-MARLBORO", "JAN 1996", "136.80-", "115.74-". These are estimated amounts. It's a budget document.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
> - Evidence: No material safety data sheet, no product formulation.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
> - Evidence: Not a slide deck.
> 
> **Check 10: ADMINISTRATIVE FORM**
> - Evidence: It has a form footer "FORM M01A REV 04-14-83". But check 7 (financial document) takes precedence if the primary structure is financial. "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." Also, "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)." So if it's budget, it's budget, not form.
> 
> **Check 11: CORRESPONDENCE**
> - Evidence: No TO/FROM/RE memo header, no letter structure.
> 
> **Check 12: PUBLISHED JOURNALISM**
> - Evidence: No newspaper/magazine masthead.
> 
> **Check 13: ORIGINAL RESEARCH WRITE-UP**
> - Evidence: No running narrative prose.
> 
> **Check 14: PROMOTIONAL MATERIAL**
> - Evidence: Not an ad.
> 
> So the classification is budget.
> 
> Let's double check Check 7:
> "budget: ... an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> The document is titled "NEWSPAPER ESTIMATE RECAP - PN05". It has "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". This is clearly an estimate recap, which is budget.
> 
> Let's review the scratchpad steps:
> 1. file_folder: no — has actual content (estimate recap table).
> 2. handwritten: no — typed text.
> 3. FAX: no.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. financial document: yes — "NEWSPAPER ESTIMATE RECAP", "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". This is an agency/vendor estimate/recap projecting spend, which is budget.
> 8. specification: no.
> 9. presentation: no.
> 10. form: no — money records are budget/invoice (check 7 overrides form).
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no.
> 14. advertisement: no.
> 
> Runner-up: form, ruled out because the page's primary content is financial (an estimate recap with estimated amounts and changes), which falls under budget (check 7) and overrides the form layout (check 10). Or invoice, ruled out because it's an "ESTIMATE RECAP" with "EST AMT" (estimated amounts) projecting spend rather than billing completed work with actual charges.
> 
> Final label: budget.

---

### `test_imagesw_w_c_e_wce83f00_0001140924.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a company header "Ted Bates & company, inc./advertising", but it's a letterhead/company header, not a newspaper/magazine masthead or journal running head.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of content: "Ted Bates & company, inc./advertising", "PRODUCTION ESTIMATE REPORT AC14", tables with "WORK CODE", "COMMISSION RATE", "ORIGINAL ESTIMATE", "PRESENT ESTIMATE", totals, notes, contact/client signature lines.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed text and tables. There are some handwritten signatures/names in the "CONTACT" and "CLIENT" lines, but it's not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions or transmittal.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No resume content.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal name, volume, issue, page range, DOI.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: "PRODUCTION ESTIMATE REPORT AC14". "BILLING TYPE PROGRESSIVE". "ORIGINAL ESTIMATE 6500.00", "PRESENT ESTIMATE 6500.00". "TOTALS (NET)", "COMMISSIONS", "TOTALS (GROSS)". "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES."
> - Let's look at the definition of invoice vs budget.
> - invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, "A production estimate report... listing ACTUAL billable charges... is an invoice." But this is an "ESTIMATE REPORT".
> - budget: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - The document is titled "PRODUCTION ESTIMATE REPORT AC14". It has "ORIGINAL ESTIMATE" and "PRESENT ESTIMATE". It says "ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES IN DESIGN, TYPOGRAPHY, ILLUSTRATION, PLATES NEEDED, ETC. MAY ALTER FINAL CHARGES." This is an estimate of future charges, not a bill for completed work. It's a production estimate.
> - Wait, let's re-read check 7 carefully.
> - "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> This is under invoice. But it says "listing ACTUAL billable charges". This document lists "ESTIMATE".
> - "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> - This is an "ESTIMATE REPORT" from an advertising agency (Ted Bates) to a client (Brown & Williamson Tobacco Corp). It estimates the cost of a production job ("HISPANIC WORLD'S FAIR"). It's an estimate of future charges. Therefore, it's a budget (money planning/estimate).
> - Let's check the labels: `invoice` or `budget`. The category is `financial_document` which maps to `invoice` or `budget`. Wait, the final labels are the 16 strings. So it's either `invoice` or `budget`.
> - Let's re-read: "an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> - This is an estimate report for a production job. It's an estimate of what it will cost. So it's `budget`.
> 
> Let's double check.
> "PRODUCTION ESTIMATE REPORT AC14"
> "CLIENT BW BROWN & WILLIAMSON TOBACCO CORP"
> "JOB PC7501 HISPANIC WORLD'S FAIR"
> "BILLING TYPE PROGRESSIVE"
> "RUN ON OCT24/79 AT 16.27 PAGE 1"
> Table: WORK CODE, COMMISSION RATE, ORIGINAL ESTIMATE, PRESENT ESTIMATE.
> Values: 6500.00.
> "***NOTE*** ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES IN DESIGN... MAY ALTER FINAL CHARGES."
> This is clearly an estimate, not a final invoice for completed work. It's a budget/estimate document.
> So `budget`.
> 
> Let's check check 10 just in case.
> **Check 10: ADMINISTRATIVE FORM -> form**
> - It has fields like "CONTACT...", "CLIENT...", "DATE...", but the primary content is the financial estimate table. Check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." Here it lists estimates. Is it a form? "internal authorization/approval forms with an approval signature/date block." But check 7 takes precedence for financial content. "Money function overrides form layout". So it's budget.
> 
> Let's re-verify check 7 definition of budget:
> "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount... ALSO a provider's periodic customer statement... is budget, not invoice"
> "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> 
> This is an "ESTIMATE REPORT" from an agency (Ted Bates) to a client. It projects the cost (6500.00). It's an estimate. So it's `budget`.
> 
> Wait, could it be `invoice`?
> "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> The text says "listing ACTUAL billable charges". This document lists "ESTIMATE", not actual charges. The note says "MAY ALTER FINAL CHARGES". So it's not actual charges. It's an estimate. Thus, `budget`.
> 
> Let's check if there's any other check.
> Check 11: CORRESPONDENCE. No.
> Check 12: news_article. No.
> Check 13: scientific_report. No.
> Check 14: advertisement. No.
> 
> So the label is `budget`.
> 
> Let's review the scratchpad steps:
> 1. file_folder: no — page has substantial content (estimate report, tables, notes).
> 2. handwritten: no — mostly typed, only small handwritten signatures.
> 3. fax: no — no fax header.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. financial_document (invoice/budget): yes — "PRODUCTION ESTIMATE REPORT", "ORIGINAL ESTIMATE", "PRESENT ESTIMATE", "6500.00", note "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES". This is an agency/vendor estimate projecting spend, not billing completed work. Matches budget.
> Runner-up: invoice, ruled out because the document is an estimate of future charges ("ESTIMATE REPORT", "MAY ALTER FINAL CHARGES") rather than a bill for actual completed work ("listing ACTUAL billable charges").
> 
> Final label: budget.

---

### `test_imagesy_y_n_j_ynj47c00_2084022615.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". This is a company logo/header, not a newspaper/magazine masthead or journal running head.
> - Fax transmission header: None.
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
>     *   Evidence: The page has a lot of content: "LEO BURNETT U.S.A.", "NEWSPAPER ESTIMATE RECAP - PN05", tables with "PRODUCT", "PERIOD", "EST AMT AMOUNT", etc. Not just an identifier.
>     *   Result: not this check.
> 
> *   **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
>     *   Evidence: Typed text throughout. No majority handwriting.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET -> form**
>     *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: No survey questions or transmittal for a survey.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
>     *   Evidence: No biographical info.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
>     *   Evidence: No journal name, volume, issue, page range, DOI.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: "NEWSPAPER ESTIMATE RECAP - PN05". "EST NO: 6089 REVISES EST DTD 02/14/97". "DESC: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS". "TOTALS BY MRKT/S ZON /PRODUCT/MONTH". Table with "PRODUCT", "PERIOD", "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". Values: "10-MARLBORO", "JAN 1996", "136.80-", "115.74-".
>     *   Analysis: This is an "ESTIMATE RECAP". Check 7 says: "Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical... is scientific_report... But an agency/vendor document that lists actual charges and totals owed is an invoice... ALSO a provider's periodic customer statement... is budget... An estimate/recap projecting FUTURE work is budget (planning), not invoice; a bill for completed goods/services is invoice."
>     *   Wait, let's look closer at the text: "EST NO: 6089 REVISES EST DTD 02/14/97". "DESC: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS". "EST AMT AMOUNT 136.80-". "EST AMT LESS C/D 115.74-". This is an estimate recap. It's projecting or revising an estimate. "ESTIMATE RECAP".
>     *   Check 7 text: "budget: internal money planning, tracking, or disbursement... ALSO a provider's periodic customer statement... is budget... An estimate/recap projecting FUTURE work is budget (planning), not invoice".
>     *   Wait, is this an invoice? "an agency/vendor document that lists actual charges and totals owed is an invoice". This is an "ESTIMATE RECAP". It has "EST AMT" (Estimated Amount). It's revising an estimate. This looks like budget/planning/estimation.
>     *   Let's re-read Check 7 carefully: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts... ALSO a provider's periodic customer statement... is budget... An estimate/recap projecting FUTURE work is budget (planning), not invoice".
>     *   The document is titled "NEWSPAPER ESTIMATE RECAP". It shows "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". This is clearly an estimate/recap for budgeting/planning purposes (advertising spend estimate).
>     *   Therefore, it falls under **budget**.
> 
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
>     *   Evidence: No material safety data, product formulation, "shall/must".
>     *   Result: not this check.
> 
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
>     *   Evidence: Not a slide deck, not a press release.
>     *   Result: not this check.
> 
> *   **Check 10: ADMINISTRATIVE FORM -> form**
>     *   Evidence: It has a form layout ("FORM MO1A REV 04-14-83" at bottom left). But Check 7 (Financial Document) overrides form if the primary content is financial. "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." Wait, is this a billing page? It's an "ESTIMATE RECAP". Check 7 says "An estimate/recap projecting FUTURE work is budget (planning), not invoice". So it's budget. Budget is a financial document category. Does budget override form? Yes, Check 7 is before Check 10. "Check 7 applies only when financial content IS the page's primary structure... If the page is otherwise formatted as correspondence... classify it as correspondence... instead". Here, the primary structure is a financial table (estimate recap). So it's budget.
> 
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
>     *   Evidence: No TO/FROM/RE header followed by prose. No external address/salutation.
>     *   Result: not this check.
> 
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
>     *   Evidence: No masthead, byline, dateline.
>     *   Result: not this check.
> 
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
>     *   Evidence: No running narrative prose.
>     *   Result: not this check.
> 
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
>     *   Evidence: Not a marketing layout.
>     *   Result: not this check.
> 
> **Re-evaluating Check 7 (Financial Document -> budget vs invoice vs form):**
> The document is "NEWSPAPER ESTIMATE RECAP - PN05".
> Client: P.M. INC.
> Est No: 6089.
> Desc: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS.
> Table columns: PRODUCT, PERIOD, EST AMT AMOUNT, EST AMT CHANGE, EST AMT LESS C/D.
> Row: 10-MARLBORO, JAN 1996, 136.80-, 115.74-.
> Bottom left: "FORM MO1A REV 04-14-83".
> 
> This is an estimate recap. It's tracking estimated amounts, changes, and adjustments. This is money planning/tracking.
> Check 7: "budget: internal money planning, tracking, or disbursement... An estimate/recap projecting FUTURE work is budget (planning), not invoice".
> Even though it says "REVISES EST DTD 02/14/97" and "1991 & PRIOR ADJUSTMENTS", it's an estimate recap (financial tracking/planning document). It is not a bill for completed goods/services (invoice). It is a financial document whose primary structure is a table of estimated amounts.
> Therefore, **budget**.
> 
> Wait, could it be a form? "FORM MO1A REV 04-14-83".
> Check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> And: "Check 7 applies only when financial content IS the page's primary structure". Here, the primary structure is a financial table (estimate recap).
> So it's budget.
> 
> Let's double check if it's an invoice. "an agency/vendor document that lists actual charges and totals owed is an invoice". This lists "EST AMT" (Estimated Amount), not actual charges. "REVISES EST". It's an estimate. Estimate = budget (planning).
> 
> So the label is **budget**.
> 
> Let's check the labels again: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> 
> Label: budget.
> 
> Evidence for budget: "NEWSPAPER ESTIMATE RECAP", "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D", "REVISES EST". This is an estimate/recap for money planning/tracking.
> 
> Runner-up: form. Ruled out because the page's primary content is financial (estimate recap with dollar amounts), which falls under Check 7 (budget) before Check 10 (form). Also, "Money function overrides form layout".
> 
> Wait, is there any chance it's a form?
> Check 10: "administrative form -> form". "internal authorization/approval forms with an approval signature/date block". This doesn't have an approval block. It has a form number "FORM MO1A REV 04-14-83".
> But Check 7 takes precedence if financial content is primary. "Check 7 applies only when financial content IS the page's primary structure...". Yes, the table of amounts is the primary structure.
> "budget: ... An estimate/recap projecting FUTURE work is budget (planning), not invoice".
> 
> Final decision: budget.

---

### `test_imagesd_d_a_v_dav40c00_ti16801308.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: No newspaper/magazine masthead. No journal running head. There is a Bates number "T11680-1308" at the bottom right.
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
>     *   Evidence: The page has a lot of content: "ESTIMATE CHANGE ORDER", tables with financial data, descriptions, approvals. Not identifier-only.
>     *   Result: not this check.
> 
> *   **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
>     *   Evidence: Mostly typed text. Only signatures and a date are handwritten.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET -> form**
>     *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: No survey questions.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
>     *   Evidence: No CV/resume content.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
>     *   Evidence: No journal name, volume, issue, page range on the page itself.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: The document is titled "ESTIMATE CHANGE ORDER". It has columns for "Estimate", "Change Order", "New Estimate" with dollar amounts (6,900.00, 21,600.00, 47,740.00, 100,000.00).
>     *   Let's look at the definitions for invoice vs budget.
>     *   Invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, the text says: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... is an invoice."
>     *   Budget: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
>     *   Let's read the document carefully. Title: "ESTIMATE CHANGE ORDER".
>     *   Description: "Receive 'We Card' orders via 800#. includes operator training and time, scripting, report interpretations evaluating proper allocation of resources. *2/8/95 change order: TO REFLECT INCREASE IN 800 NUMBER-OPERATOR REQUESTS FROM 10,000 TO 25,000."
>     *   Table:
>         *   800 Number - Fax Contacts Total: Estimate 6,900.00, New Estimate 6,900.00
>         *   Management 800 Number - Operator: Estimate 21,600.00, Change Order 47,740.00, New Estimate 71,500.00
>         *   Telephone Operators Total: Estimate 45,360.00, Change Order 47,740.00, New Estimate 93,100.00
>         *   TOTAL: Estimate $ 52,260.00, Change Order 47,740.00, New Estimate 100,000.00
>     *   Footer text: "Estimate is based on estimated personnel and production costs prior to receipt of all final bids, assuming no changes to the job specifications. Final invoice to reflect total actual personnel and production costs."
>     *   This is an "ESTIMATE CHANGE ORDER". It is adjusting an estimate. It is not billing for completed work yet ("Final invoice to reflect total actual..."). It is planning/projecting spend or adjusting the projected spend.
>     *   Wait, let's re-read Check 7 carefully.
>     *   "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> This implies an estimate change order *could* be an invoice if it lists actual billable charges. But here it says "Estimate is based on estimated personnel... Final invoice to reflect total actual...". So this is NOT an invoice for completed work.
>     *   "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
>     *   This document is an "ESTIMATE CHANGE ORDER" that adjusts the projected budget from 52,260 to 100,000. It is a budget document (planning/projected spend).
>     *   Wait, is it a form? Check 10: "internal authorization/approval forms with an approval signature/date block." It has an "Approvals" block with Account Executive, Account VP, Client Approval.
>     *   But Check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." Here it lists *estimates* and *change orders* to a new estimate. It's a financial document.
>     *   Is it invoice or budget?
>     *   "Final invoice to reflect total actual personnel and production costs." -> This is not the final invoice. It's an estimate change order.
>     *   "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
>     *   This is an estimate change order adjusting the projected spend. So it's a budget.
> 
> Let's re-evaluate Check 7 vs Check 10.
> Check 7: "FINANCIAL DOCUMENT -> invoice or budget". "Money function overrides form layout...". The primary structure is a line-item table of financial estimates/changes.
> Check 10: "ADMINISTRATIVE FORM -> form". "internal authorization/approval forms with an approval signature/date block."
> The rule says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> Also: "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." Here it lists estimates, not actual charges owed yet. But it is a financial document (budget/estimate).
> Wait, "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget".
> This document has billable charges (estimates of them). "800 Number - Fax Contacts Total: 6,900.00". It's a financial table.
> The text says: "Estimate is based on estimated personnel and production costs prior to receipt of all final bids... Final invoice to reflect total actual...".
> This is a budget document (an estimate change order). Budget is the correct financial category.
> 
> Let's check the labels: `invoice`, `budget`.
> The document is an "ESTIMATE CHANGE ORDER".
> Is an estimate change order an invoice or a budget?
> "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> This definition says an estimate change order is an invoice *if* it lists actual billable charges. This one does not list actual charges, it lists estimates and a change order to the estimate.
> "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> This fits "budget" perfectly. It's an estimate change order planning projected spend.
> 
> Let's check if there's any other check.
> Check 8: specification. No.
> Check 9: presentation. No.
> Check 11: correspondence. No.
> Check 12: news_article. No.
> Check 13: scientific_report. No.
> Check 14: advertisement. No.
> 
> So it's between `invoice` and `budget` (Check 7) or `form` (Check 10).
> The primary structure is a financial table (Estimate, Change Order, New Estimate).
> "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> This page has a financial table and an approval block. Since it's financial (budget/estimate), it falls under Check 7.
> Is it `invoice` or `budget`?
> The text explicitly says "Final invoice to reflect total actual...". So this is NOT the invoice. It's an estimate change order.
> "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> This is an estimate change order, which is a budget document.
> 
> Therefore, the label is `budget`.
> 
> Let's double check Check 7 definition for invoice: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> The document is an "ESTIMATE CHANGE ORDER". But it does NOT list "ACTUAL billable charges". It lists "Estimate", "Change Order", "New Estimate". And the footnote says "Final invoice to reflect total actual...". So it's not an invoice.
> It is a budget (projected spend).
> 
> Wait, what about Check 10? "internal authorization/approval forms with an approval signature/date block."
> But Check 7 says: "Money function overrides form layout...". And "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." Even though this doesn't list *actual* charges, it's a financial document (budget). The rule "Money function overrides form layout" applies.
> Also, "an internal expenditure-authorization form ... with an approval signature/date block but no billable charges) is a form (check 10), not budget". This document HAS billable charges (estimates of them, 52,260.00, 100,000.00). So it's not just an authorization form; it's a financial document.
> 
> So `budget` is the correct label.
> 
> Let's review the scratchpad steps:
> 1. file_folder: no, has content.
> 2. handwritten: no, mostly typed.
> 3. fax: no.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. financial document: yes. Title "ESTIMATE CHANGE ORDER", table with dollar amounts (Estimate, Change Order, New Estimate), total $100,000.00. Footnote: "Final invoice to reflect total actual...". This is an estimate/budget document, not an invoice for completed work. Budget.
> 8. specification: no.
> 9. presentation: no.
> 10. form: has approval block, but money function overrides.
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no.
> 14. advertisement: no.
> 
> Runner-up: invoice. Ruled out because the document is an estimate change order adjusting projected spend, with a footnote stating "Final invoice to reflect total actual...", meaning it is not billing for completed work (which would make it an invoice), but rather planning/projecting (budget).
> Another runner-up: form. Ruled out because the primary structure is a financial table (money function overrides form layout).
> 
> Final label: budget.

---

### `test_imagesw_w_c_e_wce83f00_0001140924.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a company header "Ted Bates & company, inc./advertising", but it's a letterhead/company header, not a newspaper/magazine masthead or journal running head.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of content: company header, client info, a table with financial data, notes, signatures. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed text and a table. Some handwritten signatures/names. Not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax cover sheet header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions or transmittal.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No resume content.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal running head, volume, issue, page range.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: "PRODUCTION ESTIMATE REPORT AC14". "BILLING TYPE PROGRESSIVE". Table with "ORIGINAL ESTIMATE", "PRESENT ESTIMATE", "TOTALS (NET)", "COMMISSIONS", "TOTALS (GROSS)". Note: "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES."
> - Let's look at the definitions for invoice vs budget.
> - invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, "A production estimate report... listing ACTUAL billable charges... is an invoice." But this is an "ESTIMATE REPORT".
> - budget: "Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical... is scientific_report... But an agency/vendor document that lists actual charges and totals owed is an invoice... Wait. Let's re-read carefully.
> - "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> - "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - This document is a "PRODUCTION ESTIMATE REPORT". It has "ORIGINAL ESTIMATE" and "PRESENT ESTIMATE". It says "ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES IN DESIGN, TYPOGRAPHY, ILLUSTRATION, PLATES NEEDED, ETC MAY ALTER FINAL CHARGES." This is an estimate of future charges, not a bill for completed work. It's an agency/vendor estimate that projects spend. So it's a budget.
> - Wait, let's look at the text again: "PRODUCTION ESTIMATE REPORT AC14". "BILLING TYPE PROGRESSIVE". "RUN ON OCT24/79". "EST NO KM-NISC-60-1".
> - Is it an invoice or budget?
> - "an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> - This is an estimate report for a job (PC7581 HISPANIC WORLD'S FAIR). It shows original estimate 6500.00 and present estimate 6500.00. It's an estimate, not a final bill. So it's budget.
> - Let's check check 10: ADMINISTRATIVE FORM -> form. "internal authorization/approval forms with an approval signature/date block." This has "CONTACT... DATE...", "CLIENT... DATE...". But it's primarily a financial document (estimate report). Check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "an agency/vendor document that lists actual charges and totals owed is an invoice... But an agency/vendor document that lists actual charges and totals owed is an invoice... wait. "an agency/vendor estimate or recap that projects upcoming placements/periods ... is budget, not invoice."
> - So this is budget.
> 
> Let's re-evaluate Check 7:
> - "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> This says a production estimate report IS an invoice IF it lists ACTUAL billable charges. But this one lists "ESTIMATE", not actual charges. "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES." So it's not actual charges.
> - "budget: ... an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice." -> This matches perfectly. It's an estimate report projecting spend.
> 
> So Check 7 matches -> budget.
> 
> Let's double check Check 10 just in case.
> - "administrative form ... internal authorization/approval forms with an approval signature/date block."
> - But Check 7 says "Money function overrides form layout... a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "an agency/vendor document that lists actual charges and totals owed is an invoice... never a form." Wait, what about an estimate? "an agency/vendor estimate or recap ... is budget, not invoice." It doesn't say "never a form" for budget, but Check 7 is "FINANCIAL DOCUMENT -> invoice or budget". The primary structure is financial (estimate table). So it's budget.
> 
> Let's review the evidence for budget:
> - Header: "PRODUCTION ESTIMATE REPORT AC14"
> - Table columns: "ORIGINAL ESTIMATE", "PRESENT ESTIMATE"
> - Values: "6500.00"
> - Note: "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES."
> - This is an agency (Ted Bates) providing an estimate to a client (Brown & Williamson Tobacco Corp). It projects spend (6500.00). This is budget.
> 
> Let's check if there's any other check.
> - Check 11: CORRESPONDENCE. No TO/FROM/RE memo header, no letterhead with external address + Dear + closing. It's a form/report.
> - Check 12: news_article. No.
> - Check 13: scientific_report. No.
> - Check 14: advertisement. No.
> 
> So the label is budget.
> 
> Wait, is it "invoice"?
> "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed. It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
> This document is titled "PRODUCTION ESTIMATE REPORT". It does NOT bill charges already incurred. It says "MAY ALTER FINAL CHARGES". So it's not an invoice. It's an estimate.
> "budget: ... an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> Matches perfectly.
> 
> Final check of the text:
> "Ted Bates & company, inc./advertising"
> "CLIENT BM BROWN & WILLIAMSON TOBACCO CORP"
> "PRODUCTION ESTIMATE REPORT AC14"
> "BILLING TYPE PROGRESSIVE"
> Table: "WORK CODE", "COMMISSION RATE", "ORIGINAL ESTIMATE", "PRESENT ESTIMATE"
> "64 MISCELLANEOUS", "ZERO", "6500.00", "6500.00"
> "TOTALS (NET)", "6500.00", "6500.00"
> "TOTALS (GROSS)", "6500.00", "6500.00"
> "***NOTE*** ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES IN DESIGN, TYPOGRAPHY, ILLUSTRATION, PLATES NEEDED, ETC MAY ALTER FINAL CHARGES."
> "CONTACT... DATE..."
> "CLIENT... DATE..."
> 
> This is clearly an estimate report, which falls under budget.
> 
> Scratchpad:
> file_folder: no — page has substantial content including a company header, client details, a financial table, and notes.
> handwritten: no — mostly typed text and a table, with only small handwritten signatures.
> form: no — although it has fields and signature lines, the primary structure is a financial estimate report.
> invoice: no — it is an "ESTIMATE REPORT" that states charges "MAY ALTER FINAL CHARGES", meaning it does not bill actual completed charges.
> budget: yes — titled "PRODUCTION ESTIMATE REPORT", it is an agency/vendor document projecting spend ("ORIGINAL ESTIMATE", "PRESENT ESTIMATE" of 6500.00) rather than billing completed work.
> Runner-up: invoice, ruled out because the document is an estimate that explicitly states charges may alter and does not bill actual completed work, fitting the budget definition for an agency/vendor estimate projecting spend.
> 
> Label: budget.

---

### `test_imagesy_y_n_j_ynj47c00_2084022615.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> 
> **1. Mandatory pre-scan:**
> - Mail-client header block: None.
> - Masthead or running head: No newspaper/magazine masthead. No journal running head.
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
>     *   Evidence: The page has a lot of content: "LEO BURNETT U.S.A.", "NEWSPAPER ESTIMATE RECAP - PN05", tables with "PRODUCT", "PERIOD", "EST AMT AMOUNT", etc. Not just an identifier.
>     *   Result: not this check.
> 
> *   **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
>     *   Evidence: Typed text throughout. No majority handwriting.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET -> form**
>     *   Evidence: No "FACSIMILE" or fax header.
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: No survey questions.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
>     *   Evidence: No career history.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
>     *   Evidence: No journal name/volume/issue.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: "LEO BURNETT U.S.A. ADVERTISING", "NEWSPAPER ESTIMATE RECAP - PN05", "PERIOD 01/01/96 TO 12/31/96", "DATE 03/14/97", "CLIENT: P.M. INC.", "DESC: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS", "TOTALS BY MRKT/S ZON /PRODUCT/MONTH", "PRODUCT 10-MARLBORO", "PERIOD JAN 1996", "EST AMT AMOUNT 136.80-", "EST AMT LESS C/D 115.74-".
>     *   Analysis: This is an "ESTIMATE RECAP". Check 7 says: "Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical... is scientific_report... But an agency/vendor document that lists actual charges and totals owed is an invoice... Wait, let's re-read carefully."
>     *   "budget: internal money planning, tracking, or disbursement... ALSO a provider's periodic customer statement... is budget, not invoice — it is a statement of charges for an ongoing account... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
>     *   The document is titled "ESTIMATE RECAP". It shows "EST AMT AMOUNT", "EST AMT CHANGE", "EST AMT LESS C/D". It's an estimate recap for Leo Burnett (advertising agency) for P.M. Inc. (Philip Morris). It's an estimate/recap projecting spend or tracking budget. Wait, "DESC: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS". "EST NO: 6089 REVISES EST DTD 02/14/97". This is an estimate recap. Check 7 explicitly says: "an agency/vendor document that lists actual charges and totals owed is an invoice... But an agency/vendor document that lists actual charges and totals owed is an invoice... Wait. Let's look at the budget definition: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
>     *   This is an "ESTIMATE RECAP". It has "EST AMT". It's an estimate. Therefore, it's budget.
>     *   Let's check invoice definition: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, the invoice definition says "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... is an invoice."
>     *   Let's re-read carefully:
>         *   Invoice: "...a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> This implies if it lists *actual* billable charges, it's an invoice.
>         *   Budget: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
>     *   The document has "EST AMT AMOUNT 136.80-", "EST AMT LESS C/D 115.74-". These are *estimated* amounts, not actual charges. "EST NO: 6089 REVISES EST DTD 02/14/97". It's an estimate recap. It's planning/tracking projected spend. So it's budget.
>     *   Wait, is it a form? "FORM M01A REV 04-14-83" at the bottom left. But the content is financial (estimate recap). Check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "an agency/vendor document that lists actual charges and totals owed is an invoice... never a form." But this is an *estimate* recap, not actual charges. So it's budget.
>     *   Let's re-read the invoice part: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... is an invoice." This means if the estimate recap lists *actual* charges, it's an invoice. Here, it lists "EST AMT" (Estimated Amount). So it's not actual charges. It's an estimate.
>     *   Budget definition: "an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice." This matches perfectly. "ESTIMATE RECAP", "EST AMT". It's budget.
> 
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
>     *   Evidence: No material safety data, no product formulation.
>     *   Result: not this check.
> 
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
>     *   Evidence: Not a slide deck.
>     *   Result: not this check.
> 
> *   **Check 10: ADMINISTRATIVE FORM -> form**
>     *   Evidence: It has a form number "FORM M01A REV 04-14-83" at the bottom. But Check 7 says "Money function overrides form layout... an agency/vendor document that lists actual charges and totals owed is an invoice... never a form." Wait, this is an estimate, so it's budget. "Money PLANNING for future work is budget... an agency/vendor estimate or recap... is budget, not invoice." Does budget override form? Yes, "Money function overrides form layout". So it's budget, not form.
> 
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
>     *   Evidence: No TO/FROM/RE header followed by prose.
>     *   Result: not this check.
> 
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
>     *   Evidence: No masthead.
>     *   Result: not this check.
> 
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
>     *   Evidence: No running narrative prose.
>     *   Result: not this check.
> 
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
>     *   Evidence: Not an ad.
>     *   Result: not this check.
> 
> Let's double check Check 7.
> Document title: "NEWSPAPER ESTIMATE RECAP - PN05"
> Header: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING"
> Fields: CLIENT: P.M. INC., EST NO: 6089 REVISES EST DTD 02/14/97, DESC: 760A MULTIPLE PRODUCT ROP 1991 & PRIOR ADJUSTMENTS.
> Table: PRODUCT, PERIOD, EST AMT AMOUNT, EST AMT CHANGE, EST AMT LESS C/D.
> Row: 10-MARLBORO, JAN 1996, 136.80-, (blank), 115.74-.
> Bottom: FORM M01A REV 04-14-83.
> Bates number: 2084022615.
> 
> This is an estimate recap from an advertising agency (Leo Burnett) for a client (P.M. Inc.). It shows estimated amounts.
> Check 7: "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> This is exactly an "ESTIMATE RECAP" showing "EST AMT". It is budget.
> 
> Wait, is it a form? "FORM M01A REV 04-14-83".
> Check 10: "administrative form -> form". But Check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." For budget, it says "internal money planning... budget or expense lines...". An estimate recap is money planning. So it's budget.
> 
> Let's confirm the label: `budget`.
> 
> Let's review the scratchpad steps again to be sure.
> 1. file_folder: no, has content.
> 2. handwritten: no, typed.
> 3. fax: no.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. financial document: yes. "ESTIMATE RECAP", "EST AMT". It's an estimate recap for advertising placements. Budget definition explicitly includes "an agency/vendor estimate or recap that projects upcoming placements/periods ... is budget, not invoice."
> 8. specification: no.
> 9. presentation: no.
> 10. form: no, money function overrides.
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no.
> 14. advertisement: no.
> 
> Final label: budget.
> Runner-up: form (because of "FORM M01A" at the bottom), ruled out because Check 7 (financial document) overrides form layout when the content is money planning/tracking (estimate recap).
> Another runner-up: invoice, ruled out because it lists "EST AMT" (estimated amounts) for an "ESTIMATE RECAP", which Check 7 explicitly classifies as budget ("plans projected spend rather than billing completed work"), not invoice (which requires "ACTUAL billable charges").
> 
> The text "FORM M01A REV 04-14-83" is at the bottom left.
> The text "NEWSPAPER ESTIMATE RECAP - PN05" is at the top right.
> The text "LEO BURNETT U.S.A." is at the top left.
> This is clearly a financial document (estimate recap).
> 
> I will output `budget`.

---

### `test_imagesd_d_a_v_dav40c00_ti16801308.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. Just a logo "wka Walt Klein & Associates, Inc." and "ESTIMATE CHANGE ORDER". Bottom right has "T11680-1308" (Bates number).
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of content: title "ESTIMATE CHANGE ORDER", description, table with financial data, approvals. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed, with some handwritten signatures and dates in the approvals section. Not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No resume content.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal masthead, volume, issue, page range.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: Title is "ESTIMATE CHANGE ORDER". It has a table with "Estimate", "Change Order", "New Estimate" columns, showing dollar amounts (6,900.00, 21,600.00, 47,740.00, 100,000.00).
> - Let's look at the definition of invoice vs budget.
> - "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> - Wait, the text says: "A production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... is an invoice."
> - Let's re-read check 7 carefully:
>   - "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
>   - "budget: ... an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - The document is titled "ESTIMATE CHANGE ORDER". It has a description: "Receive 'We Card' orders via 800#. Includes operator training and time, scripting, report interpretations evaluating proper allocation of resources. *2/8/95 change order: TO REFLECT INCREASE IN 800 NUMBER-OPERATOR REQUESTS FROM 10,000 TO 25,000."
> - The table shows "Estimate", "Change Order", "New Estimate". Total New Estimate is 100,000.00.
> - The footnote says: "Estimate is based on estimated personnel and production costs prior to receipt of all final bids, assuming no changes to the job specifications. Final invoice to reflect total actual personnel and production costs."
> - Wait, is this an invoice or a budget?
> - Let's look at the invoice definition again: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed. It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
> - But the footnote says "Final invoice to reflect total actual...". This implies it's NOT the final invoice yet. It's an estimate change order.
> - Let's look at the budget definition: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - This is an "ESTIMATE CHANGE ORDER" that adjusts the estimate from 52,260.00 to 100,000.00. It is planning/projecting spend, not billing completed work. The footnote explicitly says "Final invoice to reflect...". So this is a budget/estimate document.
> - Wait, let's re-read the invoice definition: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges...". This is confusing. It says an "estimate change order" is an invoice IF it lists ACTUAL billable charges. But here it lists estimates.
> - Let's re-read budget: "budget: internal money planning, tracking, or disbursement... Also covers money-only records... an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice."
> - This document is an estimate change order projecting spend (New Estimate = 100,000.00). It is not billing completed work. Therefore, it is a budget.
> - Let's check if there's any other category. Form? It has an approvals block. But check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." Here it lists estimates, not actual charges. So it's budget.
> - Let's re-evaluate: Is it a form? Check 10: "internal authorization/approval forms with an approval signature/date block." But check 7 says financial content overrides form layout if it's a billing/payment page. Is this a billing page? It's an estimate change order. The footnote says "Final invoice to reflect...". So it's not a final invoice. It's a budget/estimate document.
> - Let's look at the exact wording for invoice: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." This implies an estimate change order that bills actual charges is an invoice. But this one doesn't bill actual charges; it changes the estimate.
> - Budget definition: "an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice." This fits perfectly. It's an estimate change order projecting spend.
> 
> Let's double check.
> Title: ESTIMATE CHANGE ORDER
> Table columns: Estimate, Change Order, New Estimate.
> Values: 52,260.00, 47,740.00, 100,000.00.
> Footnote: "Estimate is based on estimated personnel... Final invoice to reflect total actual..."
> This is clearly a budget/estimate document, not an invoice for completed work.
> So Check 7 -> budget.
> 
> Let's check Check 8: specification. No.
> Check 9: presentation. No.
> Check 10: form. It has an approvals block, but check 7 takes precedence for financial documents. "Money function overrides form layout...". Wait, does it override if it's a budget? "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." Yes.
> Check 11: correspondence. No.
> Check 12: news_article. No.
> Check 13: scientific_report. No.
> Check 14: advertisement. No.
> 
> So the label is budget.
> 
> Let's review the invoice vs budget distinction again.
> Invoice: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> Budget: "an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> 
> The document is an "ESTIMATE CHANGE ORDER". It changes the estimate from 52,260 to 100,000. It does not list actual billable charges. The footnote says "Final invoice to reflect total actual...". Thus, it is planning projected spend, not billing completed work. It is a budget.
> 
> Wait, is there any chance it's a form?
> Check 10: "internal authorization/approval forms with an approval signature/date block."
> But Check 7: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> Is this a "billing or payment page"? It's an estimate change order. The budget definition includes "an agency/vendor estimate or recap". So it falls under financial document (Check 7).
> Therefore, budget.
> 
> Let's confirm the evidence for budget:
> - Title: "ESTIMATE CHANGE ORDER"
> - Table with "Estimate", "Change Order", "New Estimate" columns and dollar amounts.
> - Footnote: "Final invoice to reflect total actual personnel and production costs." indicating this is a projection/estimate, not a final bill.
> 
> Runner-up: invoice. Ruled out because the document is an estimate change order projecting future spend (New Estimate = 100,000.00) and explicitly states "Final invoice to reflect total actual...", meaning it does not bill actual completed charges. It is a budget/estimate document.
> 
> Wait, looking closely at the invoice definition: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges...". This is a bit ambiguous. It could mean "an estimate change order [that is] listing ACTUAL billable charges". Since this one doesn't list actual charges, it's not an invoice. It's a budget.
> 
> Final check of the steps:
> 1. file_folder: no, has content.
> 2. handwritten: no, mostly typed.
> 3. fax: no.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. financial document: yes. It's an estimate change order with financial tables. It's a budget because it projects spend and is not a final invoice.
> 8. specification: no.
> 9. presentation: no.
> 10. form: no, check 7 overrides.
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no.
> 14. advertisement: no.
> 
> Label: budget.

---

### `test_imagesw_w_c_e_wce83f00_0001140924.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: No newspaper/magazine masthead. No journal running head. There is a company header "Ted Bates & company, inc./advertising".
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: The page has a lot of content: a header, a table with financial data, notes, signature lines. It's not just an identifier/stamp.
>     *   Result: not this check.
> 
> *   **Check 2: handwritten**
>     *   Evidence: Mostly typed text and a table. There are some handwritten signatures/names ("Contact...", "Client..."), but it's not majority handwritten.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: No survey questions.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
>     *   Evidence: No CV/resume content.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
>     *   Evidence: No journal name/volume/issue/page number.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: "PRODUCTION ESTIMATE REPORT AC14". "BILLING TYPE PROGRESSIVE". Table with "ORIGINAL ESTIMATE", "PRESENT ESTIMATE", "TOTALS (NET)", "COMMISSIONS", "TOTALS (GROSS)". Values like 6500.00. Note: "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES."
>     *   Let's look at the definition of invoice vs budget.
>     *   Invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, let's re-read carefully.
>     *   "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges..." -> Wait, the text says: "It does not have to be titled 'INVOICE' — a voucher, recap, or change order that bills charges already incurred and totals is an invoice. Look for goods sold or one-off services performed (items, quantities, unit prices). ... A running 'BALANCE DUE' column does not make a bill a budget 'statement of account'."
>     *   "budget: ... money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical ... is scientific_report ... Also covers money-only records: ... a provider's periodic customer statement ... is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
>     *   Wait, let's look at the budget definition again: "money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an 'ESTIMATE RECAP' of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
>     *   The document is titled "PRODUCTION ESTIMATE REPORT AC14". It has "ORIGINAL ESTIMATE" and "PRESENT ESTIMATE". It says "ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES IN DESIGN, TYPOGRAPHY, ILLUSTRATION, PLATES NEEDED, ETC MAY ALTER FINAL CHARGES." This is an estimate for future work / projected spend, not a bill for completed work. It's an agency (Ted Bates) providing an estimate to a client (Brown & Williamson Tobacco Corp) for a job (Hispanic World's Fair).
>     *   Wait, is it an invoice? "a production estimate report... listing ACTUAL billable charges". But this says "ESTIMATE... MAY ALTER FINAL CHARGES". It's an estimate.
>     *   Let's check the budget definition: "an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
>     *   This is a "PRODUCTION ESTIMATE REPORT". It projects the cost (6500.00). It's not billing completed work. It's an estimate. So it's budget.
>     *   Let's re-read check 7 carefully.
>     *   "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> This implies if it lists *actual* billable charges, it's an invoice. But this document is an *estimate*. "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES."
>     *   "budget: ... money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
>     *   This document is an estimate report. It's planning projected spend. So it's budget.
>     *   Wait, is it a form? "internal authorization/approval forms with an approval signature/date block." It has "CONTACT...", "CLIENT...", "DATE...". But the primary content is the financial estimate table.
>     *   Let's look at the "Money function overrides form layout" rule. "a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
>     *   Is it an invoice or budget?
>     *   "PRODUCTION ESTIMATE REPORT". "ESTIMATE IS BASED ON JOB AS OF THIS DATE... MAY ALTER FINAL CHARGES." This is clearly an estimate, not a final bill. Estimates are budget (planning future spend).
>     *   Let's check the invoice definition again: "a production estimate report... listing ACTUAL billable charges". This report does *not* list actual billable charges; it lists estimates.
>     *   So it's budget.
> 
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
>     *   Evidence: No material safety data, no product formulation, no "shall/must".
>     *   Result: not this check.
> 
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
>     *   Evidence: Not a slide deck.
>     *   Result: not this check.
> 
> *   **Check 10: ADMINISTRATIVE FORM -> form**
>     *   Evidence: It has a table and signature lines. But check 7 (financial document) takes precedence if financial content is the primary structure. "Money function overrides form layout". The primary structure is the financial estimate table.
>     *   Wait, is an estimate form a form or a budget?
>     *   "budget: ... money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
>     *   This is an agency/vendor estimate. So it's budget.
> 
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
>     *   Evidence: No TO/FROM/RE header followed by prose. No letterhead with external address + salutation + closing. It's a business form/report.
>     *   Result: not this check.
> 
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
>     *   Evidence: No masthead, no news typography.
>     *   Result: not this check.
> 
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
>     *   Evidence: No running narrative prose about research.
>     *   Result: not this check.
> 
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
>     *   Evidence: Not an ad. It's an internal/agency estimate.
>     *   Result: not this check.
> 
> Let's re-evaluate Check 7 (invoice vs budget).
> Document: "Ted Bates & company, inc./advertising". Client: Brown & Williamson Tobacco Corp. Job: PC7581 Hispanic World's Fair.
> Title: "PRODUCTION ESTIMATE REPORT AC14".
> Table columns: WORK CODE, COMMISSION RATE, ORIGINAL ESTIMATE, PRESENT ESTIMATE.
> Row: 64 MISCELLANEOUS, ZERO, 6500.00, 6500.00.
> Totals: 6500.00.
> Note: "ESTIMATE IS BASED ON JOB AS OF THIS DATE. CHANGES IN DESIGN... MAY ALTER FINAL CHARGES."
> This is an estimate of costs for a job. It is not a bill for completed work (invoice). It is a projection of spend (budget).
> Definition of budget: "money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an 'ESTIMATE RECAP' of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> This matches perfectly. It's an agency (Ted Bates) estimate for a client (Brown & Williamson).
> 
> Wait, is it a form?
> Check 10: "administrative form... internal authorization/approval forms with an approval signature/date block."
> But Check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> And "budget: ... money PLANNING for future work is budget: an agency/vendor estimate...".
> So it's budget.
> 
> Let's double check if it could be an invoice.
> "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> The text says "listing ACTUAL billable charges". This document lists "ESTIMATE", not actual charges. The note says "MAY ALTER FINAL CHARGES". So it's not an invoice.
> 
> Therefore, it is a budget.
> 
> Let's check the labels again.
> advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> 
> The document is a "PRODUCTION ESTIMATE REPORT".
> It is a financial document (Check 7).
> It is an estimate (planning future spend), so it is budget.
> 
> Final check of the steps:
> 1. file_folder: No, has content.
> 2. handwritten: No, mostly typed.
> 3. fax: No.
> 4. questionnaire: No.
> 5. resume: No.
> 6. scientific_publication: No.
> 7. financial document: Yes. "PRODUCTION ESTIMATE REPORT", table with estimates, totals. It's an agency estimate for future work. -> budget.
> 8. specification: No.
> 9. presentation: No.
> 10. form: No, financial content overrides.
> 11. correspondence: No.
> 12. news_article: No.
> 13. scientific_report: No.
> 14. advertisement: No.
> 
> The label is budget.

---

### `test_imagesj_j_o_w_jow70f00_0011930077.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a "VOUCHER" header and "BROWN & WILL FARROW TOBACCO CORPORATION" (or similar, looks like "BROWN & WILL FARROW" or "BROWN & WILLIAMSON"). Wait, let's look closer. "BROWN & WILL FARROW TOBACCO CORPORATION" -> "BROWN & WILLIAMSON TOBACCO CORPORATION". It's a voucher.
> 
> **2. Scratchpad checks:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: The page has a lot of content: a voucher form with fields, dates, amounts, descriptions. Not just an ID or stamp.
>     *   Result: not this check.
> 
> *   **Check 2: handwritten**
>     *   Evidence: Mostly typed form fields filled in. There is some handwriting at the bottom ("November 16 '87"), but the majority is a printed form with typed entries.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
>     *   Evidence: No survey questions.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY**
>     *   Evidence: No resume content.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE**
>     *   Evidence: No journal running head.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: The document is titled "VOUCHER". It has "VENDOR NO.", "DATE", "The Franklin Institute", "Benjamin Franklin Parkway", "Philadelphia, PA 19103". "ITEM DESCRIPTION": "Final contribution for grant to above institute for basic research". "ITEM AMOUNT": "$278,000.00". "PAY THIS AMOUNT": "$278,000.00". "Gen, Corp; Contributions- Medical- Other".
>     *   This is a payment voucher / payment request / bill for a grant contribution.
>     *   Let's check the definitions for invoice vs budget.
>     *   **invoice**: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work".
>     *   **budget**: "internal money planning, tracking, or disbursement... a check face or check stub, a check/payment register... a provider's periodic customer statement".
>     *   Wait, the definition says: "a payment voucher... is an invoice". Let's re-read carefully.
>     *   "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work... Look for goods sold or one-off services performed".
>     *   "budget: ... internal money planning, tracking, or disbursement... a check face or check stub...".
>     *   This is a "VOUCHER" from "BROWN & WILLIAMSON TOBACCO CORPORATION". It's paying "The Franklin Institute" a "Final contribution for grant...".
>     *   Is a voucher an invoice or a budget?
>     *   The text says: "invoice: ... a payment voucher ... is an invoice".
>     *   Wait, let's look at the "budget" definition: "internal money planning, tracking, or disbursement... a check face or check stub". A voucher is often part of the accounting process to authorize payment (like a check stub or voucher).
>     *   However, the text explicitly says under **invoice**: "a payment voucher... is an invoice". Let's check that again.
>     *   "invoice: an outside vendor, supplier, or agency states charges owed... a payment voucher, a vendor's price... a receipt, a payment request...".
>     *   Wait, usually a voucher is an internal document to authorize payment. But the text says "a payment voucher... is an invoice". Let's look closer.
>     *   "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work: a production estimate report... listing ACTUAL billable charges...".
>     *   Actually, let's look at the "budget" definition again. "budget: internal money planning, tracking, or disbursement... a check face or check stub...".
>     *   This document is a "VOUCHER" from Brown & Williamson Tobacco Corporation. It records a payment of $278,000.00 to The Franklin Institute.
>     *   Item description: "Final contribution for grant to above institute for basic research".
>     *   This looks like a payment voucher / disbursement record.
>     *   Let's re-read the invoice definition: "invoice: an outside vendor... states charges owed... a payment voucher...". Wait, if the *vendor* states charges, it's an invoice. If the *company* creates a voucher to pay, is it a voucher (form?) or budget?
>     *   "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
>     *   "invoice: ... a payment voucher ... is an invoice". This is a specific bullet point. "a payment voucher... is an invoice".
>     *   Wait, let's look at the text: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work..."
>     *   This implies a payment voucher *is* an invoice category.
>     *   However, let's look at the content. It's a voucher *from* Brown & Williamson *to* The Franklin Institute. It's an internal accounting document (voucher) authorizing payment.
>     *   Is it a budget? "budget: internal money planning, tracking, or disbursement... a check face or check stub...". A voucher is very similar to a check stub or payment record.
>     *   Let's look at the "form" check (Check 10). "internal authorization/approval forms with an approval signature/date block". But Check 7 says "Money function overrides form layout".
>     *   Let's look at the specific wording for invoice: "a payment voucher... is an invoice".
>     *   Let's look at the specific wording for budget: "a check face or check stub... a provider's periodic customer statement... is budget, not invoice".
>     *   This is a one-off grant contribution ("Final contribution for grant..."). It's not a periodic statement.
>     *   It looks like a payment voucher. The text says "a payment voucher... is an invoice".
>     *   Wait, is "payment voucher" in the invoice list referring to a vendor's payment voucher (like a remittance advice) or an internal voucher?
>     *   "an outside vendor... states charges owed... a payment voucher [by the vendor?]". Usually a vendor sends a payment voucher or remittance advice.
>     *   Here, the document is titled "VOUCHER" and has "BROWN & WILL FARROW TOBACCO CORPORATION" (Brown & Williamson). It has "REMITTANCE ADVICE INFO (TS CHAIR ONLY)". It has checkboxes for "MAIL CHECK TO ADDRESS SHOWN", "MAIL CHECK WITH ATTACHMENTS", "OTHER". It has "Yard to W. Pepple". This is an internal payment authorization/voucher from Brown & Williamson.
>     *   Under Check 7, "budget": "internal money planning, tracking, or disbursement... a check face or check stub...". A voucher is a disbursement record.
>     *   Under Check 7, "invoice": "an outside vendor... states charges owed...". The Franklin Institute is the recipient. Is The Franklin Institute stating charges owed? "Final contribution for grant...". It looks like a payment record.
>     *   Let's look at Check 10: "administrative form". "internal authorization/approval forms with an approval signature/date block". This has approval blocks? "Signed by Mr. W. L. DeWitt", "Tax this amount", "Account Name", "Account Code". It has "November 16 '87".
>     *   But Check 7 says "Money function overrides form layout".
>     *   Is this an invoice or a budget?
>     *   "invoice": "billing document for COMPLETED work... listing ACTUAL billable charges". A grant contribution is a payment.
>     *   "budget": "internal money planning, tracking, or disbursement... a check face or check stub". This looks like a check stub or voucher for disbursement.
>     *   Let's re-read the invoice definition carefully: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work".
>     *   The phrase "a payment voucher" is listed under invoice. This suggests that if the document is a payment voucher, it's an invoice.
>     *   However, the context is "an outside vendor... states charges owed... [such as] a payment voucher". This implies the vendor's payment voucher (remittance advice).
>     *   Here, the document is from Brown & Williamson (the payer). It's a voucher *to* pay The Franklin Institute.
>     *   Let's look at the "budget" definition again. "budget: internal money planning, tracking, or disbursement... a check face or check stub...". This is a disbursement record (voucher/check stub equivalent).
>     *   Also, "A contribution/expenditure request or approval form whose whole content is an amount... is budget". This is an approval for a contribution ($278,000). "Gen, Corp; Contributions- Medical- Other".
>     *   Wait, "internal authorization/approval forms with an approval signature/date block" is form (Check 10). BUT "Money function overrides form layout". And "A contribution/expenditure request or approval form whose whole content is an amount... is budget".
>     *   This document is a voucher for a contribution. It has the amount $278,000.00.
>     *   Let's look at the "invoice" definition again. "invoice... a payment voucher...". If I have to choose between invoice and budget.
>     *   The document is a "VOUCHER". It records a payment.
>     *   Let's look at the "form" check (Check 10). "Filled or blank fields... for capturing factual data... internal authorization/approval forms".
>     *   But Check 7 says "Money function overrides form layout".
>     *   Is it an invoice? An invoice is from a vendor. This is from the company (Brown & Williamson) to pay a vendor (Franklin Institute). It's a payment voucher.
>     *   In accounting, a voucher is an internal document. A check is a payment.
>     *   The text says: "budget: ... internal money planning, tracking, or disbursement ... a check face or check stub". A voucher is essentially a check stub or payment authorization.
>     *   The text says: "invoice: ... a payment voucher ... is an invoice". This is confusing. Does "payment voucher" mean the vendor's voucher (remittance advice) or the company's voucher?
>     *   "an outside vendor ... states charges owed ... a payment voucher [from the vendor]". Yes, likely.
>     *   Here, the company is creating the voucher. So it's internal disbursement tracking. -> budget.
>     *   Let's check the labels. "budget" covers "internal money planning, tracking, or disbursement". This is a disbursement of $278,000.
>     *   Also, "A contribution/expenditure request or approval form whose whole content is an amount... is budget". This is an approval for a contribution.
>     *   So "budget" seems appropriate.
> 
>     *   Wait, let's look at the document again.
>     *   Header: "VOUCHER", "BROWN & WILLIAMSON TOBACCO CORPORATION".
>     *   Date: 11/20/87. Vendor No: 18118. Vendor: The Franklin Institute.
>     *   Item Description: "Final contribution for grant to above institute for basic research". Amount: $278,000.00.
>     *   Signed by: Mr. W. L. DeWitt.
>     *   Account Name: Gen, Corp; Contributions- Medical- Other. Account Code: 665 08-4694.
>     *   This is a payment voucher / disbursement record.
>     *   Under Check 7: "budget: internal money planning, tracking, or disbursement... a check face or check stub...". This fits "disbursement".
>     *   Under Check 7: "invoice: an outside vendor... states charges owed". The Franklin Institute is not stating charges owed here; Brown & Williamson is recording the payment. Although the description says "Final contribution for grant...", it's the payer's record.
>     *   Actually, often a "voucher" is the document that accompanies a check. It's a check stub or payment record.
>     *   So "budget" is the best fit for financial document.
> 
>     *   Wait, is it a "form"? Check 10: "internal authorization/approval forms with an approval signature/date block".
>     *   But Check 7 says "Money function overrides form layout". And "A contribution/expenditure request or approval form whose whole content is an amount... is budget".
>     *   This form is about an amount ($278,000). So it's budget.
> 
>     *   Let's reconsider "invoice". "invoice: ... a payment voucher ... is an invoice".
>     *   If the text explicitly says "a payment voucher ... is an invoice", maybe I should follow that?
>     *   "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work".
>     *   The list "an INVOICE header..., a payment voucher, a vendor's price..., a receipt, a payment request..." are all examples of what constitutes an invoice *category*.
>     *   Usually, a "payment voucher" in this context refers to a vendor's document (like a remittance advice or a voucher sent with payment).
>     *   But here, the document is titled "VOUCHER" and is from the corporation.
>     *   If I treat it as a "payment request" or "billing document", it could be invoice. But it's from the payer.
>     *   Let's look at "budget": "internal money planning, tracking, or disbursement". This is definitely internal disbursement tracking.
>     *   So "budget" is the correct financial category.
> 
>     *   Wait, is there a chance it's "form"?
>     *   Check 10: "administrative form". "internal authorization/approval forms".
>     *   Check 7: "Money function overrides form layout". "A contribution/expenditure request or approval form whose whole content is an amount... is budget".
>     *   This document is an approval/disbursement for a contribution amount. So it's budget.
> 
>     *   Let's check if it's a "scientific_report". No, it's a financial document.
>     *   Let's check if it's a "letter". No.
> 
>     *   So the label is "budget".
> 
>     *   Wait, let's look at the "invoice" definition again. "invoice: ... a payment voucher ... is an invoice".
>     *   If the prompt says "a payment voucher ... is an invoice", and this document is a "VOUCHER", maybe it's invoice?
>     *   But the context is "an outside vendor ... states charges owed ... [examples: invoice header, payment voucher, receipt...]". This implies the payment voucher is from the vendor (remittance advice).
>     *   Here, the document is from Brown & Williamson (the buyer/payer). It's an internal voucher.
>     *   Internal vouchers/check stubs are "budget" (tracking/disbursement).
>     *   So "budget" is correct.
> 
>     *   Let's look at the "form" check again.
>     *   "A research grant application ... stays form". This is not an application. This is a payment record.
>     *   "internal authorization/approval forms ... is form". But money overrides.
>     *   "A contribution/expenditure request or approval form whose whole content is an amount ... is budget".
>     *   This is an approval form (signed by W.L. DeWitt) for a contribution amount ($278,000).
>     *   So it is budget.
> 
>     *   Final decision: budget.
> 
>     *   Wait, could it be "invoice"?
>     *   "Final contribution for grant to above institute for basic research".
>     *   If The Franklin Institute sent this as a bill (invoice) for the grant, it would be an invoice.
>     *   But the header says "BROWN & WILL FARROW TOBACCO CORPORATION" (Brown & Williamson). And "REMITTANCE ADVICE INFO". And checkboxes "MAIL CHECK TO...". This is clearly an internal document from Brown & Williamson to process the payment.
>     *   So it's an internal disbursement record -> budget.
> 
>     *   Let's check the labels again.
>     *   advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> 
>     *   Label: budget.
> 
>     *   Wait, is there any other check?
>     *   Check 10: "form". "Filled or blank fields...".
>     *   But Check 7 says "Money function overrides form layout".
>     *   And "A contribution/expenditure request or approval form whose whole content is an amount... is budget".
>     *   This fits perfectly.
> 
>     *   One more check: "invoice".
>     *   "invoice: ... a payment voucher ... is an invoice".
>     *   If the text considers *any* payment voucher as an invoice, then this is invoice.
>     *   "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work".
>     *   The dash after "SOLD" suggests the list follows. "an INVOICE header..., a payment voucher...". These are examples of invoice-type documents.
>     *   Usually, a "payment voucher" is a document from the vendor (remittance advice) or a document from the company (internal voucher).
>     *   If it's an internal voucher, it's tracking disbursement -> budget.
>     *   If it's a vendor's payment voucher (remittance advice), it's invoice.
>     *   This document is from Brown & Williamson. It's an internal voucher.
>     *   So it's budget.
> 
>     *   Let's look at the "budget" definition: "internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register...".
>     *   A voucher is very close to a check stub or payment register entry.
>     *   So "budget" is the right label.
> 
>     *   Wait, is it "form"?
>     *   The document is a form (fields, boxes).
>     *   But Check 7 says "Money function overrides form layout".
>     *   And "A contribution/expenditure request or approval form whose whole content is an amount... is budget".
>     *   So "budget" overrides "form".
> 
>     *   Final check: "invoice".
>     *   "invoice: ... a payment voucher ... is an invoice".
>     *   If I strictly follow "a payment voucher ... is an invoice", then it's invoice.
>     *   But the context is "an outside vendor ... states charges owed". This document is from the company, not the vendor stating charges. The company is stating they are paying.
>     *   So it's not an invoice in the sense of "vendor states charges owed".
>     *   It is a budget document (internal disbursement).
> 
>     *   Let's assume the label is "budget".
> 
>     *   Wait, looking closely at the text: "Final contribution for grant to above institute for basic research".
>     *   This is a payment.
>     *   Label: budget.
> 
>     *   Let's reconsider "invoice".
>     *   Sometimes "voucher" is used interchangeably.
>     *   But the definition for budget includes "check face or check stub". A voucher is the document that supports a check. It's part of the disbursement process.
>     *   So "budget" is correct.
> 
>     *   One detail: "Gen, Corp; Contributions- Medical- Other". This is an account code for contributions.
>     *   Contributions are budget items.
> 
>     *   Final conclusion: budget.

---

### `test_imagesd_d_a_v_dav40c00_ti16801308.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. Just a company logo "wka Walt Klein & Associates, Inc." and a Bates number "T11680-1308" at the bottom right.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of content: "ESTIMATE CHANGE ORDER", tables, descriptions, approvals. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed, with a signature and date in the approvals section. Not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax cover sheet header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions or transmittal for a survey.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No CV/resume content.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal masthead, volume, issue, page range.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: Title is "ESTIMATE CHANGE ORDER". It has a table with "Estimate", "Change Order", "New Estimate" columns, showing dollar amounts (6,900.00, 21,600.00, 47,740.00, 100,000.00).
> - Let's look at the definition of invoice vs budget.
> - invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, the text says: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges... is an invoice."
> - budget: "an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - Let's read the document carefully.
> - Title: "ESTIMATE CHANGE ORDER"
> - Description: "Receive 'We Card' orders via 800#. includes operator training and time, scripting, report interpretations evaluating proper allocation of resources. *2/8/95 change order: TO REFLECT INCREASE IN 800 NUMBER-OPERATOR REQUESTS FROM 10,000 TO 25,000."
> - Table:
>   - 800 Number - Fax Contacts Total: Estimate 6,900.00, New Estimate 6,900.00
>   - Management 800 Number - Operator: Estimate 23,760.00, Change Order 47,740.00, New Estimate 71,500.00
>   - Telephone Operators Total: Estimate 45,360.00, Change Order 47,740.00, New Estimate 93,100.00
>   - TOTAL: Estimate 52,260.00, Change Order 47,740.00, New Estimate 100,000.00
> - Note at bottom: "Estimate is based on estimated personnel and production costs prior to receipt of all final bids, assuming no changes to the job specifications. Final invoice to reflect total actual personnel and production costs."
> - This is an "ESTIMATE CHANGE ORDER". It is modifying an estimate. It is not billing for completed work (it says "Final invoice to reflect total actual..."). It is planning/projecting spend or adjusting the estimate for upcoming work.
> - Wait, check 7 says: "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." But this is an *estimate* change order, not actual charges. "Estimate is based on estimated personnel... Final invoice to reflect total actual..."
> - Let's re-read budget definition: "budget: internal money planning, tracking, or disbursement... ALSO a provider's periodic customer statement... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice."
> - This is an estimate change order for future work (increasing operator requests from 10,000 to 25,000). It's an estimate. So it's budget.
> - Wait, is it a form? Check 10: "internal authorization/approval forms with an approval signature/date block." But check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." And "an agency/vendor document that lists actual charges and totals owed is an invoice... never a form." But this is an estimate, not actual charges. Is an estimate a budget? Yes, "Money PLANNING for future work is budget: an agency/vendor estimate... plans projected spend rather than billing completed work — budget, not invoice."
> - Let's check if there's any other category. It has an "Approvals" block with signatures. But the primary content is the financial estimate/change order.
> - Let's re-evaluate "invoice" vs "budget".
> - "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> This requires listing ACTUAL billable charges. The document says "Estimate is based on estimated personnel... Final invoice to reflect total actual...". So it does NOT list actual billable charges. It lists estimates.
> - "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> - This perfectly matches "budget". It's an estimate change order planning projected spend.
> 
> Let's double check check 10 (form). "internal authorization/approval forms with an approval signature/date block." But check 7 says financial content overrides form layout if it's a billing/payment page. Is an estimate change order a billing/payment page? It's a financial document. "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." An estimate change order is a financial document (budget).
> 
> Let's review the exact text of check 7:
> "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed. It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
> "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> 
> The document is titled "ESTIMATE CHANGE ORDER". The description says "TO REFLECT INCREASE IN 800 NUMBER-OPERATOR REQUESTS FROM 10,000 TO 25,000." The note says "Final invoice to reflect total actual personnel and production costs." This means it is NOT billing charges already incurred. It is planning/projecting spend. Therefore, it is a budget.
> 
> Wait, is there any chance it's a form?
> Check 10: "internal authorization/approval forms with an approval signature/date block."
> But check 7: "Money function overrides form layout... an agency/vendor document that lists actual charges and totals owed is an invoice... never a form." What about an estimate? "Money PLANNING for future work is budget...". Budget is under check 7. Check 7 precedes check 10. So if it's budget, it's budget.
> 
> Let's confirm the evidence for budget:
> - Title: "ESTIMATE CHANGE ORDER"
> - Content: Table with "Estimate", "Change Order", "New Estimate" columns, dollar amounts.
> - Note: "Estimate is based on estimated personnel... Final invoice to reflect total actual..."
> - Function: Money planning for future work (projecting spend).
> 
> Runner-up: invoice. Ruled out because the document is an estimate change order for future work (projecting spend), not billing actual charges already incurred (it explicitly states "Final invoice to reflect total actual...").
> 
> Let's check if there's any other check.
> Check 8: specification. No.
> Check 9: presentation. No.
> Check 10: form. Has approval block, but financial content (budget) overrides.
> Check 11: correspondence. No.
> Check 12: news_article. No.
> Check 13: scientific_report. No.
> Check 14: advertisement. No.
> 
> So the label is budget.
> 
> Wait, let's re-read the invoice definition carefully: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> The text says "ESTIMATE CHANGE ORDER". But it also says "listing ACTUAL billable charges". This document does NOT list actual billable charges. It lists estimates. So it doesn't fit the invoice definition's requirement for actual charges.
> The budget definition says: "an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> This fits perfectly.
> 
> Let's do a quick pass of the scratchpad rules.
> - Pre-scan: No mail header, no masthead.
> - Check 1: file_folder. No, has content.
> - Check 2: handwritten. No, mostly typed.
> - Check 3: fax. No.
> - Check 4: questionnaire. No.
> - Check 5: resume. No.
> - Check 6: scientific_publication. No.
> - Check 7: financial document. Yes, "ESTIMATE CHANGE ORDER" with financial tables. It's an estimate for future work, so budget.
> - Runner-up: invoice. Ruled out because it's an estimate for future work, not actual charges.
> 
> Final label: budget.

---

## news_article → scientific_publication (9 errors)

### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right says "Vol. 119, No. 4", "Printed in U.S.A.". Bottom center has page number "624". Bottom right has "T10447-0692". This is a journal running head/footer.
> 
> **Check 1: file_folder**
> - Evidence: The page has a full article with title, authors, abstract, and running prose. Not just an identifier.
> - Result: not this check.
> 
> **Check 2: handwritten**
> - Evidence: Mostly typed text. There is a handwritten "Lung C." at the top right, but it's not majority handwritten.
> - Result: not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No fax cover sheet header.
> - Result: not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - Evidence: Not a survey.
> - Result: not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - Evidence: Not a resume.
> - Result: not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right: "Vol. 119, No. 4", "Printed in U.S.A.". Bottom center: "624". This is a named journal + volume/issue + page number + copyright on THIS page.
> - Result: YES. Stop here.
> 
> Runner-up: scientific_report, ruled out because the page carries its own journal running head/footer (American Journal of Epidemiology, Vol. 119, No. 4, page 624, copyright 1984), making it a published reprint (check 6 precedes check 13).
> 
> Let's double check.
> Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES"
> Authors: RICHARD G. STEVENS and SURESH H. MOOLGAVKAR
> Journal: AMERICAN JOURNAL OF EPIDEMIOLOGY, Vol. 119, No. 4, 1984.
> This perfectly matches check 6.
> 
> Final label: scientific_publication.

---

### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right says "Vol. 119, No. 4 Printed in U.S.A.". Bottom center says "624". Bottom right says "T10447-0692". This is a journal running head/footer with volume, issue, page number, and copyright. This points strongly to check 6 (scientific_publication).
> 
> **Check 1: file_folder**
> - Evidence: The page has a full article with title, authors, abstract, and running prose. Not just an identifier.
> - Result: not this check.
> 
> **Check 2: handwritten**
> - Evidence: Mostly typed text. There is a handwritten "Lung Ca" at the top right, but it's not majority handwritten.
> - Result: not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No fax cover sheet header.
> - Result: not this check.
> 
> **Check 4: questionnaire**
> - Evidence: No survey instrument.
> - Result: not this check.
> 
> **Check 5: resume**
> - Evidence: Not a CV/resume.
> - Result: not this check.
> 
> **Check 6: scientific_publication**
> - Evidence: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984", page number "624". This is a published journal article.
> - Result: STOP HERE. This is check 6.
> 
> Runner-up: scientific_report, ruled out because the page carries its own journal running head/footer with journal name, volume, issue, page number, and copyright (check 6 precedes check 13).
> 
> Final label: scientific_publication.

---

### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead or running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health". Top right says "Vol. 119, No. 4", "Printed in U.S.A.". Bottom center says "624". Bottom right says "T10447-0692". This is a journal running head/footer with volume, issue, page number, and copyright. This points strongly to check 6 (scientific_publication).
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a full article with title, authors, abstract, and running text. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed text. There is a handwritten "Lung Ca" at the top right, but it's not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No fax cover sheet header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: Not a survey instrument.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: Not a resume.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health". Top right: "Vol. 119, No. 4". Bottom center: "624". This is a named journal ("AMERICAN JOURNAL OF EPIDEMIOLOGY") plus publication identifiers (volume 119, issue 4, page 624, copyright 1984) on THIS page itself.
> - STOP HERE. This is check 6.
> 
> Runner-up: scientific_report, ruled out because the page carries its own journal running head/footer with journal name, volume, issue, page number, and copyright (check 6 precedes check 13).
> 
> Final label: scientific_publication.

---

### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health", "Printed in U.S.A.", page number "624". This is a journal running head/footer.
> 
> **Check 1: file_folder**
> - Evidence: The page has a full article with title, authors, abstract, and running prose. Not just an identifier.
> - Result: not this check.
> 
> **Check 2: handwritten**
> - Evidence: Mostly typed text. There is a handwritten "Lung Ca" at the top right, but it's not majority handwritten.
> - Result: not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No fax header.
> - Result: not this check.
> 
> **Check 4: questionnaire**
> - Evidence: No survey instrument.
> - Result: not this check.
> 
> **Check 5: resume**
> - Evidence: Not a CV/resume.
> - Result: not this check.
> 
> **Check 6: scientific_publication**
> - Evidence: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984", page number "624". This is a named journal + volume + issue + page range + copyright on THIS page.
> - Result: YES. Stop here.
> 
> Runner-up: scientific_report, ruled out because the page carries its own journal running head/footer (American Journal of Epidemiology, Vol 119, No 4, page 624, copyright 1984), making it a published reprint (check 6 precedes check 13).
> 
> Final label: scientific_publication.

---

### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I need to follow a specific scratchpad procedure, checking conditions 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead or running head: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health", "Printed in U.S.A.", page number "624". This is a journal running head/footer.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a full article with title, authors, abstract, and running text. Not just an identifier.
> - Result: not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed text. There is a handwritten "Lung Ca" at the top right, but it's not majority handwritten.
> - Result: not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No fax cover sheet header.
> - Result: not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions or transmittal.
> - Result: not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: Not a resume.
> - Result: not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984", page number "624". This is a named journal with volume, issue, page range, and copyright on this page.
> - Result: STOP HERE. This is check 6.
> 
> Runner-up: scientific_report, ruled out because the page carries its own journal running head/footer with journal name, volume, issue, page number, and copyright line (check 6 precedes check 13).
> 
> Final label: scientific_publication.

---

### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right says "Vol. 119, No. 4 Printed in U.S.A.". Bottom center says "624". Bottom right says "T10447-0692". This is a journal running head/footer with volume, issue, page number, and copyright. This points strongly to check 6 (scientific_publication).
> 
> **Check 1: file_folder**
> - Evidence: No, there is a full article with title, authors, abstract, and running text.
> - Not this check.
> 
> **Check 2: handwritten**
> - Evidence: There is a handwritten "Lung C." at the top right, but the majority of the content is printed text.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No fax header.
> - Not this check.
> 
> **Check 4: questionnaire**
> - Evidence: No survey instrument.
> - Not this check.
> 
> **Check 5: resume**
> - Evidence: No career history.
> - Not this check.
> 
> **Check 6: scientific_publication**
> - Evidence: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984", page number "624". This is a published journal article.
> - STOP HERE. This is check 6.
> 
> Let's double check.
> Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES"
> Authors: RICHARD G. STEVENS and SURESH H. MOOLGAVKAR
> Journal: AMERICAN JOURNAL OF EPIDEMIOLOGY, Vol. 119, No. 4, 1984.
> This is clearly a scientific publication.
> 
> Runner-up: scientific_report. Ruled out because the page itself carries a journal running head (American Journal of Epidemiology, Vol. 119, No. 4, page 624, copyright 1984), making it a published reprint (check 6), not an internal write-up (check 13).
> 
> Final label: scientific_publication.

---

### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header:** None. There's a handwritten "Lung Ca" at the top right, but no From/To/Sent/Subject.
> - **Masthead/Running head:**
>     - Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved".
>     - Top right: "Vol. 119, No. 4", "Printed in U.S.A.".
>     - Bottom center: "624".
>     - Bottom right: "T10447-0692" (Bates number).
>     - This looks like a page from a scientific journal. Specifically, the American Journal of Epidemiology.
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: The page has a full article title "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES", authors, abstract, and running text.
>     *   Result: Not this check.
> 
> *   **Check 2: handwritten**
>     *   Evidence: There is a handwritten note "Lung Ca" at the top right. But the rest is typed text.
>     *   Result: Not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: No fax header.
>     *   Result: Not this check.
> 
> *   **Check 4: questionnaire**
>     *   Evidence: No survey questions.
>     *   Result: Not this check.
> 
> *   **Check 5: resume**
>     *   Evidence: No career history.
>     *   Result: Not this check.
> 
> *   **Check 6: scientific_publication**
>     *   Evidence: Top left header: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health". Top right: "Vol. 119, No. 4". Bottom center: page number "624". The text is an article "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES" by Richard G. Stevens and Suresh H. Moolgavkar. It cites "Am J Epidemiol 1984;119:624-41".
>     *   This matches the criteria for scientific_publication: named journal ("AMERICAN JOURNAL OF EPIDEMIOLOGY") + publication identifier (Vol. 119, No. 4, page 624, copyright line).
>     *   Result: STOP HERE. This is check 6.
> 
> *   **Check 7: FINANCIAL DOCUMENT**
>     *   (Skipped because check 6 matched)
> 
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
>     *   (Skipped)
> 
> *   **Check 9: SLIDE DECK...**
>     *   (Skipped)
> 
> *   **Check 10: ADMINISTRATIVE FORM**
>     *   (Skipped)
> 
> *   **Check 11: CORRESPONDENCE**
>     *   (Skipped)
> 
> *   **Check 12: PUBLISHED JOURNALISM**
>     *   (Skipped)
> 
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP**
>     *   (Skipped)
> 
> *   **Check 14: PROMOTIONAL MATERIAL**
>     *   (Skipped)
> 
> **Final Decision:**
> The page is a reprint from the "American Journal of Epidemiology", Vol 119, No 4, page 624. It has the journal name, volume, issue, copyright, and page number. This fits Check 6 perfectly.
> 
> Runner-up: scientific_report. Ruled out because the page carries its own journal running head (American Journal of Epidemiology, Vol 119, No 4, page 624), making it a published scientific publication (check 6 precedes check 13).
> 
> Let's double check the text.
> "AMERICAN JOURNAL OF EPIDEMIOLOGY"
> "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health."
> "Vol. 119, No. 4"
> "Printed in U.S.A."
> Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES"
> Authors: Richard G. Stevens and Suresh H. Moolgavkar.
> Reference in text: "Am J Epidemiol 1984;119:624-41."
> Page number at bottom: 624.
> 
> This is definitely a scientific_publication.
> 
> One detail: "Lung Ca" is handwritten at the top. This is just a marginal note, likely from a reader or archivist. It doesn't make the page "handwritten" (Check 2 requires *most* content to be freeform handwriting).
> 
> The page is a scientific publication.
> 
> Label: scientific_publication.

---

### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right says "Vol. 119, No. 4 Printed in U.S.A.". Bottom center says "624". Bottom right says "T10447-0692". This is a journal running head/footer with volume, issue, page number, and copyright.
> 
> **Check 1: file_folder**
> - Evidence: The page has a full article with title, authors, abstract, and running prose. Not just an identifier.
> - Result: not this check.
> 
> **Check 2: handwritten**
> - Evidence: Mostly typed text. There is a handwritten "Lung C." at the top right, but it's not majority handwritten.
> - Result: not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No fax cover sheet header.
> - Result: not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - Evidence: Not a survey.
> - Result: not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - Evidence: Not a resume.
> - Result: not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984", page number "624". This is a named journal + volume + issue + page range/copyright on THIS page.
> - Result: YES. STOP HERE.
> 
> Let's double check.
> Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES"
> Authors: RICHARD G. STEVENS and SURESH H. MOOLGAVKAR
> Journal info at top: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved", "Printed in U.S.A."
> Page number at bottom: "624"
> This perfectly matches check 6: "a named journal on the page plus a publication identifier (volume/issue, page range, DOI, journal copyright line...)".
> 
> Runner-up: scientific_report. Ruled out because the page carries its own journal running head/footer with journal name, volume, issue, page number, and copyright, making it a published reprint (scientific_publication) rather than an internal write-up.
> 
> Final label: scientific_publication.

---

### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I need to follow a specific scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright c 1984 by The Johns Hopkins University School of Hygiene and Public Health", "Printed in U.S.A.", page number "624". This is a journal running head/footer.
> 
> **Check 1: file_folder**
> - Evidence: No, there is a full article with text, title, authors, abstract. Not just an ID/stamp.
> - Not this check.
> 
> **Check 2: handwritten**
> - Evidence: There is a handwritten note "Lung C." at the top right, but the majority of the content is typed text.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No fax cover sheet header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - Evidence: No survey questions or transmittal.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - Evidence: No resume/CV.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright c 1984", page number "624". This is a named journal with volume, issue, page range, copyright on THIS page.
> - Stop here. This is scientific_publication.
> 
> **Runner-up:** scientific_report. Ruled out because the page carries its own journal running head/footer (American Journal of Epidemiology, Vol 119, No 4, page 624, copyright 1984), making it a published reprint (check 6), not an internal write-up.
> 
> Let's double check.
> The page has:
> - "AMERICAN JOURNAL OF EPIDEMIOLOGY"
> - "Vol. 119, No. 4"
> - "Copyright c 1984 by The Johns Hopkins University School of Hygiene and Public Health"
> - "Printed in U.S.A."
> - Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES"
> - Authors: RICHARD G. STEVENS and SURESH H. MOOLGAVKAR
> - Abstract and text.
> - Page number 624 at the bottom.
> - Bates number TI0447-0692 at the bottom right.
> 
> This perfectly matches Check 6: PUBLISHED EVIDENCE -> scientific_publication.
> Evidence: named journal ("AMERICAN JOURNAL OF EPIDEMIOLOGY") plus publication identifier (Vol. 119, No. 4, page 624, copyright line).
> 
> Final label: scientific_publication.

---

## budget → form (6 errors)

### `test_imagesu_u_s_a_usa07d00_timo0000799.tif.png`
**Expected:** `budget` | **Predicted:** `form`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify the provided document into one of 16 categories.
> I will follow the scratchpad procedure, checking each condition in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITRG No.001 P.02". This looks like internal routing/metadata, not a journal masthead or newspaper masthead. "TIMO 0000799" and "Confidential Missouri Tobacco Litigation Case No. 972-1455" are Bates/litigation stamps.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a title "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", filled fields, signatures. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: The page has typed fields and labels, filled by hand. Not majority handwritten freeform.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax cover sheet header. The top line is internal routing info.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: Not a survey instrument.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: Not a resume.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal running head.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". Contains "Amount 250.00", "Account Code", "Check Payable to".
> - Wait, check 7 says: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget".
> - This is a "CONTRIBUTION REQUEST" with an amount, account code, check payable to, and approval signatures. It's an authorization/request for a contribution.
> - Let's look at check 10: "internal authorization/approval forms with an approval signature/date block".
> - Let's re-read check 7: "budget: ... a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category (amounts need not be legible)."
> - Wait, check 7 says: "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
> - Let's read carefully: "budget: ... ALSO a provider's periodic customer statement... ALSO a contribution/expenditure request or approval form whose whole content is an amount..."
> - BUT check 10 says: "internal authorization/approval forms with an approval signature/date block".
> - Let's re-read check 7 caveat: "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> - Ah! "authorizing a single expenditure is not planning or tracking money." This is a single contribution request for $250.00. It has an approval signature block ("Approved by: Regional Vice President's signature", "Senior Vice President's signature").
> - Therefore, it is an internal authorization/approval form -> form (check 10).
> 
> Let's double check check 7 vs check 10.
> Check 7: "budget: ... a contribution/expenditure request or approval form whose whole content is an amount..."
> Check 7 caveat: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> This document is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It requests a single expenditure ($250.00) and has approval signatures. It is an authorization form. Thus, it falls under the caveat in check 7 and goes to check 10.
> 
> Let's check check 10: "ADMINISTRATIVE FORM -> form"
> - "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
> - This document has fields (Name, Address, Amount, Account Code), checkboxes (State/Local), and approval signature blocks.
> - It is a filled form.
> 
> Let's review the whole document:
> Title: POLITICAL CAMPAIGN CONTRIBUTION REQUEST
> Fields: Date, State/Local checkbox, Recipient Information (Name, Address, Current Office, etc.), Contribution Information (Amount, Account Code, Check Payable to, Address, Notes).
> Signatures: Approved by (Regional Vice President, Senior Vice President).
> Footer: Confidential Missouri Tobacco Litigation Case No. 972-1455, TIMO 0000799.
> 
> This is clearly a form. Specifically, an internal authorization/approval form for a contribution.
> 
> Let's check if there's any other category.
> - invoice: No, it's a request/authorization, not a bill from a vendor.
> - budget: No, it's a single expenditure authorization, not planning/tracking.
> - letter/memo: No.
> 
> So the label is `form`.
> 
> Let's trace the checks:
> 1. file_folder: no, has content.
> 2. handwritten: no, typed template filled by hand.
> 3. fax: no.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. financial document: has money ($250), but it's a single expenditure authorization form with approval signatures. Caveat in check 7 says this is a form (check 10), not budget.
> 8. specification: no.
> 9. presentation: no.
> 10. form: yes, filled fields, checkboxes, approval signature block. "internal authorization/approval forms with an approval signature/date block".
> 
> Runner-up: budget. Ruled out because check 7 caveat explicitly states that an internal expenditure-authorization form with an approval signature block authorizing a single expenditure is a form (check 10), not budget.
> 
> Final label: form.

---

### `test_imagesu_u_s_a_usa07d00_timo0000799.tif.png`
**Expected:** `budget` | **Predicted:** `form`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITigation No.001 P.02" at the top. This looks like internal routing/metadata, not a journal masthead or newspaper masthead. Bottom has "Confidential Missouri Tobacco Litigation Case No. 972-1455" and "TIMO 0000799".
> 
> **Check 1: file_folder**
> - Content: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", filled fields, signature blocks. Not just an identifier/stamp.
> - Result: not this check.
> 
> **Check 2: handwritten**
> - Most content is typed form with handwritten entries. Not majority freeform handwriting.
> - Result: not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - No "FACSIMILE" or "FAX COVER SHEET" header. The top line is internal routing.
> - Result: not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Not a survey instrument. It's a contribution request.
> - Result: not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Not a resume.
> - Result: not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - No journal name/volume/issue/page number on the page itself.
> - Result: not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". Contains "Amount 250.00", "Account Code", "Check Payable to".
> - Is this an invoice or budget?
> - Invoice: outside vendor states charges owed. No.
> - Budget: internal money planning, tracking, or disbursement. "contribution/expenditure request or approval form whose whole content is an amount" -> budget. Wait, let's look at the labels.
> - "A contribution/expenditure request or approval form whose whole content is an amount... is budget, not invoice".
> - Wait, is it a form or budget?
> - Check 10: ADMINISTRATIVE FORM -> form. "internal authorization/approval forms with an approval signature/date block".
> - Let's re-read Check 7: "A contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts... ALSO a provider's periodic customer statement... is budget, not invoice".
> - Wait, Check 7 says: "budget: ... A contribution/expenditure request or approval form whose whole content is an amount ... is budget".
> - But Check 10 says: "internal authorization/approval forms with an approval signature/date block" is form.
> - Let's check the priority. Check 7 is before Check 10.
> - "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> - "A contribution/expenditure request or approval form whose whole content is an amount ... is budget".
> - This page is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It has fields for recipient info, contribution information (Amount, Account Code, Check Payable to), and approval signatures.
> - Is it budget or form?
> - Check 7: "budget: internal money planning, tracking, or disbursement ... A contribution/expenditure request or approval form whose whole content is an amount ... is budget".
> - Wait, the text says: "But an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> - Ah! "authorizing a single expenditure is not planning or tracking money." -> form (check 10).
> - This is a "CONTRIBUTION REQUEST" with an amount ($250.00) and approval signatures. It's authorizing a single expenditure/contribution. So it's a form, not budget.
> - Let's re-read carefully: "But an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> - This page has "Amount 250.00", "Check Payable to Koller for Rep". It's authorizing a single expenditure (a political contribution). So it's a form.
> - Let's check Check 10: "administrative form ... internal authorization/approval forms with an approval signature/date block." Yes, this matches perfectly.
> 
> Let's double check Check 7 vs Check 10.
> Check 7: "invoice: ... A hotel/motel guest bill ... is an invoice". "budget: ... A contribution/expenditure request or approval form whose whole content is an amount ... is budget".
> Wait, the caveat in Check 7 says: "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> This page is exactly an internal expenditure-authorization form (a contribution request with approval signatures). So it falls under the caveat and is a form (check 10).
> 
> Let's check Check 10: "ADMINISTRATIVE FORM -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; ... internal authorization/approval forms with an approval signature/date block."
> This page has:
> - Title: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST"
> - Fields: Date, State/Local checkboxes, Recipient Information (Name, Address, Current Office, etc.), Contribution Information (Amount, Account Code, Check Payable to, Address, Notes).
> - Approval block: "Approved by: (Regional Vice President's signature), (Senior Vice President's signature)".
> - This is a filled administrative form with an approval block.
> 
> Therefore, Check 10 is the correct match.
> 
> Let's quickly review other checks to be sure.
> Check 8: specification. No.
> Check 9: presentation. No.
> Check 11: correspondence. No.
> Check 12: news_article. No.
> Check 13: scientific_report. No.
> Check 14: advertisement. No.
> 
> Final classification: form.
> 
> Wait, is there any possibility it's budget?
> "budget: ... A contribution/expenditure request or approval form whose whole content is an amount ... is budget"
> But the caveat says: "But an internal expenditure-authorization form ... with an approval signature/date block but no billable charges is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> This page authorizes a single expenditure ($250 contribution). It has an approval signature block. So it's a form.
> 
> Let's confirm the exact wording of Check 10: "internal authorization/approval forms with an approval signature/date block."
> Yes, this matches perfectly.
> 
> Scratchpad:
> - file_folder: no — has substantial body content (form fields, title, signatures).
> - handwritten: no — mostly typed form with handwritten entries.
> - fax: no — no fax cover sheet header.
> - questionnaire: no — not a survey instrument.
> - resume: no — not a career history.
> - scientific_publication: no — no journal identifier.
> - financial (invoice/budget): no — it's an internal expenditure-authorization form authorizing a single contribution, which the check 7 caveat explicitly excludes from budget and assigns to form (check 10).
> - specification: no — not a product/material doc.
> - presentation: no — not a slide deck or cover.
> - form: yes — titled "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", has filled fields (recipient info, contribution amount, account code), and an internal authorization/approval signature block (Regional VP, Senior VP). Matches check 10.
> - correspondence: no — not an email, memo, or letter.
> - news_article: no — no masthead or journalistic layout.
> - scientific_report: no — no running narrative prose.
> - advertisement: no — not promotional material.
> 
> Runner-up: budget, ruled out because the page is an internal expenditure-authorization form authorizing a single contribution with an approval signature block, which the check 7 caveat explicitly classifies as a form (check 10) rather than budget.
> 
> Label: form.

---

### `test_imagesa_a_c_y_acy93e00_2040329511.tif.png`
**Expected:** `budget` | **Predicted:** `form`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "11/16/89" and "2040329451". No journal masthead.
> 
> **Check 1: file_folder**
> - Evidence: The page has a large table with data ("PRICE VALUE ESTIMATES", "YEAR", "INDUSTRY VOLUME++", "PM-USA PRICE VALUE", etc.). It has real content (a table of data). Not file_folder.
> 
> **Check 2: handwritten**
> - Evidence: No handwriting. All text is typed. Not handwritten.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No fax header. Not fax.
> 
> **Check 4: questionnaire**
> - Evidence: No survey questions. Not questionnaire.
> 
> **Check 5: resume**
> - Evidence: No career history. Not resume.
> 
> **Check 6: scientific_publication**
> - Evidence: No journal name, volume, issue, page range, DOI, or copyright line belonging to a journal. Not scientific_publication.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: The table contains "PRICE VALUE ESTIMATES", "INDUSTRY VOLUME++", "PM-USA PRICE VALUE", "SHARE", "% CHANGE VS. YAG", "VOLUME*", "DIFF". It has years 1983-1994. It shows projections ("*PROJECTIONS", "**(BILLIONS)"). This looks like a budget or financial projection/forecast table. Wait, let's look closer. It's a table of estimates. Is it an invoice? No, it's not billing for goods. Is it a budget? "budget: internal money planning, tracking, or disbursement... forecast vs. actual... money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice." This table shows "PRICE VALUE ESTIMATES" with years 1983-1994, including projections for 1991-1994. It's a financial forecast/estimate. Wait, let's check check 10.
> 
> **Check 8: specification**
> - Evidence: No material safety data, product formulation, "shall/must" language. Not specification.
> 
> **Check 9: presentation**
> - Evidence: The page is a table. Not a slide deck. Not a presentation.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - Evidence: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)... is a form (this check)". The page is a large table titled "PRICE VALUE ESTIMATES" with rows (years 1983-1994) and columns (INDUSTRY VOLUME, PM-USA PRICE VALUE, etc.). It is a standalone labeled data chart/table. Wait, is it a form? "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values); a filled analytical or lab data sheet... is a form". Yes, a standalone labeled data chart or table is a form. Let's re-read check 7. "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This is a table of estimates/projections. Is it a budget? "budget: internal money planning... forecast vs. actual...". This is "PRICE VALUE ESTIMATES" with projections. It could be budget. But check 10 says "A standalone labeled data chart or table... is a form". Wait, check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." But this is a table of data. Let's look at check 7 again: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This is a line-item table of financial data (volume, price value, share, projections). Is it an invoice or budget? It's estimates/projections. "money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods... plans projected spend rather than billing completed work — budget, not invoice." This table projects volume and price value for 1991-1994. It's a financial forecast. So it could be budget.
> Wait, let's look at the labels. "form" is check 10. "budget" is check 7.
> Let's re-read check 10: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)... is a form (this check)".
> Let's re-read check 7: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face."
> If it's a financial table, does check 7 override check 10? "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." But this isn't a billing page. It's a table of estimates.
> Actually, let's look at the table content: "PRICE VALUE ESTIMATES", "YEAR", "INDUSTRY VOLUME++", "PM-USA PRICE VALUE", "SHARE", "% CHANGE VS. YAG", "VOLUME*", "DIFF". This is a data table. Is it a form? A form captures factual data. This table *presents* data. "A standalone labeled data chart or table... is a form". Wait, is a table of published data a form? "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values); a filled analytical or lab data sheet... is a form". Yes, the rule explicitly says a standalone labeled data chart or table is a form.
> But wait, check 7: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This is a line-item table of financial content (price value, volume, share). Is it an invoice or budget? It's not an invoice (no vendor, no charges owed). Is it a budget? "budget: internal money planning, tracking, or disbursement... forecast vs. actual...". This is "ESTIMATES" and "PROJECTIONS". It's a forecast. So it could be budget.
> Let's check the balance of labels. "form, scientific_report, and handwritten are historically the most over-predicted labels; news_article and presentation are historically under-predicted."
> If I classify this as "form" (check 10), it fits "A standalone labeled data chart or table".
> If I classify as "budget" (check 7), it fits "forecast... plans projected spend". But this is "PRICE VALUE ESTIMATES" for the industry and PM-USA. It's market data, not necessarily internal money planning. "PM-USA" is Philip Morris USA. "INDUSTRY" is the tobacco industry. This is market share and price value estimates. It's not an internal budget. It's a data table.
> Therefore, check 10 (form) is the best fit for a standalone labeled data chart/table.
> Wait, let's re-read check 10 carefully: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)... is a form (this check)".
> The page is exactly a standalone labeled data chart/table. Title: "PRICE VALUE ESTIMATES". Rows: years 1983-1994. Columns: INDUSTRY VOLUME, PM-USA PRICE VALUE, etc.
> So it is a form.
> 
> Let's double check check 7: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This is a line-item table. But is it an invoice or budget? Invoice: "outside vendor... states charges owed". No. Budget: "internal money planning, tracking, or disbursement... forecast vs. actual". This is market estimates (industry vs PM-USA), not internal money planning. So it's not budget.
> Thus, check 10 (form) is the correct label.
> 
> Let's review the scratchpad steps:
> 1. file_folder: no — page has a large data table with real content.
> 2. handwritten: no — all text is typed.
> 3. fax: no — no fax header.
> 4. questionnaire: no — no survey questions.
> 5. resume: no — no career history.
> 6. scientific_publication: no — no journal identifier.
> 7. financial: no — not an invoice (no charges owed) and not a budget (not internal money planning, it's market estimates/projections for industry vs company).
> 8. specification: no — no product specs or "shall/must".
> 9. presentation: no — not a slide deck.
> 10. form: yes — "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)... is a form". The page is a table titled "PRICE VALUE ESTIMATES" with years as rows and financial/market metrics as columns.
> 11. correspondence: no — no memo/letter structure.
> 12. news_article: no — no masthead.
> 13. scientific_report: no — no running prose.
> 14. advertisement: no — not a promo layout.
> 
> Runner-up: budget, ruled out because the table is market estimates/projections (industry vs PM-USA price value and volume), not internal money planning, tracking, or disbursement (budget). Or runner-up: presentation, ruled out because it's a dense data table, not sparse slide layout.
> 
> Wait, is there any other label? "form" is check 10.
> Let's confirm the definition of form: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)... is a form (this check)".
> Yes, this is a standalone labeled data table.
> 
> Final check of the page content:
> Title: PRICE VALUE ESTIMATES
> Columns: YEAR, INDUSTRY VOLUME++, PM-USA PRICE VALUE (SHARE, % CHANGE VS. YAG, VOLUME*, DIFF), INDUSTRY PRICE VALUE (SHARE, % CHANGE VS. YAG, VOLUME*, DIFF), PM-USA SHARE OF CATEGORY (SHARE, VS. YAG, DIFF).
> Rows: 1983 to 1994.
> Footnotes: *PROJECTIONS, **(BILLIONS).
> Bates number: 11/16/89, 2040329451.
> This is a standalone labeled data table. Label: form.
> 
> One more check on check 7: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face."
> Even if it's a line-item table, it must be an invoice or budget. It's neither. It's market data. So check 7 doesn't apply.
> Check 10 applies: "A standalone labeled data chart or table... is a form".
> 
> I will output `form`.

---

### `test_imagesu_u_s_a_usa07d00_timo0000799.tif.png`
**Expected:** `budget` | **Predicted:** `form`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITIG NO.001 P.02" at the top. This looks like an internal archive ID, not a journal masthead. Bottom: "Confidential Missouri Tobacco Litigation Case No. 972-1455 TIMO 0000799". No journal masthead.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a title "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", filled fields, signatures. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: The page has typed fields and labels, filled by hand. Not majority handwritten freeform.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax cover sheet header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: Not a survey instrument.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: Not a resume.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal running head.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". Contains "Amount 250.00", "Account Code", "Check Payable to".
> - Wait, check 7 says: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget".
> - This is a "CONTRIBUTION REQUEST" or "CONTRIBUTION INFORMATION" form. It requests a contribution of $250.00. It has an approval block ("Approved by: Regional Vice President's signature", "Senior Vice President's signature").
> - Is it a budget? "A contribution/expenditure request or approval form whose whole content is an amount... is budget". Wait, let's read check 7 carefully: "ALSO a provider's periodic customer statement... ALSO a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts... is budget, not handwritten".
> - Wait, check 10 says: "internal authorization/approval forms with an approval signature/date block... is a form (check 10)".
> - Let's re-read check 7: "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> - This is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It's an authorization/request for a contribution. It has an approval block. It's not a bill for goods/services (invoice). It's not a periodic statement (budget). It's an internal authorization form for a single expenditure/contribution.
> - Let's check check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
> - This matches check 10 perfectly. It's a form capturing contribution info and getting approval.
> 
> Let's double check check 7 vs check 10.
> Check 7: "budget: ... A contribution/expenditure request or approval form whose whole content is an amount ... is budget". Wait. "ALSO a contribution/expenditure request or approval form whose whole content is an amount ... is budget, not handwritten".
> But check 7 also says: "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> This document is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It has fields for recipient info, contribution info (amount, account code, check payable to), and an approval block. It is authorizing a single expenditure (a contribution). Therefore, it falls under the caveat in check 7 and is a form (check 10).
> 
> Let's re-read check 10: "internal authorization/approval forms with an approval signature/date block." Yes, this has "Approved by:" with signatures.
> 
> Let's check if there's any other category.
> - form: check 10.
> 
> Let's review the evidence for form (check 10):
> - Title: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST"
> - Fields: "Date:", "State:", "RECIPIENT INFORMATION" (Name, Address, Current Office, etc.), "CONTRIBUTION INFORMATION" (Amount, Account Code, Check Payable to, Address, Notes).
> - Approval block: "Approved by: (Regional Vice President's signature), (Senior Vice President's signature)".
> - This is a filled administrative form with an approval signature block.
> 
> Runner-up: budget. Ruled out because it's an internal authorization/approval form for a single expenditure (contribution request) with an approval signature block, not a budget tracking/planning document or a bill for goods/services. The caveat in check 7 explicitly states that an internal expenditure-authorization form with an approval block is a form (check 10), not budget.
> 
> Let's confirm the labels:
> advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> 
> Label: form.
> 
> Let's do a quick pass of the checks:
> 1. file_folder: no, has body content.
> 2. handwritten: no, filled form.
> 3. fax: no.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. invoice/budget: no. It's a contribution request/authorization form. Caveat in check 7 says internal expenditure-authorization form with approval block is form (check 10).
> 8. specification: no.
> 9. presentation: no.
> 10. form: yes. Filled fields, boxes, approval signature block.
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no.
> 14. advertisement: no.
> 
> Final label: form.
> Evidence for check 10: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST" title, structured fields for recipient and contribution info (Amount, Account Code, Check Payable to), and an "Approved by:" block with signature lines for Regional and Senior Vice Presidents.
> Runner-up: budget, ruled out because the page is an internal authorization/approval form for a single expenditure (contribution request) with an approval signature block, which check 7 explicitly excludes from budget and assigns to form (check 10).

---

### `test_imagesu_u_s_a_usa07d00_timo0000799.tif.png`
**Expected:** `budget` | **Predicted:** `form`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITRG NO.001 P.02" at the top. This looks like an internal document identifier, not a journal masthead or newspaper masthead. Bottom has "Confidential Missouri Tobacco Litigation Case No. 972-1455" and "TIMO 0000799". No journal running head.
> 
> **Check 1: file_folder**
> - Content: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", filled fields, signature blocks. Not just an identifier.
> - Result: not this check.
> 
> **Check 2: handwritten**
> - Most content is typed form fields with some handwritten entries (date, name, address, amount, signatures). Not majority handwritten freeform.
> - Result: not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - No "FACSIMILE" or fax cover sheet header. The top line is internal ID.
> - Result: not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Not a survey instrument. It's a contribution request form.
> - Result: not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Not a resume.
> - Result: not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - No journal identifier on this page.
> - Result: not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". Contains "Amount 250.00", "Account Code", "Check Payable to".
> - Is this an invoice or budget?
> - Invoice: outside vendor states charges owed. This is a request for a contribution.
> - Budget: internal money planning, tracking, disbursement. "contribution/expenditure request or approval form whose whole content is an amount... is budget". Wait, let's look at check 7 carefully.
> - "budget: ... ALSO a contribution/expenditure request or approval form whose whole content is an amount... is budget, not invoice."
> - Wait, is it a form or a budget?
> - Check 10: "internal authorization/approval forms with an approval signature/date block."
> - Check 7 caveat: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> - This is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It has an amount (250.00), account code, check payable to, and approval signatures (Regional Vice President, Senior Vice President).
> - Is it a form or a budget?
> - Let's re-read Check 7 budget definition: "Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts... is budget, not invoice."
> - Wait, the caveat in Check 7 says: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> - This document is a "CONTRIBUTION REQUEST" with an amount of 250.00, account code, and approval signatures. It authorizes a single expenditure (a contribution).
> - Let's check Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; ... internal authorization/approval forms with an approval signature/date block."
> - This document has fields (Name, Address, Amount, Account Code, Check Payable to), checkboxes (State/Local), and approval signature blocks ("Approved by: Regional Vice President's signature", "Senior Vice President's signature").
> - The caveat in Check 7 explicitly says an internal expenditure-authorization form with an approval signature/date block is a form (check 10), not budget. This is exactly that: a contribution request/approval form.
> - So it's a form.
> 
> Let's double check Check 10 vs Check 7.
> Check 7: "budget: ... ALSO a contribution/expenditure request or approval form whose whole content is an amount... is budget, not invoice."
> But the caveat in Check 7: "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> This document is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It has an amount (250.00), but it's a request for a political contribution, not a billable charge or ongoing account statement. It's an authorization for a single expenditure (a donation). The caveat applies: "authorizing a single expenditure is not planning or tracking money." Thus, it's a form.
> 
> Let's check Check 10 again: "internal authorization/approval forms with an approval signature/date block." Yes, this has "Approved by:" with two signature lines.
> 
> So the label is `form`.
> 
> Let's quickly review the checks to be sure.
> 1. file_folder: No, has real content.
> 2. handwritten: No, mostly typed form with some handwriting.
> 3. fax: No.
> 4. questionnaire: No.
> 5. resume: No.
> 6. scientific_publication: No.
> 7. financial document: It has money (250.00), but it's an authorization form for a single expenditure (contribution request), which the caveat in check 7 explicitly demotes to form (check 10). "an internal expenditure-authorization form ... with an approval signature/date block ... is a form (check 10), not budget".
> 8. specification: No.
> 9. presentation: No.
> 10. administrative form: Yes. Filled fields, checkboxes, approval signature blocks. "internal authorization/approval forms with an approval signature/date block".
> 11. correspondence: No.
> 12. news_article: No.
> 13. scientific_report: No.
> 14. advertisement: No.
> 
> Runner-up: budget. Ruled out because the document is an internal expenditure-authorization form (contribution request) authorizing a single expenditure, which the check 7 caveat explicitly classifies as a form (check 10), not budget.
> 
> Wait, is there any other category?
> "POLITICAL CAMPAIGN CONTRIBUTION REQUEST"
> Fields: Date, State/Local checkbox, Recipient Information (Name, Address, Current Office, Aspired Office, Party, Leadership Position, Committees), Contribution Information (Amount, Account Code, Check Payable to, Address, Notes), Approved by (signatures).
> This is a classic administrative form.
> 
> Final check of the text:
> "POLITICAL CAMPAIGN CONTRIBUTION REQUEST"
> "Date: 6/4/96"
> "State: [x] Local: [ ]"
> "RECIPIENT INFORMATION"
> Table with Name, Address, etc. filled in by hand.
> "CONTRIBUTION INFORMATION"
> Table with Amount (250.00), Account Code (1401-7710-M001), Check Payable to (Koller to Rep).
> "Approved by:" with signatures.
> "Revised 2/95"
> "Confidential Missouri Tobacco Litigation Case No. 972-1455"
> "TIMO 0000799"
> 
> This is definitely a form.
> 
> Scratchpad:
> file_folder: no — the page has a title, filled fields, and signature blocks, not just an identifier.
> handwritten: no — mostly typed form fields with some handwritten entries and signatures.
> questionnaire: no — not a survey instrument.
> invoice/budget: no — contains an amount (250.00) and approval signatures, but it is an internal expenditure-authorization form (contribution request) for a single expenditure, which the check 7 caveat explicitly classifies as a form, not budget.
> form: yes — titled "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", contains filled fields, checkboxes, and an internal authorization/approval block with signature lines ("Approved by: Regional Vice President's signature", "Senior Vice President's signature").
> Runner-up: budget, ruled out because the document authorizes a single expenditure (a political contribution) rather than planning/tracking money, and the check 7 caveat explicitly states such internal authorization forms are forms (check 10).
> 
> Label: form.

---

### `test_imagesu_u_s_a_usa07d00_timo0000799.tif.png`
**Expected:** `budget` | **Predicted:** `form`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header block:** None. There is a header "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITRG No.001 P.02". This looks like a Bates number or archive stamp, not a mail client header. Wait, "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITRG No.001 P.02". This is archive metadata.
> - **Masthead or running head:** No newspaper/magazine masthead. No journal running head. There is "TOBACCO INSTITUTE" at the top left, but it's part of the document header, not a journal masthead.
> 
> **2. Scratchpad checks:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: The page has a title "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", filled fields, signatures. It has real content.
>     *   Result: not this check.
> 
> *   **Check 2: handwritten**
>     *   Evidence: Most content is typed (form fields, labels). Handwriting fills the fields (Don Koller, address, amount 250.00, signatures). It's not majority handwritten freeform text.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. The top line is archive metadata.
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: Not a survey asking the reader to answer questions. It's a request for a contribution.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
>     *   Evidence: Not a CV.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
>     *   Evidence: No journal name/volume/issue.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: There is an "Amount" field with "250.00". "Check Payable to". "Account Code".
>     *   Let's look at the definition.
>     *   "invoice: an outside vendor... states charges owed...". This is a contribution request.
>     *   "budget: internal money planning... contribution/expenditure request or approval form whose whole content is an amount...". Wait.
>     *   "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget".
>     *   This is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It has fields for recipient info, contribution info (amount, account code, check payable to), and approval signatures ("Approved by: Regional Vice President's signature", "Senior Vice President's signature").
>     *   Is it a budget? "budget: ... a contribution/expenditure request or approval form whose whole content is an amount...". Wait, let's re-read check 7 carefully.
>     *   "budget: ... ALSO a provider's periodic customer statement... ALSO a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts..."
>     *   Wait, the text says: "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
>     *   This document is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It authorizes a contribution of $250.00. It has approval signatures. It looks like an authorization form.
>     *   Let's check Check 10: "ADMINISTRATIVE FORM -> form". "internal authorization/approval forms with an approval signature/date block".
>     *   This document has "Approved by:" with signatures. It has fields for Name, Address, Amount, Account Code.
>     *   Is it a budget? "budget: ... a contribution/expenditure request or approval form whose whole content is an amount". This form has recipient info, contribution info, approval block. It's more than just an amount. It's a request form.
>     *   Actually, let's look at the "Caveat" in Check 7 again: "an internal expenditure-authorization form ... is a form (check 10), not budget". This is a contribution request/approval form. It authorizes a payment. So it's likely a form.
> 
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
>     *   Evidence: No product data, MSDS, etc.
>     *   Result: not this check.
> 
> *   **Check 9: SLIDE DECK... -> presentation**
>     *   Evidence: Not a slide.
>     *   Result: not this check.
> 
> *   **Check 10: ADMINISTRATIVE FORM -> form**
>     *   Evidence: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". Fields: Date, State, Recipient Information (Name, Address, Current Office, etc.), Contribution Information (Amount, Account Code, Check Payable to, Address, Notes), Approved by (signatures).
>     *   "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
>     *   This fits perfectly. It's a form capturing data for a political contribution request and approval.
> 
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
>     *   Evidence: No TO/FROM/RE header followed by prose. No letterhead with external address and salutation.
>     *   Result: not this check.
> 
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
>     *   Evidence: No masthead.
>     *   Result: not this check.
> 
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
>     *   Evidence: No running narrative prose.
>     *   Result: not this check.
> 
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
>     *   Evidence: Not an ad.
>     *   Result: not this check.
> 
> **Re-evaluating Check 7 vs Check 10:**
> - Check 7 (budget): "a contribution/expenditure request or approval form whose whole content is an amount". This form has recipient info (Don Koller, P.O. Box 135...), office info, committees, amount (250.00), account code, approval signatures. It's not *just* an amount.
> - Check 7 Caveat: "an internal expenditure-authorization form ... with an approval signature/date block but no billable charges is a form (check 10), not budget". This is exactly that. It's an authorization for a contribution (expenditure).
> - Check 10 (form): "internal authorization/approval forms with an approval signature/date block". This matches perfectly. The document is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST" form with filled data and approval signatures.
> 
> So the label is `form`.
> 
> Let's double check the "budget" definition.
> "budget: ... ALSO a contribution/expenditure request or approval form whose whole content is an amount..."
> The caveat says: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> This document is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It authorizes a single expenditure ($250). It has an approval block. Therefore, it is a form, not a budget.
> 
> Final check of the document content:
> - Header: TOBACCO INSTITUTE ... (archive info)
> - Title: POLITICAL CAMPAIGN CONTRIBUTION REQUEST
> - Date: 6/4/96
> - State: Local (checked)
> - Recipient Information table: Name (Don Koller), Address, Current Office, Aspired Office, Party, Leadership Position, Committees.
> - Contribution Information table: Amount (250.00), Account Code, Check Payable to, Address, Notes.
> - Approved by: signatures.
> - Footer: Confidential Missouri Tobacco Litigation Case No. 972-1455, TIMO 0000799.
> 
> This is clearly a filled administrative form.
> 
> Label: form.

---

## budget → invoice (1 errors)

### `test_imagesq_q_i_a_qia17d00_tnwl0007433.tif.png`
**Expected:** `budget` | **Predicted:** `invoice`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: No newspaper/magazine masthead. No journal running head.
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: The page has a lot of content: a check, a detachable stub, an invoice table. Not just an identifier/stamp.
>     *   Result: not this check.
> 
> *   **Check 2: handwritten**
>     *   Evidence: There is a signature ("M..."), but the majority of the content is typed text, tables, and check details.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: No survey questions.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
>     *   Evidence: No CV/resume content.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
>     *   Evidence: No journal name/volume/issue/page number.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: The page contains a check from "THE TOBACCO INSTITUTE" to "SENATE REPUBLICAN CAMPAIGN COMMITTEE" for "$500.00". Below the check is a detachable stub and an invoice table: "INVOICE DATE", "INVOICE NO.", "DESCRIPTION" ("STATE CAMPAIGN CONTRIBUTIONS"), "INVOICE AMOUNT" ($500.00), "NET AMOUNT" ($500.00).
>     *   Wait, is this an invoice or a budget?
>     *   The table has "INVOICE DATE", "INVOICE NO.", "DESCRIPTION", "INVOICE AMOUNT", "NET AMOUNT".
>     *   The description is "STATE CAMPAIGN CONTRIBUTIONS".
>     *   The top part is a check (payable to Senate Republican Campaign Committee for Five Hundred dollars).
>     *   The bottom part is an invoice detail or a check stub with invoice details.
>     *   Let's look at the definitions:
>         *   `invoice`: an outside vendor, supplier, or agency states charges owed... a payment voucher, a vendor's price... a receipt, a payment request... a production estimate report... itemized billing statement listing ACTUAL billable charges... A hotel/motel guest bill... is an invoice.
>         *   `budget`: internal money planning... expense reports... a provider's periodic customer statement...
>     *   This is a check payment for a campaign contribution. The bottom part looks like an invoice or a payment voucher/receipt. "INVOICE DATE 09/06/96", "INVOICE NO. WA PC 96 1401-7710-WA01", "DESCRIPTION STATE CAMPAIGN CONTRIBUTIONS", "INVOICE AMOUNT $500.00".
>     *   Wait, is a check itself an invoice? No, a check is a payment. But the document includes an invoice table.
>     *   Let's re-read check 7: "invoice: an outside vendor... states charges owed... a payment voucher... a receipt...".
>     *   "budget: ... a provider's periodic customer statement... is budget, not invoice".
>     *   This is a payment for a specific contribution ("STATE CAMPAIGN CONTRIBUTIONS"). It's a one-off payment (goods/services sold / contribution made). The document shows the check and the invoice details.
>     *   Actually, let's look at the structure. Top half: Check. Bottom half: Detached check stub / Invoice detail.
>     *   "INVOICE DATE", "INVOICE NO.", "DESCRIPTION", "INVOICE AMOUNT". This is an invoice or a payment voucher/receipt.
>     *   Is it a budget? No, it's not planning or tracking money over time, it's a specific payment for a contribution.
>     *   Is it an invoice? "invoice: an outside vendor... states charges owed... a payment voucher... a receipt". A check payment document with invoice details attached is often classified as an invoice or payment voucher.
>     *   Wait, the description is "STATE CAMPAIGN CONTRIBUTIONS". The Tobacco Institute is paying the Senate Republican Campaign Committee. This is a payment. The document acts as a record of payment (check) and the invoice/receipt for it.
>     *   Let's check the labels again. `invoice` vs `budget`.
>     *   "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
>     *   "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work... It does not have to be titled 'INVOICE' — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
>     *   This document has "INVOICE DATE", "INVOICE NO.", "INVOICE AMOUNT". It is explicitly labeled as an invoice in the table headers.
>     *   Therefore, it is an `invoice`.
> 
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
>     *   Evidence: No material safety data sheet, product formulation, etc.
>     *   Result: not this check.
> 
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
>     *   Evidence: No slide layout.
>     *   Result: not this check.
> 
> *   **Check 10: ADMINISTRATIVE FORM -> form**
>     *   Evidence: There are fields, but the primary content is financial (check and invoice table). Check 7 overrides Check 10 for money records. "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
>     *   Result: not this check (because Check 7 applies).
> 
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
>     *   Evidence: No TO/FROM/RE memo header, no letterhead with external address + Dear... salutation (the check has "TO THE ORDER OF", but that's a check, not a letter).
>     *   Result: not this check.
> 
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
>     *   Evidence: No masthead.
>     *   Result: not this check.
> 
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
>     *   Evidence: No running narrative prose.
>     *   Result: not this check.
> 
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
>     *   Evidence: No marketing layout.
>     *   Result: not this check.
> 
> **Re-evaluating Check 7:**
> The page shows a check from The Tobacco Institute to the Senate Republican Campaign Committee for $500.00.
> Below the check is a detachable portion with:
> "INVOICE DATE": 09/06/96
> "INVOICE NO.": WA PC 96 1401-7710-WA01
> "DESCRIPTION": STATE CAMPAIGN CONTRIBUTIONS
> "INVOICE AMOUNT": $500.00
> "NET AMOUNT": $500.00
> 
> This is a financial document. Specifically, it's an invoice (or a check with invoice details). The headers explicitly say "INVOICE DATE", "INVOICE NO.", "INVOICE AMOUNT".
> According to Check 7: "invoice: an outside vendor, supplier, or agency states charges owed... a payment voucher... a receipt...". This is a payment record/invoice for a campaign contribution.
> Is it a budget? "budget: internal money planning... expense reports...". A campaign contribution payment is a specific expenditure, but the document is formatted as an invoice/check.
> Actually, let's look at the definition of `invoice` again: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher... a receipt...".
> Here, The Tobacco Institute is paying. They are the buyer. The Senate Republican Campaign Committee is the recipient.
> Wait, if The Tobacco Institute is paying, they are issuing a check. The bottom part looks like the vendor's invoice or the payment voucher.
> "INVOICE DATE 09/06/96... DESCRIPTION STATE CAMPAIGN CONTRIBUTIONS... INVOICE AMOUNT $500.00".
> This is an invoice for a contribution, or a payment voucher.
> Check 7 says: "invoice: ... a payment voucher ... is an invoice".
> So `invoice` is the correct label.
> 
> Let's double check `budget`.
> "budget: ... a provider's periodic customer statement ... is budget, not invoice". This is not a periodic statement.
> "budget: ... money PLANNING for future work ... is budget". This is a payment for 09/06/96, likely already incurred or being paid now.
> The document is a check + invoice stub.
> The label `invoice` fits best because of the explicit "INVOICE" headers and the nature of billing/payment for a specific item (campaign contribution).
> 
> Wait, is it a `form`?
> Check 10: "administrative form... filled or blank fields...".
> Check 7 caveat: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
> Since this is a financial document (check + invoice table), Check 7 applies.
> 
> Final decision: `invoice`.
> 
> Let's review the scratchpad steps.
> 1. file_folder: No, has content.
> 2. handwritten: No, mostly typed.
> 3. fax: No.
> 4. questionnaire: No.
> 5. resume: No.
> 6. scientific_publication: No.
> 7. financial document: Yes. Check and invoice table. "INVOICE DATE", "INVOICE AMOUNT". Describes a payment of $500 for "STATE CAMPAIGN CONTRIBUTIONS". This is an invoice/payment voucher.
> 8. specification: No.
> 9. presentation: No.
> 10. form: No, overridden by financial content (check 7).
> 11. correspondence: No.
> 12. news_article: No.
> 13. scientific_report: No.
> 14. advertisement: No.
> 
> Runner-up: form. Ruled out because the page's primary structure is financial (check and invoice table with amounts and descriptions), which falls under check 7 (invoice/budget) rather than generic administrative form. Specifically, the explicit "INVOICE" headers and check details make it an invoice/payment record.
> 
> Wait, is it a `budget`?
> "budget: ... expense reports ...".
> But the headers are "INVOICE DATE", "INVOICE NO.", "INVOICE AMOUNT". This is an invoice.
> Also, the top is a check. A check is a payment. The combination is a payment record/invoice.
> The label `invoice` is appropriate.
> 
> One detail: "A hotel/motel guest bill ... is an invoice". "a payment voucher ... is an invoice".
> This document is essentially a check with an attached invoice/receipt.
> I will classify as `invoice`.
> 
> Let's check if there's any other label.
> Could it be `form`?
> Check 10 says "internal authorization/approval forms with an approval signature/date block". This doesn't have that.
> It has a signature on the check.
> But Check 7 is specific about money. "Money function overrides form layout".
> 
> So `invoice` is the correct label.

---

## form → presentation (1 errors)

### `test_imagesj_j_e_d_jed71e00_03701993_03702011.tif.png`
**Expected:** `form` | **Predicted:** `presentation`
**Source prompt version:** v10

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "03701993" on the right edge.
> 
> **Image analysis:**
> The image shows a scanned page.
> On the right side, there's a large black rectangular area, which looks like a photographed slide or a dark background. Wait, looking closely at the right side, it's a large black rectangle with some texture, possibly a photograph or a slide.
> On the left side, there's a white strip with text.
> Text on the left strip:
> "CHAP 7"
> "A"
> "="
> "K"
> "="
> "3"
> "="
> Then a column of numbers:
> "1 3 7 7 3 3 3 3 3 3"
> "1 1 2 1 1 2 2 2 2 2"
> ...
> "1 1 2 2 2 2 2 2 2 2"
> "1 1 2 2 2 2 2 2 2 2"
> "1 1 2 2 2 2 2 2 2 2"
> "1 1 2 2 2 2 2 2 2 2"
> "1 1 2 2 2 2 2 2 2 2"
> "1 1 2 2 2 2 2 2 2 2"
> "1 1 2 2 2 2 2 2 2 2"
> "1 1 2 2 2 2 2 2 2 2"
> "1 1 2 2 2 2 2 2 2 2"
> "1 1 2 2 2 2 2 2 2 2"
> "1 1 2 2 2 2 2 2 2 2"
> "1 1 2 2 2......

---
