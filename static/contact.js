document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let firstName = document.getElementById("first-name").value.trim();
    let lastName = document.getElementById("last-name").value.trim();
    let email = document.getElementById("email").value.trim();
    let phone = document.getElementById("phone").value.trim();
    let message = document.getElementById("message").value.trim();

    if (firstName === "" || lastName === "" || email === "" || message === "") {
        alert("Please fill in all required fields.");
        return;
    }

    alert("Thank you, " + firstName + "! Your message has been sent.");

    // Reset form
    document.getElementById("contactForm").reset();
});
