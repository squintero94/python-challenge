import os
import csv

budget_csv = os.path.join("..", "Starter_Code 4", "PyBank", "Resources", "budget_data.csv")

# Counter Variable for Total Months
total_months = 0
total_profit_losses = 0
changes_in_profit_losses = []
previous_profit_loss = 0

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
        previous_profit_loss = current_profit_loss
    average_change = 0
    if len(changes_in_profit_losses) > 0:
        average_change = sum(changes_in_profit_losses) / len(changes_in_profit_losses)


    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_change:.2f}")

