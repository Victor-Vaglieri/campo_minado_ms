# Use uma imagem base com Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

ENV PYTHONPATH=/app

# Copia os arquivos necessários para o contêiner
COPY . /app

# Instala as dependências
RUN pip install -r requirements.txt

# Expõe a porta onde o serviço vai rodar
EXPOSE 5000

# Comando para iniciar o aplicativo
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
