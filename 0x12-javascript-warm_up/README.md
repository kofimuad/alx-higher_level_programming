# JavaScript Warmup

## Task 0 - First Constant, first script
A constant variable myVar, that constant a script "JavaScript is cool" and print it with console.log();

## Task 1 - Langauges
Prints three scripts on stdout.

## Task 2 - Arguments
Prints messages depending on the number of arguments passed. process.argv used.
'const { argv } = require('node:process')' => This gets the argv property from the process module and allows you to access
command line arguments.

## Task 3 - Value of my argument
Print the first argument passed to the script. Here, I made use of the forEach method. I passed to it the val and index
of each argument. Then stored the first argument in a varibale.
argv.forEach((val, index) => if (index === 2) {firstArg = val} if (index >= 2)  {count++}). This is basically the code.


