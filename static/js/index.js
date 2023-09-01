// This function is triggered when the user clicks a button to create a draft.
async function writeTeam(event) {
    event.preventDefault();

    const data = {
        "writerType": document.querySelector('input[name="writerTypeRadio"]:checked').value,
        "editorType": document.querySelector('input[name="editorTypeRadio"]:checked').value,
        "topic": document.getElementById("posttopic").value,
        "keywords": [document.getElementById("postkeywords").value]
    };

    try {
        // Send the POST request to the Flask backend to create a draft
        document.getElementById("output").innerText = "Please wait. The draft is being generated.";
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

        // Send the POST request to the Flask backend to edit the draft
        document.getElementById("editoutput").innerText = "The editor is looking over the draft now!";
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

        // Send the POST request to the Flask backend to create SEO notes
        document.getElementById("seooutput").innerText = "The SEO expert is giving notes on improvement, one moment!";
        const seoData = await fetch("/seo", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({draft: draftresult.draft, data})
        });

        // Parse the JSON response
        const seoresult = await seoData.json();

        // Display the received draft on the webpage.
        document.getElementById("seooutput").innerText = seoresult.seo;

        // Send the POST request to the Flask backend to suggest photos
        document.getElementById("photooutput").innerText = "The photo researcher is providing feedback on images to add. Please wait...";
        const photoData = await fetch("/photo", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({draft: draftresult.draft, data})
        });

        // Parse the JSON response
        const photoresult = await photoData.json();

        // Display the received draft on the webpage.
        document.getElementById("photooutput").innerText = photoresult.photo;

        // Send the POST request to the Flask backend to provide the final post
        document.getElementById("finaloutput").innerText = "The final post is being generated now! One moment until your AI-generated post is ready.";
        const finalData = await fetch("/final", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({draft: draftresult.draft, edit: editresult.edit, seo: seoresult.seo, photoresult: photoresult.photo})
        });

        // Parse the JSON response
        const finalresult = await finalData.json();

        // Display the received draft on the webpage.
        document.getElementById("finaloutput").innerText = finalresult.final;

        const down_draft = document.createElement("button")
        down_draft.innerText = "Download Draft"
        down_draft.setAttribute("class", "btn btn-primary")
        document.getElementById("draftbody").appendChild(down_draft)

    } catch (error) {
        // Handle any errors
        console.error("There was a problem with the fetch operation:", error);
    }
}

// Attach the createDraft function to a button click event
document.getElementById("mainsub").addEventListener("click", writeTeam);
