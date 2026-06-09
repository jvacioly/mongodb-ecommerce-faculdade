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

## 🖥️ Visualizando o Banco de Dados (Extensão VS Code)

Para não depender exclusivamente do terminal, recomendamos o uso da extensão oficial do MongoDB para o Visual Studio Code. Isso permite visualizar os documentos BSON e rodar consultas lado a lado com o nosso código Python.

### 1. Instalação
1. Abra o VS Code.
2. Vá na aba de Extensões (`Ctrl + Shift + X`).
3. Pesquise por **MongoDB for VS Code** (a extensão oficial tem o ícone de uma folha verde).
4. Clique em **Install**.

### 2. Como Conectar
1. Certifique-se de que o container Docker do MongoDB está rodando (`docker start mongo-ecommerce`).
2. Clique no ícone da folha verde do MongoDB que apareceu na barra lateral esquerda do VS Code.
3. No painel superior, clique em **Add Connection** (ou no ícone de `+` em CONNECTIONS).
4. Cole a seguinte string de conexão e aperte Enter:
   ```text
   mongodb://127.0.0.1:27017/
   ```
5. Uma mensagem de sucesso confirmará a conexão.

### 3. Navegando pelos Dados

    No painel da extensão, expanda a conexão 127.0.0.1:27017.

    Expanda o nosso banco de dados: ecommerce_db.

    Expanda a coleção produtos e clique em Documents.

    A lista de IDs dos produtos cadastrados vai aparecer. Ao clicar em qualquer um deles, o VS Code abrirá o documento formatado em JSON, permitindo visualizar a estrutura flexível dos nossos eletrônicos e vestuários.

### 4. Executando Consultas Visuais (Playgrounds)

Para testar consultas diretamente no editor sem usar o terminal:

    Clique com o botão direito sobre o ecommerce_db e escolha Create New Playground.

    O VS Code abrirá um arquivo de rascunho. Você pode digitar comandos nativos do Mongo, como:
    ```JavaScript
    use('ecommerce_db');
    db.produtos.find({ categoria: "Eletrônicos" });
    ```
    Clique no botão de Play no canto superior direito da aba (ou Ctrl + Alt + E). O resultado aparecerá instantaneamente em uma aba lateral.