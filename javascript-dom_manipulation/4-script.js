const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', function () {
  const newItem = document.createElement('li');
  const list = document.querySelector('.my_list');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});
