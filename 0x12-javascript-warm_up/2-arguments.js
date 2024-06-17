#!/usr/bin/node

const args = process.argv.length - 2;

if (args < 1) {
  console.log('No argument');
} else if (args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
