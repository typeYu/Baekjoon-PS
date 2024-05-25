const fs = require('fs');
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "/Users/Type/JavascriptProject/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split('\n');


for (let i = 0; i < input.length; i++) {
  let [name, age, weight] = input[i].split(' ');
  age = parseInt(age);
  weight = parseInt(weight);
  
  if (name === '#' && age === 0 && weight === 0) {
      break;
  }
  
  if (age > 17 || weight >= 80) {
      console.log(`${name} Senior`);
  } else {
      console.log(`${name} Junior`);
  }
}