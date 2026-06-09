use ecommerce_db; // Cria o banco

// Inserindo um eletrônico
db.produtos.insertOne({
    nome: "Smart TV 55 polegadas",
    categoria: "Eletrônicos",
    preco: 2500.00,
    estoque: 15,
    especificacoes: { // Objeto embutido flexível
        resolucao: "4K",
        sistema_operacional: "Android TV",
        voltagem: "Bivolt"
    }
});

// Inserindo uma roupa na MESMA coleção
db.produtos.insertOne({
    nome: "Camisa Polo Básica",
    categoria: "Vestuário",
    preco: 89.90,
    estoque: 50,
    especificacoes: { // Propriedades totalmente diferentes
        tamanho: "M",
        cor: "Azul Marinho",
        tecido: "Algodão"
    }
});