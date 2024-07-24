async function summarizeText() {
    const text = document.getElementById("inputText").value;
    if (!text) {
        alert("Please enter text to summarize.");
        return;
    }

    const response = await fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
    });

    const data = await response.json();
    if (data.error) {
        alert(data.error);
    } else {
        document.getElementById("summary").innerText = data.summary;
    }
}
