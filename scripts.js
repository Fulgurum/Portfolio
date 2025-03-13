document.addEventListener("DOMContentLoaded", function () {
    // Highlight menu items on hover
    let menuLinks = document.querySelectorAll(".menu ul li a");
    menuLinks.forEach(link => {
        link.addEventListener("mouseenter", function () {
            this.style.color = "#00ffff";
            this.style.textShadow = "0 0 10px #00ffff";
        });
        link.addEventListener("mouseleave", function () {
            this.style.color = "#ff00ff";
            this.style.textShadow = "none";
        });
    });

    // Load guestbook entries dynamically
    if (document.getElementById("entries")) {
        fetch("/load_guestbook.py")
            .then(response => response.text())
            .then(data => {
                document.getElementById("entries").innerHTML = data;
            })
            .catch(error => console.error("Error loading guestbook entries:", error));
    }
});
