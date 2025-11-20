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

