#!/bin/bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source ./venv/bin/activate

# Install the package
python -m pip install .

# Activate the virtual environment
source ./venv/bin/activate

echo "Setup complete and the environment is activated."
