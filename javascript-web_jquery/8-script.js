// 8-script.js
// cpmoore0317

// Wait for the DOM to be fully loaded
$(document).ready(function () {
    // Define the URL for fetching the character data
    const apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";

    // Use jQuery's AJAX method to fetch data from the URL
    $.ajax({
        url: apiUrl,
        method: "GET",
        success: function (data) {
            // Extract the character name from the data
            const listMovies = $("#list_movies");

            $.each(data.results, function (index, movie) {
                // Create a new LI element with the movie title
                // appended to the list
                $("<li>").text(movie.title).appendTo(listMovies);
            });
        }
    });
});