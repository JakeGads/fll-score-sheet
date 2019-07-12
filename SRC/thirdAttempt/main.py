import xlrd
import logging
from flask import Flask
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
            orderedScores.append(self.scores[i])

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
    teams = []

    sheet = book.sheet_by_name('Teams')

    for i in range(sheet.nrows - 1):
        try:
            teams.append(Team(number=int(sheet.cell(i,0).value), name=sheet.cell(i,1).value))
        except:
            None

    get_scores()


def get_scores():
    sheet = book.sheet_by_name('Entry')

    try:
        for i in range(sheet.nrows - 1):
            teamNumber = sheet.cell(i,0).value
            score = sheet.cell(i,1).value
            if type(teamNumber) == type(1):
                for team in teams:
                    if teamNumber is team.number:
                        team.scores.append(score)
    except:
        None

def sortTeams():
    for i in range(len(teams)):   
        # Find the minimum element in remaining unsorted array 
        max_idx = i 
        for j in range(i+1, len(teams)): 
            if teams[max_idx].gen_average() < teams[j].gen_average(): 
                max_idx = j 
        # Swap the found minimum element with the first element         
        teams[i], teams[max_idx] = teams[max_idx], teams[i]

app = Flask(__name__)

@app.route('/')
def updateScoreBoard():
    # auto scroll JS Command “var scroll = setInterval(function(){ window.scrollBy(0,1000); }, 2000);”
    # refresh JS Command "document.location.reload(True)"
    get_teams()
    sortTeams()

    maxRound = 0

    for team in teams:
        if len(team.scores) > maxRound:
            maxRound = len(team.scores)


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
            '''

    for team in range(maxRound):
        html += '''
                <th>
                Round {roundNum}
                </th>
                '''.format(roundNum = team + 1)


    html += '''
            <th>
            Top {average} Average
            </th>
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
        '''.format( postion = counter, number = team.number, name = team.name)

        for i in range(maxRound):
            try:
                html +=  '''
                            <th>
                            {score}
                            </th>
                        '''.format(team.scores[i])
            except:
                html += '''
                            <th>
                            N/A
                            </th>
                        '''
        html += '''
                <th>
                {average}
                </th>
            
                '''.format(average = team.genAverage())
    html += '''
    </tr>
    </table>
    '''
    return html    


if __name__ == "__main__":
    book = filedialog.askopenfilename(initialdir = "/",title = "Select File",filetypes = (("xlsx files","*.xlsx"),("xls files","*.xls"),("all files","*.*")))
    app.run()