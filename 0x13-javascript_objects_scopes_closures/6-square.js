#!/usr/bin/node
const SquareX = require('./5-square');
module.exports = class Square extends SquareX {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
