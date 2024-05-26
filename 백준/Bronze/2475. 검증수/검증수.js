const fs = require('fs');
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "/Users/Type/JavascriptProject/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split(' ');

let result = 0;
for (let i = 0; i < input.length; i++) {
  let a = parseInt(input[i]) ** 2
  result += a
}

console.log(result % 10)