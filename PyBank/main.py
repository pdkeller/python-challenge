#Create file paths.
import os

#Open csv reader.
import csv

#Create path.
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

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

    # Read each row of data after the header
    for row in csvreader:
        month_total = month_total + 1
        net_total = net_total + int(row[1])
        profit_loss_change.append(int(row[1]))

#Print results.
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: " + month_total)
print(f"Total: " + net_total)
print(f"Average Change: " + average_change)
print(f"Greatest Increase in Profit: " + greatest_increase)
print(f"Greatest Decrease in Profit: " + greatest_decrease)
