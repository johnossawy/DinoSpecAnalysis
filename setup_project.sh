#!/bin/bash

# Navigate to your project root directory
cd /Users/johnossawy/Code/projects/CME/DinoSpecAnalysis

# Create the directory structure
mkdir -p src data tests

# Move Python scripts to the src/ directory
mv DinoDataAnalysis.py SecureDinoDataAnalysis.py src/

# Move the dataset to the data/ directory
mv dinosaurs.csv data/

# Create empty __init__.py in src/
touch src/__init__.py

echo "Project directory structure set up successfully."
