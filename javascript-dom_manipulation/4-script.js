#!/usr/bin/node
const add_item = document.querySelector('#add_item');
const my_list = document.querySelector('.my_list');

add_item.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  my_list.appendChild(newItem);
})
