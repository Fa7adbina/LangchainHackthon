function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var language = document.getElementById("language-select").value;
    appendMessage("User: " + userInput);

    // Send the user input and language to the Python backend
    fetch('/backend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: userInput,
            language: language
        })
    })
    .then(response => response.json())
    .then(data => {
        // Receive the response from the Python backend
        var botResponse = data.message;
        appendMessage("Legal Researcher: " + botResponse);
    });

    // Clear the user input
    document.getElementById("user-input").value = "";
}

function appendMessage(message) {
    var chatLog = document.getElementById("chat-log");
    var messageElement = document.createElement("p");
    messageElement.innerText = message;
    chatLog.appendChild(messageElement);
}
