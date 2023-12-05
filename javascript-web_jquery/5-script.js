// 5-script.js
// cpmoore0317

// Wait for the DOM to be fully loaded
$(document).ready(function () {
    // Select the add_item element and define a click event listener
    $("#add_item").click(function () {
        // Create a <li> element with the text "Item"
        let newItem = $("<li>").text("Item");

        // Append the new <li> element to UL.my_list
        $("ul.my_list").append(newItem);
    });
});