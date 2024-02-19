function valorComImposto (valor) {
    const valorDoImposto = (valor*8.875)/100
    const valorFinal = valor + valorDoImposto
    console.log(`O valor a ser pago é R$${valorFinal.toFixed(2)}`);
};

valorComImposto(150);