import data from '../data'

export default class Team {
    Team(name, number){
        this.name = name;
        this.number = number;
        this.scores = [];
        this.average = 0;
    }

    calcAverage(){
        if(this.scores.length == 0){
            this.average = 0;
        }
        else if(this.scores.length < data.TopAverage){
            let sum = 0;
            for(let i in this.scores){
                sum += this.scores[i];
            }
            average = sum / this.scores.length;
        }
        else if(this.scores.length >= data.TopAverage){
            let sum = 0;
            let count = 0;
            let compareList = []
            
            for(let i in this.scores){
                compareList.push(this.scores[i]);
            }
            
            compareList.sort((a,b)=>b-a);

            while(count < data.TopAverage){
                sum += compareList[count];
                count += 1;
            }

            this.average = sum / data.TopAverage;
        }
    }
}

export default function sortTeams(teams){
    let length = teams.length;
    for (let i = 1; i < length; i++) {
        let key = teams[i];
        let j = i - 1;
        while (j >= 0 && teams[j].average > key.average) {
            teams[j + 1] = teams[j];
            j = j - 1;
        }
        teams[j + 1] = key;
    }
    return teams;
}