// 2-script.js

// Wait for DOM to be fully loaded
$(document).ready(function () {
    // Select the red_header element and define a click event handler
    $("#red_header").click(function () {
        // Select the <header> element and update the text to red
        $("header").css("color", "#FF0000");
    });
});