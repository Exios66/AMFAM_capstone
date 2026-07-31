"""
Versioned classification prompts for document classification task.
Each version represents iterative improvements based on experimental results.
"""

# v1: Original baseline (677 words)
PROMPT_V1 = """You are a document classification expert analyzing document images with a vision model. Classify the given image into one of these 16 categories:

Available Classes:
advertisement - Marketing materials, promotional content, flyers, brochures
budget - Financial budgets, expense reports, financial planning documents, statements of account, checks, check stubs, expense tracking, and payment records across categories. A check or statement of account is NOT an invoice.
email - Email messages, email threads, electronic correspondence
file_folder - File folder labels, directory listings, file organization documents. Includes file folder covers, index pages, or nearly blank pages with only a handwritten label, ID number, or classification stamp. If the page is mostly blank with just a label or ID, choose file_folder.
form - Application forms, data entry forms, structured questionnaires. Includes fax cover sheets and fax transmission forms. Documents with "FACSIMILE", "TELEFAX", or "FAX" headers are forms, NOT memos or letters.
handwritten - Handwritten documents, notes, letters, manuscripts. If the MAJORITY of the document content is handwritten (not typed/printed), classify as handwritten regardless of whether it resembles a letter, memo, or note. Typed documents with only a handwritten signature are NOT handwritten.
invoice - Bills, invoices, receipts, payment requests. Must have explicit "INVOICE" header with line items, quantities, and "Amount Due" from a vendor/supplier. A check or statement of account is NOT an invoice.
letter - Formal letters, correspondence, business communications. Letters have external addresses, date, salutation ("Dear..."), and a formal closing with signature.
memo - Memorandums, internal communications, office memos. Memos have internal "TO:/FROM:/RE:/DATE:" header blocks. A fax cover sheet is NOT a memo.
news_article - Newspaper articles, news reports, journalistic content. Must be PUBLISHED journalism with bylines, columns, and publication names. A corporate press release is NOT a news article.
presentation - Presentation slides, slide decks, visual presentations. Includes press releases. Documents with "FOR IMMEDIATE RELEASE" are press releases and should be classified as presentation, NOT news_article.
questionnaire - Surveys, questionnaires, data collection forms with opinion questions, rating scales, multiple choice, or open-ended survey responses.
resume - CVs, resumes, job applications, professional profiles
scientific_publication - Published journal articles with journal name, volume/issue numbers, DOI, or explicit journal headers (e.g., "American Journal of..."). Must show evidence of being PUBLISHED in a journal.
scientific_report - Internal research reports, draft manuscripts, lab reports, grant applications, and technical studies NOT published in a journal. If it says "DRAFT" or lacks a journal header, it's a report. Do NOT use this for product data sheets, specifications, MSDS, or formulations.
specification - Technical specifications, requirements documents, product specs. Includes Material Safety Data Sheets (MSDS), product formulations, manufacturing change documents, rate sheets, and any document defining product requirements or properties. Look for part numbers, ingredient lists, "shall/must" language, or safety data sections.

Critical Disambiguation Rules:
- form vs memo/letter: Forms have BLANK FIELDS to fill in (lines, boxes, checkboxes). Fax cover sheets are forms. Memos and letters contain completed prose text.
- budget vs invoice: Budgets show planned/tracked spending, checks, or account statements. Invoices request payment with "Amount Due" and vendor details.
- specification vs scientific_report: Specifications define product requirements, MSDS, or formulations. Scientific reports present original research findings.
- presentation vs news_article: Press releases ("FOR IMMEDIATE RELEASE") are presentations. News articles are published journalism.
- scientific_publication vs scientific_report: Publications appear in named journals. Reports are internal/draft documents without journal attribution.
- letter vs memo: Letters have external addresses and "Dear [name]" salutation. Memos have "TO:/FROM:/RE:/DATE:" header blocks.
- When uncertain, scientific_report should be your LAST choice — only use it when the document clearly presents research findings with methodology.

Input Data:
- Document image (300 DPI grayscale)

Analysis Approach:
1. Examine the visual layout of the image (headers, tables, columns, formatting)
2. Read any visible text for key terms and document-specific vocabulary
3. Identify structural features (signatures, form fields, sections)
4. Consider document purpose and context
5. Check the disambiguation rules above before finalizing your choice

Output:
Output only the class name. No explanation, no JSON, no additional text.

Example: If the document has "INVOICE" header, line items table, and total amount, output only:
invoice"""

