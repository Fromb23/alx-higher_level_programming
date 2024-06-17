#!/usr/bin/node

const n = parseInt(process.argv[2]);

function factorial (a) {
  if (a === 0 || isNaN(process.argv[2])) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(n));
