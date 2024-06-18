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

    function cargarContenido(contenedor, url, id) {
        var xhr = new XMLHttpRequest();
        let urlConMensaje = url + '?id=' + encodeURIComponent(id);
        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                if (xhr.status == 200) {
                    contenedor.innerHTML = xhr.responseText;
                    
                } else {
                    console.error('Error en la solicitud:', xhr.status);
                }
            }
        };
        xhr.open('GET', urlConMensaje, true);
        xhr.send();
    }
    
    const tabla = document.getElementById('tablaJugadores');
    tabla.addEventListener('click', function(e){
        var fila = e.target.closest("tr");
        if (fila) {
            var datosFila = Array.from(fila.children).map(td => td.textContent); // los datos de una fila en un array
            console.log(datosFila[0]," ",datosFila[1]);
            let id = datosFila[0];
            let contenedor = document.getElementById('contenedorJugador');
            switch(datosFila[2].toLowerCase()) {
                case "defensa central":
                    cargarContenido(contenedor, 'verJugadores/defensa', String(id));
                    break;
                case "delantero centro":
                    cargarContenido(contenedor, 'verJugadores/delantero', String(id));
                    break;
                case "extremo derecho":
                    cargarContenido(contenedor, 'verJugadores/extremoDer', String(id));
                    break;
                case "extremo izquierdo":
                    cargarContenido(contenedor, 'verJugadores/extremoIzq', String(id));
                    break;
                case "lateral derecho":
                    cargarContenido(contenedor, 'verJugadores/lateralDer', String(id));
                    break;
                case "lateral izquierdo":
                    cargarContenido(contenedor, 'verJugadores/lateralIzq', String(id));
                    break;
                case "mediapunta":
                    cargarContenido(contenedor, 'verJugadores/mediaPunta', String(id));
                    break;
                case "mediocentro ofensivo":
                    cargarContenido(contenedor, 'verJugadores/medioCampOf', String(id));
                    break;
                case "pivote":
                    cargarContenido(contenedor, 'verJugadores/pivote', String(id));
                    break;
                case "portero":
                    cargarContenido(contenedor, 'verJugadores/portero', String(id));
                    break;
                case "mediocentro":
                    cargarContenido(contenedor, 'verJugadores/medioCemp', String(id));
                    break;
                default:
                    console.error('Posición no reconocida:', datosFila[2]);
            }
            
        }
    });
});
