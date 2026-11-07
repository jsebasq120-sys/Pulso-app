class PulsoController {
    static async inicializarDashboard() {
        await this.actualizarVistas();
        this.configurarEventosFormularios();
    }

    static async actualizarVistas() {
        // 1. Cargar Jugadores
        let jugadores = await PulsoModel.getJugadores();
        let tbodyJ = document.querySelector('#tabla-jugadores tbody');
        if (tbodyJ) {
            tbodyJ.innerHTML = jugadores.map(j => `
                <tr>
                    <td>${j.id}</td>
                    <td><b>#${j.numero_camiseta}</b></td>
                    <td>${j.nombre}</td>
                    <td>${j.posicion}</td>
                    <td>${j.edad} años</td>
                </tr>
            `).join('');
        }

        // 2. Cargar Mediciones
        let mediciones = await PulsoModel.getMediciones();
        let tbodyM = document.querySelector('#tabla-mediciones tbody');
        if (tbodyM) {
            tbodyM.innerHTML = mediciones.map(m => `
                <tr>
                    <td>${m.jugador}</td>
                    <td>${m.frecuencia_cardiaca} BPM</td>
                    <td>${m.fatiga_nivel} / 5</td>
                    <td>${m.velocidad_maxima} km/h</td>
                    <td>${m.fecha_registro}</td>
                </tr>
            `).join('');
        }

        // 3. Cargar Pruebas Físicas
        let pruebas = await PulsoModel.getPruebasFisicas();
        let tbodyP = document.querySelector('#tabla-pruebas tbody');
        if (tbodyP) {
            tbodyP.innerHTML = pruebas.map(p => `
                <tr>
                    <td>${p.jugador}</td>
                    <td>${p.tipo_prueba}</td>
                    <td><b>${p.resultado}</b></td>
                    <td>${p.fecha}</td>
                </tr>
            `).join('');
        }
    }

    static configurarEventosFormularios() {
        // Formulario Jugador
        const formJugador = document.getElementById('form-jugador');
        if (formJugador) {
            formJugador.addEventListener('submit', async (e) => {
                e.preventDefault();
                let nuevoJ = {
                    nombre: document.getElementById('j-nombre').value,
                    posicion: document.getElementById('j-posicion').value,
                    edad: parseInt(document.getElementById('j-edad').value),
                    numero_camiseta: parseInt(document.getElementById('j-dorsal').value),
                    usuario_id: 1
                };
                let res = await PulsoModel.crearJugador(nuevoJ);
                if (res.status === 'success') {
                    alert("¡Jugador registrado con éxito!");
                    formJugador.reset();
                    this.actualizarVistas();
                } else {
                    alert("Error al registrar jugador.");
                }
            });
        }

        // Formulario Medición
        const formMedicion = document.getElementById('form-medicion');
        if (formMedicion) {
            formMedicion.addEventListener('submit', async (e) => {
                e.preventDefault();
                let nuevaM = {
                    jugador_id: parseInt(document.getElementById('m-jugador-id').value),
                    frecuencia_cardiaca: parseInt(document.getElementById('m-fc').value),
                    fatiga_nivel: parseInt(document.getElementById('m-fatiga').value),
                    velocidad_maxima: parseFloat(document.getElementById('m-vel').value)
                };
                let res = await PulsoModel.crearMedicion(nuevaM);
                if (res.status === 'success') {
                    alert("¡Medición registrada con éxito!");
                    formMedicion.reset();
                    this.actualizarVistas();
                } else {
                    alert("Error al registrar medición.");
                }
            });
        }

        // Formulario Prueba Física
        const formPrueba = document.getElementById('form-prueba');
        if (formPrueba) {
            formPrueba.addEventListener('submit', async (e) => {
                e.preventDefault();
                let nuevaP = {
                    jugador_id: parseInt(document.getElementById('p-jugador-id').value),
                    tipo_prueba: document.getElementById('p-tipo').value,
                    resultado: parseFloat(document.getElementById('p-resultado').value)
                };
                let res = await PulsoModel.crearPruebaFisica(nuevaP);
                if (res.status === 'success') {
                    alert("¡Prueba física guardada con éxito!");
                    formPrueba.reset();
                    this.actualizarVistas();
                } else {
                    alert("Error al guardar prueba física.");
                }
            });
        }
    }
}