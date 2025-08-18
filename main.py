from controller.UserController import UserController

def main():
    controller = UserController()

    while True:
        print("\n=== Menu ===")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Deletar usuário")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            controller.cadastrar_usuario()
        elif opcao == "2":
            controller.listar_usuarios()
        elif opcao == "3":
            controller.deletar_usuario()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
