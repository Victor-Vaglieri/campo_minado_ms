# Campo minado em microsserviço

Este projeto é uma implementação do jogo Campo Minado utilizando **Flask** e **Docker**. Ele simula um campo minado onde o jogador interage com células para descobrir minas ou ganhar o jogo.

## Requisitos para Execução

Antes de executar o projeto, é necessário garantir que você tenha os seguintes requisitos instalados:

- **Docker**: Para rodar os containers de forma isolada e facilitar a execução do ambiente.
- **Docker Compose**: Para gerenciar múltiplos containers de forma mais fácil (se for o caso de uso).
- **Python 3.x**: Caso queira rodar o código fora do Docker ou desenvolver localmente.

## Como Instalar o Docker

Para instalar o Docker e op Docker-compose, siga os passos abaixo conforme o seu sistema operacional:

### **No Windows**:

1. Acesse o site oficial do Docker: [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop).
2. Clique em **Download Docker Desktop** e siga as instruções de instalação.
3. Após a instalação, abra o Docker Desktop e aguarde a inicialização.

### **No macOS**:

1. Acesse o site oficial do Docker: [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop).
2. Clique em **Download Docker Desktop** e siga as instruções de instalação.
3. Após a instalação, abra o Docker Desktop e aguarde a inicialização.

### **No Linux**:

Execute os seguintes comandos para instalar o Docker no Ubuntu (ou distribuições baseadas no Debian):

```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
``` 

## Execução

para executar o programa, basta rodar o seguinte comando no terminal:
```cod
sudo docker-compose up --build
```

e entrar no dominio
> 127.0.0.1:80

Para parar e remover os containers definidos no seu arquivo docker-compose.yml, você deve usar o comando:
```cod1
docker-compose down
```

Para limpar containers, imagens, volumes e redess, você pode usar:
```cod2
docker system prune -a
```

## [video](https://youtu.be/uBJurVwt9YQ)
