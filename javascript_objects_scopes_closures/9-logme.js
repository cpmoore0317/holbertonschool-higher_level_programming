#!/usr/bin/node

// Initialize a counter variable to keep track of the number of times the function is called
let counter = 0;

// Define and export a function named 'logMe' that takes an 'item' parameter
exports.logMe = function count (item) {
  // Print the current counter value and the provided 'item' to the console
  console.log(`${counter}: ${item}`);

  // Increment the counter by 1 for the next call
  counter += 1;
};
