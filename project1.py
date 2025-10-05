### code for project 1
### Kyndal D
### ID: 85174585
### kyndald@umich.edu
### Gen AI used for debugging and helping with parts of code and structure
### Fall 2025
### Dataset: Penguins (from Kaggle)

import csv

# Function 1: Read CSV into a list of dictionaries
def read_csv(penguins_size.csv):
    with open('penguins_size.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data


# Function 2: Calculate average body mass per species per island
def calculate_avg_body_mass(data):
    # Dictionary to store sums and counts
    result = {}
    
    for row in data:
        species = row['species']
        island = row['island']
        mass = row['body_mass_g']
        
        # Skip missing data
        if mass == '' or species == '' or island == '':
            continue
        
        mass = float(mass)
        
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


# Function 3: Calculate percentage of male vs female penguins per island
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
        perc_result[island] = {
            'male_percentage': round((result[island]['male'] / total) * 100, 2),
            'female_percentage': round((result[island]['female'] / total) * 100, 2)
        }
    
    return perc_result


# Function 4: Write dictionary results to CSV
def write_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Determine headers
        headers = ['Island'] + list(next(iter(results.values())).keys())
        writer.writerow(headers)
        
        for island, values in results.items():
            row = [island] + [values[key] for key in values]
            writer.writerow(row)


# Main program
def main():
    # Read the data
    data = read_csv('penguins.csv')
    
    # Calculation 1
    avg_mass = calculate_avg_body_mass(data)
    write_results_to_csv(avg_mass, 'avg_body_mass.csv')
    
    # Calculation 2
    sex_percentages = calculate_sex_percentage(data)
    write_results_to_csv(sex_percentages, 'sex_percentages.csv')
    
    print("Analysis complete! Results written to avg_body_mass.csv and sex_percentages.csv")

if __name__ == '__main__':
    main()