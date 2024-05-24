const fs = require('fs')
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "/Users/Type/JavascriptProject/input.txt";
const input = fs.readFileSync(filePath).toString().trim();

let num = Number(input);
let sum;
let i = 0;

while(true) {
  sum = Math.floor(num / 10) + (num % 10);
  num = (num % 10) * 10 + (sum % 10);
  i++;
  if (Number(input) === num) {
    break;
  }
}

console.log(i);