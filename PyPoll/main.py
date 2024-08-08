#Create file paths.
import os
# Open csv reader.
import csv
from collections import Counter

# Create path.
csvpath = os.path.join('python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

# Establish Variables.
total_votes = 0
vote_counter = Counter()

# Open File.
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    # Read each row of data after the header
    for row in csvreader:
        total_votes += 1
        vote_counter[row[2]] += 1

# Calculate results
results = []
results.append("Election Results")
results.append("----------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("----------------------------")

for candidate, votes in vote_counter.items():
    percentage = round((votes / total_votes) * 100, 3)
    results.append(f"{candidate}: {percentage}% ({votes})")

results.append("----------------------------")

winner = max(vote_counter, key=vote_counter.get)
results.append(f"Winner: {winner}")
results.append("----------------------------")

# Print results to terminal
for line in results:
    print(line)

# Write results to text file
output_path = os.path.join('python-challenge', 'PyPoll', 'analysis', 'election_results.txt')

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w') as txtfile:
    for line in results:
        txtfile.write(line + '\n')

print(f"\nResults have been written to {output_path}")