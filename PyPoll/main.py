import os
import csv
electiondata = os.path.join('/Users','mariamiller','Documents','python-challenge','Resources','election_data.csv')
with open(electiondata, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    totalvotes = 0
    candidates = []
    votes = {}
    maxvotes = 0
    for row in csvreader:
        totalvotes = totalvotes+1
        voter_id, county, candidate = row
        if candidate not in votes.keys():
            votes[candidate] = 0
        votes[candidate] += 1
        if votes[candidate]>maxvotes:
            maxvotes = votes[candidate]
            winner = candidate

    print("Total votes: "+ str(totalvotes))
    print("The winner is "+winner)
    for candidate in votes.keys():
        print(f"{candidate}: {votes[candidate]}, {votes[candidate]/totalvotes*100}%")

output_file = os.path.join("./poll_final.txt")
with open(output_file, "w") as text_file:
    print("Total votes: "+ str(totalvotes),file=text_file)
    print("The winner is "+winner,file=text_file)
    for candidate in votes.keys():
        print(f"{candidate}: {votes[candidate]}, {votes[candidate]/totalvotes*100}%",file=text_file)