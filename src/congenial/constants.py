"""Constants used throughout the congenial package."""

# Default values
DEFAULT_NAME = "friend"
DEFAULT_STYLE = "standard"
DEFAULT_TIMEZONE = None

# Greeting styles
STYLES = ["standard", "casual", "formal"]

# Name validation limits
MIN_NAME_LENGTH = 1
MAX_NAME_LENGTH = 100

# ANSI color codes
ANSI_RESET = "\033[0m"
ANSI_GREEN = "\033[32m"
ANSI_BLUE = "\033[34m"
ANSI_YELLOW = "\033[33m"
ANSI_RED = "\033[31m"

# Package metadata
PACKAGE_NAME = "congenial"
PACKAGE_VERSION = "0.1.0"



"""
Congenial Octo Waddle - Performance Improvement
"""

import logging
from functools import lru_cache

logger = logging.getLogger(__name__)

@lru_cache(maxsize=128)
def cached_computation(value):
    """Cached computation for better performance"""
    logger.debug(f"Computing value: {value}")
    return value ** 2

def batch_process(items, batch_size=100):
    """Process items in batches for better memory usage"""
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        yield process_batch(batch)

def process_batch(batch):
    """Process a single batch"""
    return [item.upper() for item in batch]
