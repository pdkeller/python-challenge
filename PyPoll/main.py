#Create file paths.
import os

#Open csv reader.
import csv

#Create path.
csvpath = os.path.join('python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

#Establish Variables.
total_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

#Open File.
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_votes = total_votes + 1
        if(row[2] == "Charles Casper Stockham"):
            stockham_votes = stockham_votes + 1
        if(row[2] == "Diana DeGette"):
            degette_votes = degette_votes + 1
        if(row[2] == "Raymon Anthony Doane"):
            doane_votes = doane_votes + 1

stockham_pct = round(stockham_votes / total_votes * 100, ndigits = 3)
degette_pct = round(degette_votes / total_votes * 100, ndigits = 3)
doane_pct = round(doane_votes / total_votes * 100, ndigits = 3)

if(int(stockham_votes) > int(degette_votes) and int(stockham_votes) > int(doane_votes)):
    winner = "Charles Casper Stockham"
elif(int(degette_votes) > int(stockham_votes) and int(degette_votes) > int(doane_votes)):
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"

#Print 
print("Election Results")
print("----------------------------")
print(f"Total Votes: " + str(total_votes))
print("----------------------------")
print("----------------------------")
print(f"Charles Casper Stockham: " + str(stockham_pct) + " % (" + str(stockham_votes) + ")")
print(f"Diana DeGette: " + str(degette_pct) + " % (" + str(degette_votes) + ")")
print(f"Raymon Anthony Doane: " + str(doane_pct) + " % (" + str(doane_votes) + ")")
print("----------------------------")
print(f"Winner: " + str(winner))
