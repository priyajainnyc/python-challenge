#create file path across operating systems
import os

#module for reading csv files
import csv

#path to file with election data
csvpath = os.path.join('resources', 'election_data.csv')

#create dictionary to hold candidate name and vote count
elecdict = {}

#set variable to zero
total_votes = 0

#get data file and specify delimiter
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    csv_header = next(csvreader)

    #read each row of data after header
    for row in csvreader:
        total_votes += 1
        if row[2] not in elecdict:
            elecdict[row[2]] = 1
        else:
            elecdict[row[2]] += 1   
        
#print data     
print("Election Results")
print("------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------")

for candidate, votes in elecdict.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_votes) + " (" +  str(votes) + ")")
    
print("------------------------") 

winner = max(elecdict, key=elecdict.get)

print(f"Winner: {winner}")

#export data
export = os.path.join(".", 'export.txt')
with open(export,"w") as f:
    f.write("Election Results")
    f.write('\n')
    f.write("------------------------")
    f.write('\n')
    f.write("Total Votes: " + str(total_votes))
    f.write('\n')
    f.write("------------------------")
    f.write('\n')

    for candidate, votes in elecdict.items():
        f.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + " (" +  str(votes) + ")")
        f.write('\n')
    
    f.write("------------------------") 
    f.write('\n')
    f.write(f"Winner: {winner}")
    f.write('\n')
    f.write("------------------------") 