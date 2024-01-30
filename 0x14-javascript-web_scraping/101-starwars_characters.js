#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + filmId;

request(filmUrl, function (filmError, filmResponse, filmBody) {
  if (!filmError) {
    const characterUrls = JSON.parse(filmBody).characters;
    printCharacters(characterUrls, 0);
  }
});

function printCharacters (urls, index) {
  request(urls[index], function (characterError, characterResponse, characterBody) {
    if (!characterError) {
      console.log(JSON.parse(characterBody).name);
      if (index + 1 < urls.length) {
        printCharacters(urls, index + 1);
      }
    }
  });
}

