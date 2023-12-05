// 7-script.js
// cpmoore0317

// Wait for the DOM to be fully loaded
$(document).ready(function () {
    // Define the URL for fetching the character data
    const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";

    // Use jQuery's AJAX method to fetch data from the URL
    $.ajax({
        url: apiUrl,
        method: "GET",
        success: function (data) {
            // Extract the character name from the data
            const characterName = data.name;

            // Select the character element and update its content
            $("#character").text(characterName);
        }
    });
});