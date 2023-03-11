#create file path across operating systems
import os

#module for reading csv files
import csv

#path to file with budget data
csvpath = os.path.join('resources', 'budget_data.csv')
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #skip header
    header = next(csvreader)

    #create empty lists to add csv values 
    num_of_months = []
    profit_loss = []
    change_profit_loss = []
                      
    #run through values and add to empty list 
    for row in csvreader:
        num_of_months.append(row[0])
        profit_loss.append(int(row[1]))
    for x in range(len(profit_loss)-1):
        change_profit_loss.append(profit_loss[x+1]-profit_loss[x])
                      
#determine max and min from list
increase = max(change_profit_loss)
decrease = min(change_profit_loss)

#determine greatest increase and decrease by using index
greatest_increase = change_profit_loss.index(max(change_profit_loss))+1
greatest_decrease = change_profit_loss.index(min(change_profit_loss))+1

#print data
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(num_of_months)}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: {round(sum(change_profit_loss)/len(change_profit_loss),2)}")
print(f"Greatest Increase in Profits: {num_of_months[greatest_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {num_of_months[greatest_decrease]} (${(str(decrease))})")      

#export data
export = os.path.join(".", 'export.txt')
with open(export,"w") as f:
    f.write("Financial Analysis")
    f.write("\n")
    f.write("------------------------")
    f.write("\n")
    f.write(f"Total Months: {len(num_of_months)}")
    f.write("\n")
    f.write(f"Total: ${sum(profit_loss)}")
    f.write("\n")
    f.write(f"Average Change: {round(sum(change_profit_loss)/len(change_profit_loss),2)}")
    f.write("\n")
    f.write(f"Greatest Increase in Profits: {num_of_months[greatest_increase]} (${(str(increase))})")
    f.write("\n")
    f.write(f"Greatest Decrease in Profits: {num_of_months[greatest_decrease]} (${(str(decrease))})")