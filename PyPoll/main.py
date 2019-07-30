import os
import csv
electiondata = os.path.join('/Users','mariamiller','Documents','python-challenge','Resources','election_data.csv')

with open(electiondata, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip first line
    next(csvreader)
    totalvotes = 0
    votes = {}
    for row in csvreader:
        totalvotes += 1
        voter_id, county, candidate = row
        if candidate not in votes.keys():
            votes[candidate] = 0
        votes[candidate] += 1

    # get list of candidates
    candidates = votes.keys()
    # get the max number of votes of all candidates
    maxvotes = max(votes.values())
    # note there could be more than one if they tie
    best_candidates = [ candidate for candidate in candidates if votes[candidate] == max_votes ]

    if best_candidates.length > 1:
        ### what do you do if they tie?
        print("....")
    
    winner = best_candidates[0]
    print("Total votes: "+ str(totalvotes))
    print("The winner is "+winner)

    # this votes.items() is an elegant way to get both the key and the value (instead of doing votes[candidate])
    for (candidate,votes_for_candidate) in votes.items():
        print(f"{candidate}: {votes_for_candidate}, {votes_for_candidate/totalvotes*100}%")

output_file = os.path.join("./poll_final.txt")
with open(output_file, "w") as text_file:
    print("Total votes: "+ str(totalvotes),file=text_file)
    print("The winner is "+winner,file=text_file)
    for candidate in votes.keys():
        print(f"{candidate}: {votes[candidate]}, {votes[candidate]/totalvotes*100}%",file=text_file)
