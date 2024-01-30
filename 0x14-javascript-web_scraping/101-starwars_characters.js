#!/usr/bin/node

const request = require('request-promise-native');

async function getCharacters (movieId) {
  try {
    const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;
    const filmData = await request(filmUrl);
    const characters = filmData.characters;
    for (const characterUrl of characters) {
      const characterData = await request(characterUrl);
      console.log(JSON.parse(characterData).name);
    }
  } catch (error) {
    console.error(error.message);
  }
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
getCharacters(movieId);
