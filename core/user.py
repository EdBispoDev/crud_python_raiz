class Usuario:
    def __init__(self, nome: str, endereco: str, cpf: str, idade: int):
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido")
        if idade < 0:
            raise ValueError("Idade inválida")
        
        # Atribuições corretas (sem vírgula)
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.idade = idade

    def __repr__(self):
        return f"Usuario(nome={self.nome}, cpf={self.cpf}, idade={self.idade})"
         
usuario = Usuario("João", "Rua A", "12345678901", 25)
print(usuario)

