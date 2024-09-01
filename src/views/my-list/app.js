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


async function loadTreeFromJSON () {
    try {
        // Leer el archivo JSON 
        const res = await fetch('../../resources/data.json');

        // Si no se puede cargar; mandar error
        if (!res.ok) {
            console.log("ERROR CARGANDO");
        }

        // Devolver el objeto 
        const tree = await res.json();
        return tree;
        
    }  catch ( error ) {
        // En caso de un error inesperado
        console.error('Error:', error);
        return null;
    }
}


const visualizeTree = ( node ) => {
    // Si el nodo es null no mostrar
    if (!node) return '';

    const { data, left, right } = node;

    return `
            <div class="node__element"> ${data} </div>
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

const visualTree = (node) => {
    if (!node) return '';

    const { data, left, right } = node;

    return `
        <div class="node">
            <div class="node__element">${data}</div>
            ${left || right ? 
            `
                <div class="node__vertical-border"></div>
                <div class="node__children">
                    ${left ? (
                        `<div class="node">
                            ${visualizeTree(left)}
                        </div>`
                    ) : ""}
                    ${right ? (
                        `<div class="node">
                            ${visualizeTree(right)}
                        </div>`
                    ) : ""}
                </div>
            ` : ""}
        </div>
    `;
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
}

main();