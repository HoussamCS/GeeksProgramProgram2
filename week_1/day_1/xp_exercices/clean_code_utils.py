"""Small text helpers used for clean-code practice commits."""

from typing import Final


EXPORTED_HELPERS: Final[list[str]] = ["normalize_spaces", "to_title_case"]
__all__ = EXPORTED_HELPERS
DEFAULT_EMPTY_RESULT: Final[str] = ""


def normalize_spaces(text: str) -> str:
    """Collapse repeated spaces and trim outer spaces."""
    if not text:
        return DEFAULT_EMPTY_RESULT
    parts = text.split()
    return " ".join(parts)


def to_title_case(text: str) -> str:
    """Convert text to title case after space normalization."""
    return normalize_spaces(text).title()
