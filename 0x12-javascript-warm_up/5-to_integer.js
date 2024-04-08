#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('No Number');
} else {
  console.log('My number: ' + firstArg);
}
