#!/usr/bin/node

/* a script that prints two arguments passed to it, in the following format:  "is” */

const firstName = process.argv;
const concatnet = firstName[2] + ' is ' + firstName[3];

console.log(concatnet);
