import re

class Usuario:
    def __init__(self, nome: str, endereco: str, cpf: str, idade: int):
        if not 2 <= len(nome) <= 50 or not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome):
            raise ValueError(
                "Nome inválido! Deve conter apenas letras e ter entre 2 e 50 caracteres."
            )

        if not 5 <= len(endereco) <= 100 or not re.fullmatch(r"[A-Za-z0-9\s\-,\.]+", endereco):
            raise ValueError(
                "Endereço inválido! Deve ter entre 5 e 100 caracteres e conter apenas caracteres válidos."
            )

        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF inválido! Deve conter exatamente 11 números.")

        if not isinstance(idade, int) or not (0 <= idade <= 120):
            raise ValueError("Idade inválida! Deve ser um número entre 0 e 120.")

        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.idade = idade

    def __repr__(self):
        return f"Usuario(nome={self.nome}, cpf={self.cpf}, idade={self.idade})"


if __name__ == "__main__":
    try:
        usuario = Usuario("João", "Rua A, 123", "12345678901", 25)
        print(usuario)
    except ValueError as e:
        print("Erro ao criar usuário:", e)
