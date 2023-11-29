#!/usr/bin/node

// Import the Rectangle class from the './4-rectangle' module
const Rectangle = require('./4-rectangle');

// Define and export a new class Square that extends the Rectangle class
module.exports = class Square extends Rectangle {
  // Constructor for the Square class, taking a single argument 'size'
  constructor (size) {
    // Call the constructor of the base class (Rectangle) with 'size' for both width and height
    super(size, size);
  }

  // Override the double method inherited from the Rectangle class
  double () {
    // Call the double method of the base class (Rectangle) using super
    super.double();
  }
};
