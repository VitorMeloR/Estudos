let nome = '';
let dataNascimento = '';
const botao = document.getElementById('daysTilBirthday');
const anoAtual = new Date().getUTCFullYear();

function calcularDiasAteAniversario() {
  nome = document.getElementById('name').value;
  dataNascimento = document.getElementById('birthday').value;
  if (!nome.length || !dataNascimento.length) {
    alert('Preencha o seu nome e data de nascimento');
    return;
  }
  const dataNascimentoTipoDate = new Date(dataNascimento);
  const momentoAtual = new Date();
  let proximoAniversarioEhAnoQueVem =
    momentoAtual.getUTCMonth() > dataNascimentoTipoDate.getUTCMonth() ||
    (momentoAtual.getUTCMonth() === dataNascimentoTipoDate.getUTCMonth() &&
      momentoAtual.getUTCDate() < dataNascimentoTipoDate.getUTCDate());

  const proximoAniversario = proximoAniversarioEhAnoQueVem
    ? new Date(
        `${anoAtual + 1}-${
          dataNascimentoTipoDate.getUTCMonth() + 1
        }-${dataNascimentoTipoDate.getUTCDate()}`
      )
    : new Date(
        `${anoAtual}-${
          dataNascimentoTipoDate.getUTCMonth() + 1
        }-${dataNascimentoTipoDate.getUTCDate()}`
      );

  const diasAteProximoAniversario = Math.ceil(
    (proximoAniversario.getTime() - momentoAtual.getTime()) /
      (1000 * 60 * 60 * 24)
  );
  alert(
    `${nome}, seu próximo aniversário é em ${diasAteProximoAniversario} dias`
  );
}

botao.addEventListener('click', calcularDiasAteAniversario);
