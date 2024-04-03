$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (response) {
      const movies = response.results;
      $.each(movies, function (index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    },
    error: function () {
      $('#list_movies').append('<li>Movie could not be found</li>');
    }
  });
});
