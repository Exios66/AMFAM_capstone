"""Shared OpenRouter constants and request helpers."""

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"


def build_vision_messages(
    prompt: str,
    image_base64: str,
    image_format: str = "png",
) -> list[dict]:
    """Build an OpenAI-style ``messages`` payload with a text prompt and image.

    Args:
        prompt: The text instruction sent alongside the image.
        image_base64: Base64-encoded image contents.
        image_format: Image format for the data URI (e.g. "png").
    """
    return [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/{image_format};base64,{image_base64}"
                    },
                },
            ],
        }
    ]
