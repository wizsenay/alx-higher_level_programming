#!/usr/bin/node

const copSquare = require('./5-square');

class Square extends copSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += c;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
