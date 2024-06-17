#!/usr/bin/node

let args = process.argv[2];

if (isNaN(args)) {
  console.log('Not a number');
} else {
  args = parseInt(args);
  console.log('My number: ' + args);
}
