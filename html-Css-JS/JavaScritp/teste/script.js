let elemento = document.getElementById('meuElemento');
let posicao = 0;
let limiteEsquerdo = 0;
let limiteDireito = 400; // Ajuste de acordo com a largura da área

function moverElemento(direcao) {
  if (direcao === 'esquerda' && posicao > limiteEsquerdo) {
    posicao--;
  } else if (direcao === 'direita' && posicao < limiteDireito) {
    posicao++;
  }
  elemento.style.left = posicao + 'px';
}

document.addEventListener('keydown', (event) => {
  if (event.key === 'ArrowLeft') {
    moverElemento('esquerda');
  } else if (event.key === 'ArrowRight') {
    moverElemento('direita');
  }
});