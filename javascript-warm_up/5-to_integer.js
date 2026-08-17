#!/usr/bin/node
const myNum = parseInt(process.argv[2], 10);
if (Number.isNaN(myNum) || myNum === undefined) {
  console.log('Not a number');
} else {
  console.log(myNum);
}
