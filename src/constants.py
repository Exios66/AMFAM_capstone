"""Shared constants used across the document intelligence pipeline."""

# Single source of truth for the 16 RVL-CDIP document classes.
DOCUMENT_CLASSES = (
    "advertisement",
    "budget",
    "email",
    "file_folder",
    "form",
    "handwritten",
    "invoice",
    "letter",
    "memo",
    "news_article",
    "presentation",
    "questionnaire",
    "resume",
    "scientific_publication",
    "scientific_report",
    "specification",
)

# Image file extensions handled by the dataset/EDA tooling (lowercase, with dot).
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp")
