import pygame
import random
import sys

# Configurações do jogo
LARGURA = 1000
ALTURA = 1000
TAM_CELULA = 200
LINHAS = ALTURA // TAM_CELULA
COLUNAS = LARGURA // TAM_CELULA
NUM_MINAS = 6

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (192, 192, 192)
AZUL = (0, 0, 255)
VERDE = (17,145 ,13)
VERMELHO = (255, 0, 0)

# Inicializa o Pygame
pygame.init()

# Tela do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Campo Minado")

# Carregar a imagem da mina

# Função para criar o campo
def criar_campo():
    campo = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
    minas = random.sample(range(LINHAS * COLUNAS), NUM_MINAS)
    
    for mina in minas:
        linha = mina // COLUNAS
        coluna = mina % COLUNAS
        campo[linha][coluna] = -1  # -1 representa uma mina

    for i in range(LINHAS):
        for j in range(COLUNAS):
            if campo[i][j] != -1:
                # Conta as minas vizinhas
                minas_vizinhas = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= i + dx < LINHAS and 0 <= j + dy < COLUNAS:
                            if campo[i + dx][j + dy] == -1:
                                minas_vizinhas += 1
                campo[i][j] = minas_vizinhas
    return campo

# Função para desenhar o campo
def desenhar_campo(campo, descoberto):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            retangulo = pygame.Rect(j * TAM_CELULA, i * TAM_CELULA, TAM_CELULA, TAM_CELULA)
            if (i, j) in descoberto:
                pygame.draw.rect(tela, BRANCO, retangulo)
                if campo[i][j] == -1:
                    # Desenha a imagem da mina
                    tela.blit(pygame.transform.scale(pygame.image.load("mina1.png"), (TAM_CELULA, TAM_CELULA)), retangulo)
                elif campo[i][j] > 0:
                    # Centraliza o texto
                    fonte = pygame.font.Font(None, TAM_CELULA)
                    texto = fonte.render(str(campo[i][j]), True, PRETO)
                    # Posição centralizada
                    texto_rect = texto.get_rect(center=retangulo.center)
                    tela.blit(texto, texto_rect)
            else:
                pygame.draw.rect(tela, CINZA, retangulo)

            pygame.draw.rect(tela, PRETO, retangulo, 2)

# Função para desenhar a tela de vitória ou derrota
def desenhar_tela_final(mensagem, cor):
    tela.fill(BRANCO)  # Fundo preto
    largura_texto = len(mensagem) * 20  # Ajusta com base no tamanho do texto
    retangulo = pygame.Rect((LARGURA - largura_texto) // 2, ALTURA // 3, largura_texto, 100)
    pygame.draw.rect(tela, cor, retangulo)
    fonte = pygame.font.Font(None, 48)
    texto = fonte.render(mensagem, True, BRANCO)
    texto_rect = texto.get_rect(center=retangulo.center)
    tela.blit(texto, texto_rect)
    pygame.display.flip()

# Função para mostrar o campo após o fim do jogo
def mostrar_campo_completo(campo):
    descoberto = set()
    for i in range(LINHAS):
        for j in range(COLUNAS):
            descoberto.add((i, j))
    desenhar_campo(campo, descoberto)
    pygame.display.flip()

# Função para verificar se o jogador ganhou
def verificar_vitoria(campo, descoberto):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if campo[i][j] != -1 and (i, j) not in descoberto:
                return False  # Se houver uma célula não-minada ainda não descoberta, o jogador não venceu
    return True  # O jogador venceu se todas as células não-minadas forem descobertas

# Função principal do jogo
def jogo():
    campo = criar_campo()
    descoberto = set()
    rodando = True

    while rodando:
        tela.fill(PRETO)

        # Desenha o campo
        desenhar_campo(campo, descoberto)

        # Verifica vitória
        if verificar_vitoria(campo, descoberto):
            desenhar_tela_final("Você Venceu!", VERDE)
            pygame.time.wait(3000)  # Aguarda 3 segundos antes de fechar

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                linha = y // TAM_CELULA
                coluna = x // TAM_CELULA

                if campo[linha][coluna] == -1:
                    mostrar_campo_completo(campo)
                    pygame.time.wait(2000)
                    desenhar_tela_final("Você Perdeu!", VERMELHO)
                    pygame.display.flip()  # Atualiza a tela
                    pygame.time.wait(2000)  # Aguarda 3 segundos antes de fechar
                else:
                    descoberto.add((linha, coluna))

        # Atualiza a tela
        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Inicia o jogo
jogo()
