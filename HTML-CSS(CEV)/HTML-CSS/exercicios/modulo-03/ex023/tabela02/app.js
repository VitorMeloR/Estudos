   // script feito em chatgpt, pois ainda não tenho capacidade de conseguir fazer isso em JavaScript, estou começando a aprender esse linguagem, apenas quis fazer um teste neste exercício, por isso a ajuda do chatgpt
   let elementos = document.querySelectorAll('.num');

   let soma = 0;

   elementos.forEach(function(elemento) {
    const elementoTratado = elemento.innerHTML.replace(/\./g, '')
     
    soma += parseInt(elementoTratado);
   });

   const resultado = soma.toLocaleString('pt-BR');
   document.getElementById('resultado').innerHTML = resultado;