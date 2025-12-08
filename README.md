# congenial-octo-waddle

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Status](https://img.shields.io/badge/status-active-success)

A tiny sandbox repository for trying out tooling experiments.

## Quickstart

1. Create a virtual environment with `python -m venv .venv`.
2. Activate it and install dependencies via `pip install -e .`.
3. Run `python -m congenial.cli` or `scripts/run.sh` to print a friendly message.
4. Prefer the installed entry point via `congenial-greet` once the package is installed.

## Testing

- Install dev dependencies (currently none) and run `pytest`.
- Set `PYTHONPATH=src` if you do not install the package first.
- Run `pytest -q` for a terse test report when iterating quickly.

## Features

- Lightweight Python package structure.
- Simple CLI entry point for experimentation.
- Basic unit test illustrating usage.
- Color support for terminal output (`--color` flag).
- Configuration file support (congenial.toml).
- Logging functionality for debugging.
- Utility functions for name sanitization and validation.
- Error handling with custom exceptions.
- Version command (`--version`).

## Usage Examples

```bash
# Basic greeting
python -m congenial.cli Alice

# Greet someone in a specific timezone
python -m congenial.cli Carol --style formal --color

# With colored output
python -m congenial.cli Bob --color

# Show version
python -m congenial.cli --version
```

## Logging Example

```python
from congenial.logger import setup_logger

logger = setup_logger()
logger.info("Greeter ready")
```

## FAQ

**Why do I see timestamps in greetings?**  
Timestamps make it easy to tell when a message was generated; disable them by editing `congenial.toml`.

**How do I change the default greeting name?**  
Set `CONGENIAL_NAME` in `.env` or update the config file.

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.
