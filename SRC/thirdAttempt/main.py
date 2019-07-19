import xlrd
import xlwt
import logging
from flask import Flask, render_template
from flask_assets import Bundle, Environment
from subprocess import call, check_output
from tkinter import filedialog
from config import FONT_SIZE,  TOPSCORES



book = None
teams = []

class Team():
    def __init__(self, number=None, name=None, scores='', average=None):
        self.number = number
        self.name = name
        self.scores = scores
        self.average = average

'''
!!!!IMPORTANT!!!!
Excel should be formatted as follows

A sheet named "Teams" with colum A consisting of Team numbers and colum B consisting of Team names

A sheet named "Entry" with colum A consisting of Team numbers and colum B consisting of scores colum C can mark the round but is not nessairy for this application to function

These pages can be in any order and additional pages can be added as well
if one or both tho the sheets are not there the program will not run (see example)
'''

def genAverage(arr):
    orderedScores = []
    for i in arr:
        orderedScores.append(i)

    orderedScores.sort(reverse=True)

    sum = 0
    count = 0
    for i in range(TOPSCORES):
        try:
            sum += orderedScores[i]
            count += 1
        except:
            if count is 0:
                count = 1

    return sum / count    


def get_teams():
    sheet = book.sheet_by_name('Teams')

    for i in range(sheet.nrows - 1):
        
        try:
            teams.append(Team(number=int(sheet.cell(i,0).value), name=sheet.cell(i,1).value))
        except:
            print('Error adding {number} to the teams list'.format(number = sheet.cell(i,0).value))
    
    get_scores()


def get_scores():
    sheet = book.sheet_by_name('Entry')
    # I realize that this is very unoptimized but this has something to do with memory managment
    try:
        for team in teams:
            teamScores = []
            for i in range(sheet.nrows - 1):
                teamNumber = int(sheet.cell(i,0).value)
                score = int(sheet.cell(i,1).value)
                
                if team.number == teamNumber:
                    teamScores.append(score)
            
            team.average = genAverage(teamScores)
            team.scores = str(teamScores).replace('[','').replace(']','')

    except:
        print('Failed to add Score')

def sortTeams():
    for i in range(len(teams)):   
        # Find the minimum element in remaining unsorted array 
        max_idx = i 
        for j in range(i+1, len(teams)): 
            if teams[max_idx].average < teams[j].average: 
                max_idx = j 
        # Swap the found minimum element with the first element         
        teams[i], teams[max_idx] = teams[max_idx], teams[i]

app = Flask(__name__)

js = Bundle('main.js', output='gen/main.js')
assets = Environment(app)
assets.register('main_js', js)

from flask_table import Table, Col

class teamTable(Table):
    postion = Col('Postion')
    teamNum = Col('Team #')
    teamName = Col('Name')
    scores = Col('Scores')
    average = Col('Top {average} Average'.format(average=TOPSCORES))  

class teamItem(object):
    def __init__(self, postion, team):
        self.postion = postion
        self.teamNum = team.number
        self.teamName = team.name
        self.scores = team.scores
        self.average = round(team.average, 2)



@app.route('/')
def updateScoreBoard():
    # auto scroll JS Command “var scroll = setInterval(function(){ window.scrollBy(0,1000); }, 2000);”
    # refresh JS Command "document.location.reload(True)"
    print('Generating Scores and Sorting the teams')
    get_scores()
    sortTeams()

    teamItems = []

    for i in range(len(teams)):
        try:
            teamItems.append(teamItem(i + 1, teams[i]))            
        except:
            None

    table = teamTable(teamItems)
    
    # so now we apply the old code but replace the body of the table in here

    return render_template('main.html', table=table)

    
def finalize():
    None


if __name__ == "__main__":
    # book = xlrd.open_workbook(filedialog.askopenfilename(initialdir = "/",title = "Select File",filetypes = (("xlsx files","*.xlsx"),("xls files","*.xls"),("all files","*.*"))))
    book = xlrd.open_workbook('example.xls')
    
    
    get_teams()

    try:
        call('fuser -k 5000/tcp')
        print('killed the Linux Port')
    except:
        try:
            output = check_output('netstat  -ano  |  findstr  5000')
            processID = output[-4:]
            call(' taskkill  /F  /PID  {processID}'.format(processID=processID))
            print('killed the windows port')
        except:
            print('Failed to kill process you may have to restart')
    
    try:
        call('cls')
    except:
        call('clear')
    finally:
        None

    app.run()

    finalize()
