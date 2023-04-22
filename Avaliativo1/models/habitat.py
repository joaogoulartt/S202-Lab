from models.cuidador import Cuidador

class Habitat:
    def __init__(self, nome, tipoAmbiente, cuidador: Cuidador, id = None):
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador
        self.id = id

    def serialize(self):
        return {
            "nome": self.nome,
            "tipoAmbiente": self.tipoAmbiente,
            "cuidador": self.cuidador.serialize()
        }
    
    def deserialize(habitat:dict):
        return Habitat(
            habitat['nome'], 
            habitat['tipoAmbiente'], 
            Cuidador.deserialize(habitat['cuidador']), 
            habitat['id'])
    
    def schema():
        return {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['nome', 'tipoAmbiente', 'cuidador'],
                'properties': {
                    'nome': {
                        'bsonType': 'string',
                        'description': 'Nome do habitat deve ser uma string',
                    },
                    'tipoAmbiente': {
                        'bsonType': 'string',
                        'description': 'Tipo de ambiente do habitat deve ser uma string',
                    },
                    'cuidador': Cuidador.schema()['$jsonSchema']
                }
            }
        }