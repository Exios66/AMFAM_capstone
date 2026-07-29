"""Shared helpers for loading and validating environment variables."""

import os
import sys


class MissingEnvironmentError(RuntimeError):
    """Raised when required environment variables are not set."""


def load_dotenv_if_available() -> None:
    """Load variables from a .env file if python-dotenv is installed."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("Note: python-dotenv is not installed; relying on existing environment variables.")


def get_env(*names: str) -> tuple[str, ...]:
    """Return the requested environment variables.

    Loads a .env file first (if python-dotenv is available).

    Raises:
        MissingEnvironmentError: If any of the variables is unset or empty.
    """
    load_dotenv_if_available()

    missing = [name for name in names if not os.environ.get(name)]
    if missing:
        raise MissingEnvironmentError(
            f"Missing environment variables: {', '.join(missing)}. "
            f"Set them in your .env file or terminal."
        )

    return tuple(os.environ[name] for name in names)


def require_env(*names: str) -> tuple[str, ...]:
    """Return the requested environment variables, exiting if any are missing.

    Intended for use directly from a script entrypoint; library code should call
    :func:`get_env` and let ``MissingEnvironmentError`` propagate.
    """
    try:
        return get_env(*names)
    except MissingEnvironmentError as e:
        print(f"Error: {e}")
        sys.exit(1)
