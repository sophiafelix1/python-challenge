import os 
import csv
#Figure out amount of candidates and how many votes each candidate received
candidates = []
votes_per_candidate = {}
#Out of the total votes of the election what was the percentage of votes per candidate
Total_Votes = 0
election_data = os.path.join(".","PyPoll", "Resources", "election_data.csv")
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
#Loop through data
    for row in csvreader:
        Total_Votes += 1
        Name_Candidate = row[2]
        if Name_Candidate not in candidates:
            candidates.append(Name_Candidate)
            votes_per_candidate[Name_Candidate] = 0
        votes_per_candidate[Name_Candidate] += 1
#percentages of vote per candidate
percent_votes = {}
for candidates, votes in votes_per_candidate.items():
    percent_votes[candidates] = (votes /Total_Votes) * 100

Winner =max(votes_per_candidate, key=votes_per_candidate.get)
#Print the results 
print("Election Results")
print("-------------------------")
print(f" Total Votes : {Total_Votes}")
print("-------------------------")
for candidates, vote in votes_per_candidate.items():
    print(f"{candidates}: {percent_votes[candidates]:.3f}% ({votes})")
print("-------------------")
print(f"Winner: {Winner}")
print("------------------------")
