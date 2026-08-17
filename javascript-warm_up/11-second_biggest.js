#!/usr/bin/node

const numbers = process.argv.map(Number);
const len = numbers.length;

if (len <= 3) {
  console.log(0);
  process.exit(0);
}

let max = numbers[2];

for (let i = 3; i < len; i++) {
  if (numbers[i] > max) {
    max = numbers[i];
  }
}

let secondMax = -Infinity;

for (let i = 2; i < len; i++) {
  if (numbers[i] > secondMax && numbers[i] < max) {
    secondMax = numbers[i];
  }
}

if (secondMax === -Infinity) {
  console.log(0);
} else {
  console.log(secondMax);
}
