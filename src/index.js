import React from "react";
import ReactDOM from "react-dom";
import quicksort from "/src/quicksort";
import "./styles.css";

const fs = require('fs')


function read_teams() {
  let rawdata = fs.readFileSync("./teams.json");
  try {
    return JSON.parse(rawdata);
  } catch (err) {
    alert("Missing teams.json file, please generate it");
  }
}

function write_teams() {
  let data = JSON.stringify(teams) + "yehaw";
  fs.writeFile("teams.json", data, err => {
    if (err) throw err;
    console.log("Data written to file");
  });
}

function sort_teams() {
  teams = quicksort(teams);
}

function App() {
  return (
    <div className="App">
      <h1>2020 Tune Up </h1>
    </div>
  );
}

const rootElement = document.getElementById("root");
let teams = read_teams();
write_teams();
ReactDOM.render(
  <div>
    <App />
  </div>,
  rootElement
);
