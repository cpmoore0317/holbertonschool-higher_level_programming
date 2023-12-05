// 3-script.js

// Wait for the DOM to be fully loaded
$(document).ready(function () {
    // Select the red_header element and define a click event handler
    $("#red_header").click(function () {
        // Select the <header> element and definer a click event handler
        $("header").addClass("red");
    });
});