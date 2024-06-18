#!/usr/bin/node

/* a script that prints x times “C is fun” */

const input = process.argv;

if (!isNaN(Number(input[2]))) {
  let num = Number(input[2]);

  if (num > 0) {
    while (num > 0) {
      console.log('C is fun');
      num--;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
