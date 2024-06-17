document.addEventListener('DOMContentLoaded', function () {
    const precioHastaInput = document.getElementById('precioHasta');

    precioHastaInput.addEventListener('input', function () {
        if (parseFloat(precioHastaInput.value) < 0) {
            precioHastaInput.value = '0';
        }
    });

    const precioDesdeInput = document.getElementById('precioDesde');

    precioDesdeInput.addEventListener('input', function () {
        if (parseFloat(precioDesdeInput.value) < 0) {
            precioDesdeInput.value = '0';
        }
    });

    const form = document.getElementById('jugadorBusquedaForm');

    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            let nombre = document.getElementById('jugador').value;
            let equipo = document.getElementById('equipo').value;
            let posicion = document.getElementById('posicion').value;
            let min = document.getElementById('precioDesde').value;
            let max = document.getElementById('precioHasta').value;

            if (nombre === 'Nombre jugador') {
                nombre = '';
            }
            if (equipo === 'Elija un equipo') {
                equipo = '';
            }
            if (posicion === 'Elija posición') {
                posicion = '';
            }
            console.log(posicion, min, max, nombre, equipo);
        });
    }

    function cargarContenido(contenedor, url) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                if (xhr.status == 200) {
                    contenedor.innerHTML = xhr.responseText;
                } else {
                    console.error('Error en la solicitud:', xhr.status);
                }
            }
        };
        xhr.open('GET', url, true);
        xhr.send();
    }
    
    const tabla = document.getElementById('tablaJugadores');
    tabla.addEventListener('click', function(e){
        var fila = e.target.closest("tr");
        if (fila) {
            var datosFila = Array.from(fila.children).map(td => td.textContent); // los datos de una fila en un array
            console.log(datosFila[2]);
            let contenedor = document.getElementById('contenedorJugador');
            if(datosFila[2].toLowerCase() =="defensa central"){

                cargarContenido(contenedor,'verJugadores/defensa');
                
                // aquiva lo de actualiza las estadisticas
                
            } else if(datosFila[2].toLowerCase() =="delantero centro"){
                cargarContenido(contenedor,'verJugadores/delantero');
            } else if(datosFila[2].toLowerCase() == "extremo derecho"){
                cargarContenido(contenedor,'verJugadores/extremoDer');
            } else if(datosFila[2].toLowerCase() == "extremo izquierdo"){
                cargarContenido(contenedor,'verJugadores/extremoIzq');
            } else if (datosFila[2].toLowerCase() == "lateral derecho"){
                cargarContenido(contenedor,'verJugadores/lateralDer');
            } else if (datosFila[2].toLowerCase() == "lateral izquierdo"){
                cargarContenido(contenedor,'verJugadores/lateralIzq');
            } else if (datosFila[2].toLowerCase() == "mediapunta"){
                cargarContenido(contenedor,'verJugadores/mediaPunta');
            } else if (datosFila[2].toLowerCase() == "mediocentro ofensivo"){
                cargarContenido(contenedor,'verJugadores/medioCampOf');
            } else if (datosFila[2].toLowerCase() == "pivote"){
                cargarContenido(contenedor,'verJugadores/pivote');
            } else if (datosFila[2].toLowerCase() == "portero"){
                cargarContenido(contenedor,'verJugadores/portero');
            } else if (datosFila[2].toLowerCase() == "mediocentro"){
                cargarContenido(contenedor,'verJugadores/medioCemp');
            }
        }
    });
});
