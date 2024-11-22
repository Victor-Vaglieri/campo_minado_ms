import pygame
import sys
from campo import criar_campo
from desenho import desenhar_campo, mostrar_campo_completo,desenhar_tela_final
from logica_jogo import verificar_vitoria

def jogo():
    pygame.init()

    largura = 1000
    altura = 1000
    tam_celula = 200
    linhas = altura // tam_celula
    colunas = largura // tam_celula
    num_minas = 4

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Campo Minado")
    campo = criar_campo(linhas, colunas, num_minas)
    descoberto = set()
    rodando = True

    while rodando:
        desenhar_campo(tela, campo, descoberto, largura, altura, tam_celula)
        if verificar_vitoria(campo, descoberto, linhas, colunas):
            desenhar_tela_final(tela,largura,"Você Venceu!",(17,147,20))
            print("Você Venceu!")
            rodando = False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                linha = y // tam_celula
                coluna = x // tam_celula
                if campo[linha][coluna] == -1:
                    mostrar_campo_completo(campo, tela, largura, altura, tam_celula)
                    desenhar_tela_final(tela,largura,"Você Perdeu!",(255,0,0))
                    print("Você Perdeu!")
                    rodando = False
                else:
                    descoberto.add((linha, coluna))
        pygame.display.flip()
    pygame.quit()
    sys.exit()

jogo()