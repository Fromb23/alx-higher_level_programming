#!/usr/bin/node

// Define the function to export
exports.converter = function (base) {
  // Define an inner function to perform the conversion recursively
  function convertToBase10 (number) {
    if (number < base) {
      // Base case: when the number is less than the base, return the number itself
      return number.toString();
    } else {
      // Recursive case: divide the number by the base and continue converting
      return convertToBase10(Math.floor(number / base)) + (number % base).toString();
    }
  }

  // Return the inner function for use
  return convertToBase10;
};
