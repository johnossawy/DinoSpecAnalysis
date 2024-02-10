import pandas as pd
import os
import csv
import argparse
import logging
import sys

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_valid_csv(file_path):
    """Enhanced validation to check file extension and use csv.Sniffer for content inspection."""
    if not file_path.lower().endswith('.csv'):
        logging.error("This file doesn't end in .csv. Please verify the file extension.")
        sys.exit("Exiting due to incorrect file extension.")  # Exit script execution

    try:
        with open(file_path, 'r') as csvfile:
            sample = csvfile.read(2048)
            csvfile.seek(0)
            if csv.Sniffer().has_header(sample) and csv.Sniffer().sniff(sample):
                logging.info("CSV file looks valid.")
                return True
    except csv.Error as e:
        logging.error("Parsing issue with the CSV file: %s", e)
        sys.exit("Exiting due to CSV parsing issue.")  # Exit script execution
    except Exception as e:
        logging.error("Unable to read file: %s. Please confirm the file is a CSV and the dataset is correct.", e)
        sys.exit("Exiting due to file reading issue.")  # Exit script execution

    # If the function hasn't exited by now, it means the file doesn't seem to be a valid CSV
    logging.error("The file does not appear to be a valid CSV.")
    sys.exit("Exiting as the file does not appear to be a valid CSV.")  # Exit script execution

# Task 1: Species with the largest average length
# Exclude rows without a species and calculate average length per species
def preprocess_data(dino_data, default_length_m=1.0):
    """Preprocesses the dinosaur data by cleaning and preparing the 'length' field."""
    try:
        # Convert 'length' values to float after removing 'm' suffix
        # This step assumes 'length' values are stored as strings like '5m', '10.5m', etc.
        dino_data['length'] = dino_data['length'].str.replace('m', '').astype(float)
    except ValueError as e:
        # Log an error message if the 'length' column contains values that cannot be converted to float
        logging.error("Data cleaning error - 'length' column: %s. Check the CSV data for non-numeric values.", e)
        sys.exit("Exiting due to data cleaning error.")  # Exit script

    # Identify and log rows with negative 'length' values, if any
    if (dino_data['length'] < 0).any():
        logging.error("Data validation error - Negative 'length' values found. Review the data for inaccuracies.")
        sys.exit("Exiting due to data validation error.")  # Exit script

    # Fill missing 'length' values with the default length and drop rows missing 'species' information
    dino_data['length'] = dino_data['length'].fillna(default_length_m)
    dino_data.dropna(subset=['species'], inplace=True)

    return dino_data

def analyse_data(dino_data):
    """Performs analysis on the preprocessed dinosaur data."""
    average_lengths_per_species = dino_data.groupby('species')['length'].mean()
    longest_dino_species = average_lengths_per_species.idxmax()
    longest_dino_average_length = average_lengths_per_species.max()
    print(f"\nPart1: The longest dino species is {longest_dino_species}, averaging a whopping {longest_dino_average_length}m.\n")

    # Task 2: Grouping names by the same letters
    # Sort the letters of each name and use as a key for grouping
    dino_data['sorted_name'] = dino_data['name'].apply(lambda x: ''.join(sorted(x.lower().replace(' ', ''))))
    grouped_anagrams = dino_data.groupby('sorted_name')['name'].agg(list)  # Group names by sorted_name and aggregate as lists
    anagrams = grouped_anagrams[grouped_anagrams.apply(len) > 1]  # Filter groups with more than one name

    # Check if there are any groups of names with the same letters
    if not anagrams.empty:
        print("Part2: Dino name mix-up! Here are some dinos that could swap names if they wanted to:")
        for anagram_group in anagrams:
            print(f"    - {' and '.join(anagram_group)} are anagram buddies! 🦖")
    else:
        print("Part2: No dino name mix-ups today. Every dino is uniquely named, as it should be!\n")

def main(csv_file_path, default_length_m=1.0):
    """Main function to orchestrate the CSV validation, preprocessing, and analysis."""
    if not is_valid_csv(csv_file_path):
        logging.error("That doesn't look like a dino dataset. Are you sure it's a CSV file?")
        return

    try:
        dino_data = pd.read_csv(csv_file_path)
        preprocessed_data = preprocess_data(dino_data, default_length_m)
        if preprocessed_data is not None:
            analyse_data(preprocessed_data)
    except (FileNotFoundError, pd.errors.ParserError) as e:
        logging.error("Couldn't process that CSV file. check formatting of the CSV.")

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
    description='This script processes dinosaur data from a CSV file. It performs various analyses, such as calculating the average length of dinosaurs by species and identifying dinosaur names that are anagrams of each other.',
    epilog='Example: python3 dinosaurs_secure.py dinosaurs.csv\n'
)    
    # Add an argument for the CSV file path
    parser.add_argument(
    'csv_file_path', 
    type=str, 
    help='Path to the CSV file containing dinosaur data. The file should be in CSV format with columns for species, length, etc.'
)    
    # Parse the command line arguments
    args = parser.parse_args()
    
    # Call main with the provided CSV file path
    main(args.csv_file_path)