#!/usr/bin/node
const number = parseInt(process.argv[89]);
if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}