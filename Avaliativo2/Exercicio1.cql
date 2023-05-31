//QUESTÕES:

// Quem é amigo de Bob?
MATCH (a:Usuario)-[:AMIGO]-(b:Usuario {nome: 'Bob'}) RETURN a.nome;

// Resultado da Query
[
  {
    "a.nome": "Charlie"
  },
  {
    "a.nome": "Alice"
  }
]

// Quem postou a 'Postagem 2'?
MATCH (a:Usuario)-[:POSTOU]->(b:Postagem {titulo: 'Memórias da Tarde'}) RETURN a.nome;

// Resultado da Query
[
  {
    "a.nome": "Bob"
  }
]

//Quem tem mais de 35 anos e fez uma postagem?
MATCH (a:Usuario)-[:POSTOU]->(b:Postagem) WHERE a.idade > 35 RETURN a.nome;

// Resultado da Query
'(no changes, no records)'

