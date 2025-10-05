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
