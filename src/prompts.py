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

# v4: Handwriting fix + illegible-page rule + experimental data boundary (1052 words)
PROMPT_V4 = """You are a document classification expert analyzing document images with a vision model. Classify the given image into one of these 16 categories:

Available Classes:
advertisement - Marketing materials, promotional content, flyers, brochures
budget - Financial budgets, expense reports, financial planning documents, statements of account, checks, check stubs, expense tracking, and payment records across categories. A check or statement of account is NOT an invoice.
email - Email messages, email threads, electronic correspondence
file_folder - File folder labels, directory listings, file organization documents. Includes file folder covers, index pages, or nearly blank pages with only a handwritten label, ID number, or classification stamp. If the page is mostly blank with just a label or ID, choose file_folder.
form - Application forms, data entry forms, structured questionnaires. Includes fax cover sheets and fax transmission forms. Documents with "FACSIMILE", "TELEFAX", or "FAX" headers are forms, NOT memos or letters.
handwritten - Handwritten documents, notes, letters, manuscripts. If the document contains SUBSTANTIAL HANDWRITTEN CONTENT that carries the main message (not just signatures, initials, or marginalia), classify as handwritten regardless of whether it resembles a letter, memo, or note. Focus on MESSAGE-CARRYING content, not area.
invoice - Bills, invoices, receipts, payment requests. Must have explicit "INVOICE" header with line items, quantities, and "Amount Due" from a vendor/supplier. A check or statement of account is NOT an invoice.
letter - Formal letters, correspondence, business communications. Letters have external addresses, date, salutation ("Dear..."), and a formal closing with signature.
memo - Memorandums, internal communications, office memos. Memos have internal "TO:/FROM:/RE:/DATE:" header blocks. A fax cover sheet is NOT a memo.
news_article - Newspaper articles, news reports, journalistic content. Must be PUBLISHED journalism with bylines, columns, and publication names. A corporate press release is NOT a news article.
presentation - Presentation slides, slide decks, visual presentations. Includes press releases. Documents with "FOR IMMEDIATE RELEASE" are press releases and should be classified as presentation, NOT news_article.
questionnaire - Surveys, questionnaires, data collection forms with opinion questions, rating scales, multiple choice, or open-ended survey responses.
resume - CVs, resumes, job applications, professional profiles
scientific_publication - Published journal articles with journal name, volume/issue numbers, DOI, or explicit journal headers (e.g., "American Journal of..."). Must show evidence of being PUBLISHED in a journal.
scientific_report - Internal research reports, draft manuscripts, lab reports, grant applications, and technical studies NOT published in a journal. If it says "DRAFT" or lacks a journal header, it's a report. Use for research findings, methodology, and analysis documents. Do NOT use for product data sheets, specifications, MSDS, or formulations.
specification - Technical specifications, requirements documents, product specs. Includes Material Safety Data Sheets (MSDS), product formulations, manufacturing change documents, rate sheets, and any document defining product requirements or properties. Look for part numbers, ingredient lists, "shall/must" language, or safety data sections. Includes experimental data plots and test results that define product properties or exhibit characteristics.

Ranked Decision Cascade (check in order):
1. **illegible_page**: Is the page nearly blank with only Bates stamps, stickers, or scanning artifacts? Choose file_folder.
2. **file_folder**: Is the page mostly blank with only a label, ID number, or classification stamp? Choose file_folder.
3. **handwritten**: Does the document contain SUBSTANTIAL HANDWRITTEN CONTENT that carries the main message (not just signatures, initials, or marginalia)? Choose handwritten. Focus on message-carrying content, not area.
4. **invoice**: Does it have "INVOICE" header, line items, quantities, and "Amount Due" from a vendor? Choose invoice.
5. **memo**: Does it have "TO:/FROM:/RE:/DATE:" header blocks? Choose memo.
6. **letter**: Does it have external addresses, date, "Dear [name]" salutation, and formal closing? Choose letter.
7. **email**: Does it show email headers (From/To/Subject) or email thread formatting? Choose email.
8. **form**: Does it have blank fields to fill in (lines, boxes, checkboxes) or "FAX"/"FACSIMILE" headers? Choose form.
9. **questionnaire**: Does it contain survey questions with rating scales, multiple choice, or opinion responses? Choose questionnaire.
10. **presentation**: Does it have slide formatting or "FOR IMMEDIATE RELEASE"? Choose presentation.
11. **news_article**: Is it published journalism with bylines, columns, and publication names? Choose news_article.
12. **scientific_publication**: Does it have journal name, volume/issue, DOI, or explicit journal headers? Choose scientific_publication.
13. **specification**: Does it define product requirements, MSDS, formulations, part numbers, ingredient lists, OR experimental data plots/test results that define product properties? Choose specification.
14. **scientific_report**: Only if it presents research findings with methodology but lacks journal headers and is NOT product test data. LAST CHOICE for research documents.
15. **budget**: Financial documents showing planned/tracked spending, checks, or account statements.
16. **resume**: CVs, resumes, job applications.
17. **advertisement**: Marketing materials, promotional content.

Critical Constraints:
- When uncertain, scientific_report should be your LAST choice — only use it when the document clearly presents research findings with methodology.
- Press releases ("FOR IMMEDIATE RELEASE") are presentations, NOT news_article.
- Fax cover sheets are forms, NOT memos or letters.
- Checks and statements of account are budgets, NOT invoices.
- Handwritten classification focuses on MESSAGE-CARRYING content, not just area or signature presence.
- Experimental data plots and test results that define product properties go to specification, not scientific_report.
- Nearly blank pages with only Bates stamps or scanning artifacts should be file_folder.

Input Data:
- Document image (300 DPI grayscale)

Output:
Output only the class name. No explanation, no JSON, no additional text.

Example: If the document has "INVOICE" header, line items table, and total amount, output only:
invoice"""

# Mapping of prompt versions to their content
PROMPTS = {
    "v1": PROMPT_V1,
    "v2": PROMPT_V2,
    "v3": PROMPT_V3,
    "v4": PROMPT_V4,
}

DEFAULT_PROMPT_VERSION = "v4"


def get_prompt(version: str = DEFAULT_PROMPT_VERSION) -> str:
    """Get the prompt for a specific version."""
    return PROMPTS.get(version, PROMPT_V4)


def list_prompt_versions() -> list[str]:
    """List available prompt versions."""
    return list(PROMPTS.keys())