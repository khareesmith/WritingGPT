// This function is triggered when the user clicks a button to create a draft.
async function createDraft(event) {
    // Sample data to send. You can replace this with real data from your form or other UI elements.
    event.preventDefault();
    document.getElementById("output").innerText = "Please wait...";
    const data = {
        "writerType": document.querySelector('input[name="writerTypeRadio"]:checked').value,
        "topic": document.getElementById("posttopic").value,
        "keywords": [document.getElementById("postkeywords").value]
    };

    try {
        // Send the POST request to the Flask backend
        console.log("before fetch. Writer type: " + document.querySelector('input[name="writerTypeRadio"]:checked').value)
        const response = await fetch("/draft", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        // Parse the JSON response
        const result = await response.json();
        answer = result.draft;

        // Display the received draft on your webpage.
        // Here, we assume you have an element with the id "output" where the draft should be displayed.
        document.getElementById("output").innerText = answer;
        console.log(answer);

    } catch (error) {
        // Handle any errors
        console.error("There was a problem with the fetch operation:", error);
    }

    console.log("after fetch")
}

// Attach the createDraft function to a button click event
document.getElementById("mainsub").addEventListener("click", createDraft);
