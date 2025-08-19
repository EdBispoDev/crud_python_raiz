import logging
from core.user import Usuario
from repository.UserRepository import UserRepository

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, db_path="usuarios_db"):
        self.repo = UserRepository(db_path)

    def cadastrar_usuario(self, nome: str, endereco: str, cpf: str, idade: int):
        if len(cpf) != 11 or not cpf.isdigit():
            logger.error("CPF inválido!")
            return None
        if idade < 0:
            logger.error("Idade inválida!")
            return None

        if self.repo.buscar_por_cpf(cpf):
            logger.error(f"CPF {cpf} já cadastrado!")
            return None

        usuario = Usuario(nome, endereco, cpf, idade)
        self.repo.salvar(usuario)
        logger.info(f"Usuário {nome} cadastrado com sucesso.")
        return usuario

    def listar_usuarios(self):
        return self.repo.listar_todos()

    def deletar_usuario(self, cpf: str):
        usuario = self.repo.buscar_por_cpf(cpf)
        if not usuario:
            logger.error(f"CPF {cpf} não encontrado!")
            return
        self.repo.deletar(cpf)
        logger.info(f"Usuário com CPF {cpf} deletado com sucesso.")
