function mediaAluno (nota1, nota2, nota3) {
    const mediaAntesPf = (nota1 + nota2+ nota3)/3;
    console.log(`A média desse aluno é: ${mediaAntesPf.toFixed(2)}`);
    if (mediaAntesPf <= 10) {
            console.log(`Aluno em recuperação, precisa de prova final`)
            
    };
    return mediaAntesPf;
};

function mediaAlunoPf (media, notaFinal){
    console.log(`A média final desse aluno é: ${((media+notaFinal)/2).toFixed(2)}`);
};

const media = mediaAluno(1,2,3);
mediaAlunoPf(media, 10);
