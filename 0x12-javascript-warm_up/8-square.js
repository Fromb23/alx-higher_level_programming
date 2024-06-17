#!/usr/bin/node

if (process.argv < 2 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = process.argv[2];
  for (let i = 0; i < size; i++) {
    let row = ' ';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
