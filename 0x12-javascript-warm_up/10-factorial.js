#!/usr/bin/node

const args = process.argv;

function factorial (number) {
  if (number < 0) {
    return false;
  } else if (number === 0) {
    return true;
  }
  return number * factorial(number - 1);
}

console.log(factorial(Number(args[2])));
