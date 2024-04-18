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
        # Calculate Vote %
        CCS_vote_share = round((CCS_votes / total_votes) * 100, 3)
        DD_vote_share = round((DD_votes / total_votes) * 100, 3)
        RAD_vote_share = round((RAD_votes / total_votes) * 100, 3)
 # Find Winner
if (CCS_votes > DD_votes) & (CCS_votes > RAD_votes):
    winner = str("Charles Casper Stockham")
elif (DD_votes > CCS_votes) & (DD_votes > RAD_votes):
    winner = str("Diana DeGette")
elif (RAD_votes > CCS_votes) & (RAD_votes > DD_votes):
    winner = str("Raymon Anthony Doane")
                               

# Print the Result to the Terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Charles Casper Stockham: {CCS_vote_share}% ({CCS_votes})")
print(f"Diana DeGette: {DD_vote_share}% ({DD_votes})")
print(f"Raymon Anthony Doane: {RAD_vote_share}% ({RAD_votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Define the output file path
output_file = os.path.join("PyPoll_Results.txt")

# Write the results to a text file
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"Charles Casper Stockham: {CCS_vote_share}% ({CCS_votes})\n")
    file.write(f"Diana DeGette: {DD_vote_share}% ({DD_votes})\n")
    file.write(f"Raymon Anthony Doane: {RAD_vote_share}% ({RAD_votes})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------\n")

# Print a message to confirm the export
print("Results have been exported to 'PyPoll_Results.txt'")