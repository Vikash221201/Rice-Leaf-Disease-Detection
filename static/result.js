document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    
    document.getElementById("disease").textContent = urlParams.get("disease") || "Unknown";
    document.getElementById("remedies").textContent = urlParams.get("remedies") || "No remedies available.";
    document.getElementById("medicines").textContent = urlParams.get("medicines") || "No medicines suggested.";
    document.getElementById("pesticides").textContent = urlParams.get("pesticides") || "No pesticides suggested.";
});

document.getElementById("predict").addEventListener("click", function() {
    let fileInput = document.getElementById("imageInput").files[0];
    if (!fileInput) {
        alert("Please select an image first!");
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput);

    document.getElementById("loading").style.display = "block";  // Show loading text

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("loading").style.display = "none";  // Hide loading
        let queryString = `?disease=${encodeURIComponent(data.disease)}&remedies=${encodeURIComponent(data.remedies)}&medicines=${encodeURIComponent(data.medicines)}&pesticides=${encodeURIComponent(data.pesticides)}`;
        window.location.href = `/result${queryString}`;
    })
    .catch(error => console.error("Error:", error));
});