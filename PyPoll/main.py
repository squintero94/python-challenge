import os
import csv

election_csv = os.path.join("..", "Starter_Code 4", "PyPoll", "Resources", "election_data.csv")

# Establish Counter / Capture Variables
total_votes = 0
CCS_votes = 0
DD_votes = 0
RAD_votes = 0

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip the header row if it exists
    header = next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        if row[2] == "Charles Casper Stockham":
            CCS_votes += 1
        elif row[2] == "Diana DeGette":
            DD_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            RAD_votes += 1

# Print the Result to the Terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Charles Casper Stockham: {CCS_votes}")
print(f"Diana DeGette: {DD_votes}")
print(f"Raymon Anthony Doane: {RAD_votes}")