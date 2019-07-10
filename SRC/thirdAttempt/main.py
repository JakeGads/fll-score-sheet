import xlrd
import logging
from flask import Flask
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
    book = xlrd.open_workbook(input('Excel File (can be dragged and dropped for windows)'))

    sheet = book.sheet_by_name('Teams')

    for i in range(sheet.nrows - 1):
        try:
            teams.append(Team(number=int(sheet.cell(i,0).value), name=sheet.cell(i,1).value))
        except:
            None

    get_scores()


def get_scores():
    sheet = book.sheet_by_name('Entry')

    for i in range(sheet.nrows - 1):
        value = sheet.cell(i,0).value
        if type(value) == type(1):
            for team in teams:
                if i is team.number:



