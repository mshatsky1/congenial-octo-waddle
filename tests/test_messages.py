from congenial import build_greeting
from congenial.utils import sanitize_name, capitalize_words, validate_name


def test_build_greeting_includes_name():
    result = build_greeting("Alice")
    assert "Alice" in result
    assert result.startswith("Hello, Alice!")


def test_build_greeting_defaults_to_friend():
    result = build_greeting()
    assert "friend" in result
    assert result.startswith("Hello, friend!")


def test_build_greeting_with_color():
    result = build_greeting("Bob", use_color=True)
    assert "Bob" in result
    assert "\033" in result  # ANSI escape code


def test_sanitize_name():
    assert sanitize_name("John@Doe!") == "JohnDoe"
    assert sanitize_name("  test  ") == "test"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("JOHN DOE") == "John Doe"


def test_validate_name():
    assert validate_name("Alice") is True
    assert validate_name("") is False
    assert validate_name("a" * 101) is False


"""
Congenial Octo Waddle - Bug Fix
"""

def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def parse_config(config_str):
    """Parse configuration string with improved error handling"""
    if not config_str:
        return {}
    
    try:
        import json
        return json.loads(config_str)
    except json.JSONDecodeError as e:
        print(f"Warning: Invalid JSON config: {e}")
        return {}
