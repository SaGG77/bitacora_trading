const filtro = document.querySelector('#filtroActivo');
const filas = document.querySelectorAll('#tablaTrades tbody tr');

if (filtro) {
  filtro.addEventListener('input', (event) => {
    const valor = event.target.value.trim().toUpperCase();

    filas.forEach((fila) => {
      const activo = fila.querySelector('.activo')?.textContent.toUpperCase() ?? '';
      fila.style.display = activo.includes(valor) ? '' : 'none';
    });
  });
}
