//QUESTÕES

//Encontre o usuário mais velho.
MATCH (u:Usuario)
RETURN u.nome, u.idade
ORDER BY u.idade DESC
LIMIT 1;

//Resposta da Query
[
  {
    "u.nome": "Eve",
    "u.idade": 45
  }
]

//Quantos usuários têm mais de 30 anos?
MATCH (u:Usuario)
WHERE u.idade > 30
RETURN count(u);

//Resposta da Query
[
  {
    "count(u)": 3
  }
]

//Qual é a média de idade dos usuários?
MATCH (u:Usuario)
RETURN avg(u.idade);

//Resposta da Query
[
  {
    "avg(u.idade)": 35.0
  }
]