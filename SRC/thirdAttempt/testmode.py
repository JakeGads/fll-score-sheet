import xlwt
from random import randint

writable = [
    [2450, 'GreenBots'],
    [5692, 'Blockheads'],
    [12954, 'Yeetus'],
    [13049, 'Cyber Crusaders'],
    [5788, 'St. Stans Robotics Lab'],
    [145690, 'RoboLegoLancers'],
    [5422, 'RuffBois'],
    [24231, 'Mechanical Mauraders'],
    [8978, 'Mech Mustang'],
    [7684, 'Yuppers'],
    [540023, 'Corpus Christy'],
    [1218, 'Vulcan Robotics'],
    [4750, 'Bert'],
    [225, 'Techfire'],
    [223, 'Xtreme Heat'],
    [224, 'The Tribe'],
    [222, 'TigerTrons'],
    [11, 'MORT'],
    [193, 'MORT Beta'],
    [25, 'Raider Robotics'],
    [75, 'RoboRaiders'],
    [433, 'Firebirds'],
    [5420, 'Velocity'],
    [4454, 'Artisinal Rockets'],
    [6667, 'STEM Clippers'],
    [103, 'CyberSonics'],
    [2607, 'Fighting Robotics Vikings'],
    [607, 'Botic Vikings'],
    [102, 'Gearheads'],
    [1, 'Juggernauts'],
    [4, 'Team 4 Element'],
    [254, 'The Cheesy Poofs'],
    [321, 'Robolancers'],
    [303, 'TEST Team'],
    [708, 'Hatters Robotics'],
    [709, 'Femme Tech Fatale'],
    [5181, 'Explorers'],
    [2590, 'Nemesis'],
    [14133, 'Junior Cyber Crusaders'],
    [42069, 'Nice'],
    [365, 'Miracle Workers'],
    [2539, 'Krypton Cougers'],
]

workbook = xlwt.Workbook()
teamSheet = workbook.add_sheet(sheetname='Teams', True)
entrySheet = workbook.add_sheet(sheetname='Entry', True)

for i in range(len(writable)):
    teamSheet.write(i, 0, writable[i][0])
    teamSheet.write(i, 1, writable[i][1])

for i in range(randint(0,480)):
    team = writable[randint(0, len(writable) - 1)][0]
    score = randint(0, 500)
    entrySheet(i,0 team)
    entrySheet(i,1 score)

workbook.save('example.xls')