document.addEventListener("DOMContentLoaded", function () {
    console.log("Publications Page Loaded Successfully");

    // Smooth Scroll Effect for Navigation Links
    document.querySelectorAll('.nav-menu a').forEach(anchor => {
        anchor.addEventListener("click", function (event) {
            if (this.getAttribute("href").startsWith("#")) {
                event.preventDefault();
                const targetId = this.getAttribute("href").substring(1);
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 60, // Adjust for header height
                        behavior: "smooth"
                    });
                }
            }
        });
    });

    // Dropdown Functionality (For Future Enhancements)
    document.querySelectorAll(".dropdown").forEach(dropdown => {
        dropdown.addEventListener("mouseenter", function () {
            let dropdownMenu = this.querySelector(".dropdown-content");
            if (dropdownMenu) {
                dropdownMenu.style.display = "block";
            }
        });

        dropdown.addEventListener("mouseleave", function () {
            let dropdownMenu = this.querySelector(".dropdown-content");
            if (dropdownMenu) {
                dropdownMenu.style.display = "none";
            }
        });
    });

    // Hover Effect for Publication Cards
    document.querySelectorAll(".publication-card").forEach(card => {
        card.addEventListener("mouseenter", function () {
            this.style.transform = "scale(1.08)";
            this.style.boxShadow = "0px 6px 14px rgba(0, 0, 0, 0.2)";
        });

        card.addEventListener("mouseleave", function () {
            this.style.transform = "scale(1)";
            this.style.boxShadow = "0px 4px 8px rgba(0, 0, 0, 0.1)";
        });
    });
});
