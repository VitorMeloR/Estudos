console.log('Resultado do ex01:')
const primeiraVariavel = 2148;
let segundaVariavel;


 console.log(`O valor da minha primeira variavel é: ${primeiraVariavel}`);

 segundaVariavel = 500

console.log(`O valor da minha segunda variavel é: ${segundaVariavel}`);

console.log(`A soma das duas Variaveis é ${primeiraVariavel+segundaVariavel}`);

console.log(`Minha segunda variavel elevado a 2 é: ${segundaVariavel**2}`);

console.log(`Minha segunda variavel divido por 3 é: ${(segundaVariavel/3).toFixed(2)}`);

console.log('Resultado do ex02:');
const variavelTrue = true;
const variavelFalse = false;

console.log('Teste de booleano entre varivaleTrue e variavelFasle.');
console.log(`Metodo AND: ${variavelTrue && variavelFalse}`);
console.log(`Metodo OR: ${variavelTrue || variavelFalse}`);

const variavelTrue1 = true;

console.log('Teste de booleano entre varivaleTrue, variavelFasle e variavelTrue1.');
console.log(`Metodo AND: ${variavelTrue && variavelFalse && variavelTrue1}`);
console.log(`Metodo OR: ${variavelTrue || variavelFalse || variavelTrue1}`);