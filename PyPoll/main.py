import csv

file = "Resources/election_data.csv"
rows = []
cands = []
votes = [0,0,0,0]

with open(file, 'r') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=",")
	first_row = next(csvreader)
	rows = list(csvreader)

with open("PollResults.txt", 'w') as outfile:

	outfile.write("Election Results")
	outfile.write("\n-----------------------")
	outfile.write("\nTotal Votes: " + str(len(rows)))
	outfile.write("\n-----------------------") 
	for row in rows:
		if row[2] not in cands:
			
			cands.append(row[2])
			votes[len(cands)-1]
		else:
			votes[cands.index(row[2])] = votes[cands.index(row[2])] + 1

	for cand in cands:
		outfile.write("\n" + cand + ":   " + "{0:.3%}".format(votes[cands.index(cand)]/len(rows)) + " (" + str(votes[cands.index(cand)]) + ")")

	outfile.write("\n-----------------------")
	outfile.write("\nWinner: " + cands[votes.index(max(votes))])
	outfile.write("\n-----------------------")

with open("PollResults.txt", 'r') as outfile:

	print(outfile.read())

#outfile.write(' '.join(row) + "\n")
