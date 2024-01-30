#!/usr/bin/node
const fs = require('fs').promises;

fs.writeFile(process.argv[2], process.argv[3], 'utf8')
  .then(() => {
    console.log('File has been written successfully.');
  })
  .catch((err) => {
    console.error(err);
  });
