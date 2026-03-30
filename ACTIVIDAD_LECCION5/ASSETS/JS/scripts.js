alert("¡Si ves esto, el archivo está bien conectado!");
// 1. Buscamos el botón en el documento (asegúrate de que tu botón tenga id="ir-arriba")
const btn = document.getElementById('ir-arriba');

// Mostrar/Ocultar botón al hacer scroll
window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        btn.style.display = 'block';
    } else {
        btn.style.display = 'none';
    }
});

// Smooth scroll al hacer clic
btn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});