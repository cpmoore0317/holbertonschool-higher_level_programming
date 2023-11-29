#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Constructor takes two arguments: w (width) and h (height).
    // Check if w or h is not a positive integer or is equal to 0.
    if (w <= 0 && h <= 0) {
      // If the conditions are met, create an empty object.
      return this;
    } else {
      // Otherwise, initialize the instance attributes width and height with the provided values.
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
