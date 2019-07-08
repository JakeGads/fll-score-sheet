from config import TOPSCORES
from json import dump, dumps, load


class Team():
    def init(self, number=None, name=None, json_file=None):
        if number is not None and name is not None:
            self.number = number
            self.name = name
            self.scores = []
            self.average = self.gen_average()
        else:
            with open(json_file) as file_in:
                data = load(file_in)
                self.number = data['number']
                self.name = data['name']
                self.scores = data['scores']
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
        file_loc = str(self.number) + '.json'
        with open(file_loc, 'w+') as file_out:
            dump(
                dumps({
                    'number': self.number,
                    'name': self.name,
                    'scores': self.scores,
                    'average': self.average
                }),
                file_out
            )
