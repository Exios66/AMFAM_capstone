"""Shared image helpers: base64 encoding and image discovery."""

import base64
from pathlib import Path
from typing import Iterable, Union

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
