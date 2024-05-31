const fs = require('fs');
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "/Users/Type/JavascriptProject/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split('');
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

let result = ''
for (let i = 0; i < input.length; i++) {
  if (upper.includes(input[i])) {
    result += lower[upper.indexOf(input[i])]
  }
  else if (lower.includes(input[i])) {
    result += upper[lower.indexOf(input[i])]
  }
}

console.log(result)