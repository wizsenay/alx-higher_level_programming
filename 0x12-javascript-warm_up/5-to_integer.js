#!/usr/bin/node

/* a script that prints My number:
   <first argument converted in integer>
   if the first argument can be converted to an integer */

const intiger = process.argv;

if (!isNaN(Number(intiger[2]))) {
  console.log('My number: ' + intiger[2]);
} else {
  console.log('Not a number');
}
