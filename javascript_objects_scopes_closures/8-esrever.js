#!/usr/bin/node

// Define and export a function named 'esrever' that takes a list as a parameter
exports.esrever = function (list) {
  // Create an empty array to store the reversed elements
  const revList = [];

  // Iterate through the input list in reverse order
  for (let i = list.length - 1; i >= 0; --i) {
    // Push each element to the 'revList' array
    revList.push(list[i]);
  }

  // Return the reversed array
  return revList;
};