# v2: Added disambiguation rules (946 words) - had contradictions and gold-label conflicts
PROMPT_V2 = """You are a document classification expert analyzing document images with a vision model. Classify the given image into one of these 16 categories:

Available Classes:
advertisement - Marketing materials, promotional content, flyers, brochures
budget - Financial budgets, expense reports, financial planning documents, statements of account, checks, check stubs, expense tracking, and payment records across categories. A check or statement of account is NOT an invoice. Includes vouchers and rate sheets.
email - Email messages, email threads, electronic correspondence
file_folder - File folder labels, directory listings, file organization documents. Includes file folder covers, index pages, or nearly blank pages with only a handwritten label, ID number, or classification stamp. If the page is mostly blank with just a label or ID, choose file_folder.
form - Application forms, data entry forms, structured questionnaires. Includes fax cover sheets and fax transmission forms. Documents with "FACSIMILE", "TELEFAX", or "FAX" headers are forms, NOT memos or letters. Surveys and questionnaires should be classified as questionnaire, not form.
handwritten - Handwritten documents, notes, letters, manuscripts. If the MAJORITY of the document content is handwritten (not typed/printed), classify as handwritten regardless of whether it resembles a letter, memo, or note. Typed documents with only a handwritten signature are NOT handwritten.
invoice - Bills, invoices, receipts, payment requests. Must have explicit "INVOICE" header with line items, quantities, and "Amount Due" from a vendor/supplier. A check or statement of account is NOT an invoice. Rate sheets are specifications, not invoices.
letter - Formal letters, correspondence, business communications. Letters have external addresses, date, salutation ("Dear..."), and a formal closing with signature.
memo - Memorandums, internal communications, office memos. Memos have internal "TO:/FROM:/RE:/DATE:" header blocks. A fax cover sheet is NOT a memo.
news_article - Newspaper articles, news reports, journalistic content. Must be PUBLISHED journalism with bylines, columns, and publication names. A corporate press release is NOT a news article.
presentation - Presentation slides, slide decks, visual presentations. Includes press releases. Documents with "FOR IMMEDIATE RELEASE" are press releases and should be classified as presentation, NOT news_article.
questionnaire - Surveys, questionnaires, data collection forms with opinion questions, rating scales, multiple choice, or open-ended survey responses.
resume - CVs, resumes, job applications, professional profiles
scientific_publication - Published journal articles with journal name, volume/issue numbers, DOI, or explicit journal headers (e.g., "American Journal of..."). Must show evidence of being PUBLISHED in a journal.
scientific_report - Internal research reports, draft manuscripts, lab reports, grant applications, and technical studies NOT published in a journal. If it says "DRAFT" or lacks a journal header, it's a report. Do NOT use this for product data sheets, specifications, MSDS, or formulations.
specification - Technical specifications, requirements documents, product specs. Includes Material Safety Data Sheets (MSDS), product formulations, manufacturing change documents, rate sheets, and any document defining product requirements or properties. Look for part numbers, ingredient lists, "shall/must" language, or safety data sections.

Critical Disambiguation Rules:
- form vs memo/letter: Forms have BLANK FIELDS to fill in (lines, boxes, checkboxes). Fax cover sheets are forms. Memos and letters contain completed prose text.
- form vs questionnaire: Forms are for data entry with blank fields. Questionnaires have survey questions with rating scales or opinion responses.
- budget vs invoice: Budgets show planned/tracked spending, checks, or account statements. Invoices request payment with "Amount Due" and vendor details.
- specification vs scientific_report: Specifications define product requirements, MSDS, or formulations. Scientific reports present original research findings.
- presentation vs news_article: Press releases ("FOR IMMEDIATE RELEASE") are presentations. News articles are published journalism.
- scientific_publication vs scientific_report: Publications appear in named journals. Reports are internal/draft documents without journal attribution.
- letter vs memo: Letters have external addresses and "Dear [name]" salutation. Memos have "TO:/FROM:/RE:/DATE:" header blocks.
- When uncertain, scientific_report should be your LAST choice — only use it when the document clearly presents research findings with methodology.

Input Data:
- Document image (300 DPI grayscale)

Analysis Approach:
1. Examine the visual layout of the image (headers, tables, columns, formatting)
2. Read any visible text for key terms and document-specific vocabulary
3. Identify structural features (signatures, form fields, sections)
4. Consider document purpose and context
5. Check the disambiguation rules above before finalizing your choice

Output:
Output only the class name. No explanation, no JSON, no additional text.

Example: If the document has "INVOICE" header, line items table, and total amount, output only:
invoice"""

