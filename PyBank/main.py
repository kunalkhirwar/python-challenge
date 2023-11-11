import os
import csv
import math

total_amount = 0
change = 0

print("Financial Analysis")
print("------------------------------")

data_path = r"Resources\budget_data.csv"

with open(data_path , 'r') as datafile:

    csv_reader = csv.reader(datafile, delimiter=',')
    next(csv_reader)
    
    total_months = list(csv_reader)
    print(f"Total Months: {len(total_months)}")
    
    for column in csv_reader:
        total_amount += int(column[1])
    print(f"Total: ${total_amount}")

    
    

