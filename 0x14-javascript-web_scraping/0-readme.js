#!/usr/bin/node

'use strict';

const fs = require('fs');

function readFile (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error('An error occured:', err);
      return;
    }
    console.log(data);
  });
}

if (process.argv.length !== 2) {
  console.error('Usage: ./readme.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[1];
readFile(filePath);
