#!/usr/bin/node

class Square extends Rectangle {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }

  for (let i = 0; i < this.height; i++) {
    console.log(c.repeat(this.width));
  }
  }
}

module.exports = {
	Rectangle: Rectangle,
	Square: Square
};
