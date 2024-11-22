from flask import jsonify, request
from app import app
from .campo import criar_campo
from .logica_jogo import verificar_vitoria

# Variáveis globais
campo = None
descoberto = set()
linhas = 5
colunas = 5
num_minas = 8

@app.route('/criar_campo', methods=['GET'])
def criar_novo_campo():
    global campo, descoberto
    campo = criar_campo(linhas, colunas, num_minas)
    descoberto = set()
    return jsonify({"campo": campo, "status": "campo criado"})

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

if __name__ == '__main__':
    app.run(debug=True)