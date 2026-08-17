#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
if (Number.isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < myNum) {
    console.log('C is fun');
    i++;
  }
}
