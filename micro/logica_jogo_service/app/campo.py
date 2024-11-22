import random

def criar_campo(linhas, colunas, num_minas):
    campo = [[0 for _ in range(colunas)] for _ in range(linhas)]
    minas = random.sample(range(linhas * colunas), num_minas)
    
    for mina in minas:
        linha = mina // colunas
        coluna = mina % colunas
        campo[linha][coluna] = -1  # -1 representa uma mina

    for i in range(linhas):
        for j in range(colunas):
            if campo[i][j] != -1:
                minas_vizinhas = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= i + dx < linhas and 0 <= j + dy < colunas:
                            if campo[i + dx][j + dy] == -1:
                                minas_vizinhas += 1
                campo[i][j] = minas_vizinhas
    return campo
