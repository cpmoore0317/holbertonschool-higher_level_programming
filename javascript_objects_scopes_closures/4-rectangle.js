#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Constructor takes two arguments: w (width) and h (height).
    // Check if w or h is not a positive integer or is equal to 0.
    if (w <= 0 || h <= 0) {
      // If the conditions are met, create an empty object.
      return {};
    } else {
      // Otherwise, initialize the instance attributes width and height with the provided values.
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Instance method print() prints the rectangle using the character 'X'.
    for (let i = 0; i < this.height; i++) {
      // Loop through each row (height) of the rectangle.
      let row = '';
      for (let j = 0; j < this.width; j++) {
        // Append 'X' to the row for each column (width) of the rectangle.
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    // Instance method rotate() exchanges the width and the height of the rectangle.
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    // Instance method double() multiplies the width and the height of the rectangle by 2.
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
