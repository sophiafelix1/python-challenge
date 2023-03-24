import os
import csv

# Set path for file
filepath = os.path.join('PyBank', 'budget_data.csv')

# Creating dictionary to store data 
budget_data = {}

# Opening the CSV
with open(filepath, newline= "", encoding="utf-8") as budget_file:
    reader = csv.reader(budget_file, delimiter=",")
    header = next(reader)
    for row in reader:
        budget_data[row[0]] = int(row[1])

#Calculate the total number of months
total_months = len(budget_data)

#Net total amount of PL
net_total =sum(budget_data.values())

#list of PL
profit_loss = list(budget_data.values())
average_change = int(sum(profit_loss[1:])/(len(profit_loss)-1))

#Find the greatest Increase of Pl
max_increase = max(profit_loss[1:]) - profit_loss[0]
max_increase_month = [key for key, value in budget_data.items() if value == max(profit_loss[1:])][0]
#find the greatest decrease of Pl
max_decrease = min(profit_loss[1:]) - profit_loss[0]
max_decrease_month =[key for key, value in budget_data.items() if value == min(profit_loss[1:])][0]

#print answers

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_total:}")
print(f"Average Change: ${average_change:d}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase: })")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease: })")

