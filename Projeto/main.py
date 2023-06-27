from database import Database
from category import Category
from products import Product


def main():
    db = Database("bolt://54.236.31.5:7687", "neo4j", "temperatures-cartridge-permits")
    category_model = Category(db)
    product_model = Product(db)

    while True:
        print("========= MENU =========")
        print("1. Criar Categoria")
        print("2. Obter Categoria")
        print("3. Atualizar Categoria")
        print("4. Excluir Categoria")
        print("5. Criar Produto")
        print("6. Obter Produto")
        print("7. Atualizar Produto")
        print("8. Excluir Produto")
        print("9. Obter Produtos da Categoria")
        print("10. Obter Todas as Categorias")
        print("11. Obter Todos os Produtos")
        print("12. Sair")

        opcao = input("Digite a opcao desejada: ")

        if opcao == "1":
            name = input("Digite o nome: ")
            description = input("Digite a descrição: ")
            category_model.create(name, description)
            print("Categoria criada com sucesso.")

        elif opcao == "2":
            name = input("Digite o nome: ")
            category = category_model.get_category_by_name(name)
            if category:
                print(f"Nome: {category['name']}, Descrição: {category['description']}")
            else:
                print("Categoria não encontrada.")

        elif opcao == "3":
            name = input("Digite o nome: ")
            description = input(
                "Digite a nova descrição (pressione Enter para pular): "
            )
            category = category_model.update(name, description)
            if category:
                print("Categoria atualizada com sucesso.")
            else:
                print("Categoria não encontrada.")

        elif opcao == "4":
            name = input("Digite o nome: ")
            category = category_model.delete(name)
            if category:
                print("Falha ao excluir categoria.")
            else:
                print("Categoria excluída com sucesso.")

        elif opcao == "5":
            category_name = input("Digite o nome da categoria: ")
            category = category_model.get_by_name(category_name)
            if category:
                name = input("Digite o nome: ")
                description = input("Digite a descrição: ")
                quantity = input("Digite a quantidade: ")
                product_model.create(category_name, name, description, quantity)
                print("Produto criado com sucesso.")
            else:
                print("Categoria não encontrada. Por favor, crie a categoria primeiro.")

        elif opcao == "6":
            name = input("Digite o nome: ")
            product = product_model.get_by_name(name)
            if product:
                record = product[0]  # Acessando o primeiro elemento da lista
                quantity = int(record['p']['quantity'])
                name = record['p']['name']
                description = record['p']['description']
                print(f"Nome: {name}, Descrição: {description}, Quantidade: {quantity}")
            else:
                print("Produto não encontrado.")

        elif opcao == "7":
            name = input("Digite o nome: ")
            description = input(
                "Digite a nova descrição (pressione Enter para pular): "
            )
            quantity = input("Digite a nova quantidade (pressione Enter para pular): ")
            product = product_model.update(name, description, quantity)
            if product:
                print("Produto atualizado com sucesso.")
            else:
                print("Produto não encontrado.")

        elif opcao == "8":
            name = input("Digite o nome: ")
            product = product_model.delete(name)
            if product:
                print("Falha ao excluir produto.")
            else:
                print("Produto excluído com sucesso.")

        elif opcao == "9":
            category_name = input("Digite o nome da categoria: ")
            products = product_model.get_products_by_category(category_name)
            if products:
                print(f"Produtos da categoria '{category_name}':")
                for product in products:
                    print(product['p.name'])
            else:
                print("Nenhum produto encontrado para essa categoria.")

        elif opcao == "10":
            categories = category_model.get_all()
            if categories:
                print("Todas as categorias:")
                for category in categories:
                    print (category['c.name'])
    
            else:
                print("Nenhuma categoria encontrada.")

        elif opcao == "11":
            products = product_model.get_all()
            if products:
                print("Todos os produtos:")
                for product in products:
                    print(product['p.name'])
            else:
                print("Nenhum produto encontrado.")

        elif opcao == "12":
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


main()
