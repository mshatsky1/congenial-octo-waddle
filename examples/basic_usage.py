#!/usr/bin/env python3
"""Example usage of the congenial package."""

from congenial import build_greeting
from congenial.utils import sanitize_name, capitalize_words


def main():
    """Demonstrate basic usage of congenial functions."""
    # Basic greeting
    print(build_greeting("World"))
    
    # Greeting with color
    print(build_greeting("Developer", use_color=True))
    
    # Using utility functions
    name = "john@doe.com"
    sanitized = sanitize_name(name)
    capitalized = capitalize_words(sanitized)
    print(f"Original: {name}")
    print(f"Sanitized: {sanitized}")
    print(f"Capitalized: {capitalized}")
    print(build_greeting(capitalized))


if __name__ == "__main__":
    main()



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
