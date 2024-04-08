#!/usr/bin/node

function secondLargest(args) {
  // Convert all arguments to integers
  const integers = args.slice(2).map(Number);

  // Check if the number of arguments is less than 2
  if (integers.length < 2) {
    return 0;
  }

  // Sort the list in descending order
  const sortedIntegers = integers.sort((a, b) => b - a);

  // Print the second element in the sorted list
  return sortedIntegers[1];
}

const args = process.argv;

console.log(secondLargest(args));
