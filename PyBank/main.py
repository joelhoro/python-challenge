import os
import csv
budget_data = os.path.join('/Users','mariamiller','Documents','python-challenge','Resources','budget_data.csv')
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",",)
    #first_row = next(csvreader)
    total = 0

    totalmonths=0
    greatestincrease = 0
    greatestdecrease = 0
    prevrow=0
    totalchange=0
    #rows = list(csvreader)

    for row in csvreader:
        totalmonths += 1
        if totalmonths == 1:
            continue
        current = float(row[1])
        total = total+float(current)
        change=current-prevrow
        totalchange= totalchange + change
        if change > greatestincrease:
            greatestincrease = change
            increasemonth = row[0]
        if change < greatestdecrease:
            greatestdecrease = change
            decreasemonth = row[0]
        prevrow=current
totalmonths -= 1
averagechange = totalchange/totalmonths
print("Total number of months: "+str(totalmonths)+ ". Average change: " +str(averagechange)+". Total Profit/Loss: " + str(total)+ ". Greatest increase in Profits: "+ str(greatestincrease)+" in "+increasemonth+". Greatest decrease in Profits: " + str(greatestdecrease)+" in "+decreasemonth)
output_file = os.path.join("./budget_final.txt")
with open(output_file, "w") as text_file:
    print(f"Total number of months: {totalmonths}. Average change: {averagechange}. Total Profit/Loss: {total}. Greatest increase in Profits: {greatestincrease} in {increasemonth}. Greatest decrease in losses: {greatestdecrease} in {decreasemonth}", file=text_file)
