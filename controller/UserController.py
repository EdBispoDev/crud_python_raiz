from service.UserService import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def cadastrar_usuario(self):
        print("=== Cadastro de Usuário ===")
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        cpf = input("CPF (apenas números): ")
        idade_str = input("Idade: ")

        try:
            idade = int(idade_str)
        except ValueError:
            print("Idade inválida!")
            return

        usuario = self.user_service.cadastrar_usuario(nome, endereco, cpf, idade)
        if usuario:
            print(f"Usuário cadastrado com sucesso: {usuario}")

    def listar_usuarios(self):
        print("=== Lista de Usuários ===")
        usuarios = self.user_service.listar_usuarios()
        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for u in usuarios:
            print(u)

    def deletar_usuario(self):
        print("=== Deletar Usuário ===")
        cpf = input("Digite o CPF do usuário a ser deletado: ")
        self.user_service.deletar_usuario(cpf)
