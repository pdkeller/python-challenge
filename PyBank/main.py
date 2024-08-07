#Create file paths.
import os

#Open csv reader.
import csv

#Create path.
csvpath = os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

#Establish variables.
month_total = 0
net_total = 0
profit_loss_change = []
average_change = 0
greatest_increase = 0
greatest_decrease = 0

#Open File.
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csvheader = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        month_total = month_total + 1
        net_total = net_total + int(row[1])
        profit_loss_change.append(int(row[1]))

#Calculations.
average_change = sum(profit_loss_change) / len(profit_loss_change)
greatest_increase = max(profit_loss_change)
greatest_decrease = min(profit_loss_change)

#Print results.
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: " + str(month_total))
print(f"Total: $" + str(net_total))
print(f"Average Change: " + str(average_change))
print(f"Greatest Increase in Profit: " + str(greatest_increase))
print(f"Greatest Decrease in Profit: " + str(greatest_decrease))
