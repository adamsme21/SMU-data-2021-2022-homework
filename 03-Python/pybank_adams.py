import csv

csvpath = "resources_hw/budget_data.csv"

#variables
total_months = 0
total_profit = 0
pf_changes = []
prev_profit = 0
month_change =[]

#csv reader code from Netflix activity, edited
with open(csvpath, "r") as file:

    csvreader = csv.reader(file, delimiter=',')

    csvheader = next(csvreader)

    print(csvheader)
    print()

    for row in csvreader:
        #Determining total months and profits
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        
        #if not first row, determine profit change
        if total_months > 1:
            #Change in profit
            change = int(row[1]) - prev_profit
            #Add differences in list 
            pf_changes.append(change)
            #Add months to list
            month_change.append(row[0])

        #reset profit    
        prev_profit = int(row[1])
        
        print(row)

print(total_months)
print(total_profit)
print(pf_changes)
#print(len(pf_changes))
print(sum(pf_changes) / len(pf_changes))
print(max(pf_changes))
print(min(pf_changes))

#Variables for summary table
avg_change = sum(pf_changes) / len(pf_changes)
max_change = max(pf_changes)
min_change = min(pf_changes)

#Determine month of max profit
maxMonth_idx = pf_changes.index(max(pf_changes))
maxMonth = month_change[maxMonth_idx]
print(maxMonth)

#Determine month of max profit
minMonth_idx = pf_changes.index(min(pf_changes))
minMonth = month_change[minMonth_idx]
print(minMonth)

# create summary string
summary = f"""Financial Analysis
    ----------------------------
    Total Months: {total_months}
    Total: ${total_profit}
    Average  Change: ${avg_change}
    Greatest Increase in Profits: {maxMonth} (${max_change})
    Greatest Decrease in Profits: {minMonth} (${min_change})
    """

print(summary)

# writes to file
with open("pybank_analysis.txt", "w") as file:
    file.write(summary)
