document.addEventListener('DOMContentLoaded', function () {


    // js to make error messages go away after a 5 seconds
    const errorList = document.querySelector(".errorlist")

    setTimeout(() => {
        errorList.remove()
    }, 5000)
})