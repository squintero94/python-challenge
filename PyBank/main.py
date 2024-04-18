import os
import csv

budget_csv = os.path.join("..", "Starter_Code 4", "PyBank", "Resources", "budget_data.csv")

# Counter Variable for Total Months
total_months = 0
total_profit_losses = 0
changes_in_profit_losses = []
previous_profit_loss = 0
greatest_increase_amount = 0
greatest_increase_date = ""
greatest_decrease_amount = 0
greatest_decrease_date = ""

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Skip the header row if it exists
    header = next(csv_reader)
    
    for row in csv_reader:
        total_months = total_months + 1
        profit_loss = int(row[1])
        total_profit_losses += profit_loss
        current_profit_loss = int(row[1])
        if previous_profit_loss != 0:
            change = current_profit_loss - previous_profit_loss
            changes_in_profit_losses.append(change)
            # Check for greatest increase
            if change > greatest_increase_amount:
                greatest_increase_amount = change
                greatest_increase_date = row[0]
            # Check for greatest decrease
            if change < greatest_decrease_amount:
                greatest_decrease_amount = change
                greatest_decrease_date = row[0]
        previous_profit_loss = current_profit_loss
    average_change = 0
    if len(changes_in_profit_losses) > 0:
        average_change = sum(changes_in_profit_losses) / len(changes_in_profit_losses)

# Print the Result to the Terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

# Define the output file path
output_file = os.path.join("PyBank_Results.txt")

# Write the results to a text file
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

# Print a message to confirm the export
print("Results have been exported to 'PyBank_Results.txt'")