import xlrd
import logging
from flask import Flask
from config import FONT_SIZE,  TOPSCORES


book = None

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

A page named Teams with colum A consisting of team numbers and colum B consting of Team names
'''
def get_teams():
    book = xlrd.open_workbook(input('Excel File (can be dragged and dropped for windows)'))