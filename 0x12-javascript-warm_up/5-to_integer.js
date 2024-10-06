#!/usr/bin/node

const args = process.argv;
const index = Number(args[2]);

if (index >= 0) {
	console.log("My number:", index);
} else {
	console.log("Not a number");
}
