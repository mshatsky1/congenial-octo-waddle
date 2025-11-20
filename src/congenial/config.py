from __future__ import annotations

import tomli
from pathlib import Path


def load_config(config_path: Path | None = None) -> dict:
    """Load configuration from TOML file.
    
    Args:
        config_path: Path to config file. If None, looks for congenial.toml in current dir.
    
    Returns:
        Dictionary with configuration values
    """
    if config_path is None:
        config_path = Path("congenial.toml")
    
    if not config_path.exists():
        return {}
    
    with open(config_path, "rb") as f:
        return tomli.load(f)

