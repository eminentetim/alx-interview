#!/usr/bin/node

const request = require('request');

// Function to fetch data from a URL and return a promise
const fetchData = (url) => {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else if (response.statusCode !== 200) {
                reject(new Error(`Failed to fetch data. Status Code: ${response.statusCode}`));
            } else {
                resolve(JSON.parse(body));
            }
        });
    });
};

// Main function to get the movie characters
const getMovieCharacters = async (movieId) => {
    try {
        // Construct the URL for the movie endpoint
        const movieUrl = `https://swapi.dev/api/films/${movieId}/`;
        
        // Fetch movie details
        const movieData = await fetchData(movieUrl);
        const characterUrls = movieData.characters;
        
        // Fetch character details
        const characterPromises = characterUrls.map(url => fetchData(url));
        const characters = await Promise.all(characterPromises);
        
        // Print character names in order
        characters.forEach(character => {
            console.log(character.name);
        });
    } catch (error) {
        console.error('Error:', error.message);
    }
};

// Parse command-line arguments to get Movie ID
const movieId = process.argv[2];
if (!movieId) {
    console.error('Please provide a Movie ID as the first argument');
    process.exit(1);
}

// Execute the function to get movie characters
getMovieCharacters(movieId);

