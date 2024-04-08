#!/usr/bin/node

function factorial (n) {
  if (n <= 1) {
    return n;
  } else {
    return n * factorial(n - 1);
  }
}

let arg = 1;
if (process.argv[2] !== undefined) {
  arg = parseInt(process.argv[2]);
}

console.log(factorial(arg));
