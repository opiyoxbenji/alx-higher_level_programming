#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const starwarsApiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(starwarsApiUrl, (_err, _res, body) => {
  const { title } = JSON.parse(body);
  console.log(title);
});
