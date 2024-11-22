from flask import render_template, jsonify
from app import app
import requests

@app.route('/')
def home():
    try:
        # Tentando acessar a rota do logica_jogo_service
        response = requests.get("http://logica_jogo_service:5000/criar_campo")
        data = response.json()

        # Ajuste para garantir que 'campo' e 'colunas' estejam definidos
        campo = data['campo']
        linhas = len(campo)  # Número de linhas
        colunas = len(campo[0]) if campo else 0  # Número de colunas (assumindo que o campo é uma lista de listas)

    except requests.exceptions.RequestException as e:
        data = {"error": str(e)}
        linhas = 0
        colunas = 0  # Definindo 'colunas' como 0 em caso de erro

    return render_template('index.html', data=data, linhas=linhas, colunas=colunas)
