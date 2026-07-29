"""Shared helpers for console output."""


def print_header(title: str, width: int = 60) -> None:
    """Print a title framed by a line of ``=`` above and below it."""
    print("=" * width)
    print(title)
    print("=" * width)
