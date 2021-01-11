import os
import csv

voterIDs = []
counties = []
candidates = []
khan = 'Khan'
correy = 'Correy'
li = 'Li'
oTooley = "O'Tooley"
khanCount = 0
correyCount = 0
liCount = 0
oTooleyCount = 0
winner = ['',0]
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    # Reads file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Saves headers
    csv_header = next(csvreader)

    # Saves data in appropriate place
    for row in csvreader:
        voterIDs.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
    
    # Tracks vote count
    for candidate in candidates:
        if candidate == khan:
            khanCount += 1
        elif candidate == correy:
            correyCount += 1
        elif candidate == li:
            liCount += 1
        else:
            oTooleyCount += 1
    
    # Determines winner
    if khanCount > winner[1]:
        winner[0] = 'Khan'
        winner[1] = khanCount
    if correyCount > winner[1]:
        winner[0] = 'Correy'
        winner[1] = correyCount
    if liCount > winner[1]:
        winner[0] = 'Li'
        winner[1] = liCount
    if oTooleyCount > winner[1]:
        winner[0] = "O'Tooley"
        winner[1] = oTooleyCount
    
    # Determines candidates' percentages
    totalVotes = khanCount + correyCount + liCount + oTooleyCount
    khanPercent = str(round(((khanCount / totalVotes) * 100), 3)) + '%'
    correyPercent = str(round(((correyCount / totalVotes) * 100), 3)) + '%'
    liPercent = str(round(((liCount / totalVotes) * 100), 3)) + '%'
    oTooleyPercent = str(round(((oTooleyCount / totalVotes) * 100), 3)) + '%'

    if khanCount > winner[1]:
        winner = khanCount
    if correyCount > winner[1]:
        winner = correyCount
    if liCount > winner[1]:
        winner = lifCount
    if oTooleyCount > winner[1]:
        winner = oTooleyCount


    #print(voterIDs[-1])
    #print(counties[-1])
    #print(candidates[-1])
    
    #for row in counties:
        #print(row)

    #for row in candidates:
        #print(row)
    
    # Prints election results
    print('\n' + 'Election Results')
    print('-------------------------')
    print('Total Votes: ' + str(len(voterIDs)))
    print('-------------------------')
    print('Khan: ' + khanPercent + ' ' + '(' + str(khanCount) + ')')
    print('Correy: ' + correyPercent + ' ' + '(' + str(correyCount) + ')')
    print('Li: ' + liPercent + ' ' + '(' + str(liCount) + ')')
    print("O'Tooley: " + oTooleyPercent + ' ' + '(' + str(oTooleyCount) + ')')
    print('-------------------------')
    print('Winner: ' + winner[0])
    print('-------------------------')

    # Writes eletion resutls to a txt file
    file = open('election-analysis.txt', 'w')
    file.write('Election Results' + '\n')
    file.write('-------------------------' + '\n')
    file.write('Khan: ' + khanPercent + ' ' + '(' + str(khanCount) + ')' + '\n')
    file.write('Correy: ' + correyPercent + ' ' + '(' + str(correyCount) + ')' + '\n')
    file.write('Li: ' + liPercent + ' ' + '(' + str(liCount) + ')' + '\n')
    file.write("O'Tooley: " + oTooleyPercent + ' ' + '(' + str(oTooleyCount) + ')' + '\n')
    file.write('-------------------------' + '\n')
    file.write('Winner: ' + winner[0] + '\n')
    file.write('-------------------------')
    file.close()
