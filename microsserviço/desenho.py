import pygame
import random

def desenhar_campo(tela, campo, descoberto, largura, altura, tam_celula):
    tela.fill((0, 0, 0))
    for i in range(altura // tam_celula):
        for j in range(largura // tam_celula):
            retangulo = pygame.Rect(j * tam_celula, i * tam_celula, tam_celula, tam_celula)
            if (i, j) in descoberto:
                pygame.draw.rect(tela, (255, 255, 255), retangulo)
                if campo[i][j] == -1:
                    tela.blit(pygame.transform.scale(pygame.image.load("img/mina"+str(random.randint(1,3))+".png"), (tam_celula, tam_celula)), retangulo)
                elif campo[i][j] > 0:
                    fonte = pygame.font.Font(None, tam_celula)
                    texto = fonte.render(str(campo[i][j]), True, (0, 0, 0))
                    texto_rect = texto.get_rect(center=retangulo.center)
                    tela.blit(texto, texto_rect)
            else:
                pygame.draw.rect(tela, (192, 192, 192), retangulo)

            pygame.draw.rect(tela, (0, 0, 0), retangulo, 2)

def mostrar_campo_completo(campo, tela, largura, altura, tam_celula):
    descoberto = set()
    for i in range(altura // tam_celula):
        for j in range(largura // tam_celula):
            descoberto.add((i, j))
    desenhar_campo(tela, campo, descoberto, largura, altura, tam_celula)
    pygame.display.flip()
    pygame.time.wait(2000)

def desenhar_tela_final(tela,largura,mensagem, cor):
    tela.fill((255,255,255))  # Fundo preto
    largura_texto = len(mensagem) * 20  # Ajusta com base no tamanho do texto
    retangulo = pygame.Rect((largura - largura_texto) // 2, largura // 3, largura_texto, 100)
    pygame.draw.rect(tela, cor, retangulo)
    fonte = pygame.font.Font(None, 48)
    texto = fonte.render(mensagem, True, (0,0,0))
    texto_rect = texto.get_rect(center=retangulo.center)
    tela.blit(texto, texto_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

