// 9-script.js
// cpmoore0317

// Wait for the DOM to be fully loaded using jQuery
$(document).ready(function () {
    const apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";

    // Use jQuery's AJAX method to fetch data from the URL
    $.ajax({
        url: apiUrl,
        method: "GET",
        success: function (data) {
            // Select the hello element and update its content
            $("#hello").text(data.hello);
        }
    });
});