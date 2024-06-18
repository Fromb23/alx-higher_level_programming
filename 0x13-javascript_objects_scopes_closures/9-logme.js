#!/usr/bin/node

// Initialize a counter outside of the function scope
let count = 0;

// Define the function to export
exports.logMe = function (item) {
  // Print the current count and the item value in the specified format
  console.log(`${count}: ${item}`);

  // Increment the count for the next call
  count++;
};
