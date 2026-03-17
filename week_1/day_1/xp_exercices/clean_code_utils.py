"""Small text helpers used for clean-code practice commits."""

from typing import Final


EXPORTED_HELPERS: Final[list[str]] = ["normalize_spaces", "to_title_case"]
__all__ = EXPORTED_HELPERS
DEFAULT_EMPTY_RESULT: Final[str] = ""


def has_content(text: str) -> bool:
    """Return True when text contains at least one non-space character."""
    return bool(trim_edges(text))


def trim_edges(text: str) -> str:
    """Trim leading and trailing whitespace safely."""
    return text.strip() if text else DEFAULT_EMPTY_RESULT


def normalize_spaces(text: str) -> str:
    """Collapse repeated spaces and trim outer spaces."""
    if not has_content(text):
        return DEFAULT_EMPTY_RESULT
    # split() without arguments collapses any run of whitespace.
    parts = text.split()
    return " ".join(parts)


def to_title_case(text: str) -> str:
    """Convert text to title case after space normalization."""
    normalized_text = normalize_spaces(text)
    return normalized_text.title()
