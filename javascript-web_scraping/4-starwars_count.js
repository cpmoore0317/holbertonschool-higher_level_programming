#!/usr/bin/node

// Importing the 'request' module for making HTTP requests
const request = require('request');

// Accessing command line arguments
const argv = process.argv;

// Making a request to the provided URL
request(argv[2], function (error, response, body) {
  // Handling errors, if any
  if (error) {
    console.error(error);
  } else {
    // Parsing the JSON response to extract Star Wars films information
    const starWarsFilms = JSON.parse(body).results;

    // Counting the number of times character '18' appears in films
    let numTimes = 0;
    for (const film of starWarsFilms) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          numTimes += 1;
        }
      }
    }

    // Logging the result
    console.log(numTimes);
  }
});
