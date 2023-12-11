#!/usr/bin/node

const x = process.argv[2];

const toInteger = parseInt(x);

if (!isNaN(toInteger)) {
  console.log(`My number: ${toInterger}`);
} else {
  console.log("Not a number");
