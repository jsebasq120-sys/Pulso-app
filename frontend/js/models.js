const API_URL = 'http://127.0.0.1:8000';

class PulsoModel {
    static async getJugadores() {
        let res = await fetch(`${API_URL}/jugadores`);
        let data = await res.json();
        return data.jugadores || [];
    }

    static async crearJugador(jugadorData) {
        let res = await fetch(`${API_URL}/jugadores`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(jugadorData)
        });
        return await res.json();
    }

    static async getMediciones() {
        let res = await fetch(`${API_URL}/mediciones`);
        let data = await res.json();
        return data.mediciones || [];
    }

    static async crearMedicion(medicionData) {
        let res = await fetch(`${API_URL}/mediciones`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(medicionData)
        });
        return await res.json();
    }

    static async getPruebasFisicas() {
        let res = await fetch(`${API_URL}/pruebas-fisicas`);
        let data = await res.json();
        return data.pruebas_fisicas || [];
    }

    static async crearPruebaFisica(pruebaData) {
        let res = await fetch(`${API_URL}/pruebas-fisicas`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(pruebaData)
        });
        return await res.json();
    }
}