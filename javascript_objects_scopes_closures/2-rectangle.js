#!/usr/bin/node

// Define the Rectangle class
class Rectangle {
  // Constructor for creating a Rectangle instance
  constructor(w, h) {
    // Check if both width and height are greater than 0
    if (w > 0 && h > 0) {
      // If conditions are met, set the width and height
      this.width = w;
      this.height = h;
    } else {
      // If conditions are not met, create an invalid Rectangle
    }
  }
}

// Export the Rectangle class for use in other modules
module.exports = Rectangle;
