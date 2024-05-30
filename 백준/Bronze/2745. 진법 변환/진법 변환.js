const fs = require('fs');
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "/Users/Type/JavascriptProject/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split(' ');

let result = parseInt(input[0], Number(input[1]))
console.log(result)