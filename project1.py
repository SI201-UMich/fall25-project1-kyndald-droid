### code for project 1
### Kyndal D
### ID: 85174585
### kyndald@umich.edu
### Gen AI used for debugging and helping with parts of code and structure
### Fall 2025
### Dataset: Penguins (from Kaggle)

import csv

# Function 1: Read CSV into a list of dictionaries
def read_csv(filename):
    with open(filename, newline='') as csvfile:
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