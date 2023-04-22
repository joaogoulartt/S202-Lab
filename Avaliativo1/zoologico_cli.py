from zoologico_dao import ZoologicoDAO
from models.animal import Animal
from models.habitat import Habitat
from models.cuidador import Cuidador

class ZoologicoCLI:
    def __init__(self, zoologico_dao: ZoologicoDAO) -> None:
        self.zoologico_dao = zoologico_dao

    def create_animal(self):
        print("-----------------------")
        print('Informações do Cuidador')
        nome_cuidador = input("Nome: ")
        documento_cuidador = input("Documento: ")
        id_cuidador = input("Id: ")
        cuidador = Cuidador(nome_cuidador, documento_cuidador, id_cuidador)

        print("-----------------------")
        print("Informações do Habitat")
        nome_habitat = input("Nome: ")
        tipo_ambiente = input("Tipo de ambiente: ")
        id_habitat = input("Id: ")
        habitat = Habitat(nome_habitat, tipo_ambiente, cuidador, id_habitat)

        print("-----------------------")
        print("Informações do Animal")
        nome_animal = input("Nome: ")
        especie = input("Especie: ")
        idade = int(input("Idade: "))
        animal = Animal(nome_animal, especie, idade, habitat)

        self.zoologico_dao.createAnimal(animal)

    def read_animal_by_id(self):
        id = input("ID: ")
        animal = self.zoologico_dao.read_animal_by_id(id)

        print("Resultado da pesquisa:")
        print("Nome:", animal.nome)
        print("Especie:", animal.especie)
        print("Idade:", animal.idade)
        print("Habitat:", animal.habitat.nome)
        print("Tipo de ambiente:", animal.habitat.tipo_ambiente)
        print("Cuidador:", animal.habitat.cuidador.nome)
        print("Documento do Cuidador:", animal.habitat.cuidador.documento)

    def update_animal(self):
        id_animal = input("Digite o id do animal: ")

        animal = self.zoologico_dao.readAnimal(id_animal)

        print("Atualize apenas o que desejar")

        animal['nome'] = input("Nome: ") or animal['nome']
        animal['especie'] = input("Especie: ") or animal['especie']
        animal['idade'] = input("Idade: ") or animal['idade']
        animal['habitat']['id'] = input(
            "Id do Habitat: ") or animal['habitat']['id']
        animal['habitat']['nome'] = input(
            "Habitat: ") or animal['habitat']['nome']
        animal['habitat']['tipoAmbiente'] = input(
            "Tipo de ambiente: ") or animal['habitat']['tipoAmbiente']
        animal['habitat']['cuidador']['id'] = input(
            "Id do Cuidador: ") or animal['habitat']['cuidador']['id']
        animal['habitat']['cuidador']['nome'] = input(
            "Cuidador: ") or animal['habitat']['cuidador']['nome']
        animal['habitat']['cuidador']['documento'] = input(
            "Documento do Cuidador: ") or animal['habitat']['cuidador']['documento']

        updated_animal = self.zoologico_dao.updateAnimal(id_animal, Animal.deserialize(animal))

        if updated_animal is None:
            print("Animal não encontrado.")
            return

        print("Animal atualizado com sucesso!")

    def delete_animal(self):
        id = input("ID: ")
        response = self.zoologico_dao.delete_animal(id)

        if (response is None):
            print("Animal não encontrado.")
            return

        if (response.deleted_count > 0):
            print("Animal deletado com sucesso!")
        else:
            print("Animal não encontrado.")