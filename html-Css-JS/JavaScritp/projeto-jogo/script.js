function arrowleft(event) {
  const div = document.getElementById('nave');
  const distancia = 10;

  if (event.key === 'ArrowLeft') {
    div.style.left = parseInt(div.style.left) - distancia + 'px';
  } else if (event.key === 'ArrowRight') {
    div.style.left = parseInt(div.style.left) + distancia + 'px';
  }
}

function inimig(event) {
  const ini1 = document.getElementById('inimigo');
  const distancia = 10;

  if (event.key === 'd') {
    ini1.style.left = parseInt(ini1.style.left) - distancia + 'px';
  } else if (event.key === 'a') {
    ini1.style.left = parseInt(ini1.style.left) + distancia + 'px';
  }
}

// Adicionando o event listener para a função inimigo
document.addEventListener('keydown', arrowleft);
document.addEventListener('keydown', inimig);









