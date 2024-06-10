document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const data = {
        nombre_empresa: document.getElementById('nombre_empresa').value,
        representante_legal: document.getElementById('representante_legal').value,
        direccion: document.getElementById('direccion').value,
        telefono: document.getElementById('telefono').value,
        correo: document.getElementById('correo').value,
        clave: document.getElementById('clave').value
    };

    fetch('/register_empresa', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert(data.message);
            document.getElementById('registerForm').reset();
            var myModalEl = document.getElementById('registerModal');
            var modal = bootstrap.Modal.getInstance(myModalEl);
            modal.hide();
        }
    });
});
