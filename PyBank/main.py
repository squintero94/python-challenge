import os
import csv

budget_csv = os.path.join("..", "Starter_Code 4", "PyBank", "Resources", "budget_data.csv")

# Counter Variable for Total Months
total_months = 0

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Skip the header row if it exists
    header = next(csv_reader)
    
    for row in csv_reader:
        total_months = total_months + 1

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")

