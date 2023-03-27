from database import Database
from jsonService import writeAJson

class ProductAnalyzer(object): 

    def __init__(self, db: Database):
        self.db = db

    def getTotalAmountPurchaseByLetter(self, letter: str):
        letterUpper = letter.upper()

        result = self.db.collection.aggregate([{"$unwind": "$produtos"},
                                    {"$group": {"_id": "$cliente_id", "total": {
                                        "$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
                                    {"$match": {"_id": letterUpper}}])
        
        writeAJson(result, "Total comprado pelo cliente " + letterUpper)
        print ("Arquivo JSON gerado com sucesso! Verifique a pasta 'json'.")
    
    def getLeastSoldProduct(self):
        result = self.db.collection.aggregate([{"$unwind": "$produtos"},
                                    {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
                                    {"$sort": {"total": 1}},
                                    {"$limit": 1}])

        writeAJson(result, "Produto menos vendido")
        print ("Arquivo JSON gerado com sucesso! Verifique a pasta 'json'.")

    def getCustomerWhoSpentTheLeastAmountInOnePurchase(self):
        result = self.db.collection.aggregate([{"$unwind": "$produtos"},
                                    {"$group": {"_id": "$cliente_id", "total": {
                                        "$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
                                    {"$sort": {"total": 1}},
                                    {"$limit": 1}])

        writeAJson(result, "Cliente que gastou menos em uma compra")
        print ("Arquivo JSON gerado com sucesso! Verifique a pasta 'json'.")

    def getProductsThatWereSold2UnitsOrMore(self):
        result = self.db.collection.aggregate([{"$unwind": "$produtos"},
                                    {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
                                    {"$match": {"total": {"$gte": 2}}},
                                    {"$sort": {"_id": 1}}])

        writeAJson(result, "Produtos que foram vendidos 2 unidades ou mais")
        print ("Arquivo JSON gerado com sucesso! Verifique a pasta 'json'.")