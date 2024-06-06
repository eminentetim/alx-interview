#!/usr/bin/node

const request = require('request');

// Step 1: Parse command-line arguments to get Movie ID
const movieId = process.argv[2];
if (!movieId) {
    console.error('Please provide a Movie ID as the first argument');
    process.exit(1);
}

// Step 2: Construct the URL for the movie endpoint
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

// Step 3: Fetch the movie details
request(movieUrl, (error, response, body) => {
    if (error) {
        console.error('Error fetching movie data:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error('Failed to fetch movie data. Status Code:', response.statusCode);
        return;
    }

    // Step 4: Parse the movie data
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Step 5: Fetch character details
    characters.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.error('Error fetching character data:', error);
                return;
            }

            if (response.statusCode !== 200) {
                console.error('Failed to fetch character data. Status Code:', response.statusCode);
                return;
            }

            // Step 6: Parse and print the character name
            const characterData = JSON.parse(body);
            console.log(characterData.name);
        });
    });
});

