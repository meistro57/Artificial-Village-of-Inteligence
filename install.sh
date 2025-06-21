#!/usr/bin/env bash
# Setup script for Ubuntu
# This script installs Python dependencies in a virtual environment
# and runs the test suite.

set -e

# Install required system packages
sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-pip

# Create virtual environment if it does not exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run tests to verify installation
pytest

echo "Installation complete. Activate with 'source .venv/bin/activate' to run the project."
