"""Small text helpers used for clean-code practice commits."""

from typing import Final


EXPORTED_HELPERS: Final[list[str]] = ["normalize_spaces", "to_title_case"]


def normalize_spaces(text: str) -> str:
    """Collapse repeated spaces and trim outer spaces."""
    if not text:
        return ""
    return " ".join(text.split())


def to_title_case(text: str) -> str:
    """Convert text to title case after space normalization."""
    return normalize_spaces(text).title()
