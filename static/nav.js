document.addEventListener("DOMContentLoaded", function () {
  const dropdowns = document.querySelectorAll(".dropdown");

  dropdowns.forEach(dropdown => {
      let timeout; // To prevent flickering

      // Show dropdown on hover
      dropdown.addEventListener("mouseenter", function () {
          clearTimeout(timeout);
          const dropdownContent = this.querySelector(".dropdown-content");
          if (dropdownContent) {
              dropdownContent.style.display = "block";
          }
      });

      // Delay hiding to prevent flickering
      dropdown.addEventListener("mouseleave", function () {
          const dropdownContent = this.querySelector(".dropdown-content");
          if (dropdownContent) {
              timeout = setTimeout(() => {
                  dropdownContent.style.display = "none";
              }, 300);
          }
      });

      // Keep dropdown open when hovering over the menu
      const dropdownContent = dropdown.querySelector(".dropdown-content");
      if (dropdownContent) {
          dropdownContent.addEventListener("mouseenter", function () {
              clearTimeout(timeout);
              this.style.display = "block"; // Keep dropdown open
          });

          dropdownContent.addEventListener("mouseleave", function () {
              timeout = setTimeout(() => {
                  this.style.display = "none";
              }, 300);
          });
      }
  });
});
