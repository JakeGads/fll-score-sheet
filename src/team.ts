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

    if (this.scores.length === 0) {
      this.average = 0;
    } else if (this.scores.length < topNum) {
      for (let i = 0; i < this.scores.length; i += 1) {
        sum += this.scores[i];
      }
      this.average = sum / topNum;
    } else if (this.scores.length >= topNum) {
      const copy: Array<number> = [];
      // note we need to do a deep copy to ensure the integrity of the original array

      for (let i = 0; i < this.scores.length; i += 1) {
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
