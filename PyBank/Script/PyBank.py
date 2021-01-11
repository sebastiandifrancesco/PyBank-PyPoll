import os
import csv
dates = []
profitLosses = []
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    # Reads file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Saves headers
    csv_header = next(csvreader)
     # Saves dates
    for row in csvreader:
        dates.append(row[0])
        profitLosses.append(row[1])
    
    #for row in dates:
    #    print(row)
    
    #for row in profitLosses:
    #    print(row)
    
    # Convert profit/losses to int
    for i in range(0, len(profitLosses)): 
        profitLosses[i] = int(profitLosses[i])
    
    # Create <list> to store monthly changes
    allMonthlyChanges = []
    # Saves monthly changes
    for i in range(0, (len(profitLosses) - 1)):
        currentChange = profitLosses[i + 1] - profitLosses[i]
        allMonthlyChanges.append(currentChange)
    #for change in allMonthlyChanges:
        #print(str(change))

    # Function for average
    def Avg(lst): 
        return sum(lst) / len(lst)

    # Saves average change rounded to second decimal
    averageChange = round(Avg(allMonthlyChanges), 2)

    # Create variables to store greatest increase and greatest decrease in profits as well as their respective dates
    grstInc = max(allMonthlyChanges)
    grstDec = min(allMonthlyChanges)
    grstIncDate = dates[allMonthlyChanges.index(grstInc) + 1]
    grstDecDate = dates[allMonthlyChanges.index(grstDec) + 1]

    # Change these to string for the print statement
    grstInc = str(grstInc)
    grstDec = str(grstDec)

    # Print the analysis 
    print('\n' + "Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(dates)))
    print("Total: " + str(sum(profitLosses)))
    print("Average Change: " + '$' + str(averageChange))
    print("Greatest Increase in Profits: " + grstIncDate + ' ($' + grstInc + ')')
    print("Greatest Decrease in Profits: " + grstDecDate + ' ($' + grstDec + ')')

    file = open('financial-analysis.txt', 'w')
    file.write("Financial Analysis" + '\n')
    file.write("----------------------------" + '\n')
    file.write("Total Months: " + str(len(dates)) + '\n')
    file.write("Total: " + str(sum(profitLosses)) + '\n')
    file.write("Average Change: " + '$' + str(averageChange) + '\n')
    file.write("Greatest Increase in Profits: " + grstIncDate + ' ($' + grstInc + ')' + '\n')
    file.write("Greatest Decrease in Profits: " + grstDecDate + ' ($' + grstDec + ')')
    file.close()