# v3: Ranked decision cascade, gold-verified rules, removed contradictions (895 words)
PROMPT_V3 = """You are a document classification expert analyzing document images with a vision model. Classify the given image into one of these 16 categories:

Available Classes:
advertisement - Marketing materials, promotional content, flyers, brochures
budget - Financial budgets, expense reports, financial planning documents, statements of account, checks, check stubs, expense tracking, and payment records across categories. A check or statement of account is NOT an invoice.
email - Email messages, email threads, electronic correspondence
file_folder - File folder labels, directory listings, file organization documents. Includes file folder covers, index pages, or nearly blank pages with only a handwritten label, ID number, or classification stamp. If the page is mostly blank with just a label or ID, choose file_folder.
form - Application forms, data entry forms, structured questionnaires. Includes fax cover sheets and fax transmission forms. Documents with "FACSIMILE", "TELEFAX", or "FAX" headers are forms, NOT memos or letters.
handwritten - Handwritten documents, notes, letters, manuscripts. If the MAJORITY of the document content is handwritten (not typed/printed), classify as handwritten regardless of whether it resembles a letter, memo, or note. Typed documents with only a handwritten signature are NOT handwritten.
invoice - Bills, invoices, receipts, payment requests. Must have explicit "INVOICE" header with line items, quantities, and "Amount Due" from a vendor/supplier. A check or statement of account is NOT an invoice.
letter - Formal letters, correspondence, business communications. Letters have external addresses, date, salutation ("Dear..."), and a formal closing with signature.
memo - Memorandums, internal communications, office memos. Memos have internal "TO:/FROM:/RE:/DATE:" header blocks. A fax cover sheet is NOT a memo.
news_article - Newspaper articles, news reports, journalistic content. Must be PUBLISHED journalism with bylines, columns, and publication names. A corporate press release is NOT a news article.
presentation - Presentation slides, slide decks, visual presentations. Includes press releases. Documents with "FOR IMMEDIATE RELEASE" are press releases and should be classified as presentation, NOT news_article.
questionnaire - Surveys, questionnaires, data collection forms with opinion questions, rating scales, multiple choice, or open-ended survey responses.
resume - CVs, resumes, job applications, professional profiles
scientific_publication - Published journal articles with journal name, volume/issue numbers, DOI, or explicit journal headers (e.g., "American Journal of..."). Must show evidence of being PUBLISHED in a journal.
scientific_report - Internal research reports, draft manuscripts, lab reports, grant applications, and technical studies NOT published in a journal. If it says "DRAFT" or lacks a journal header, it's a report. Do NOT use this for product data sheets, specifications, MSDS, or formulations.
specification - Technical specifications, requirements documents, product specs. Includes Material Safety Data Sheets (MSDS), product formulations, manufacturing change documents, rate sheets, and any document defining product requirements or properties. Look for part numbers, ingredient lists, "shall/must" language, or safety data sections.

Ranked Decision Cascade (check in order):
1. **file_folder**: Is the page mostly blank with only a label, ID number, or classification stamp? Choose file_folder.
2. **handwritten**: Is the MAJORITY of the document content handwritten (not typed/printed)? Choose handwritten.
3. **invoice**: Does it have "INVOICE" header, line items, quantities, and "Amount Due" from a vendor? Choose invoice.
4. **memo**: Does it have "TO:/FROM:/RE:/DATE:" header blocks? Choose memo.
5. **letter**: Does it have external addresses, date, "Dear [name]" salutation, and formal closing? Choose letter.
6. **email**: Does it show email headers (From/To/Subject) or email thread formatting? Choose email.
7. **form**: Does it have blank fields to fill in (lines, boxes, checkboxes) or "FAX"/"FACSIMILE" headers? Choose form.
8. **questionnaire**: Does it contain survey questions with rating scales, multiple choice, or opinion responses? Choose questionnaire.
9. **presentation**: Does it have slide formatting or "FOR IMMEDIATE RELEASE"? Choose presentation.
10. **news_article**: Is it published journalism with bylines, columns, and publication names? Choose news_article.
11. **scientific_publication**: Does it have journal name, volume/issue, DOI, or explicit journal headers? Choose scientific_publication.
12. **specification**: Does it define product requirements, MSDS, formulations, or have part numbers/ingredient lists? Choose specification.
13. **scientific_report**: Only if it presents research findings with methodology but lacks journal headers. LAST CHOICE.
14. **budget**: Financial documents showing planned/tracked spending, checks, or account statements.
15. **resume**: CVs, resumes, job applications.
16. **advertisement**: Marketing materials, promotional content.

Critical Constraints:
- When uncertain, scientific_report should be your LAST choice — only use it when the document clearly presents research findings with methodology.
- Press releases ("FOR IMMEDIATE RELEASE") are presentations, NOT news_article.
- Fax cover sheets are forms, NOT memos or letters.
- Checks and statements of account are budgets, NOT invoices.

Input Data:
- Document image (300 DPI grayscale)

Output:
Output only the class name. No explanation, no JSON, no additional text.

Example: If the document has "INVOICE" header, line items table, and total amount, output only:
invoice"""

