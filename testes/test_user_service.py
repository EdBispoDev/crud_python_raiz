import unittest
from service.UserService import UserService
import tempfile
import os

class TestUserService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_file = tempfile.NamedTemporaryFile(delete=False).name
        cls.service = UserService(db_path=cls.db_file)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.db_file):
            os.remove(cls.db_file)

    def test_cadastrar_usuario_valido(self):
        usuario = self.service.cadastrar_usuario("Maria", "Rua B", "98765432100", 30)
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.nome, "Maria")
        self.assertEqual(usuario.cpf, "98765432100")
        self.assertEqual(usuario.idade, 30)

    def test_cadastrar_cpf_invalido(self):
        usuario = self.service.cadastrar_usuario("Ana", "Rua A", "111", 20)
        self.assertIsNone(usuario)

    def test_cadastrar_usuario_duplicado(self):
        self.service.cadastrar_usuario("Carlos", "Rua D", "11122233344", 28)
        usuario_duplicado = self.service.cadastrar_usuario("Carlos", "Rua D", "11122233344", 28)
        self.assertIsNone(usuario_duplicado)

    def test_listar_usuarios(self):
        self.service.cadastrar_usuario("João", "Rua C", "12345678901", 25)
        usuarios = self.service.listar_usuarios()
        self.assertGreaterEqual(len(usuarios), 1)

if __name__ == "__main__":
    unittest.main()
