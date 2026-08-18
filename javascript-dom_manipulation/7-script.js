fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const movieList = document.querySelector('#list_movies');

    const films = data.results;

    for (let i = 0; i < films.length; i++) {
      const listItem = document.createElement('li');

      listItem.textContent = films[i].title;

      movieList.appendChild(listItem);
    }
  });
