#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.log(`Error: Received status code ${response.statusCode}`);
  }
});
