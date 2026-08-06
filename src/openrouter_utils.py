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

# The classification prompts (v4+) end their instruction context with a
# "## Output format" section. Everything BEFORE that header is the static
# introduction context (preamble, labels, scratchpad procedure, pre-scan,
# checks, calibration, worked examples) and can be offloaded to the system
# message; the output-format section stays in the user turn alongside the
# image so the response contract is written next to the content.
OUTPUT_FORMAT_MARKER = "## Output format"


def split_prompt(prompt: str) -> tuple[str, str]:
    """Split a classification prompt into ``(system_text, user_text)``.

    ``system_text`` is the instruction context up to (and excluding) the first
    ``## Output format`` header; ``user_text`` is the remainder (the output
    format contract, plus any trailing calibration/work-example text). The
    split is byte-lossless: ``system_text + user_text == prompt`` — no tokens
    are added or removed, so model behavior is not changed by the split.

    Prompts without the marker (e.g. pre-v4 versions) fall back to the whole
    prompt as system text and an empty user text (the image-only user turn).
    """
    if not prompt:
        return "", ""
    idx = prompt.find(OUTPUT_FORMAT_MARKER)
    if idx == -1:
        return prompt, ""
    system_text = prompt[:idx]
    user_text = prompt[idx:]
    return system_text, user_text


def build_vision_messages(
    prompt: str,
    image_base64: str,
    image_format: str = "png",
    split_intro: bool = False,
) -> list[dict]:
    """Build an OpenAI-style ``messages`` payload with a text prompt and image.

    Args:
        prompt: The text instruction sent alongside the image.
        image_base64: Base64-encoded image contents.
        image_format: Image format for the data URI (e.g. "png").
        split_intro: When True, offload the prompt's introduction context
            (everything before ``## Output format``) into a ``system`` message
            and send the output-format text + image in the ``user`` message
            instead of passing the whole prompt in one bulk user request.
    """
    if split_intro:
        system_text, user_text = split_prompt(prompt)
        messages = []
        if system_text:
            messages.append({"role": "system", "content": system_text})
        user_content: list[dict] = []
        if user_text:
            user_content.append({"type": "text", "text": user_text})
        user_content.append(
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/{image_format};base64,{image_base64}"
                },
            }
        )
        messages.append({"role": "user", "content": user_content})
        return messages

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
