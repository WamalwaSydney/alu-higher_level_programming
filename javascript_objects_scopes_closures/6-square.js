#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }

  charPrint(c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
