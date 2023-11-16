import os
import csv
import math

total_month = 0
total_amount = 0
change = 0
next_value = 0
value_list = []
counter = 0
sum = 0
average_value = 0
greatest_decrease = 0
greatest_increase = 0

print("Financial Analysis")
print("------------------------------")

data_path = r"PyBank\Resources\budget_data.csv"

with open(data_path , 'r') as datafile:

    csv_reader = csv.reader(datafile, delimiter=',')
    next(csv_reader)
               
    for row in csv_reader:
        total_amount += int(row[1])     #used 'total_amount' variable to sum the value in 'Profit/Losses' column each time the 'for' loop iterates 
        total_month += 1                #used 'total_month' variable to add 1 every time the 'for' loop iterates
    
        counter += 1
        current_value = row[1]
            
        if counter == 1:                      # used 'if' statment to skip the first value as no value exists before to subtract
            previous_value = current_value
                                                    
        else:
            # used'subtract' variable to store the difference between current value and previus value which changes with 'counter' every time 'for' loop iterates
            subtraction = int(current_value) - int(previous_value)

            # 'current value' of present iteration becomes previus value for next iteration
            previous_value = current_value 
                
            value_list.append(subtraction)
            
    print(f"Total Months: {total_month}")
    print(f"Total: ${total_amount}")           
    
    for values in value_list:
        sum += values
        average_value = round((sum)/len(value_list),2)
    greatest_increase = max(value_list)
    greatest_decrease = min(value_list)
    print(f"Average Change: ${average_value}") 
    print(f"Greatest Increase in Profits: (${greatest_increase})") 
    print(f"Greatest Decrease in Profits: (${greatest_decrease})")      
    
with open("PyBank\Analysis\Result.txt", "w") as result_file:
    result_file.write("Financial Analysis\n")
    result_file.write("----------------------------\n")
    result_file.write(f"Total Months: {total_month}\n")
    result_file.write(f"Total: ${total_amount}\n")
    result_file.write(f"Average Change: ${average_value}\n")
    result_file.write(f"Greatest Increase in Profits: (${greatest_increase})\n")
    result_file.write(f"Greatest Decrease in Profits: (${greatest_decrease})\n")
    