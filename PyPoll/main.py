#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
import os 
import csv
election_data = os.path.join("election_data.csv")
#Figure out amount of candidates and how many votes each candidate received
candidates = []
Candidate_Vote = []
#Out of the total votes of the election what was the percentage of votes per candidate
Total_Votes = 0
Percent_Votes = []
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
#Loop through data
    for row in csvreader:
        candidates = candidates + 1
#List of candidates and add each vote per candidate
    if(row[2] not in Candidate_Vote):
        Candidate_Vote.append(row[2])
        Total_Votes.append(0)
candidatesIndex = candidates.index (row[2])
Total_Votes[candidatesIndex] += 1
#Print the results 
print("Election Results")
print("-------------------------")
print(f" Total Votes : {Total_Votes}")
print("-------------------------")
#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote


