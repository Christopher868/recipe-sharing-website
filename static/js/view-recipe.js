// recipe like system
document.addEventListener('DOMContentLoaded', function () {
    const url = window.AppConfig.likeUrl;
    document.querySelectorAll('#like-btn').forEach(button => {
        button.addEventListener('click', function () {
            const recipeId = this.dataset.recipeId
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken,
                    "Content-Type": "application/x-www-form-urlencoded"

                },
                body: `recipe_id=${recipeId}`
            })
                .then(response => {
                    const contentType = response.headers.get('content-type') || '';
                    if (!response.ok || !contentType.includes('application/json')) {
                        throw new Error('Not authenticated');
                    }
                    return response.json();
                })
                .then(data => {
                    this.innerHTML = data.liked
                        ? `Liked <i class="fa-solid fa-thumbs-up"></i>`
                        : `Like <i class="fa-regular fa-thumbs-up"></i>`
                })
                .catch(error => {
                    console.error('Something went wrong', error);
                });
        });
    });
});