"""Shared helpers for loading and validating environment variables."""

import os
import sys


def load_dotenv_if_available() -> None:
    """Load variables from a .env file if python-dotenv is installed."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass


def require_env(*names: str) -> tuple[str, ...]:
    """Return the requested environment variables, exiting if any are missing.

    Loads a .env file first (if python-dotenv is available). If any variable is
    unset, prints the missing names and exits with status 1.
    """
    load_dotenv_if_available()

    missing = [name for name in names if not os.environ.get(name)]
    if missing:
        print(f"Error: Missing environment variables: {', '.join(missing)}")
        print("Set them in your .env file or terminal.")
        sys.exit(1)

    return tuple(os.environ[name] for name in names)
