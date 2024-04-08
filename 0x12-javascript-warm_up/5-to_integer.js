#!/usr/bin/node

const firstArg = parseInt(process.argv[2], 10);

if (!Number.isNaN(firstArg)) {
  console.log(`My number: ${firstArg}`);
} else {
  console.log('No number');
}
