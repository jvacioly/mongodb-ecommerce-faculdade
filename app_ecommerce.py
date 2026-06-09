from pymongo import MongoClient

# Conexão com o Docker
cliente = MongoClient('mongodb://localhost:27017/')
db = cliente['ecommerce_db']
colecao_produtos = db['produtos']

def cadastrar_produto(nome, categoria, preco, especificacoes):
    # Trava de segurança: só cadastra se o produto não existir
    if colecao_produtos.count_documents({"nome": nome}) == 0:
        produto = {
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "especificacoes": especificacoes
        }
        colecao_produtos.insert_one(produto)
        print(f"Produto '{nome}' cadastrado com sucesso!")
    else:
        print(f"Produto '{nome}' já existe no banco. Pulando cadastro.")

def buscar_por_categoria(categoria):
    print(f"\n--- Catálogo: {categoria} ---")
    produtos = colecao_produtos.find({"categoria": categoria})
    for p in produtos:
        detalhes = ", ".join([f"{k}: {v}" for k, v in p['especificacoes'].items()])
        print(f"-> {p['nome']} | R$ {p['preco']:.2f} | Detalhes: {detalhes}")

def aplicar_desconto_categoria(categoria, porcentagem):
    fator_multiplicacao = 1 - (porcentagem / 100)
    resultado = colecao_produtos.update_many(
        {"categoria": categoria},
        {"$mul": {"preco": fator_multiplicacao}} 
    )
    print(f"\n>> Desconto de {porcentagem}% aplicado em {resultado.modified_count} produtos da categoria {categoria}!")

# --- INÍCIO DA EXECUÇÃO ---
print("Iniciando o painel de administração via Python...\n")

# O Python cadastra novos produtos (e não duplica se rodar de novo)
cadastrar_produto("Notebook Gamer", "Eletrônicos", 5000.00, {"RAM": "16GB", "Placa de Vídeo": "RTX 3060"})
cadastrar_produto("Tênis de Corrida", "Calçados", 300.00, {"Tamanho": "42", "Pisada": "Neutra"})

# Busca a categoria Eletrônicos (Vai achar a TV do mongosh e o Notebook do Python)
buscar_por_categoria("Eletrônicos")

# Aplica desconto em toda a categoria
aplicar_desconto_categoria("Eletrônicos", 10) 

# Busca novamente para mostrar os novos preços
buscar_por_categoria("Eletrônicos")