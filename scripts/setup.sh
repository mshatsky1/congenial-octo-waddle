#!/bin/bash
# Setup script for congenial-octo-waddle

set -e

echo "Setting up congenial-octo-waddle..."

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -e .

echo "Setup complete! Activate the virtual environment with: source .venv/bin/activate"

