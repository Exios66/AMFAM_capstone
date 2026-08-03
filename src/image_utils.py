"""Shared image helpers: base64 encoding, image discovery, and resizing."""

import base64
from pathlib import Path
from typing import Iterable, Tuple, Union

from PIL import Image

from src.constants import IMAGE_EXTENSIONS


def encode_image_base64(image_path: Union[str, Path]) -> str:
    """Read an image file and return its base64-encoded contents."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def find_images(
    directory: Union[str, Path],
    extensions: Iterable[str] = IMAGE_EXTENSIONS,
    recursive: bool = False,
) -> list[Path]:
    """Return a sorted list of image paths in ``directory``.

    Args:
        directory: Directory to search.
        extensions: Image extensions to include (lowercase, with leading dot).
        recursive: If True, search subdirectories as well.
    """
    directory = Path(directory)
    globber = directory.rglob if recursive else directory.glob
    paths: list[Path] = []
    for ext in extensions:
        paths.extend(globber(f"*{ext}"))
    return sorted(paths)


def _pad_color_for_mode(mode: str, fill: Union[int, Tuple[int, ...]]) -> Union[int, Tuple[int, ...]]:
    """Coerce a padding fill color to a value valid for the given image mode."""
    if mode == "L":
        return fill if isinstance(fill, int) else fill[0]
    if mode == "1":
        return 1 if fill else 0
    if mode == "RGBA":
        return fill if isinstance(fill, tuple) else (fill, fill, fill, fill)
    # RGB or any fallback converted to RGB
    return fill if isinstance(fill, tuple) else (fill, fill, fill)


def resize_with_padding(
    img: Image.Image,
    target_size: Tuple[int, int],
    fill: Union[int, Tuple[int, ...]] = 255,
) -> Image.Image:
    """Scale an image to fit inside ``target_size``, then center-pad to the exact size."""
    target_w, target_h = target_size

    scale = min(target_w / img.width, target_h / img.height)
    new_w = max(1, int(img.width * scale))
    new_h = max(1, int(img.height * scale))
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    # Convert palette/other modes to RGB so a solid fill always works
    if resized.mode not in ("L", "1", "RGB", "RGBA"):
        resized = resized.convert("RGB")

    bg_fill = _pad_color_for_mode(resized.mode, fill)
    background = Image.new(resized.mode, target_size, bg_fill)

    x = (target_w - new_w) // 2
    y = (target_h - new_h) // 2
    if resized.mode == "RGBA":
        background.paste(resized, (x, y), resized)
    else:
        background.paste(resized, (x, y))

    return background
