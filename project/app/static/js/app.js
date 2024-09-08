const draggable = document.querySelector('.draggable');
const content = document.querySelector('.tree-container');

const searchInput = document.getElementById("search-input")
const dropdownList = document.querySelector('.dropdown-list');

let isDragging = false;
let initial = { x: 0, y: 0 };
let offset = { x: 0, y: 0 };
let scale = 1

draggable.addEventListener('mousedown', (e) => {
    isDragging = true;

    offset.x = e.clientX - content.offsetLeft;
    offset.y = e.clientY - content.offsetTop;
});

draggable.addEventListener('mousemove', (e) => {
    if (isDragging) {
        initial.x = e.clientX - offset.x;
        initial.y = e.clientY - offset.y;
        content.style.left = `${initial.x}px`;
        content.style.top = `${initial.y}px`;
    }
});

draggable.addEventListener('mouseup', () => {
    isDragging = false;
});

draggable.addEventListener('mouseleave', () => {
    isDragging = false;
});

content.addEventListener('wheel', (e) => {
    e.preventDefault();

    if (e.deltaY < 0) {
        // Acercar
        scale *= 1.1;
    } else {
        // Alejar
        scale /= 1.1;
    }

    content.style.transform = `scale(${scale})`;
});

document.addEventListener('click', function(event) {
    if (!dropdownList.contains(event.target) && event.target !== searchInput) {
      dropdownList.style.display = 'none';
    }
  });

searchInput.addEventListener('focus', () => {
    dropdownList.style.display = 'block';
});

const options = document.querySelectorAll('.dropdown-list ul li');
options.forEach(option => {
  option.addEventListener('click', function() {
    const bubbleText = this.querySelector('.bubble').textContent.trim();
    
    const keyword = bubbleText.split(':')[0].trim() + ":";
    
    searchInput.value = searchInput.value + keyword;
    
    dropdownList.style.display = 'none';
  });
});


const visualizeTree = (node) => {
    // Si el nodo es null no mostrar
    if (!node) return '';

    const { data, left, right, balance, level, parent, uncle, grandparent } = node;
    console.log(data)

    // Encode the full node data, including level, parent, uncle, and grandparent
    const encodedData = JSON.stringify({ ...data, level, parent, uncle, grandparent });

    return `
        <div class="node__element" onclick='displayData(${encodedData},${balance})'> ${data.title} </div>
        <p class="lbl-balance">${balance}</p>
        ${
            // En caso de tener un hijo
            left || right ?
            `
                <div class="node__vertical-border"></div>
                <div class="node__children">
                    ${
                        // Si es el izquierdo reutilizar el llamado
                        left ? (
                        `
                            <div class="node node--left">
                                ${visualizeTree(left)}
                            </div>
                        `
                        ) : ""
                    }
                    ${
                        // Caso del derecho
                        right ? (
                        `
                            <div class="node node--right">
                                ${visualizeTree(right)}
                            </div>
                        `
                        ) : ""
                    }
                </div>
            `
            : ""
        }
    `;
}

function displayData(movieData, balance) {
    const movieTitle = document.getElementById('movie-title');
    const yearElement = document.querySelector('.movie-info li:nth-child(1)');
    const foreignElement = document.querySelector('.movie-info li:nth-child(2)');
    const domesticElement = document.querySelector('.movie-info li:nth-child(3)');
    const worldwideElement = document.querySelector('.movie-info li:nth-child(4)');
    const foreignPercentElement = document.querySelector('.movie-info li:nth-child(5)');
    const domesticPercentElement = document.querySelector('.movie-info li:nth-child(6)');

    const levelElement = document.querySelector('.node-info li:nth-child(1)');
    const balanceElement = document.querySelector('.node-info li:nth-child(2)');
    const parentElement = document.querySelector('.node-info li:nth-child(3)');
    const uncleElement = document.querySelector('.node-info li:nth-child(4)');
    const grandparentElement = document.querySelector('.node-info li:nth-child(5)');

    movieTitle.textContent = movieData.title;
    yearElement.innerHTML = `Year: ${movieData.year}`;
    foreignElement.innerHTML = `Foreign Earnings: $${movieData.foreign}`;
    domesticElement.innerHTML = `Domestic Earnings: $${movieData.domestic}`;
    worldwideElement.innerHTML = `Worldwide Earnings: $${movieData.worldwide}`;
    foreignPercentElement.innerHTML = `Foreign Percent Earnings: ${movieData.foreign_percent}%`;
    domesticPercentElement.innerHTML = `Domestic Percent Earnings: ${movieData.domestic_percent}%`;

    levelElement.innerHTML = `Level: ${movieData.level}`;
    balanceElement.innerHTML = `Balance: ${balance}`;
    parentElement.innerHTML = `Parent Node: ${movieData.parent || 'N/A'}`;
    uncleElement.innerHTML = `Uncle Node: ${movieData.uncle || 'N/A'}`;
    grandparentElement.innerHTML = `Grandparent Node: ${movieData.grandparent || 'N/A'}`;
}

async function main() {
    const rootNode = await loadTreeFromJSON();

    // Si el objeto existe, cargar el árbol
    if (rootNode) {
        const treeContainer = document.getElementById('tree');
        treeContainer.innerHTML = visualizeTree(rootNode.root);
    } else {
        console.error('No se pudo cargar el árbol AVL.');
    }

    const btn = document.getElementById('hide');
    const movieDataContainer = document.querySelector('.movie-data-container');

    btn.onclick = function () {
        movieDataContainer.classList.toggle('active');

        if (movieDataContainer.classList.contains('active')) {
            btn.textContent = '<<<'
        } else {
            btn.textContent = '>>>'
        }
    }

    const deleteButton = document.getElementById('delete-node');
    deleteButton.addEventListener('click', async function () {
        const movieTitle = document.getElementById('movie-title').textContent;
        
        try {
            const res = await fetch('/my-list', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({title: movieTitle, action:'delete'}),
            });

            if ( !res.ok ){
                console.error('Error enviando el titulo a eliminar')
            }

            treeContainer.innerHTML = visualizeTree(rootNode.root);
        } catch ( error ) {
            console.error('ERROR:', error);
        }
    });

}

main();