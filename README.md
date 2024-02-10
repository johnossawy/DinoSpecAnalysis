
# DinoSpecsAnalysis 🦖

## Overview
This project contains Python scripts developed for analysing dinosaur data. The scripts identify the dinosaur species with the largest average length and group names that are anagrams of each other.

## Challenge Objectives
The main objectives of this coding challenge are twofold:
1. **Identify the Dinosaur with the Largest Average Length**: Determine which dinosaur species has the highest average length based on the given dataset, showcasing the giants of the prehistoric era.
2. **Group Anagram Names**: Group dinosaur names that are anagrams of each other.

## Project Structure
- `src/`: Contains all the source code.
  - `DinoDataAnalysis.py`: A basic script for data analysis with standard validation and error handling.
  - `SecureDinoDataAnalysis.py`: An enhanced version with additional security features, comprehensive validation, and logging.
- `data/`: Contains the dinosaur dataset (`dinosaurs.csv`), structured as follows:
  - `name`: Name of the dinosaur species
  - `diet`: Types of vore
  - `period`: The age of dinosaurs
  - `lived_in`: Country
  - `type`: Dinosaur
  - `length`: Length of the dinosaur (in meters)
  - `species`: The species classification of the dinosaur

## Expected Input Format
The scripts expect a CSV file named `dinosaurs.csv` with specific columns as outlined above. It's important to note:
- **Missing Values**: In cases where the 'length' value is missing, the script assumes a default length of 1.0m to maintain continuity in data analysis.
- **Ignored Rows**: Rows without a specified 'species' are disregarded, ensuring focus on well-classified data.

## Algorithmic Approach
For identifying the dinosaur with the largest average length, the script calculates the mean length for each species and identifies the maximum. For the anagram grouping:
- **Data Preprocessing**: Converts names to lowercase to ensure case-insensitive matching.
- **Sorting Letters**: For each name, letters are sorted alphabetically; this sorted version acts as a key in a dictionary where the original names are stored as values.
- **Grouping Anagrams**: Names with identical sorted letter sequences are grouped together as anagrams.

These methods ensure efficient and accurate analysis, utilising Python's robust data handling and string manipulation capabilities.

## Approach and Security Enhancements
The `SecureDinoDataAnalysis.py` script introduces several security and data integrity enhancements:
- **File Validation**: Ensures only valid CSV files are processed, mitigating the risk of malicious file execution.
- **Data Validation**: Advanced checks prevent processing of anomalous data, such as negative lengths, ensuring reliable analysis results.
- **Error Handling**: Comprehensive logging facilitates troubleshooting and enhances script robustness.

These features reflect best practices in secure software development, ensuring the script's reliability and safety in data processing.

## Setup
To run this project, you'll need to install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage
For basic analysis, navigate to the `src/` directory run:

```
python DinoDataAnalysis.py
```

For enhanced security and analysis, while still in the `src/` directory run:

```
python SecureDinoDataAnalysis.py ../data/dinosaurs.csv
```

Replace `<path-to-dinosaur-csv>` with the actual path to your dinosaur data CSV file.

## Output
Results are printed to the console, including:
- **Part 1**: The dinosaur species with the largest average length.
- **Part 2**: Groups of names that are anagrams, or a note if none are found.

## Dependencies
- Python 3.x
- Pandas
- pyarrow
