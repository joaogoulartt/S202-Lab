from database import Database
import product_analyzer as pa

db = Database("relatorio4", "mercado")
db.resetDatabase() 

ProdAnalyzer = pa.ProductAnalyzer(db)

print("Digite a opção desejada:")
print("1 - Exemplo do relatório 4")
print("2 - Customizado")
option = int(input("Digite a opção: "))

if option == 1:
    ProdAnalyzer.getTotalAmountPurchaseByLetter("B")
else:
    letter = input("Digite a letra do cliente: ")
    ProdAnalyzer.getTotalAmountPurchaseByLetter(letter)

ProdAnalyzer.getLeastSoldProduct()

ProdAnalyzer.getCustomerWhoSpentTheLeastAmountInOnePurchase()

ProdAnalyzer.getProductsThatWereSold2UnitsOrMore()


