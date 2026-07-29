"""
OpenRouter Vision Model Document Classifier
Sends only the document image to a vision-capable LLM for classification
"""

import json
import base64
import os
from pathlib import Path
import requests

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Recommended vision models on OpenRouter
VISION_MODELS = []

CLASSIFICATION_PROMPT = """You are a document classification expert analyzing document images with a vision model. Classify the given image into one of these 16 categories:

Available Classes:
advertisement - Marketing materials, promotional content, flyers, brochures
budget - Financial budgets, expense reports, financial planning documents, statements of account, checks, check stubs, expense tracking, and payment records across categories. A check or statement of account is NOT an invoice.
email - Email messages, email threads, electronic correspondence
file_folder - File folder labels, directory listings, file organization documents. Includes file folder covers, index pages, or nearly blank pages with ONLY a handwritten label, ID number, or classification stamp and NO meaningful title or organizational name. If the page has a meeting name, program title, speaker name, or organizational affiliation, it is likely a presentation cover page, NOT a file_folder.
form - Application forms, data entry forms, structured questionnaires. Includes fax cover sheets and fax transmission forms. Documents with "FACSIMILE", "TELEFAX", or "FAX" headers are forms, NOT memos or letters.
handwritten - Handwritten documents, notes, letters, manuscripts. If the MAJORITY of the document content is handwritten (not typed/printed), classify as handwritten regardless of whether it resembles a letter, memo, or note. Typed documents with only a handwritten signature are NOT handwritten.
invoice - Bills, invoices, receipts, payment requests. Must have explicit "INVOICE" header with line items, quantities, and "Amount Due" from a vendor/supplier. A check or statement of account is NOT an invoice.
letter - Formal letters, correspondence, business communications. Letters have external addresses, date, salutation ("Dear..."), and a formal closing with signature.
memo - Memorandums, internal communications, office memos. Memos have internal "TO:/FROM:/RE:/DATE:" header blocks. A fax cover sheet is NOT a memo.
news_article - Newspaper articles, news reports, journalistic content. Must be PUBLISHED journalism with bylines, columns, and publication names. A corporate press release is NOT a news article.
presentation - Presentation slides, slide decks, visual presentations, and title/cover pages of presentations or slide decks. Includes press releases. Documents with "FOR IMMEDIATE RELEASE" are press releases and should be classified as presentation, NOT news_article. A title page with a meeting name, speaker name, or program title (e.g., "BOARD OF DIRECTORS WINTER MEETING") is a presentation cover, NOT a file_folder.
questionnaire - Surveys, questionnaires, data collection forms with opinion questions, rating scales, multiple choice, or open-ended survey responses. If the document collects opinions, preferences, or survey data rather than factual/administrative information, choose questionnaire over form.
resume - CVs, resumes, job applications, professional profiles, and biographical sketches. NIH PHS 398 biographical sketch pages listing education, publications, and research experience are resumes, even though they use a standardized form template. If the content is a person's career history, classify as resume regardless of form template.
scientific_publication - Published journal articles with journal name, volume/issue numbers, DOI, or explicit journal headers (e.g., "American Journal of..."). Must show evidence of being PUBLISHED in a journal.
scientific_report - Internal research reports, draft manuscripts, lab reports, and technical studies NOT published in a journal. If it says "DRAFT" or lacks a journal header, it's a report. Do NOT use this for product data sheets, specifications, MSDS, formulations, rate sheets, smoke analysis data tables, QA inspection forms, grant applications, or project status reports with budget tracking.
specification - Technical specifications, requirements documents, product specs. Includes Material Safety Data Sheets (MSDS), product formulations, manufacturing change documents, rate sheets, and any document defining product requirements or properties. Look for part numbers, ingredient lists, "shall/must" language, or safety data sections.

Critical Disambiguation Rules:
- form vs memo/letter: Forms have BLANK FIELDS to fill in (lines, boxes, checkboxes). Fax cover sheets are forms. Memos and letters contain completed prose text.
- budget vs invoice: Budgets show planned/tracked spending, checks, vouchers, or account statements. Invoices request payment with "Amount Due" and vendor details. A voucher or check stub is budget, NOT invoice.
- specification vs scientific_report: Specifications define product requirements, MSDS, formulations, or rate sheets. Smoke analysis data tables and product testing results are specifications, NOT scientific reports.
- presentation vs file_folder: A title/cover page with a meeting name, program title, speaker name, or organizational branding is a presentation cover, NOT a file_folder. Only classify as file_folder if the page has NO meaningful title — just a bare label, ID number, or stamp.
- presentation vs news_article: Press releases ("FOR IMMEDIATE RELEASE") are presentations. News articles are published journalism.
- scientific_publication vs scientific_report: Publications appear in named journals. Reports are internal/draft documents without journal attribution.
- letter vs memo: Letters have external addresses and "Dear [name]" salutation. Memos have "TO:/FROM:/RE:/DATE:" header blocks.
- resume vs form: If the content is a person's education, publications, and career history (biographical sketch/CV), classify as resume even if it uses a standardized form template like PHS 398.
- questionnaire vs form: If the document collects opinions, survey responses, or preferences, it is a questionnaire. If it collects factual/administrative data (name, address, ID), it is a form.
- budget vs scientific_report: Monthly status reports or management reports with budget tracking are budget documents, NOT scientific reports.
- scientific_report should be your LAST choice — only use it when the document clearly presents original research findings with methodology and no other category fits.

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

VALID_CLASSES = [
    "advertisement", "budget", "email", "file_folder", "form", "handwritten",
    "invoice", "letter", "memo", "news_article", "presentation",
    "questionnaire", "resume", "scientific_publication", "scientific_report",
    "specification"
]


def encode_image(image_path: Path) -> str:
    """Encode image to base64 string for vision model input"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def clean_prediction(text: str | None) -> str:
    """Extract valid class name from LLM response"""
    if not text:
        return ""
    text = text.strip().lower()
    for cls in VALID_CLASSES:
        if cls in text:
            return cls
    return text


def classify_image(api_key: str, image_path: Path, model: str = "openai/gpt-4o") -> dict:
    """
    Classify a document image using a vision model through OpenRouter API.
    Sends only the image to the vision model - no OCR text or feature data.
    """
    image_base64 = encode_image(image_path)

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": CLASSIFICATION_PROMPT},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 20,
        "temperature": 0.1
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        OPENROUTER_API_URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        try:
            error_body = response.json()
        except Exception:
            error_body = response.text
        print(f"OpenRouter API error ({response.status_code}): {error_body}")
        raise

    result = response.json()

    try:
        prediction = result["choices"][0]["message"].get("content") or ""
    except (KeyError, IndexError, AttributeError):
        prediction = ""

    cleaned = clean_prediction(prediction)

    return {
        "status": "success" if cleaned else "empty_response",
        "classification": cleaned,
        "raw_response": prediction,
        "model": model,
        "usage": result.get("usage", {})
    }


if __name__ == "__main__":
    API_KEY = os.environ.get("OPENROUTER_API_KEY", "your-api-key-here")

    IMAGE_PATH = Path(r"c:\Users\grant\AMFAM\processed_balanced_dataset\images\advertisement_0000139610_page_0001.png")

    result = classify_image(API_KEY, IMAGE_PATH)
    print(json.dumps(result, indent=2))
