"""
OpenRouter Vision Model Document Classifier
Sends only the document image to a vision-capable LLM for classification
"""

import json
import logging
import os
from pathlib import Path
import requests

from src.constants import DOCUMENT_CLASSES
from src.image_utils import encode_image_base64
from src.openrouter_utils import OPENROUTER_API_URL, build_vision_messages

logger = logging.getLogger(__name__)

# Recommended vision models on OpenRouter
VISION_MODELS = []

CLASSIFICATION_PROMPT = """You are a document classification expert analyzing document images with a vision model. Classify the given image into one of these 16 categories:

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

VALID_CLASSES = list(DOCUMENT_CLASSES)


class OpenRouterError(RuntimeError):
    """Raised when the OpenRouter API call fails or returns an unusable response."""


def clean_prediction(text: str | None) -> str:
    """Extract valid class name from LLM response"""
    if not text:
        return ""
    text = text.strip().lower()
    for cls in VALID_CLASSES:
        if cls in text:
            return cls
    logger.warning(f"Model response does not contain a valid class name: {text!r}")
    return text


def classify_image(api_key: str, image_path: Path, model: str = "openai/gpt-4o") -> dict:
    """
    Classify a document image using a vision model through OpenRouter API.
    Sends only the image to the vision model - no OCR text or feature data.
    """
    try:
        image_base64 = encode_image_base64(image_path)
    except OSError as e:
        raise OpenRouterError(f"Could not read image {image_path}: {e}") from e

    payload = {
        "model": model,
        "messages": build_vision_messages(CLASSIFICATION_PROMPT, image_base64),
        "max_tokens": 20,
        "temperature": 0.1
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )
    except requests.exceptions.RequestException as e:
        raise OpenRouterError(f"Request to OpenRouter failed for {image_path}: {e}") from e

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        try:
            error_body = response.json()
        except ValueError:
            error_body = response.text
        raise OpenRouterError(
            f"OpenRouter API error ({response.status_code}) for {image_path}: {error_body}"
        ) from e

    try:
        result = response.json()
    except ValueError as e:
        raise OpenRouterError(
            f"OpenRouter returned a non-JSON response for {image_path}: {response.text[:500]}"
        ) from e

    # OpenRouter can report upstream failures in a 200 response body
    if isinstance(result.get("error"), dict):
        raise OpenRouterError(f"OpenRouter returned an error for {image_path}: {result['error']}")

    try:
        prediction = result["choices"][0]["message"].get("content") or ""
    except (KeyError, IndexError, TypeError, AttributeError) as e:
        raise OpenRouterError(
            f"Unexpected OpenRouter response shape for {image_path}: {json.dumps(result)[:500]}"
        ) from e

    cleaned = clean_prediction(prediction)
    if not cleaned:
        logger.warning(f"Model returned an empty prediction for {image_path}")

    return {
        "status": "success" if cleaned else "empty_response",
        "classification": cleaned,
        "raw_response": prediction,
        "model": model,
        "usage": result.get("usage", {})
    }


if __name__ == "__main__":
    import sys

    logging.basicConfig(level=logging.INFO)

    API_KEY = os.environ.get("OPENROUTER_API_KEY")
    if not API_KEY:
        sys.exit("Error: OPENROUTER_API_KEY environment variable is not set.")

    IMAGE_PATH = Path(r"c:\Users\grant\AMFAM\processed_balanced_dataset\images\advertisement_0000139610_page_0001.png")

    try:
        result = classify_image(API_KEY, IMAGE_PATH)
    except OpenRouterError as e:
        sys.exit(f"Classification failed: {e}")
    print(json.dumps(result, indent=2))
