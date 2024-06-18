#!/usr/bin/node

// Define the function to export
exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter for occurrences
  let count = 0;

  // Iterate through the list to count occurrences of searchElement
  list.forEach(element => {
    if (element === searchElement) {
      count++;
    }
  });

  // Return the count of occurrences
  return count;
};
