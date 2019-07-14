import xlrd
import logging
from flask import Flask
from subprocess import call, check_output
from tkinter import filedialog
from config import FONT_SIZE,  TOPSCORES



book = None
teams = []

class Team():
    def __init__(self, number=None, name=None, scores=[]):
        self.number = number
        self.name = name
        self.scores = scores

    def genAverage(self):

        orderedScores = []
        for i in self.scores:
            orderedScores.append(i)

        orderedScores.sort()

        sum = 0
        count = 1
        for i in range(TOPSCORES):
            try:
                sum += orderedScores[i]
                count += 1
            except:
                None

        return sum / count


'''
!!!!IMPORTANT!!!!
Excel should be formatted as follows

A sheet named "Teams" with colum A consisting of Team numbers and colum B consisting of Team names

A sheet named "Entry" with colum A consisting of Team numbers and colum B consisting of scores colum C can mark the round but is not nessairy for this application to function

These pages can be in any order and additional pages can be added as well
if one or both tho the sheets are not there the program will not run (see example)
'''


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

    try:
        for i in range(sheet.nrows - 1):
            
            teamNumber = int(sheet.cell(i,0).value)
            score = int(sheet.cell(i,1).value)

            print('TeamNumber: {teamNumber}\t\tScore: {score}'.format(teamNumber=teamNumber, score=score))

            if isinstance(teamNumber, (int, float)):
                for team in teams:
                    if teamNumber is team.number:
                        team.scores.append(score)
                        print('add {score} to {number}'.format(score=score, number=team.number))           
            else:
                print('nothing to add')
    except:
        print('Failed to add Score')

def sortTeams():
    for i in range(len(teams)):   
        # Find the minimum element in remaining unsorted array 
        max_idx = i 
        for j in range(i+1, len(teams)): 
            if teams[max_idx].genAverage() < teams[j].genAverage(): 
                max_idx = j 
        # Swap the found minimum element with the first element         
        teams[i], teams[max_idx] = teams[max_idx], teams[i]

app = Flask(__name__)

@app.route('/')
def updateScoreBoard():
    # auto scroll JS Command “var scroll = setInterval(function(){ window.scrollBy(0,1000); }, 2000);”
    # refresh JS Command "document.location.reload(True)"
    get_scores()
    sortTeams()

    html = '''
    <table style=\"width:100%\">
        <tr>
            <th>
            Postion
            </th>
            <th>
            Team #
            </th>
            <th>
            Team Name
            </th>
            <th>
            Scores
            </th>
            
            <th>
            Top {average} Average
            </th>
        </tr>
    '''.format(average= TOPSCORES)

    counter = 0

    for team in teams:
        counter += 1
        html += '''
            <tr>
                <th>
                    {postion}
                </th>
                <th>
                    {number}
                </th>
                <th>
                    {name}
                </th>
                <th>
                    {scores}
                </th>
                <th>
                    {average}
                </th>
            </tr>
            '''.format(postion = counter, number = team.number, name = team.name, scores=team.scores, average = team.genAverage())
    
    html += '''
    </table>
    '''
    return html    


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
    for team in teams:
        print('{number}:    {scores}'.format(number=team.number, scores=team.scores))

    app.run()
