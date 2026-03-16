"""Small text helpers used for clean-code practice commits."""


def normalize_spaces(text: str) -> str:
    """Collapse repeated spaces and trim outer spaces."""
    return " ".join(text.split())
