console.log("script.js loaded");

async function analyzeTasks() {
    console.log("Analyze button clicked");

    const input = document.getElementById("taskInput").value;

    let tasks;
    try {
        tasks = JSON.parse(input);
    } catch (e) {
        alert("Invalid JSON format!");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/api/tasks/analyze/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(tasks)
        });

        const data = await response.json();
        displayResults(data);

    } catch (error) {
        console.error(error);
        alert("Error contacting backend.");
    }
}

function displayResults(tasks) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";

    tasks.forEach(task => {
        const div = document.createElement("div");
        div.classList.add("task-card");

        div.innerHTML = `
            <h3>${task.title}</h3>
            <p><b>Due:</b> ${task.due_date}</p>
            <p><b>Importance:</b> ${task.importance}</p>
            <p><b>Effort:</b> ${task.estimated_hours} hrs</p>
            <p><b>Score:</b> ${task.score}</p>
        `;

        resultsDiv.appendChild(div);
    });
}
