#!/usr/bin/node
// 1-script
const header = document.querySelector('header');
const red_header = document.querySelector('#red_header');
red_header.addEventListener('click', function() {
  header.style.color = "#FF0000";
});
