
// Select the input element by its id
let nameInput = document.getElementById("name-input");
let output = document.getElementById("joke-result");
// Get the value of the input element
let nameValue = nameInput.value;
console.log(nameValue);

let jokeBtn = document.getElementById("joke-btn");
// Add a click event listener to the button
jokeBtn.addEventListener("click", function () {

    // Fetch data from a URL
    fetch(`http://localhost:8080/bot/chat?prompt=${nameValue}`)
        // Convert the response to JSON
        .then(response => response.json())
        .then(data => output.innerText = data)
        .catch(error => console.error(error));
    console.log("Button clicked!");
});