import csv


file = "Resources/budget_data.csv"
total = 0
avg = 0
months = 0
old = 0
delta = []


with open(file, 'r') as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")
        first_row = next(csvreader)
        months = sum(1 for row in csvreader)

        
with open(file, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    first_row = next(csvreader)
    #second_row = next(csvreader)
    for row in csvreader:
        total = total + int(row[1])


with open(file, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    first_row = next(csvreader)
    rows = list(csvreader)
    linecount = 0
    old = rows[0][1]
    for row in rows:
        #print(str(row[1]) + "\t" + str(int(row[1])-int(old)))
        delta.append(int(row[1]) - int(old))
        old = row[1]    


with open("FinAnalysis.txt","w+") as outfile:

   outfile.write("Financial Analysis \n-----------------------")
   outfile.write("\nMonths: " + str(months))
   outfile.write("\nTotal: $" + str(total))
   outfile.write("\nAverage Change: $" + str(round(sum(delta)/(len(delta)-1),2)))
   outfile.write("\nGreatest Increase in Profits : " + str(rows[delta.index(max(delta))][0])[0:4] + str(20) + str(rows[delta.index(max(delta))][0])[4:6] + " ($" + str(max(delta)) + ")")
   outfile.write("\nGreatest Decrease in Profits : " + str(rows[delta.index(min(delta))][0])[0:4] + str(20) + str(rows[delta.index(min(delta))][0])[4:6] + " ($" + str(min(delta)) + ")")



with open("FinAnalysis.txt","r") as outfile:

   print(outfile.read())
