#!/usr/bin/node

/* a script that computes and prints a factorial */

const input = process.argv;

if (isNaN(Number(input[2]))) {
  console.log('1');
} else {
  let n = Number(input[2]);
  function factorial (num) {
    if (num > 1) {
      return num * factorial(num - 1);
    } else {
      return num;
    }
  }
  n = factorial(n);
  console.log(n);
}
