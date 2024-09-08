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

let nodeDataStore = {};

const visualizeTree = ( node ) => {
    // Si el nodo es null no mostrar
    if (!node) return '';

    const { data, left, right, balance } = node;
    const nodeId = `node_${data.title.replace(/\s+/g, '_').toLowerCase()}`;

    nodeDataStore[nodeId] = node;

    const encodedData = JSON.stringify(node);
    console.log(node)

    return `
            <div class="node__element" onclick='displayData(${nodeId})'> ${data.title} </div>
            <p class="lbl-balance">${balance}</p>
            ${ // En caso de tener un hijo
                left || right ? 
                `
                    <div class="node__vertical-border"></div>
                    <div class="node__children">
                        ${ // Si es el izquierdo reutilizar el llamado
                            left ? (
                            ` 
                                <div class="node node--left">
                                    ${visualizeTree(left)}
                                </div>
                            `
                            ) : ""
                        }
                        ${ // Caso del derecho
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
    `
}

function displayData(nodeId) {
    const movieData = nodeDataStore[nodeId];  // Retrieve the data using the ID
    if (!movieData) return;

    console.log(movieData);
    
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

    movieTitle.textContent = movieData.data.title;
    yearElement.innerHTML = `Year: ${movieData.data.year}`;
    foreignElement.innerHTML = `Foreign Earnings: $${movieData.data.foreign}`;
    domesticElement.innerHTML = `Domestic Earnings: $${movieData.data.domestic}`;
    worldwideElement.innerHTML = `Worldwide Earnings: $${movieData.data.worldwide}`;
    foreignPercentElement.innerHTML = `Foreign Percent Earnings: ${movieData.data.foreign_percent}%`;
    domesticPercentElement.innerHTML = `Domestic Percent Earnings: ${movieData.data.domestic_percent}%`;

    levelElement.innerHTML = `Nivel: ${movieData.level || 'N/A'}`;
    balanceElement.innerHTML = `Balance: ${movieData.balance}`;
    parentElement.innerHTML = `Nodo Padre: ${movieData.parent || 'N/A'}`;
    uncleElement.innerHTML = `Nodo Tio: ${movieData.uncle || 'N/A'}`; 
    grandparentElement.innerHTML = `Nodo Abuelo: ${movieData.grandparent || 'N/A'}`;
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

    const performSearch = document.getElementById('btn-search')
    performSearch.addEventListener('click', function () {
        const flairs = searchInput.value.trim();
        
        loadTreeFromJSON().then(tree => {
            if (tree && tree.root) {
                const filtered = filterBy(tree.root, flairs)

                const treeContainer = document.getElementById('tree')
                treeContainer.innerHTML = '';

                treeContainer.innerHTML += visualizeTree(tree.root)
            }
        });
    });

    const btn = document.getElementById('hide');
    const movieDataContainer = document.querySelector('.movie-data-container');

    btn.onclick = function () {
        movieDataContainer.classList.toggle('active');
        if ( btn.textContent === '>>>') {
            btn.textContent = '<<<'
        } else {
            btn.textContent = '>>>'
        }
    }
}

main();