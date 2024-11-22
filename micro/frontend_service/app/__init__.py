# frontend_service/__init__.py
from flask import Flask

app = Flask(__name__)

# Importar as rotas do serviço frontend
from app.routes import *
