#!/usr/bin/node
const fs = require('fs');

function contentReader(path) {
	fs.readFile(path, 'utf-8', (err, data) => {
		if (err) {
			console.error(`An error occured: ${err.message}`);
		} else {
			console.log(data);
		}
	});
}

if (process.argv.length !== 3) {
	console.log('Usage: node script.js <path>');
	process.exit(1);
}

const path = process.argv[2];
contentReader(path);
