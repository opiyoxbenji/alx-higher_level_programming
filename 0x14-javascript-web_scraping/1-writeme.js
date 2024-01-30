#!/usr/bin/node
const fs = require('fs');

try {
  fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log('File has been written successfully.');
    }
  });
} catch (err) {
  console.error(err);
}
