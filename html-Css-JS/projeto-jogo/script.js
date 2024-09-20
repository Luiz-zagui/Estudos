const nave = document.getElementById('nave');
const tironave = document.getElementById('tironave');
const tiroOriginal = document.getElementById('tiro'); 


function mostrarTelaFimDeJogo() {
  const telaFimDeJogo = document.getElementById('telaFimDeJogo');
  telaFimDeJogo.style.display = 'block';

  // Esconder outros elementos do jogo (opcional)
  nave.style.display = 'none';
  // ... esconder outros elementos
}


function criarEAnimarTiro() {
  
  const tiroCopia = tiroOriginal.cloneNode(true);


  document.body.appendChild(tiroCopia);

 
  const inimigoRect = inimigo.getBoundingClientRect();
  const tiroRect = tiroCopia.getBoundingClientRect();

  tiroCopia.style.transform = `translateX(${inimigoRect.left - tiroRect.width / 2}px) translateY(${inimigoRect.top}px)`;

 
  tiroCopia.classList.toggle('animacaoInimigo');
  tiroCopia.classList.add('animacaoTiroacao');


  setTimeout(() => {
    document.body.removeChild(tiroCopia);
  }, 2000); 
}

setInterval(criarEAnimarTiro, 6000);


function movimento(event) {

  const distancia = 40;

  if (event.key === 'ArrowLeft') {  
    nave.style.left = parseInt(nave.style.left) -distancia + 'px';
    tironave.style.left = parseInt(tironave.style.left) -distancia + 'px';
  } else if(event.key === 'ArrowRight'){   
    nave.style.left = parseInt(nave.style.left) +distancia + 'px';
    tironave.style.left = parseInt(tironave.style.left) +distancia + 'px';
  }
}

document.addEventListener('keydown', (event) => {
  if (event.code === 'Space') {
    // Seleciona o elemento original
    const tiroNave = document.getElementById('tironave');

    // Clona o elemento
    const novoTiro = tiroNave.cloneNode(true);

    // Posiciona o clone nas mesmas coordenadas do original
    novoTiro.style.top = tiroNave.style.top;
    novoTiro.style.left = tiroNave.style.left;

    // Adiciona a classe de animação
    novoTiro.classList.add('animacaotiroamigo');

    // Adiciona o clone ao corpo do documento
    document.body.appendChild(novoTiro);
  }
});

document.addEventListener('keydown', movimento);

function verificarColisaoComLimite() {
  const tiros = document.querySelectorAll('.animacaoTiroacao');
  const limite = document.getElementById('limite');

  tiros.forEach(tiro => {
    const tiroRect = tiro.getBoundingClientRect();
    const limiteRect = limite.getBoundingClientRect();

    if (
      tiroRect.left < limiteRect.right &&
      tiroRect.right > limiteRect.left &&
      tiroRect.top < limiteRect.bottom &&
      tiroRect.bottom > limiteRect.top
    ) {
      // Colisão detectada!
      mostrarTelaFimDeJogo();
      // Adicione aqui as ações a serem realizadas após a colisão, como mostrar a tela de fim de jogo
      
    }
  });
}

// Chame a função inicialmente (opcional)
setInterval(verificarColisaoComLimite, 0.1);














// ... (código existente)

function checkCollision() {
  const tirosNave = document.querySelectorAll('.animacaotiroamigo');
  const tirosInimigo = document.querySelectorAll('.animacaoTiroacao');

  tirosNave.forEach(tiroNave => {
    tirosInimigo.forEach(tiroInimigo => {
      const tiroNaveRect = tiroNave.getBoundingClientRect();
      const tiroInimigoRect = tiroInimigo.getBoundingClientRect();

      if (
        tiroNaveRect.left < tiroInimigoRect.right &&
        tiroNaveRect.right > tiroInimigoRect.left &&
        tiroNaveRect.top < tiroInimigoRect.bottom &&
        tiroNaveRect.bottom > tiroInimigoRect.top
      ) {
        // Colisão detectada!
        tiroNave.remove();
        tiroInimigo.remove();
      }
    });
  });
}


setInterval(checkCollision, 0.1); 