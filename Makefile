.PHONY: help install test clean

help:
	@echo "Available targets:"
	@echo "  install - Install package in development mode"
	@echo "  test    - Run tests"
	@echo "  clean   - Remove build artifacts"

install:
	pip install -e .

test:
	pytest

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache

