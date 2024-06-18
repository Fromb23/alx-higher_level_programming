#!/usr/bin/node

// Define the function to export
exports.esrever = function (list) {
  // Initialize an empty array to store reversed elements
  const reversedList = [];

  // Iterate through the list from end to start
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  // Return the reversed array
  return reversedList;
};
