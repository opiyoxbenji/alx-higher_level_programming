#!/usr/bin/node

let args = process.argv.slice(2);

if (!args) {
	console.log('No argument');
} else if (args == 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
