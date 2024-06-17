#!/usr/bin/node

const factorial = process.argv[2];
let result = 1;

for (let i = 1; i <= factorial; i++) {
  result *= i;
}
console.log(result);
