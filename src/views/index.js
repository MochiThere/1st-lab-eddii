const API_KEY = "sssssss";
const BASE_URL = 'http://www.omdbapi.com/';

async function getMoviePoster(title) {
    try {
        // Hacer la petición a la API
        const response = await fetch(`${BASE_URL}?t=${encodeURIComponent(title)}&apikey=${API_KEY}`);
        const data = await response.json();

        // Si encuentra la película en la API
        if (data.Response === "True") {
            // Actualizar el nombre y el poster
            document.getElementById('movie-name').textContent = data.Title;
            const posterUrl = data.Poster;

            if (posterUrl && posterUrl !== "N/A") {
                const imgElement = document.getElementById('poster');
                imgElement.src = posterUrl;
                imgElement.alt = data.Title;
            } else {
                document.getElementById('poster').alt = 'Poster not registered';
            }
        } else {
            document.getElementById('movie-name').textContent = title;
            document.getElementById('poster').alt = 'No poster available';
        }
    } catch (error) {
        console.error('Error fetching movie data:', error);
    }
}

function changeTo(){
    window.location.href = '../main-page/main-page.html';
}

function toProfiles(){
    window.location.href = '../profiles/profiles.html';
}

function toMyList(){
    window.location.href = '../my-list/my-list.html';
}

// ========================================================================
const carousel = document.querySelector('.carousel');
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

let scrollPosition = 0;

prevButton.addEventListener('click', () => {
    scrollPosition -= carousel.clientWidth;
    if (scrollPosition < 0) {
        scrollPosition = carousel.scrollWidth - carousel.clientWidth;
    }
    carousel.style.transform = `translateX(-${scrollPosition}px)`;
});

nextButton.addEventListener('click', () => {
    scrollPosition += carousel.clientWidth;
    if (scrollPosition >= carousel.scrollWidth) {
        scrollPosition = 0;
    }
    carousel.style.transform = `translateX(-${scrollPosition}px)`;
});