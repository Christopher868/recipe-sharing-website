
// js  for removing informative messages after a given amount of time
setTimeout(() => {
    const messages = document.querySelectorAll(".messages");
    messages.forEach((message) => {
        message.style.transition = "opacity 2s";
        message.style.opacity = "0";
        setTimeout(() => message.remove(), 2000);
    });
}, 5000);

document.addEventListener('DOMContentLoaded', function () {

    // js for hiding search bar
    const searchButton = document.querySelector('.search-icon')
    const searchForm = document.querySelector("#search-bar")

    if (searchButton) {
        searchButton.addEventListener("click", () => {
            searchForm.classList.toggle("hide")
        });
    }

    // js for changing search input placeholder depending on option selected
    const option = document.querySelector('#select-category')
    const searchInput = document.querySelector('#search-input')

    if (option) {
        option.addEventListener("change", (e) => {
            console.log(option.selectedOptions[0].value)
            if (option.selectedOptions[0].value === 'recipe-name') {
                searchInput.setAttribute("placeholder", "Search by Recipe Name");
            } else if (option.selectedOptions[0].value === 'author-name') {
                searchInput.setAttribute("placeholder", "Search by Recipe Author");
            }
        })
    }
    // js for hiding account dropdown menu and changing arrow direction

    const dropdownButton = document.querySelector('.button')
    const dropdown = document.querySelector('.dropdown-content')
    const arrow = document.querySelector('#arrow')

    if (dropdownButton) {
        dropdownButton.addEventListener("click", () => {
            dropdown.classList.toggle("hide")
            if (arrow.classList.contains("down")) {
                arrow.className = 'fas fa-angle-up up'
            } else {
                arrow.className = 'fas fa-angle-down down'
            }
        })

        // js for closing dropdown or search bar if a user clicks somewhere else
        document.addEventListener("click", (e) => {
            if (!dropdownButton.contains(e.target) && !dropdown.contains(e.target)) {
                if (!dropdown.classList.contains("hide")) {
                    dropdown.classList.toggle("hide")
                }
                if (arrow.classList.contains("up")) {
                    arrow.className = 'fas fa-angle-down down'
                }
            }
            if (!searchForm.contains(e.target) && !searchButton.contains(e.target)) {
                if (!searchForm.classList.contains("hide")) {
                    searchForm.classList.toggle("hide")
                }
            }
        })
    }
    // js for hiding and displaying contact form
    const contactDropdownButton = document.querySelector('#contact-dropdown-button')
    const contactForm = document.querySelector('#contact-form')
    if (contactDropdownButton) {
        contactDropdownButton.addEventListener("click", () => {
            contactForm.classList.toggle("hide")
        })
    }

})
