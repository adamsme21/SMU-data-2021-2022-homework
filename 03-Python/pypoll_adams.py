
#Import csv
import csv

csvpath = "resources_hw/election_data.csv"

#Variables
total_votes = 0
candidates = set()
candidate_dict = {"Li": 0, "Correy": 0, "Khan": 0, "O'Tooley": 0}


with open(csvpath, "r") as file:

    # read csv
    csvreader = csv.reader(file, delimiter=',')
    #skip header
    csvheader = next(csvreader)

    print(csvheader)
    print()

    for row in csvreader:
        total_votes = total_votes + 1
        #print(row)
        #Create set of candidates
        candidates.add(row[2])
        #adding votes per candidate
        if row[2] == "Li":
            candidate_dict["Li"] += 1
        elif row[2] == "Correy":
            candidate_dict["Correy"] += 1
        elif row[2] == "Khan":
            candidate_dict["Khan"] += 1
        else:
            candidate_dict["O'Tooley"] += 1




print(total_votes)
print(candidates) 
print(candidate_dict)

# Find max. Used: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
max_cand = max(candidate_dict, key=candidate_dict.get)
max_votes = candidate_dict[max_cand]

print(max_cand)
print(max_votes)


#Results print out (percentage not determined)
results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidate_dict}
-------------------------
Winner: {max_cand}
-------------------------
"""

print(results)

#Save to file
with open("election_data_analysis.txt", "w") as file:
    file.write(results)