from __future__ import annotations

from datetime import datetime


def build_greeting(name: str = "friend") -> str:
    """Return a friendly greeting with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello, {name}! ({timestamp})"
