import os
import csv

csv_file = r"PyPoll\Resources\election_data.csv"

candidate_name = {}
candidate_list = []
lines = []
percent_vote = 0
winner = 0

# Open csv file and read it
with open(csv_file, 'r') as datasheet:
    csvreader = csv.reader(datasheet, delimiter=",")
    next(csvreader)

    #total number of votes
    for row in csvreader:
        if not row[2] in candidate_name.keys():         #this will check if the candidate already exists in the candidate_name dictionary 
            candidate_name[row[2]] = 1                  #if candidate does not exist in candidate_name dictionary, candidate key will be created with '1' value

        else:
            candidate_name[row[2]] += 1                 #if candidate already exists in candidate_name dictionary, 1 will be added to it's existing value
    
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {sum(candidate_name.values())}")
    print("------------------------")
    
    #list of candidates who received votes, percent of votes each candidate won and total number of votes each candidate won
    for candidate in candidate_name:
        percent_vote = round(candidate_name[candidate]/sum(candidate_name.values())*100,3)
        print(f"{candidate} : {percent_vote}%  ({candidate_name[candidate]})")

        #used lines list to populate different rows for each candidate in the txt file
        lines.append(candidate + " : " + str(percent_vote) + "%" + " (" + str(candidate_name[candidate]) + ")") 

        candidate_list.append(candidate_name[candidate])

    #winner of the election based on maximum votes received
    #the following code separates the dictionary's values in a list, finds the position of the maximum value I have, and gets the key at that position. 
    winner = (list(candidate_name.keys())[list(candidate_name.values()).index(max(candidate_list))])
    
    print("---------------------------")
    print(f"Winner : {winner}")
    print("---------------------------")

    #writing to the result file
    with open("PyPoll\Analysis\Result.txt", "w") as final_file:
        final_file.write("Election Results\n")
        final_file.write("-------------------------\n")
        final_file.write(f"Total Votes: {sum(candidate_name.values())}\n")
        final_file.write("-------------------------\n")
        for line in lines:
            final_file.write(f"{line}\n")
        final_file.write("-------------------------\n")
        final_file.write(f"Winner: {winner}\n")
        final_file.write("-------------------------\n")