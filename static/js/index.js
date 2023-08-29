// This function is triggered when the user clicks a button to create a draft.
async function writeTeam(event) {
    event.preventDefault();
    document.getElementById("output").innerText = "Please wait...";
    document.getElementById("editoutput").innerText = "Please wait...";

    const data = {
        "writerType": document.querySelector('input[name="writerTypeRadio"]:checked').value,
        "editorType": document.querySelector('input[name="editorTypeRadio"]:checked').value,
        "topic": document.getElementById("posttopic").value,
        "keywords": [document.getElementById("postkeywords").value]
    };

    try {
        // Send the POST request to the Flask backend
        const draftData = await fetch("/draft", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        // Parse the JSON response
        const draftresult = await draftData.json();

        // Display the received draft on the webpage.
        document.getElementById("output").innerText = draftresult.draft;

        const editData = await fetch("/edit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({draft: draftresult.draft, data})
        });

        // Parse the JSON response
        const editresult = await editData.json();

        // Display the received draft on the webpage.
        document.getElementById("editoutput").innerText = editresult.edit;


    } catch (error) {
        // Handle any errors
        console.error("There was a problem with the fetch operation:", error);
    }
}

// Attach the createDraft function to a button click event
document.getElementById("mainsub").addEventListener("click", writeTeam);
