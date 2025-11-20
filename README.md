# congenial-octo-waddle

A tiny sandbox repository for trying out tooling experiments.

## Quickstart

1. Create a virtual environment with `python -m venv .venv`.
2. Activate it and install dependencies via `pip install -e .`.
3. Run `python -m congenial.cli` or `scripts/run.sh` to print a friendly message.

## Testing

- Install dev dependencies (currently none) and run `pytest`.
- Set `PYTHONPATH=src` if you do not install the package first.

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

# With colored output
python -m congenial.cli Bob --color

# Show version
python -m congenial.cli --version
```

## License

Released under the MIT License.
