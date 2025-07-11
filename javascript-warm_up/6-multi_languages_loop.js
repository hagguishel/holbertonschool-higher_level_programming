#!/usr/bin/node
const tableau = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let result = '';
for (let i = 0; i < tableau.length; i++) {
  result += tableau[i];
  if (i < tableau.length - 1) {
    result += '\n';
  }
}
console.log(result);
