import re
from service.UserService import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()
        self.re_nome = re.compile(r"^[A-Za-zÀ-ÿ\s]{2,50}$")
        self.re_endereco = re.compile(r"^[A-Za-z0-9\s\-,\.]{5,100}$")

    def cadastrar_usuario(self):
        while True:
            nome = input("Nome: ").strip()
            if self.re_nome.fullmatch(nome):
                break
            print("Nome inválido! Apenas letras e espaços, 2 a 50 caracteres.")

        while True:
            endereco = input("Endereço: ").strip()
            if self.re_endereco.fullmatch(endereco):
                break
            print("Endereço inválido! 5 a 100 caracteres, apenas caracteres válidos.")

        while True:
            cpf = input("CPF (apenas números): ").strip()
            if cpf.isdigit() and len(cpf) == 11:
                break
            print("CPF inválido! Deve conter exatamente 11 números.")

        while True:
            idade_str = input("Idade: ").strip()
            try:
                idade = int(idade_str)
                if 0 <= idade <= 120:
                    break
                print("Idade inválida! Deve ser entre 0 e 120.")
            except ValueError:
                print("Idade inválida! Digite um número inteiro.")

        usuario = self.user_service.cadastrar_usuario(nome, endereco, cpf, idade)
        if usuario:
            print(f"Usuário cadastrado com sucesso: {usuario}")
