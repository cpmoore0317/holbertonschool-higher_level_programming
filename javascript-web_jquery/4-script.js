// 4-script.js

// Wait for the DOM to be fully loaded
$(document).ready(function () {
    // Select the toggle_header element and define a click event handler
    $("#toggle_header").click(function () {
        // Select the <header> element
        let headerElement = $("header");

        // Check if the header had the red class
        if (headerElement.hasClass("red")) {
            // If it does, remove red and add green
            headerElement.removeClass("red").addClass("green");
        } else {
            // If it doesn't have red, remove green and add red
            headerElement.removeClass("green").addClass("red");
        }
    });
});