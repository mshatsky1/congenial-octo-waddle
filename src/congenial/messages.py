from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo


# ANSI color codes
COLORS = {
    "reset": "\033[0m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "yellow": "\033[33m",
}


def build_greeting(
    name: str = "friend",
    use_color: bool = False,
    timezone: str | None = None,
    style: str = "standard"
) -> str:
    """Return a friendly greeting with a timestamp.
    
    Args:
        name: The name to greet
        use_color: Whether to use ANSI color codes in output
        timezone: Optional timezone string (e.g., 'America/New_York').
                  If None, uses system local time.
        style: Greeting style - 'standard', 'casual', or 'formal'
    """
    if timezone:
        tz = ZoneInfo(timezone)
        timestamp = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Different greeting styles
    styles = {
        "standard": f"Hello, {name}!",
        "casual": f"Hey, {name}!",
        "formal": f"Good day, {name}.",
    }
    
    greeting_template = styles.get(style, styles["standard"])
    greeting = f"{greeting_template} ({timestamp})"
    
    if use_color:
        greeting = f"{COLORS['green']}{greeting}{COLORS['reset']}"
    
    return greeting
