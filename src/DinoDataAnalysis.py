import pandas as pd
from pathlib import Path

def read_csv_file(file_path):
    """Reads a CSV file into a DataFrame with error handling for file reading."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return None
    except pd.errors.ParserError:
        print("Error parsing CSV file. Please check the file format.")
        return None

def validate_and_clean_data(df):
    """Validates and cleans the data, ensuring 'length' is numeric and filling missing values."""
    try:
        df['length'] = df['length'].str.rstrip('m').astype(float)
        df['length'] = df['length'].fillna(1.0)
        
        # Check for negative lengths and raise an error
        if (df['length'] < 0).any():
            raise ValueError("Negative length values found in the dataset.")
        
    except ValueError as e:
        print(f"Error in data validation: {e}")
        return None
    
    return df.dropna(subset=['species'])  # Exclude rows without a species

def find_largest_avg_species(df):
    """Finds the species with the largest average length."""
    avg_lengths = df.groupby('species')['length'].mean()
    largest_avg_species = avg_lengths.idxmax()
    largest_avg_length = avg_lengths.max()
    return largest_avg_species, largest_avg_length

def find_anagram_groups(df):
    """Finds groups of dinosaur names that are anagrams of each other."""
    # Create a copy of the DataFrame to avoid modifying the original data
    df_copy = df.copy()
    # Sort characters of each name to facilitate anagram grouping
    df_copy['sorted_name'] = df_copy['name'].apply(lambda x: ''.join(sorted(x)))
    # Group by sorted names and filter out groups with more than one member
    anagram_groups = df_copy.groupby('sorted_name')['name'].apply(list)
    return anagram_groups[anagram_groups.apply(len) > 1].tolist()

def main():
    """Main function to orchestrate the data processing and analysis."""
    # Construct the path to the CSV file relative to the script's location
    current_dir = Path(__file__).parent  # Get the current directory (src/)
    csv_path = current_dir.parent / 'data' / 'dinosaurs.csv'  # Construct the path to the CSV

    dino_data = read_csv_file(csv_path)  # Use the constructed path
    if dino_data is not None:
        cleaned_data = validate_and_clean_data(dino_data)
        if cleaned_data is not None:
            largest_avg_species, largest_avg_length = find_largest_avg_species(cleaned_data)
            print(f"Part1: {largest_avg_species} is the species with the largest average length.")

            anagram_groups = find_anagram_groups(cleaned_data)
            if anagram_groups:
                print("\n Part2: Groups of dinosaur names with the same letters:")
                for group in anagram_groups:
                    print(f"    - {' and '.join(group)}")
            else:
                print("\nPart2: No groups of dinosaur names share the same letters.")

if __name__ == "__main__":
    main()