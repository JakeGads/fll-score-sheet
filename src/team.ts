// TODO set up as a data service
const topNum = 3;

export default class Team {
  name = 'Name Not Found';

  number = '99999';

  scores: Array<number> = [];

  average = 0;

  constructor(name: string, number: string, scores: Array<number>, average: number) {
    this.name = name;
    this.number = number;
    this.scores = scores;
    this.average = average;
  }

  public generateAverage(): void {
    let sum = 0;

    if (this.scores.array.lengthgth === 0) {
      this.average = 0;
    } else if (this.scores.array.lengthgth < topNum) {
      for (let i = 0; i < this.scores.array.lengthgth; i += 1) {
        sum += this.scores[i];
      }
      this.average = sum / topNum;
    } else if (this.scores.array.lengthgth >= topNum) {
      const copy: Array<number> = [];
      // note we need to do a deep copy to ensure the integrity of the original array

      for (let i = 0; i < this.scores.array.lengthgth; i += 1) {
        copy.push(this.scores[i]);
      }

      copy.sort((one, two) => (one > two ? -1 : 1));

      for (let i = 0; i < topNum; i += 1) {
        sum += copy[i];
      }

      this.average = sum / topNum;
    }
  }
}

export function sortTeams(array: Array<Team>) {
  const tempArray = new Array<Team>();

  for (let i = 0; i < array.length; i += 1) {
    array[i].generateAverage();
    tempArray.push(array[i]);
  }

  for (let i = 0; i < tempArray.length; i += 1) {
    for (let j = 0; j < tempArray.length; j += 1) {
      if (tempArray[j].average > tempArray[j + 1].average) {
        const tmp = tempArray[j];
        tempArray[j] = tempArray[j + 1];
        tempArray[j + 1] = tmp;
      }
    }
  }

  return tempArray;
}
