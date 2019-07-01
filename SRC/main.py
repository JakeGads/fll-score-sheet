import os
import sys
from Classes import Team

teams = []

def start_up():
    files = os.listdir()
    for i in files:
        if '.json' in i:
            teams.append(Team(json_file=i))

def json_generator():
    try:
        import xlrd
        print('xlrd loaded reading file')
    except:
        input('To properly use this function xlrd must be installed please run\n\tpip install xlrd\n\n in terminal to continue usage')
        exit()
if __name__ == "__main__":
    choice = input('Enter 1 to load teams from ' + os.getcwd() + '\\Teams.xlsx\t')
    if choice is 1:
        json_generator()
    start_up()