# v4: Scratchpad decision procedure, checks 1-14, function-over-subject-matter emphasis
PROMPT_V4 = """You classify scanned business documents (tobacco-industry archive, 300 DPI grayscale) into exactly one of 16 categories.

Labels (use these exact strings):
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification

Before answering, work through the page in a <scratchpad>. This is where you catch the cases where the "obvious" or topically-salient label is wrong because of a deeper structural cue you'd otherwise skip past. Do not rush to the label that matches the page's subject matter — match its FUNCTION.

## Scratchpad procedure

Walk checks 1-14 below IN ORDER. For each check, before moving to the next one, briefly state:
What specific evidence for this check IS present on the page (quote or closely paraphrase the actual text/layout you see — header words, field labels, masthead, journal name, "shall" language, etc.), or "none" if nothing supports it.
If evidence is present: STOP HERE. This is your check. Do not keep evaluating later checks, even if the page also superficially resembles a later category.
If no evidence: say "not this check" in one short clause and move to the next check.

Keep each check's line short (evidence-focused, not a full paragraph) — the goal is a fast, auditable pass, not an essay. Once you stop at a matching check, add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out. This forces you to name the trap before falling into it.

After the scratchpad, output your final answer.

## The checks

IDENTIFIER-ONLY PAGE -> file_folder
   The page carries almost no body content: only an archive/Bates number, a stamp, a short abbreviated or handwritten label ("Filt Cigt Dev", "Request No. 5", a date and committee name), folder/box markings, or an index/inventory card of filing metadata (e.g. INVENTOR / TITLE / patent numbers). No sentences, no prominent topical title.

MAJORITY-HANDWRITTEN PAGE -> handwritten
   Most of the content is handwritten, not typed. This wins even if the page reads like a letter, a memo with To/From/Re, a note, or a filled-in coupon/data form. A typed page with only a handwritten signature, stamp, or margin note is NOT handwritten.

FAX TRANSMISSION SHEET -> form
   A "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", "TELEFAX MESSAGE NO.", or confirmation-report header with To/From/company/phone/page-count fields. Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels.

SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
   The page asks a respondent to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, a consumer commitment/enrolment application, or a cover letter that transmits or refers to a survey/questionnaire being sent to the recipient. This wins over form and letter.

PERSON'S CAREER HISTORY -> resume
   CV, resume, professional profile, or biographical sketch listing education, positions, honors, and publications — including standardized templates such as PHS 398 "BIOGRAPHICAL SKETCH" / "Form Page" pages.

PUBLISHED-JOURNAL EVIDENCE -> scientific_publication
   A named journal on the page plus at least one publication identifier: volume/issue, page range, DOI, journal copyright line, or "Reprinted from ...". Without such evidence a scientific-looking page is NOT a publication.

FINANCIAL DOCUMENT -> invoice or budget
invoice: a vendor/supplier states what is owed for goods or services — an "INVOICE" header with line items and amount due, a payment VOUCHER naming payee, services and amount, a vendor's price or hourly-rate schedule (labour rates, overtime, travel charges), a receipt, or a payment request.
budget: internal money planning, tracking, or a payment instrument — budget or expense lines, forecast vs. actual, expense reports, a statement of account with aged balances, a check face or check stub (MICR line, "CHECK NO", "CHECK DATE", "PAY TO THE ORDER OF"), a check/payment register, or a monthly management/project status report that tracks budget and spending.

PRODUCT OR MATERIAL DOCUMENTATION -> specification
   Material Safety Data Sheet ("MATERIAL SAFETY DATA SHEET", hazardous ingredients, physical/fire data), product formulation or preparation/mixing instructions, manufacturing change authorization, product-property or test-analysis tables keyed to product/part codes (e.g. smoke analyses for products "PD 142A/B/C/D"), tolerances, or "shall/must" requirement language. Product-referenced test data is a specification, not a scientific report.

SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
   Slide/overhead layouts (large sparse type, bullet lists, chart-per-page), a deck title or section-divider page whose text is a topical heading ("RECOMMENDATIONS", "COMPETITIVE BAR PROGRAMS" — possibly rotated 90 degrees), a meeting/program/speaker cover page, or a corporate press release / issued statement ("FOR IMMEDIATE RELEASE", company statement with media contact).

ADMINISTRATIVE FORM -> form
    Blank or filled fields, boxes, checkboxes, ruled entry lines for capturing factual data; an application (research grant application, employment, service request); a structured records-management inventory or log table; a QA/parameter review sheet listing reviewed parameters and status.

CORRESPONDENCE -> email, memo, or letter
email: mail-client header block (From/To/Sent/Subject, cc, attachment lines) or a forwarded/threaded mail trail. An email page keeps this label even when its body is mostly a data table.
memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" block followed by prose.
letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature.

PUBLISHED JOURNALISM -> news_article
    Newspaper or magazine masthead, byline, dateline, multi-column news typography, "- more -" continuation, or wire-service credit.

ORIGINAL RESEARCH WRITE-UP -> scientific_report
    Research narrative with objectives, methods, results, or discussion; a draft manuscript ("DRAFT", "Send Proofs to:"); a lab or technical study title page with authors and an internal/industrial affiliation and no journal identifiers.

PROMOTIONAL MATERIAL -> advertisement
    Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures.

Nothing matched: choose the label whose defining evidence is closest to what you can actually read on the page. Never fall back to scientific_report as a catch-all. State in the scratchpad why none of checks 1-14 had positive evidence before doing this.

## Calibration

The evaluation set is balanced — every label is about 1/16 of the pages. No label should dominate your predictions.
scientific_report and form are historically the most over-predicted labels. Only choose them when their own positive evidence (check 13 / check 10) is present, not because the page looks technical or structured.
Technical subject matter alone decides nothing: the page's function decides the label.
If two labels remain, prefer the one supported by an explicit header, form field, or masthead you can read over one inferred from topic.
If your scratchpad's stopping check and your "gut" label disagree, trust the scratchpad — that disagreement is exactly the signal this process exists to catch.

## Output format

After the scratchpad, output the final label on its own line, wrapped like this and nothing else on that line:

<label>invoice</label>

The label must be lowercase, exactly one of the 16 strings above, no punctuation inside the tags, no explanation after them.

### Worked example

<scratchpad>
file_folder: no — page has multi-line prose body, not just an identifier/stamp.
handwritten: no — text is typed throughout.
fax sheet: no — no FACSIMILE/TELEFAX header.
questionnaire: no — nothing asks the reader to rate/answer/choose.
resume: no — no career/education listing.
scientific_publication: no — no journal name or volume/issue/DOI present.
financial: yes — page has "INVOICE" header, itemized goods with unit prices, and an "Amount Due" total from a vendor to the recipient. This is invoice, not budget — there's no internal forecast/actual tracking or check stub.
Runner-up: budget, ruled out because the page states what is owed to a vendor rather than tracking internal spend.
</scratchpad>
<label>invoice</label>"""

