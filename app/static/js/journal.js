const filters = {
  fecha: document.querySelector('#filterFecha'),
  activo: document.querySelector('#filterActivo'),
  direccion: document.querySelector('#filterDireccion'),
  emocion: document.querySelector('#filterEmocion'),
  tipo: document.querySelector('#filterTipoEntrada'),
};

function applyFilters() {
  const rows = document.querySelectorAll('#tradeTable tbody tr');
  rows.forEach((row) => {
    const okFecha = !filters.fecha?.value || row.dataset.fecha === filters.fecha.value;
    const okActivo = !filters.activo?.value || row.dataset.activo.toLowerCase().includes(filters.activo.value.toLowerCase());
    const okDireccion = !filters.direccion?.value || row.dataset.direccion === filters.direccion.value;
    const okEmocion = !filters.emocion?.value || row.dataset.emocion.toLowerCase().includes(filters.emocion.value.toLowerCase());
    const okTipo = !filters.tipo?.value || row.dataset.tipo.toLowerCase().includes(filters.tipo.value.toLowerCase());
    row.style.display = okFecha && okActivo && okDireccion && okEmocion && okTipo ? '' : 'none';
  });
}

Object.values(filters).forEach((el) => el?.addEventListener('input', applyFilters));

document.querySelector('#clearFilters')?.addEventListener('click', () => {
  Object.values(filters).forEach((el) => { if (el) el.value = ''; });
  applyFilters();
});

const tradeFormModal = document.querySelector('#tradeFormModal');
tradeFormModal?.addEventListener('show.bs.modal', (event) => {
  const btn = event.relatedTarget;
  const title = document.querySelector('#tradeFormTitle');
  const idField = document.querySelector('#tradeId');
  const form = document.querySelector('#tradeForm');
  form.reset();
  idField.value = '';
  title.textContent = 'Nuevo trade';

  if (btn?.classList.contains('edit-btn')) {
    title.textContent = 'Editar trade';
    Object.entries(btn.dataset).forEach(([key, value]) => {
      const input = document.querySelector(`#${key}`);
      if (input) input.value = value;
    });
    idField.value = btn.dataset.id;
  }
});

const detailModal = document.querySelector('#tradeDetailModal');
detailModal?.addEventListener('show.bs.modal', (event) => {
  const btn = event.relatedTarget;
  const comentario = document.querySelector('#detailComentario');
  const captura = document.querySelector('#detailCaptura');
  const capturaEmpty = document.querySelector('#detailCapturaEmpty');

  comentario.textContent = btn?.dataset.comentario || 'Sin comentario';
  if (btn?.dataset.captura) {
    captura.href = btn.dataset.captura;
    captura.classList.remove('d-none');
    capturaEmpty.classList.add('d-none');
  } else {
    captura.classList.add('d-none');
    capturaEmpty.classList.remove('d-none');
  }
});
