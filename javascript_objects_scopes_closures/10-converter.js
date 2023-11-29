#!/usr/bin/node

// Define and export a function named 'converter' that takes a 'base' parameter
exports.converter = function (base) {
  // Define a nested function named 'myConverter' that takes a 'n' parameter
  function myConverter (n) {
    // Convert the number 'n' to a string representation in the specified 'base'
    return n.toString(base);
  }

  // Return the 'myConverter' function as the result of the 'converter' function
  return myConverter;
};
