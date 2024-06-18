#!/usr/bin/node

/* a script that prints the first argument passed to it */

const firstName = process.argv;
if (firstName[2] !== undefined) {
  console.log(firstName[2]);
} else {
  console.log('No argument');
}
