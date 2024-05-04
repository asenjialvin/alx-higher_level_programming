#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const SUBSTRING_TO_FIND = '18';

request(url, function (err, response, body) {
    if (err) {
        console.error('Error occurred:', err);
    } else if (response.statusCode === 200) {
        try {
            const films = JSON.parse(body).results;
            let count = 0;
            for (const film of films) {
                const filmChars = film.characters;
                for (const character of filmChars) {
                    if (character.includes(SUBSTRING_TO_FIND)) {
                        count++;
                    }
                }
            }
            console.log('Count of characters with ID containing', SUBSTRING_TO_FIND + ':', count);
        } catch (error) {
            console.error('Error parsing JSON:', error);
        }
    } else {
        console.error('An error occurred. Status code:', response.statusCode);
    }
});
