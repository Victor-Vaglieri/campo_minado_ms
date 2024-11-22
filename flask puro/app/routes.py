from flask import render_template, jsonify, request
from app import app
from app.campo import criar_campo
from app.logica_jogo import verificar_vitoria

# Variáveis globais
campo = None
descoberto = set()
linhas = 10
colunas = 10
tam_celula = 100
num_minas = 10

@app.route('/')
def home():
    global campo, descoberto
    campo = criar_campo(linhas, colunas, num_minas)
    descoberto = set()
    return render_template('index.html', campo=campo, largura=colunas*tam_celula, altura=linhas*tam_celula)

@app.route('/jogar', methods=['POST'])
def jogar():
    global campo, descoberto
    data = request.get_json()
    linha = data['linha']
    coluna = data['coluna']

    if campo[linha][coluna] == -1:
        # Game Over
        return jsonify({"status": "perdeu", "campo": campo})
    
    descoberto.add((linha, coluna))
    
    if verificar_vitoria(campo, descoberto, linhas, colunas):
        return jsonify({"status": "vitoria", "campo": campo})
    
    return jsonify({"status": "continuar", "campo": campo})
