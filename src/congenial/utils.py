"""Utility helpers for working with user-provided names."""

from __future__ import annotations

import re


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
    if not name or not name.strip():
        return False
    name_len = len(name.strip())
    return min_length <= name_len <= max_length


def validate_and_sanitize(name: str) -> str:
    """Validate and sanitize a name in one step.
    
    Args:
        name: Name to validate and sanitize
    
    Returns:
        Sanitized and capitalized name
    
    Raises:
        ValueError: If name is invalid after sanitization
    """
    if not name:
        raise ValueError("Name cannot be empty")
    
    sanitized = sanitize_name(name)
    if not validate_name(sanitized):
        raise ValueError(f"Name must be between 1 and 100 characters after sanitization")
    
    return capitalize_words(sanitized)



"""
Congenial Octo Waddle - Code Refactoring
"""

from typing import List, Dict, Optional

def optimize_algorithm(data: List[Dict]) -> List[Dict]:
    """Optimized version with better performance"""
    return [
        {**item, 'processed': True}
        for item in data
        if item.get('active', True)
    ]

def extract_metadata(obj: Dict) -> Optional[Dict]:
    """Extract metadata with type hints"""
    if not isinstance(obj, dict):
        return None
    
    return {
        'id': obj.get('id'),
        'timestamp': obj.get('timestamp'),
        'version': obj.get('version', '1.0.0')
    }
