#!/usr/bin/env python3
"""Advanced usage examples of the congenial package."""

from congenial import build_greeting
from congenial.utils import sanitize_name, capitalize_words, validate_name
from congenial.logger import setup_logger

logger = setup_logger()


def demonstrate_styles():
    """Demonstrate different greeting styles."""
    name = "Developer"
    print("=== Greeting Styles ===")
    for style in ["standard", "casual", "formal"]:
        greeting = build_greeting(name, style=style)
        print(f"{style}: {greeting}")


def demonstrate_timezones():
    """Demonstrate timezone support."""
    print("\n=== Timezone Support ===")
    timezones = ["America/New_York", "Europe/London", "Asia/Tokyo"]
    for tz in timezones:
        try:
            greeting = build_greeting("World", timezone=tz)
            print(f"{tz}: {greeting}")
        except Exception as e:
            logger.error(f"Error with timezone {tz}: {e}")


def demonstrate_validation():
    """Demonstrate name validation."""
    print("\n=== Name Validation ===")
    test_names = ["Alice", "Bob123", "a" * 101, "", "Valid Name"]
    for name in test_names:
        is_valid = validate_name(name)
        print(f"'{name}': {is_valid}")


if __name__ == "__main__":
    demonstrate_styles()
    demonstrate_timezones()
    demonstrate_validation()

