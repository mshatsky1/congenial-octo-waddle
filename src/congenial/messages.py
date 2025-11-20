from __future__ import annotations

from datetime import datetime


# ANSI color codes
COLORS = {
    "reset": "\033[0m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "yellow": "\033[33m",
}


def build_greeting(name: str = "friend", use_color: bool = False) -> str:
    """Return a friendly greeting with a timestamp.
    
    Args:
        name: The name to greet
        use_color: Whether to use ANSI color codes in output
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    greeting = f"Hello, {name}! ({timestamp})"
    
    if use_color:
        greeting = f"{COLORS['green']}{greeting}{COLORS['reset']}"
    
    return greeting
