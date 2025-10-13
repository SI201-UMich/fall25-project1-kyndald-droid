### code for project 1
### Kyndal D
### ID: 85174585
### kyndald@umich.edu
### Gen AI used for debugging and helping with parts of code and structure
### Fall 2025
### Dataset: Penguins (from Kaggle)

### Project 1: Penguins Data Analysis
### Kyndal D
### ID: 85174585
### kyndald@umich.edu
### Gen AI used for debugging and helping with parts of code and structure
### Fall 2025
### Dataset: Penguins (from Kaggle)

import csv


# Function 1: Read CSV

def read_csv(filename):
    """
    Reads a CSV file and returns a list of dictionaries.
    Each row becomes a dictionary with column names as keys.
    """
    data = []  # List to hold all rows
    try:
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)  # Handles commas inside quotes
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return data


# Function 2: Average body mass per species per island

def calculate_avg_body_mass(data):
    result = {}
    
    for row in data:
        species = row['species']
        island = row['island']
        mass = row['body_mass_g']
        
        # Skip missing or invalid mass
        try:
            mass = float(mass)
        except (ValueError, TypeError):
            continue
        
        if species == '' or island == '':
            continue
        
        # Initialize nested dictionaries
        if island not in result:
            result[island] = {}
        if species not in result[island]:
            result[island][species] = {'total_mass': 0, 'count': 0}
        
        # Add mass and count
        result[island][species]['total_mass'] += mass
        result[island][species]['count'] += 1
    
    # Calculate averages
    avg_result = {}
    for island in result:
        avg_result[island] = {}
        for species in result[island]:
            total = result[island][species]['total_mass']
            count = result[island][species]['count']
            avg_result[island][species] = round(total / count, 2)
    
    return avg_result


# Function 3: Percentage of male vs female penguins per island

def calculate_sex_percentage(data):
    result = {}
    
    for row in data:
        island = row['island']
        sex = row['sex']
        
        if island == '' or sex == '':
            continue
        
        if island not in result:
            result[island] = {'male': 0, 'female': 0}
        
        if sex.lower() == 'male':
            result[island]['male'] += 1
        elif sex.lower() == 'female':
            result[island]['female'] += 1
    
    # Convert counts to percentages
    perc_result = {}
    for island in result:
        total = result[island]['male'] + result[island]['female']
        if total == 0:
            continue
        perc_result[island] = {
            'male_percentage': round((result[island]['male'] / total) * 100, 2),
            'female_percentage': round((result[island]['female'] / total) * 100, 2)
        }
    
    return perc_result


# Function 4: Write dictionary results to CSV

def write_results_to_csv(results, output_file):
    if not results:
        print(f"No data to write to {output_file}")
        return
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        headers = ['Island'] + list(next(iter(results.values())).keys())
        writer.writerow(headers)
        
        for island, values in results.items():
            row = [island] + [values[key] for key in values]
            writer.writerow(row)

 
# Main Program

def main():
    # UPDATE THIS PATH TO THE LOCATION OF YOUR CSV FILE
    csv_path = '/Users/kyndalduncan/SI201/fall25-project1-kyndald-droid/penguins_size.csv'
    
    # Read data
    data = read_csv(csv_path)
    if not data:
        return  # stop if reading failed
    
    # Calculation 1: Average body mass
    avg_mass = calculate_avg_body_mass(data)
    write_results_to_csv(avg_mass, 'avg_body_mass.csv')
    
    # Calculation 2: Sex percentages
    sex_percentages = calculate_sex_percentage(data)
    write_results_to_csv(sex_percentages, 'sex_percentages.csv')
    
    print("Analysis complete! Results written to avg_body_mass.csv and sex_percentages.csv")

# Run main
if __name__ == '__main__':
    main()
# ----------------------------
# Unit Tests for Project 1
# ----------------------------
import unittest

class TestPenguinsFunctions(unittest.TestCase):
    
    def setUp(self):
        # Sample data for testing calculations
        self.data = [
            {'species': 'Adelie', 'island': 'Biscoe', 'body_mass_g': '3700', 'sex': 'male'},
            {'species': 'Adelie', 'island': 'Biscoe', 'body_mass_g': 'NA', 'sex': 'female'},
            {'species': 'Gentoo', 'island': 'Dream', 'body_mass_g': '5000', 'sex': 'female'},
            {'species': 'Chinstrap', 'island': 'Dream', 'body_mass_g': '3550', 'sex': 'male'},
            {'species': 'Adelie', 'island': 'Dream', 'body_mass_g': '3750', 'sex': 'female'}
        ]
    
    # Test average body mass calculation
    def test_avg_body_mass(self):
        expected = {
            'Biscoe': {'Adelie': 3700.0},
            'Dream': {'Gentoo': 5000.0, 'Chinstrap': 3550.0, 'Adelie': 3750.0}
        }
        result = calculate_avg_body_mass(self.data)
        self.assertEqual(result, expected)
    
    # Test sex percentage calculation
    def test_sex_percentage(self):
        expected = {
            'Biscoe': {'male_percentage': 100.0, 'female_percentage': 0.0},
            'Dream': {'male_percentage': 33.33, 'female_percentage': 66.67}
        }
        result = calculate_sex_percentage(self.data)
        # Round the results for comparison
        for island in result:
            for key in result[island]:
                result[island][key] = round(result[island][key], 2)
        self.assertEqual(result, expected)
    
    # Test empty data
    def test_empty_data(self):
        self.assertEqual(calculate_avg_body_mass([]), {})
        self.assertEqual(calculate_sex_percentage([]), {})

# Run the tests
print("\nRunning unit tests...\n")
unittest.main(argv=[''], exit=False)
