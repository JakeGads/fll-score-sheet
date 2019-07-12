import xlwt
from random import randint

writable = [
    [2450, 'GreenBots', 0],
    [5692, 'Blockheads', 0],
    [12954, 'Yeetus', 0],
    [13049, 'Cyber Crusaders', 0],
    [5788, 'St. Stans Robotics Lab', 0],
    [145690, 'RoboLegoLancers', 0],
    [5422, 'RuffBois', 0],
    [24231, 'Mechanical Mauraders', 0],
    [8978, 'Mech Mustang', 0],
    [7684, 'Yuppers', 0],
    [540023, 'Corpus Christy', 0],
    [1218, 'Vulcan Robotics', 0],
    [4750, 'Bert', 0],
    [225, 'Techfire', 0],
    [223, 'Xtreme Heat', 0],
    [224, 'The Tribe', 0],
    [222, 'TigerTrons', 0],
    [11, 'MORT', 0],
    [193, 'MORT Beta', 0],
    [25, 'Raider Robotics', 0],
    [75, 'RoboRaiders', 0],
    [433, 'Firebirds', 0],
    [5420, 'Velocity', 0],
    [4454, 'Artisinal Rockets', 0],
    [6667, 'STEM Clippers', 0],
    [103, 'CyberSonics', 0],
    [2607, 'Fighting Robotics Vikings', 0],
    [607, 'Botic Vikings', 0],
    [102, 'Gearheads', 0],
    [1, 'Juggernauts', 0],
    [4, 'Team 4 Element', 0],
    [254, 'The Cheesy Poofs', 0],
    [321, 'Robolancers', 0],
    [303, 'TEST Team', 0],
    [708, 'Hatters Robotics', 0],
    [709, 'Femme Tech Fatale', 0],
    [5181, 'Explorers', 0],
    [2590, 'Nemesis', 0],
    [14133, 'Junior Cyber Crusaders', 0],
    [42069, 'Nice', 0],
    [365, 'Miracle Workers', 0],
    [2539, 'Krypton Cougers', 0],
]

for i in range(len(writable)):   
        # Find the minimum element in remaining unsorted array 
        max_idx = i 
        for j in range(i+1, len(writable)): 
            if writable[max_idx][0] < writable[j][0]: 
                max_idx = j 
        # Swap the found minimum element with the first element         
        writable[i], writable[max_idx] = writable[max_idx], writable[i]

workbook = xlwt.Workbook()
teamSheet = workbook.add_sheet(sheetname='Teams')
entrySheet = workbook.add_sheet(sheetname='Entry')

for i in range(len(writable)):
    teamSheet.write(i, 0, writable[i][0])
    teamSheet.write(i, 1, writable[i][1])

for i in range(randint(0,200)):
    teamLoc = randint(0, len(writable) - 1)
    while writable[teamLoc][2] == 5:
        teamLoc = randint(0, len(writable) - 1)
    writable[teamLoc][2] += 1  
    team = writable[teamLoc][0]
    score = randint(0, 500)
    entrySheet.write(i,0, team)
    entrySheet.write(i,1, score)

workbook.save('example.xls')