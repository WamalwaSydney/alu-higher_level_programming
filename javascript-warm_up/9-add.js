#!/usr/bin/node
function add(a, b) {
  return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (!isNaN(arg1) && !isNaN(arg2)) {
  console.log(`My number: ${add(arg1, arg2)}`);
} else {
  console.log("Not a number");
}
