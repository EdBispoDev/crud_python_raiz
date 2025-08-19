import sqlite3
import logging
from core.user import Usuario

logger = logging.getLogger(__name__)

class UserRepository:
    def __init__(self, db_path="usuarios_db"):
        self.db_path = db_path
        self.create_table()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                cpf TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                endereco TEXT NOT NULL,
                idade INTEGER NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def salvar(self, usuario: Usuario):
        if self.buscar_por_cpf(usuario.cpf):
            logger.error(f"CPF {usuario.cpf} já cadastrado!")
            return None

        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO usuarios (cpf, nome, endereco, idade) VALUES (?, ?, ?, ?)',
            (usuario.cpf, usuario.nome, usuario.endereco, usuario.idade)
        )
        conn.commit()
        conn.close()
        logger.info(f"Usuário {usuario.nome} salvo com sucesso.")
        return usuario

    def buscar_por_cpf(self, cpf: str):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT cpf, nome, endereco, idade FROM usuarios WHERE cpf=?',
            (cpf,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Usuario(row[1], row[2], row[0], row[3])
        return None

    def listar_todos(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT cpf, nome, endereco, idade FROM usuarios')
        rows = cursor.fetchall()
        conn.close()
        return [Usuario(row[1], row[2], row[0], row[3]) for row in rows]

    def deletar(self, cpf: str):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE cpf=?", (cpf,))
        conn.commit()
        conn.close()
        logger.info(f"Usuário com CPF {cpf} deletado com sucesso.")
