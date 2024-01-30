#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const nb = JSON.parse(body).results.reduce((acc, elem) => {
    const count = elem.characters.filter(url => url.includes('18')).length;
    return acc + count;
  }, 0);

  console.log(nb);
});
