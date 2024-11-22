# app/__init__.py
from flask import Flask

app = Flask(__name__)

# As rotas são importadas após a criação do app
from app.routes import *