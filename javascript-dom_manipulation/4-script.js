const addItemBtn = document.querySelector('#add_item');
addItemBtn.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newItem);
});