# v5: Scratchpad + labeled data chart/table -> form rule, never-output-a-ruled-out-label rule
PROMPT_V5 = """You classify scanned business documents (tobacco-industry archive, 300 DPI grayscale) into exactly one of 16 categories.

Labels (use these exact strings):
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification

Before answering, work through the page in a <scratchpad>. This is where you catch the cases where the "obvious" or topically-salient label is wrong because of a deeper structural cue you'd otherwise skip past. Do not rush to the label that matches the page's subject matter — match its FUNCTION.

## Scratchpad procedure

Walk checks 1-14 below IN ORDER. For each check, before moving to the next one, briefly state:
What specific evidence for this check IS present on the page (quote or closely paraphrase the actual text/layout you see — header words, field labels, masthead, journal name, "shall" language, etc.), or "none" if nothing supports it.
If evidence is present: STOP HERE. This is your check. Do not keep evaluating later checks, even if the page also superficially resembles a later category.
If no evidence: say "not this check" in one short clause and move to the next check.

Keep each check's line short (evidence-focused, not a full paragraph) — the goal is a fast, auditable pass, not an essay. Once you stop at a matching check, add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out. This forces you to name the trap before falling into it.

Your final label MUST be the check that had positive evidence. If you wrote "no" for every check, you missed something: most commonly check 10 (any labeled data chart/table or parameter-value grid is an administrative form). Re-scan the page and state the evidence you originally missed. Never output a label you explicitly marked "no" in your scratchpad.

After the scratchpad, output your final answer.

## The checks

IDENTIFIER-ONLY PAGE -> file_folder
   The page carries almost no body content: only an archive/Bates number, a stamp, a short abbreviated or handwritten label ("Filt Cigt Dev", "Request No. 5", a date and committee name), folder/box markings, or an index/inventory card of filing metadata (e.g. INVENTOR / TITLE / patent numbers). No sentences, no prominent topical title.

MAJORITY-HANDWRITTEN PAGE -> handwritten
   Most of the content is handwritten, not typed. This wins even if the page reads like a letter, a memo with To/From/Re, a note, or a filled-in coupon/data form. A typed page with only a handwritten signature, stamp, or margin note is NOT handwritten.

FAX TRANSMISSION SHEET -> form
   A "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", "TELEFAX MESSAGE NO.", or confirmation-report header with To/From/company/phone/page-count fields. Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels.

SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
   The page asks a respondent to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, a consumer commitment/enrolment application, or a cover letter that transmits or refers to a survey/questionnaire being sent to the recipient. This wins over form and letter.

PERSON'S CAREER HISTORY -> resume
   CV, resume, professional profile, or biographical sketch listing education, positions, honors, and publications — including standardized templates such as PHS 398 "BIOGRAPHICAL SKETCH" / "Form Page" pages.

PUBLISHED-JOURNAL EVIDENCE -> scientific_publication
   A named journal on the page plus at least one publication identifier: volume/issue, page range, DOI, journal copyright line, or "Reprinted from ...". Without such evidence a scientific-looking page is NOT a publication.

FINANCIAL DOCUMENT -> invoice or budget
invoice: a vendor/supplier states what is owed for goods or services — an "INVOICE" header with line items and amount due, a payment VOUCHER naming payee, services and amount, a vendor's price or hourly-rate schedule (labour rates, overtime, travel charges), a receipt, or a payment request.
budget: internal money planning, tracking, or a payment instrument — budget or expense lines, forecast vs. actual, expense reports, a statement of account with aged balances, a check face or check stub (MICR line, "CHECK NO", "CHECK DATE", "PAY TO THE ORDER OF"), a check/payment register, or a monthly management/project status report that tracks budget and spending. NOT an approval/authorization form: a page whose function is to obtain sign-off for a proposed expenditure — an internal authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition authorization, "DO NOT ... AUTHORIZE ANY EXPENDITURE ... UNTIL EXECUTIVE APPROVAL HAS BEEN OBTAINED HEREON") with labeled fields, budget-category rows (AIR TIME, TALENT AND PRODUCTION, SPACE, ART WORK, ...), and an approval signature/date block (Agency/Media/Sales/Marketing/Executive/Accounting) — is a form (check 10), not a budget. Budget means planning or tracking money over a period; authorizing a single expenditure is not budget.

PRODUCT OR MATERIAL DOCUMENTATION -> specification
    Material Safety Data Sheet ("MATERIAL SAFETY DATA SHEET", hazardous ingredients, physical/fire data), product formulation or preparation/mixing instructions, manufacturing change authorization, product-property or test-analysis tables keyed to product/part codes (e.g. smoke analyses for products "PD 142A/B/C/D"), tolerances, or "shall/must" requirement language. Product-referenced test data is a specification, not a scientific report. But a generic labeled chart or table with no product/part code, no requirement language, and no "shall/must" text is NOT a specification — treat it as an administrative form (check 10).

SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
   Slide/overhead layouts (large sparse type, bullet lists, chart-per-page), a deck title or section-divider page whose text is a topical heading ("RECOMMENDATIONS", "COMPETITIVE BAR PROGRAMS" — possibly rotated 90 degrees), a meeting/program/speaker cover page, or a corporate press release / issued statement ("FOR IMMEDIATE RELEASE", company statement with media contact). A standalone data chart or table of values is NOT a slide — a "chart-per-page" deck must otherwise look like slide layout (headline text, bullets, deck cover).

ADMINISTRATIVE FORM -> form
    Blank or filled fields, boxes, checkboxes, ruled entry lines for capturing factual data; an application (research grant application, employment, service request); a structured records-management inventory or log table; a QA/parameter review sheet listing reviewed parameters and status. Also a standalone labeled data display: a chart or table whose only content is labeled rows or columns (e.g. "CHART 1" with rows A-Z) and numeric/tick/measured values — that is a filled records/log table, i.e. a form, even with a chart caption. And a filled data-record sheet: a page of field labels followed by values (e.g. "ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC INSTRUMENT/COLUMN/MOBILE PHASE/DETECTOR/PURITY entries, spectrum captions) — a filled form recording measured data is still a form. A form does NOT have to be blank. Internal authorization/approval forms are forms: an expenditure-authorization page ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval) with labeled fields, budget-category rows, and an approval signature/date block — even when it names a budget allocation or authorizes a specific dollar amount.

CORRESPONDENCE -> email, memo, or letter
email: mail-client header block (From/To/Sent/Subject, cc, attachment lines) or a forwarded/threaded mail trail. An email page keeps this label even when its body is mostly a data table.
memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" block followed by prose.
letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature.

PUBLISHED JOURNALISM -> news_article
    Newspaper or magazine masthead, byline, dateline, multi-column news typography, "- more -" continuation, or wire-service credit.

ORIGINAL RESEARCH WRITE-UP -> scientific_report
    Research narrative with objectives, methods, results, or discussion; a draft manuscript ("DRAFT", "Send Proofs to:"); a lab or technical study title page with authors and an internal/industrial affiliation and no journal identifiers. A page that is only labeled field-value entries — even a data sheet headed "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line — is NOT a scientific report; it is a filled form (check 10). scientific_report requires running prose (narrative sentences of objectives, methods, results, or discussion), not a field-by-field data-capture layout.

PROMOTIONAL MATERIAL -> advertisement
    Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures.

Nothing matched: choose the label whose defining evidence is closest to what you can actually read on the page. Never fall back to scientific_report as a catch-all. State in the scratchpad why none of checks 1-14 had positive evidence before doing this.

## Calibration

The evaluation set is balanced — every label is about 1/16 of the pages. No label should dominate your predictions.
scientific_report and form are historically the most over-predicted labels. Only choose them when their own positive evidence (check 13 / check 10) is present, not because the page looks technical or structured.
A page whose only content is a labeled data chart/table (rows or columns of values, captions like "CHART 1") is an administrative form (records/log table) — not presentation, not specification, not scientific_report.
A filled analytical/lab data sheet (field labels like COMPOUND:, FORMULA:, INSTRUMENT:, PURITY: with values, plus spectrum captions) is a form, not scientific_report — a title, contract number, or investigator name does not turn a field-entry sheet into a report.
An internal expenditure/approval authorization form ("ADVERTISING AND SELLING AUTHORIZATION" with an approval signature/date block) is a form, not a budget — budget is planning or tracking money over a period, not authorizing a single expenditure.
Never output a label you marked "no" in your scratchpad; the final label must come from a check with positive evidence, or the closest available evidence.
Technical subject matter alone decides nothing: the page's function decides the label.
If two labels remain, prefer the one supported by an explicit header, form field, or masthead you can read over one inferred from topic.
If your scratchpad's stopping check and your "gut" label disagree, trust the scratchpad — that disagreement is exactly the signal this process exists to catch.

## Output format

After the scratchpad, output the final label on its own line, wrapped like this and nothing else on that line:

<label>invoice</label>

The label must be lowercase, exactly one of the 16 strings above, no punctuation inside the tags, no explanation after them.

### Worked example

<scratchpad>
file_folder: no — page has multi-line prose body, not just an identifier/stamp.
handwritten: no — text is typed throughout.
fax sheet: no — no FACSIMILE/TELEFAX header.
questionnaire: no — nothing asks the reader to rate/answer/choose.
resume: no — no career/education listing.
scientific_publication: no — no journal name or volume/issue/DOI present.
financial: yes — page has "INVOICE" header, itemized goods with unit prices, and an "Amount Due" total from a vendor to the recipient. This is invoice, not budget — there's no internal forecast/actual tracking or check stub.
Runner-up: budget, ruled out because the page states what is owed to a vendor rather than tracking internal spend.
</scratchpad>
<label>invoice</label>"""

# Mapping of prompt versions to their content
PROMPTS = {
    "v1": PROMPT_V1,
    "v2": PROMPT_V2,
    "v3": PROMPT_V3,
    "v4": PROMPT_V4,
    "v5": PROMPT_V5,
}

DEFAULT_PROMPT_VERSION = "v4"


def get_prompt(version: str = DEFAULT_PROMPT_VERSION) -> str:
    """Get the prompt for a specific version."""
    return PROMPTS.get(version, PROMPT_V4)


def list_prompt_versions() -> list[str]:
    """List available prompt versions."""
    return list(PROMPTS.keys())