const fs = require('fs');
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "/Users/Type/JavascriptProject/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [A, B, C] = input[0].split(' ').map(Number);
const cookingTime = parseInt(input[1], 10);

const totalSecondsCurrent = A * 3600 + B * 60 + C;
const totalSecondsEnd = totalSecondsCurrent + cookingTime;

const hours = Math.floor(totalSecondsEnd / 3600) % 24;
const minutes = Math.floor((totalSecondsEnd % 3600) / 60);
const seconds = totalSecondsEnd % 60;

console.log(hours, minutes, seconds);