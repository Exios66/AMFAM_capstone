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
budget - Financial budgets, expense reports, financial planning documents
email - Email messages, email threads, electronic correspondence
file_folder - File folder labels, directory listings, file organization documents
form - Application forms, data entry forms, structured questionnaires
handwritten - Handwritten documents, notes, letters, manuscripts
invoice - Bills, invoices, receipts, payment requests
letter - Formal letters, correspondence, business communications
memo - Memorandums, internal communications, office memos
news_article - Newspaper articles, news reports, journalistic content
presentation - Presentation slides, slide decks, visual presentations
questionnaire - Surveys, questionnaires, data collection forms
resume - CVs, resumes, job applications, professional profiles
scientific_publication - Research papers, academic articles, scientific journals
scientific_report - Technical reports, lab reports, scientific documentation
specification - Technical specifications, requirements documents, product specs

Input Data:
- Document image (300 DPI grayscale)

Analysis Approach:
1. Examine the visual layout of the image (headers, tables, columns, formatting)
2. Read any visible text for key terms and document-specific vocabulary
3. Identify structural features (signatures, form fields, sections)
4. Consider document purpose and context

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
