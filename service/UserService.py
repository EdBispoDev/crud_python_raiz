from core.user import Usuario
from repository.UserRepository import UserRepository


class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def cadastrar_usuario(self, nome: str, endereco: str, cpf: str, idade: int):
        # Validação básica
        if len(cpf) != 11 or not cpf.isdigit():
            print("Erro: CPF inválido!")
            return None
        if idade < 0:
            print("Erro: Idade inválida!")
            return None

        # Verificar se CPF já existe
        if self.repo.buscar_por_cpf(cpf):
            print(f"Erro: CPF {cpf} já cadastrado!")
            return None

        # Criar usuário e salvar
        usuario = Usuario(nome, endereco, cpf, idade)
        self.repo.salvar(usuario)
        return usuario

    def listar_usuarios(self):
        return self.repo.listar_todos()

    def deletar_usuario(self, cpf: str):
        usuario = self.repo.buscar_por_cpf(cpf)
        if not usuario:
            print(f"Erro: CPF {cpf} não encontrado!")
            return
        self.repo.deletar(cpf)
        print(f"Usuário com CPF {cpf} deletado com sucesso!")
