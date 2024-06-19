#!/usr/bin/node

/* a script that prints a square */

const input = process.argv;

if (!isNaN(Number(input[2]))) {
  const num = Number(input[2]);

  if (num > 0) {
    for (let i = 0; i < num; i++) {
      let line = '';
      for (let j = 0; j < num; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }
} else {
  console.log('Missing size');
}
