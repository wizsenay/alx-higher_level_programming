#!/usr/bin/node

const args = process.argv;

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const uniqueIntegers = [...new Set(args.map(Number))];
  uniqueIntegers.sort((a, b) => b - a);

  console.log(uniqueIntegers[1]);
}
