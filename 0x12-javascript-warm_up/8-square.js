#!/usr/bin/node

const x = Math.floor(Number(process.argv[2]));

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < x; r++) {
    let row = '';
    for (let c = 0; c < x; c++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
