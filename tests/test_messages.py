from congenial import build_greeting


def test_build_greeting_includes_name():
    result = build_greeting("Alice")
    assert "Alice" in result
    assert result.startswith("Hello, Alice!")
