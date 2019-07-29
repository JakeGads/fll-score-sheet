from os import system
from subprocess import call, check_output # allows to access terminal and to read the terminal output

# Native
import logging #xl writing
from tkinter import filedialog #file selections

# Defined elsewhere
from config import FONT_SIZE, TOPSCORES # self made

try:
    # third party
    import xlrd # xl reading
    from flask import Flask, render_template, Markup # webserver, template renderer and str to markup converter
    from flask_assets import Bundle, Environment # js and cs bundlers
except:
    try:
        # installer scripts
        system('pip install -r requirments.txt --user')
    except:
        try:
            system('pip install -r requirments.txt --user')
        except:
            try:
                system('pip install xlrd flask flask_assets --user')
            except:
                print('Failed to install required packages may have to be done manually\n\npip install xlrd flask flask_assets')

    # third party
    import xlrd # xl reading
    from flask import Flask, render_template, Markup # webserver, template renderer and str to markup converter
    from flask_assets import Bundle, Environment # js and cs bundlers

# sets these as the global variables
book = None # The workbook that we will use to analyze
teams = [] # Holds all of the teams 
# Team becomes a way to sort or to organize the order
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

def genAverage(userList):
    # this will reverse order a deep copy of the list
    orderedScores = []
    for i in userList:
        orderedScores.append(i)

    orderedScores.sort(reverse=True)

    # calculates the current average up to the user defined value
    # if there is no value it will avoid a divide by zero instance which would cause a server crash 
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
    # reads through the team list sheet in order to start making the team list
    sheet = book.sheet_by_name('Teams')

    for i in range(sheet.nrows - 1):
        
        try:
            teams.append(Team(number=int(sheet.cell(i,0).value), name=sheet.cell(i,1).value))
        except:
            print('Error adding {number} to the teams list'.format(number = sheet.cell(i,0).value))
    
    get_scores()


def get_scores():
    #looks through the entry
    sheet = book.sheet_by_name('Entry')
    scores = []
    for i in range(sheet.nrows):
        if i is 0:
            continue
        try:
            scores.append({'team': sheet.cell(rowx=i,cellx=0).value, 'score': sheet.cell(rowx=i,cellx=1).value})
        except:
            continue

    
    for score in scores:
        team_scores = []
        for team in teams:
            if score['team'] == team.team:
                team_scores.append(score['score'])
        
        team.average = genAverage(team_scores)
        team.scores = str(team_scores).replace('[', '').replace(']', '')

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

# webserver info
app = Flask(__name__)
# gets the javascript ready to import
js = Bundle('main.js', output='gen/main.js')
assets = Environment(app)
assets.register('main_js', js)

# the home (and only) page
@app.route('/')
def updateScoreBoard():
    # auto scroll JS Command “var scroll = setInterval(function(){ window.scrollBy(0,1000); }, 2000);”
    # refresh JS Command "document.location.reload(True)"
    print('Generating Scores and Sorting the teams')
    get_scores()
    sortTeams()

    table = ''
    # goes through each team and makes an html row out of them
    for pos in range(len(teams)):
        table += '''
        <tr>
            <td class="cell100 column2">{pos}</td>\n
            <td class="cell100 column2">{teamNum}</td>\n
            <td class="cell100 column3">{name}</td>\n
            <td class="cell100 column4">{scores}</td>\n
            <td class="cell100 column5">{average}</td>\n
        </tr>    
        '''.format(
            pos = pos + 1,
            teamNum = teams[pos].number,
            name = teams[pos].name,
            scores = teams[pos].scores,
            average = round(teams[pos].average, 2)
        )

    # returns the html from main.html with the table running through markup and the average score
    return render_template('main.html', table=Markup(table), average=TOPSCORES)

# This function is left blank as I have not figured out how to run this at the destruction
def finalize():
    None

# The main
if __name__ == "__main__":
    # sets the book to what the user selects in the tk dialogue
    book = xlrd.open_workbook(filedialog.askopenfilename(initialdir = "/",title = "Select File",filetypes = (("xlsx files","*.xlsx"),("xls files","*.xls"),("all files","*.*"))))
    
    # the testing book
    # book = xlrd.open_workbook('example.xls')
    
    # gets the team
    # note if a team is added the program must be restarted
    get_teams()

    try:
        call('fuser -k 5000/tcp')
        print('killed the Linux Port')
    except:
        try:
            output = check_output('netstat  -ano  |  findstr  5000')
            processID = str(output)[-4:]
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
