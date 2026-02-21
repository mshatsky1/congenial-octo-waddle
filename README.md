# congenial-octo-waddle

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Status](https://img.shields.io/badge/status-active-success)

A tiny sandbox repository for trying out tooling experiments.

## Installation

Install the package in development mode:

```bash
pip install -e .
```

Or use the setup script:

```bash
./scripts/setup.sh
```

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

## Troubleshooting

**Import errors?**  
Make sure you've installed the package with `pip install -e .` or set `PYTHONPATH=src`.

**Command not found?**  
After installation, use `congenial-greet` instead of `python -m congenial.cli`.

## Related Projects

This is a sandbox repository for experimentation. For production Python packages, consider:
- [Poetry](https://python-poetry.org/) for dependency management
- [setuptools](https://setuptools.pypa.io/) for packaging

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.

<!-- Update 1 -->

<!-- Update 2 -->

<!-- Update 3 -->

<!-- Update 4 -->

<!-- Update 5 -->

<!-- Update 6 -->

<!-- Update 7 -->

<!-- Update 8 -->

<!-- Update 9 -->

<!-- Update 10 -->

<!-- Update 11 -->

<!-- Update 12 -->

<!-- Update 13 -->

<!-- Update 14 -->

<!-- Update 15 -->

<!-- Update 16 -->

<!-- Update 17 -->

<!-- Update 18 -->

<!-- Update 19 -->

<!-- Update 20 -->

<!-- Update 21 -->

<!-- Update 22 -->

<!-- Update 23 -->

<!-- Update 24 -->

<!-- Update 25 -->

<!-- Update 26 -->

<!-- Update 27 -->

<!-- Update 28 -->

<!-- Update 29 -->

<!-- Update 30 -->

<!-- Update 31 -->

<!-- Update 32 -->

<!-- Update 33 -->

<!-- Update 34 -->

<!-- Update 35 -->

<!-- Update 1 -->

<!-- Update 2 -->

<!-- Update 3 -->

<!-- Update 4 -->

<!-- Update 5 -->

<!-- Update 6 -->

<!-- Update 7 -->

<!-- Update 8 -->

<!-- Update 9 -->

<!-- Update 10 -->

<!-- Update 11 -->

<!-- Update 12 -->

<!-- Update 13 -->

<!-- Update 14 -->

<!-- Update 15 -->

<!-- Update 16 -->

<!-- Update 17 -->

<!-- Update 18 -->

<!-- Update 19 -->

<!-- Update 20 -->

<!-- Update 21 -->

<!-- Update 22 -->

<!-- Update 23 -->

<!-- Update 24 -->

<!-- Update 25 -->
