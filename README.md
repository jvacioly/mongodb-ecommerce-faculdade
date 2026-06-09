# Catálogo de E-commerce com MongoDB e Python

Este projeto é a parte prática do nosso seminário sobre Bancos de Dados Orientados a Documentos. Ele demonstra a flexibilidade do MongoDB lidando com produtos de categorias totalmente diferentes na mesma coleção.

## Como rodar o projeto na sua máquina

**1. Suba o Banco de Dados (Docker)**
Abra o terminal e execute o comando abaixo para iniciar o MongoDB em segundo plano:
```bash
docker run --name mongo-ecommerce -p 27017:27017 -d mongo:latest
```

**2. Configure o Ambiente Python**
Crie um ambiente virtual e instale as dependências:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**3. Execute o Painel Administrativo**
Com o banco rodando e as bibliotecas instaladas, rode o script para popular o banco e ver a mágica dos descontos acontecendo:
```bash
python3 app_ecommerce.py
```