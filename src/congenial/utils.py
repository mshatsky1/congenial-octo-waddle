from __future__ import annotations

import re
from typing import Any


def sanitize_name(name: str) -> str:
    """Sanitize a name by removing special characters.
    
    Args:
        name: The name to sanitize
    
    Returns:
        Sanitized name with only alphanumeric and spaces
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", name).strip()


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word.
    
    Args:
        text: Text to capitalize
    
    Returns:
        Text with each word capitalized
    """
    return " ".join(word.capitalize() for word in text.split())


def validate_name(name: str, min_length: int = 1, max_length: int = 100) -> bool:
    """Validate that a name meets length requirements.
    
    Args:
        name: Name to validate
        min_length: Minimum allowed length
        max_length: Maximum allowed length
    
    Returns:
        True if name is valid, False otherwise
    """
    if not isinstance(name, str):
        return False
    return min_length <= len(name) <= max_length

