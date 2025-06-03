function cartagena(boton) {
const descripcion = boton.previousElementSibling;
descripcion.textContent += " es un distrito turístico y cultural que se encuentra localizado en el departamento de Bolívar, a orillas del mar Caribe."
boton.disabled = true;
}
function medellin(boton) {
const descripcion = boton.previousElementSibling;
descripcion.textContent += " Es la segunda ciudad más grande de Colombia y sus actividades comerciales e industriales han sido destacadas en el ámbito nacional";
boton.disabled = true;
}

function amazonas(boton) {
const descripcion = boton.previousElementSibling;
descripcion.textContent += " El Amazonas permite descubrir la increíble biodiversidad de la selva tropical más grande del mundo. Es una experiencia única para conectar con la naturaleza, conocer comunidades indígenas y explorar ríos, fauna y paisajes asombrosos.";
boton.disabled = true;
}

function cali(boton){
    const descripcion=boton.previousElementSibling;
    descripcion.textContent += " Es conocida por el baile de la salsa, del que hay muchos clubes en el suburbio de Juanchito. En el barrio más antiguo de Cali, la catedral neoclásica de San Pedro alberga pinturas de la Escuela de Quito";
    boton.disabled=true;
}


function calcularCosto() {
    const destinos = {
        "Cartagena": 250000,
        "Medellín": 200000,
        "Amazonas": 300000,
        "Cali": 350000,
    };

    // Obtener valores de los inputs
    const destino = document.getElementById("destino").value;
    const personas = parseInt(document.getElementById("personas").value);
    const dias = parseInt(document.getElementById("dias").value);

    // Verificar si el destino existe
    if (destinos[destino]) {
        const total = destinos[destino] * personas * dias;
        // Mostrar el resultado
        document.getElementById("resultado").textContent = `Costo total para ${personas} personas por ${dias} días en ${destino}: $${total}`;
    } else {
        document.getElementById("resultado").textContent = "Destino no disponible.";
    }
}


document.getElementById("botoncot").addEventListener("click", function () {
    const cotizador = document.getElementById("cotizador");
    cotizador.classList.toggle("mostrar");
});
