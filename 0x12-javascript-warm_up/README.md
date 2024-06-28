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

## Task 4 - Create a sentence
In this one I used a tenary operator after the shebang. The task wanted us to print the first and second arguments we type 
on the console on the right and left side of is. That is "is" would be entre the two arguments. process.argv[2] is the first
argument we pass as we all know and process.argv[3] is the second. process.argv[0] and process.argv[1] are reserved for the path
to the Node.js executable and script file respectively.

## Task 5 - An integer
first argument converted to an integer - use of ternary operator. isNan() used Math.floor() rounds up number, Number()
coverts string to number.

## Task 6 - Loop of languages
Using a for loop to print sentences. I stored the strings in an array and called it by its indexes.

## Task 7 - I love C
Using a loop, you print C a defined amount of time, the value of the number of times you print "I love C" is stored in the first argument

