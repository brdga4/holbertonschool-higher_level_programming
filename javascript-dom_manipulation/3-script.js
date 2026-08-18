const toggleHeader = document.querySelector('#toggle_header');
toggleHeader.addEventListener('click', function () {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
    header.classList.add('green');
    header.classList.remove('red');
  } else {
    header.classList.add('red');
    header.classList.remove('green');
  }
});
