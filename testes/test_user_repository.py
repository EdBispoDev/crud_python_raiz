import unittest
import os
from repository.UserRepository import UserRepository
from core.user import Usuario
import tempfile


class TestUserRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_file = tempfile.NamedTemporaryFile(delete=False).name
        cls.repo = UserRepository(db_path=cls.db_file)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.db_file):
            os.remove(cls.db_file)

    def test_salvar_e_buscar_usuario(self):
        usuario = Usuario("Maria", "Rua B", "98765432100", 30)
        self.repo.salvar(usuario)
        encontrado = self.repo.buscar_por_cpf("98765432100")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nome, "Maria")
        self.assertEqual(encontrado.cpf, "98765432100")
        self.assertEqual(encontrado.idade, 30)

    def test_cadastrar_usuario_duplicado(self):
        usuario = Usuario("Carlos", "Rua D", "11122233344", 28)
        self.repo.salvar(usuario)
        duplicado = self.repo.salvar(usuario)
        self.assertIsNone(duplicado)

    def test_listar_todos(self):
        self.repo.salvar(Usuario("Ana", "Rua A", "12312312300", 25))
        usuarios = self.repo.listar_todos()
        self.assertGreaterEqual(len(usuarios), 1)

    def test_deletar_usuario(self):
        usuario = Usuario("João", "Rua C", "12345678901", 25)
        self.repo.salvar(usuario)
        self.repo.deletar("12345678901")
        deletado = self.repo.buscar_por_cpf("12345678901")
        self.assertIsNone(deletado)

if __name__ == "__main__":
    unittest.main()

