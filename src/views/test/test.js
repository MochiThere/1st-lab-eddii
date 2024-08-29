fetch('data.json')
    .then(res => res.json())
    .then(data => {
        console.log(data);
        document.body.innerHTML += `<p>${data.title}</p>`
    })
    .catch(error => console.error('Error:', error ));