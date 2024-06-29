#!/usr/bin/node

const { argv } = require('node:process');

// Gets the arguments, converts to numbers and stores in array
const args = argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a); // Descending order

  console.log(args[1]);
}
