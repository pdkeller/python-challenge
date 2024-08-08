# Create file paths.
import os
# Open csv reader.
import csv

# Create path.
csvpath = os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

# Establish variables.
month_total = 0
net_total = 0
last_row = 0
profit_loss_change = []
average_change = 0
greatest_increase = 0
greatest_decrease = 0

# Open File.
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first.
    csvheader = next(csvreader)
    first_row = next(csvreader)
    month_total += 1
    net_total += int(first_row[1])
    last_row = int(first_row[1])
    
    # Read each row of data after the header
    for row in csvreader:
        month_total += 1
        net_total += int(row[1])
        
        change = int(row[1]) - last_row
        profit_loss_change.append(change)
        if change > greatest_increase:
            greatest_increase = change
            best_month = str(row[0])
        if change < greatest_decrease:
            greatest_decrease = change
            worst_month = str(row[0])
        last_row = int(row[1])

# Calculations.
average_change = round(sum(profit_loss_change) / len(profit_loss_change), 2)

# Prepare results.
results = [
    "Financial Analysis",
    "------------------------------------",
    f"Total Months: {month_total}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change}",
    f"Greatest Increase in Profits: {best_month} (${greatest_increase})",
    f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})"
]

# Print results to terminal.
for line in results:
    print(line)

# Set variable for output file.
output_path = os.path.join('python-challenge', 'PyBank', 'analysis', 'financial_analysis.txt')

# Write results to text file.
with open(output_path, 'w') as txtfile:
    for line in results:
        txtfile.write(line + '\n')

print(f"\nResults have been written to {output_path}")