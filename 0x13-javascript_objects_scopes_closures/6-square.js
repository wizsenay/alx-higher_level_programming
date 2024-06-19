#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        let line = '';
        for (let j = 0; j < this.size; j++) {
          line += c;
        }
        console.log(line);
      }
    }
  }
}

module.exports = Square;
