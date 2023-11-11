import os
import csv

csv_file = r"Resources\election_data.csv"

print("Election Results")
print("------------------------")

with open(csv_file, 'r') as datasheet:
    csvreader = csv.reader(datasheet, delimiter=",")
    next(csvreader)

    total_votes = list(csvreader)
    print(f"Total Votes: {len(total_votes)}")
    print("------------------------")

    