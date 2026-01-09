from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

from .cli import CongenialError


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
        try:
            tz = ZoneInfo(timezone)
            timestamp = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")
        except Exception as e:
            raise CongenialError(f"Invalid timezone: {timezone}. {str(e)}")
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


"""
Congenial Octo Waddle - Feature Enhancement
"""

def process_data(data):
    """Process and validate input data"""
    if not data:
        raise ValueError("Data cannot be empty")
    
    processed = []
    for item in data:
        if isinstance(item, dict):
            processed.append(validate_item(item))
        else:
            processed.append(str(item).strip())
    
    return processed

def validate_item(item):
    """Validate individual item structure"""
    required_fields = ['id', 'name']
    for field in required_fields:
        if field not in item:
            raise ValueError(f"Missing required field: {field}")
    return item

class DataProcessor:
    """Main data processing class"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.cache = {}
    
    def process(self, data):
        """Main processing method"""
        cache_key = hash(str(data))
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        result = process_data(data)
        self.cache[cache_key] = result
        return result
