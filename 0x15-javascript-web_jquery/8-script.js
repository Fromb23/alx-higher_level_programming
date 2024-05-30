$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    var movieTitle = [];
    for (var i = 0; i < data.titles.length; i++) {
        movieTitle.push(data.titles[i]);
    }
    var list = $('#list_movies');

    for (var j = 0; j < movieTitle.length; j++) {
        var listItem = $("<li></li>").text(movieTitles[]);

        list.append(listItem);
    }
});