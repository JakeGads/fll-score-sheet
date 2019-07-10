import xlrd
import logging
from flask import Flask
from config import FONT_SIZE,  TOPSCORES
from tkinter 


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
        count = 0
        for i in range(TOPSCORES):
            try:
                count += 1
                sum += orderedScores[i]
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
                    if i is team.number:
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


if __name__ == "__main__":
    book = filedialog.askopenfilename(initialdir = "/",title = "Select File",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
    app.run()