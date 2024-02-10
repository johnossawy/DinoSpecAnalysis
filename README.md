
# DinoSpecsAnalysis 🦖

## Overview
This project contains Python scripts developed for analysing dinosaur data. The scripts identify the dinosaur species with the largest average length and group names that are anagrams of each other.

## Project Structure
- `src/`: Contains all the source code.
  - `DinoDataAnalysis.py`: A basic script for data analysis with standard validation and error handling.
  - `SecureDinoDataAnalysis.py`: An enhanced version with additional security features, comprehensive validation, and logging.
- `data/`: Contains the dinosaur dataset (`dinosaurs.csv`).
  - The script expects a CSV file (dinosaurs.csv) with the following columns:
    - name: Name of the dinosaur species
    - diet: Types of vore
    - period: The age of dinosaurs
    - lived_in: Country
    - type: Dinosaur
    - length: Length of the dinosaur (in meters)
    - species: The species classification of the dinosaur

## Approach and Security Enhancements
The second script (`SecureDinoDataAnalysis.py`) is designed with a focus on security and robust data processing. Key enhancements include:

- **File Validation**: Checks the file extension and inspects the file content using `csv.Sniffer` to ensure it's a valid CSV file, reducing the risk of processing malicious files.
- **Data Validation**: Includes advanced validation such as checking for negative lengths and ensuring numeric values in the 'length' column, enhancing data integrity.
- **Error Handling**: Utilizes detailed logging for errors and exceptions, providing clearer insights into issues and facilitating easier debugging.

These enhancements are aimed at securely managing and processing the data, reflecting best practices in software development and data security.

## Setup
To run this project, you'll need to install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage
For basic analysis, navigate to the `src/` directory and run:
```
python DinoDataAnalysis.py
```
For enhanced security and analysis, while still in the `src/` directory run:
```
python SecureDinoDataAnalysis.py ../data/dinosaurs.csv
```

Replace `<path-to-dinosaur-csv>` with the actual path to your dinosaur data CSV file.

## Output
The scripts will print results directly to the console:
- Part 1: Identifies the dinosaur species with the largest average length.
- Part 2: Lists any groups of dinosaur names that are anagrams of each other, or indicates if no anagrams are found.

## Dependencies
- Python 3.x
- Pandas
- pyarrow

