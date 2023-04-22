from database import Database
from models.animal import Animal

class ZoologicoDAO:
    def __init__(self, database:Database):
        self.db = database
        self.collection = self.db.create_collection("animais", Animal.schema())

    def create_animal(self, animal: Animal):
        return self.collection.insert_one(animal.serialize())
    
    def read_animal(self, id):
        return self.collection.find_one({"id": id})
    
    def update_animal(self, id, animal: Animal):
        return self.collection.update_one({"id": id}, {"$set": animal.serialize()})
    
    def delete_animal(self, id):
        return self.collection.delete_one({"id": id})
