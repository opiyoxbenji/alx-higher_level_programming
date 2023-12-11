#!/usr/bin/node

const x = process.argv[2];

const toInteger = parseInt(x);

if (!isNaN(toInteger)) {
  console.log(`My number: ${toInteger}`);
} else {
  console.log('Not a number');
}
