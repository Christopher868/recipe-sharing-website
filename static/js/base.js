document.addEventListener('DOMContentLoaded', function () {

    // js for hiding search bar
    const searchButton = document.querySelector('.search-icon')
    const searchForm = document.querySelector("#search-bar")

    searchButton.addEventListener("click", () => {
        searchForm.classList.toggle("hide")
    });

    // js for changing search input placeholder depending on option selected
    const option = document.querySelector('#select-category')
    const searchInput = document.querySelector('#search-input')

    option.addEventListener("change", (e) => {
        console.log(option.selectedOptions[0].value)
        if (option.selectedOptions[0].value === 'recipe-name') {
            searchInput.setAttribute("placeholder", "Search by Recipe Name");
        } else if (option.selectedOptions[0].value === 'author-name') {
            searchInput.setAttribute("placeholder", "Search by Author");
        }
    })

    // js for hiding account dropdown menu
    const dropdownButton = document.querySelector('.button')
    const dropdown = document.querySelector('.dropdown-content')
    const arrow = document.querySelector('#arrow')

    dropdownButton.addEventListener("click", () => {
        dropdown.classList.toggle("hide")
        if (arrow.classList.contains("down")) {
            arrow.className = 'fas fa-angle-up up'
        } else {
            arrow.className = 'fas fa-angle-down down'
        }
    })

    // js for closing dropdown if a user clicks somewhere else
    document.addEventListener("click", (e) => {
        if (!dropdownButton.contains(e.target) && !dropdown.contains(e.target)) {
            if (!dropdown.classList.contains("hide")) {
                dropdown.classList.toggle("hide")
            }
            if (arrow.classList.contains("up")) {
                arrow.className = 'fas fa-angle-down down'
            }
        }
    })




})