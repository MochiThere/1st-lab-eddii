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
// ========================================================================