import sqlite3
from core.user import Usuario


class UserRepository:
    def __init__(self, db_name="usuarios_db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                cpf TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                endereco TEXT NOT NULL,
                idade INTEGER NOT NULL    
            )
        ''')
        self.conn.commit()

    def salvar(self, usuario: Usuario):
        if self.buscar_por_cpf(usuario.cpf):
            print(f"Erro: CPF {usuario.cpf} já cadastrado!")
            return

        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT INTO usuarios (cpf, nome, endereco, idade) VALUES (?, ?, ?, ?)
            ''',
            (usuario.cpf, usuario.nome, usuario.endereco, usuario.idade)
        )
        self.conn.commit()

    def buscar_por_cpf(self, cpf: str):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT cpf, nome, endereco, idade FROM usuarios WHERE cpf=?',
            (cpf,)
        )
        row = cursor.fetchone()
        if row:
            return Usuario(row[1], row[2], row[0], row[3])
        return None

    def listar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT cpf, nome, endereco, idade FROM usuarios')
        rows = cursor.fetchall()
        return [Usuario(row[1], row[2], row[0], row[3]) for row in rows]
