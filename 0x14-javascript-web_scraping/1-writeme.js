#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const string = process.argv[3];

function writeToFile(filePathe, string) {

        fs.writeFile(filePathe, string,  'utf8',  (error) => {

                if (error) {
                  console.log(error);
                }

                console.log(`Content has been written to: ${filePath}`);


        })

}


writeToFile(filePath, string);
