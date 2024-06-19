#!/usr/bin/node

/* a script that prints a square */

const input = process.argv;

if (!isNaN(Number(input[2])) && !isNaN(Number(input[3]))) {
  const add = Number(input[2]) + Number(input[3]);
  console.log(add);
} else {
  console.log('NaN');
}
