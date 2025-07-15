#!/usr/bin/node
const character = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    character.textContent = data.name;
  });
