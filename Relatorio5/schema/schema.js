{
    $jsonSchema: {
      bsonType: "object",
      required: [
        "_id",
        "titulo",
        "autor",
        "ano",
        "preco",
      ],
      properties: {
        _id: {
          bsonType: "int",
          description:
            "Campo obrigatório. Deve ser um inteiro",
        },
        titulo: {
          bsonType: "string",
          description:
            "Campo obrigatório. Deve ser uma string",
        },
        autor: {
          bsonType: "string",
          description:
            "Campo obrigatório. Deve ser uma string",
        },
        ano: {
          bsonType: "int",
          maximum: 2023,
          description:
            "Campo obrigatório. Deve ser um inteiro menor que 2023",
        },
        preco: {
          bsonType: "double",
          description:
            "Campo obrigatório. Deve ser um double positivo",
        },
      },
    },
  }