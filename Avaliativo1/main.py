from database import Database
from zoologico_cli import ZoologicoCLI
from zoologico_dao import ZoologicoDAO

def input_validator() -> int:
    while True:
        opt = int(input('Option: '))
        if opt < 1 or opt > 5:
            print('Opção Invalida!')
            continue
        else:
            return opt


def menu():
    print("1 - Create animal")
    print("2 - Read animal by id")
    print("3 - Update animal")
    print("4 - Delete animal")
    print("5 - Exit")

def main():
    db = Database("zoologico")
    zoo = ZoologicoDAO(db)
    cli = ZoologicoCLI(zoo)


    option = 0
    while option != 5:
        menu()
        option = input_validator()
        print(option)
        if option == 1:
            cli.create_animal()
        elif option == 2:
            cli.read_animal_by_id()
        elif option == 3:
            cli.update_animal()
        elif option == 4:
            cli.delete_animal()
        elif option == 5:
            print('Programa encerrado')

if __name__ == "__main__":
    main()