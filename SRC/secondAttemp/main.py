# built into python
from json import load, loads, dump, dumps
from config import FONT_SIZE, TOPSCORES
import logging
import tkinter

# installed using pip (pip install <packagename>)
from flask import Flask, render_template
import xlrd # TODO come back set the needed functions
import xlwt


class Team():
    def init(self, number=None, name=None, json_data=None):
        if number is not None and name is not None:
            self.number = number
            self.name = name
            self.scores = []
            self.average = self.gen_average()
        elif json_data is not None:
            self.number = json_data['number']
            self.name = json_data['name']
            self.scores = json_data['scores']
            self.average = self.gen_average()

    def add_score(self, score):
        self.scores.append(score)
        self.average = self.gen_average()

    def gen_average(self):
        self.scores.sort()
        average = 0
        spots = 1
        for i in range(TOPSCORES):
            try:
                average += self.scores[i]
                spots += 1
            except:
                break

        return round(average/spots)

    def kill(self):
        return dumps({
            'number': self.number,
            'name': self.name,
            'scores': self.scores,
            'average': self.average
        })


teams = []

def readTeamsXL(file):
    # Opens the sheet to create the teams it is configured
    # Team Number, Team Name, <Non import information>
    sheet=xlrd.open_workbook(file).sheet_by_index(0)

    for i in range(sheet.nrows - 1):
        number = sheet.cell(0, i).value
        name = sheet.cell(1, i).value
        try:
            teams.append(Team(number=number, name=name))
        except:
            logging.error('Failed to add {number} {name}'.format(number=number, name=name))

def readTeamsJSON():
    with open('Teams.json', 'r') as inRead:
        data = load(inRead)

        for i in data:
            teams.append(Team(json_data=i))
    
def updateJSON():
    endTeams = []
    for i in teams:
        endTeams.append(i.kill())
    #dump but pretty
    dump(dumps(endTeams),'Teams.json', indent=4)

def sortTeam():
    for i in range(len(teams)):   
        # Find the minimum element in remaining unsorted array 
        max_idx = i 
        for j in range(i+1, len(teams)): 
            if teams[max_idx].gen_average() < teams[j].gen_average(): 
                max_idx = j 
        # Swap the found minimum element with the first element         
        teams[i], teams[max_idx] = teams[max_idx], teams[i] 

def writeExcel(loc):
    book = xlwt.Workbook()
    sheet = book.add_sheet('Results')
    row = sheet.row(0)
    row.write(0, 'Team Number')
    row.write(1, 'Team Name')
    row.write(2, 'Top {avgNum} Avg'.format(avgNum= TOPSCORES))

    for i in range(len(teams[0].scores())):
        # so im just really gonna hope that the top team has shown up to all possible matches if not its still gonna write the scores out but it will look more wonky
        row.write(i+2, 'Score {number}'.format(number = i + 1))
    
    for i in range(len(teams)):
        row = sheet.row(i+1)
        row.write(0, teams[i].number)
        row.write(1, teams[i].name)
        row.write(2, teams[i].gen_average())
        teams[i].scores.sort()
        for h in range(len(teams[i].scores)):
            row.write(h+2, teams[i].scores[h])

# now we start handling all of the flask stuff
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html')

@app.route('/entryForm')
def entryForm():
    return render_template('entryForm.html')