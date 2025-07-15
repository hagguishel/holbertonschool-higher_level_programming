#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
  const hello = document.querySelector('#hello');
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
   .then(reponse => reponse.json())
   .then(data => {
    hello.textContent = data.hello;
   })
})
