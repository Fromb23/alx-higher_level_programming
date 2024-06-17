#!/usr/bin/node

function secondLargestNumber (...args) {
  if (args.length < 2) {
    console.log('0'); // Print '0' if there are fewer than 2 arguments
    return;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (let i = 0; i < args.length; i++) {
    if (args[i] > largest) {
      secondLargest = largest; // Update second largest
      largest = args[i]; // Update largest
    } else if (args[i] > secondLargest && args[i] !== largest) {
      secondLargest = args[i]; // Update second largest
    }
  }

  if (secondLargest === -Infinity) {
    console.log('0'); // Print '0' if no second largest found
  } else {
    console.log(secondLargest);
  }
}

// Example usage with command-line arguments
const args = process.argv.slice(2).map(Number); // Convert command-line arguments to numbers
secondLargestNumber(...args);
