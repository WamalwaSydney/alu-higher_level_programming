#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedgeURL = "https://swapi-api.alx-tools.com/api/people/18/";

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    try {
      const data = JSON.parse(body);
      let count = 0;
      data.results.forEach(film => {
        if (film.characters.includes(wedgeURL)) {
          count++;
        }
      });
      console.log(count);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
