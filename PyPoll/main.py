import os
import csv
electiondata = os.path.join('/Users','mariamiller','Documents','python-challenge','Resources','election_data.csv')
with open(electiondata, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    totalvotes = 0
    candidates = []
    votes = {}

    for row in csvreader:
        totalvotes = totalvotes+1
        voter_id, county, candidate = row
        if candidate not in votes.keys():
            votes[candidate] = 0
        votes[candidate] += 1

    print(votes)
    print(votes.keys())
    print(votes.values())