"""Shared OpenRouter constants and request helpers.

The API base is overridable via the ``OPENROUTER_BASE_URL`` environment
variable so any OpenAI-compatible vision endpoint can be plugged in without
code changes: OpenRouter (default), a local Ollama server
(``http://localhost:11434/v1``), or a self-hosted vLLM server
(``http://localhost:8000/v1``). ``OPENROUTER_API_URL`` can likewise be set to
a fully-qualified completions URL.
"""

import os

OPENROUTER_BASE_URL = os.environ.get(
    "OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"
).rstrip("/")
OPENROUTER_API_URL = os.environ.get(
    "OPENROUTER_API_URL", f"{OPENROUTER_BASE_URL}/chat/completions"
)


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
