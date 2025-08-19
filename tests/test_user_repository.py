import unittest
import tempfile
import os
import logging
from repository.UserRepository import UserRepository
from core.user import Usuario

logging.disable(logging.CRITICAL)

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
        usuario = Usuario("Lucas", "Rua X", "99988877766", 40)
        self.repo.salvar(usuario)
        encontrado = self.repo.buscar_por_cpf("99988877766")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nome, "Lucas")

    def test_salvar_usuario_duplicado(self):
        usuario = Usuario("Pedro", "Rua Y", "55544433322", 35)
        self.repo.salvar(usuario)
        duplicado = Usuario("Pedro", "Rua Y", "55544433322", 35)
        resultado = self.repo.salvar(duplicado)
        self.assertIsNone(resultado)

    def test_listar_todos(self):
        self.repo.salvar(Usuario("Ana", "Rua Z", "11122233344", 28))
        usuarios = self.repo.listar_todos()
        self.assertGreaterEqual(len(usuarios), 1)

    def test_deletar_usuario(self):
        usuario = Usuario("Beatriz", "Rua W", "77766655544", 22)
        self.repo.salvar(usuario)
        self.repo.deletar("77766655544")
        encontrado = self.repo.buscar_por_cpf("77766655544")
        self.assertIsNone(encontrado)

if __name__ == "__main__":
    unittest.main()
