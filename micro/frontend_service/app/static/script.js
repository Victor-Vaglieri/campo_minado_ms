function clicar(linha, coluna) {
    let celula = document.getElementById(`celula_${linha}_${coluna}`);
    console.log(linha,coluna);
    if (celula.classList.contains('revelada')) {
        return; // Não faz nada se a célula já foi revelada
    }
    celula.classList.add('revelada');

    fetch('http://127.0.0.1:5000/jogar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ linha: linha, coluna: coluna })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro HTTP: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log("Resposta JSON:", data);
        let status = data.status;
        let campo = data.campo;

        if (status === "vitoria") {
            alert("Você venceu!");
        } else if (status === "perdeu") {
            setTimeout(() => {
                alert("Você perdeu!");
                revelarCampo(campo);
                reiniciarJogo();
            }, 1000);
        } else {
            atualizarCampo(campo, linha, coluna);
        }
    })
    .catch(error => console.error('Erro na requisição:', error));
}

async function atualizarCampo(campo, linha, coluna) {
    let celula = document.getElementById(`celula_${linha}_${coluna}`);

    if (campo[linha][coluna] === -1) {
        // Exibe a bomba
        celula.classList.add('mina');
    } else {
        celula.innerText = campo[linha][coluna];
        celula.classList.remove('X'); // Remove a classe X após o clique
    }
}

async function revelarCampo(campo) {
    for (let i = 0; i < campo.length; i++) {
        for (let j = 0; j < campo[i].length; j++) {
            let celula = document.getElementById(`celula_${i}_${j}`);
            if (campo[i][j] === -1) {
                // Exibe as minas
                celula.classList.add('mina');
            } else {
                celula.innerText = campo[i][j];
                celula.classList.remove('X');
            }
            celula.classList.add('revelada');
        }
    }
}

async function reiniciarJogo() {
    setTimeout(() => {
        // Reinicia o campo (recarrega a página ou faz outra lógica de reinício)
        location.reload(); // Recarrega a página para reiniciar o jogo
    }, 2000); // Atraso de 2 segundos antes de reiniciar
}

document.addEventListener("DOMContentLoaded", function() {
    const campoElement = document.getElementById('campo');
    const colunas = parseInt(campoElement.getAttribute('data-colunas'));
    const linhas = parseInt(campoElement.getAttribute('data-linhas'));
    
    const campo = document.querySelector('.campo');
    campo.style.gridTemplateColumns = `repeat(${colunas}, 100px)`;
    campo.style.gridTemplateRows = `repeat(${linhas}, 100px)`;
});
