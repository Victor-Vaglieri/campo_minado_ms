# logica_jogo_service/__init__.py
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Importar as rotas do serviço de lógica do jogo
from app.routes import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)