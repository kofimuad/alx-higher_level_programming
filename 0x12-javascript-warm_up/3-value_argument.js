#!/usr/bin/node

const { argv } = require('node:process');

let numArgs = 0;
let firstArg;

argv.forEach((val, index) => {
  if (index >= 2) {
    numArgs++;
  }
  if (index === 2) {
    firstArg = val;
  }
});

if (numArgs === 0) {
  console.log('No Argument');
} else {
  console.log(firstArg);
}
