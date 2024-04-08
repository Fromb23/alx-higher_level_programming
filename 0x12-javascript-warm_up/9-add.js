#!/usr/bin/node

function add (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    return (Number(a) + Number(b)); // Convert a and b to numbers before adding
  } else {
    return 'NaN';
  }
}
const a = process.argv[2];
const b = process.argv[3];

console.log(add(a, b));
