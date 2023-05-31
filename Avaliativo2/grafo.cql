// Criação de usuários
CREATE (a:Usuario {nome: 'Alice', idade: 25});
CREATE (b:Usuario {nome: 'Bob', idade: 30});
CREATE (c:Usuario {nome: 'Charlie', idade: 35});
CREATE (d:Usuario {nome: 'David', idade: 40});
CREATE (e:Usuario {nome: 'Eve', idade: 45});

// Criação de postagens
CREATE (p1:Postagem {titulo: 'Observações do Amanhecer', conteudo: 'Conteúdo da Observações do Amanhecer'});
CREATE (p2:Postagem {titulo: 'Memórias da Tarde', conteudo: 'Conteúdo da Memórias da Tarde'});
CREATE (p3:Postagem {titulo: 'Segredos da Noite', conteudo: 'Segredos da Noite'});

// Definindo relações de amizade
CREATE (a)-[:AMIGO]->(b);
CREATE (b)-[:AMIGO]->(c);
CREATE (c)-[:AMIGO]->(d);
CREATE (d)-[:AMIGO]->(e);

// Definindo quem fez as postagens
CREATE (a)-[:POSTOU]->(p1);
CREATE (b)-[:POSTOU]->(p2);
CREATE (c)-[:POSTOU]->(p3);
