class fll_team {
    number: number;
    name: string;
    scores: Array<number>;
    average:number = 0;
    award_nomination: string = null;
    award_recived: string = null;

    constructor(number: number, name: string){
        this.number = number;
        this.name = name;
    }

    add_score(score: number){
        this.scores.push(score);
    }

    genAverage(){
        let sum = 0;
        
        this.scores.forEach(element => {
            sum += element;
        });
        
        this.average = sum / this.scores.length;
    }

    genAverageTop(topScores: number){
        function bubble_Sort(arr){
            function swap(arr, first_Index, second_Index){
                var temp = arr[first_Index];
                arr[first_Index] = arr[second_Index];
                arr[second_Index] = temp;
            }
            
            var len = arr.length,
                i, j, stop;
        
            for (i=0; i < len; i++){
                for (j=0, stop=len-i; j < stop; j++){
                    if (arr[j] > arr[j+1]){
                        swap(arr, j, j+1);
                    }
                }
            }
        
            return arr;
        }

        let sum = 0;

        this.scores = bubble_Sort(this.scores);

        for(let i = 0; i < topScores; i++){
            sum += this.scores[i];
        }

        this.average = sum / topScores;
    }

    giveNomination(award: string){
        this.award_nomination = award;
    }

    giveAward(award: string){
        this.award_recived = award;
    }
}

export let fll_teams:Array<fll_team> = new Array<fll_team>();