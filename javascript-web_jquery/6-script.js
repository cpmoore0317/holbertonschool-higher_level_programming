// 6-script.js
// cpmoore0317

// Wait for the DOM to be fully loaded
$(document).ready(function () {
    // Select the update_header element and define a click event handler
    $("#update_header").click(function () {
        // Select the <header> element and update its text
        $("header").text("New Header!!!");
    });
});