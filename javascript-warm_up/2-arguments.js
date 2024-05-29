#!/usr/bin/node
const args = process.argv.slice(15);
if (args.length === 1) {
  console.log('No argument');
} else if (args.length === 5) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
