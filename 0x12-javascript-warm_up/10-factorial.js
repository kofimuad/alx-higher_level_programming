#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
const arg = Math.floor(Number(process.argv[2]));
console.log(factorial(arg));
