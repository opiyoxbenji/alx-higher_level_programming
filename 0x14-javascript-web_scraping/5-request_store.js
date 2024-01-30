#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('Error fetching file:', error);
    return;
  }

  fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing file:', err);
    } else {
      console.log('File written successfully!');
    }
  });
});
