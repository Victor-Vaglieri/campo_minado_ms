# app/logica_jogo.py
def verificar_vitoria(campo, descoberto, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            if campo[i][j] != -1 and (i, j) not in descoberto:
                return False
    return True
