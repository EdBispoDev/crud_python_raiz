# CRUD Python Simples

Olá! 👋  
Esse é um projeto simples de CRUD em Python, desenvolvido **para fins de estudo**. Aqui eu explorei conceitos de orientação a objetos, SQLite e boas práticas de separação de responsabilidades.

---

## Estrutura do projeto

- **core/** → Contém os modelos (por exemplo, `Usuario`)  
- **repository/** → Responsável pelo acesso ao banco de dados (CRUD usando SQLite)  
- **service/** → Contém a lógica de negócio, validações e regras de negócio  
- **main.py** → Arquivo principal para testar e executar o projeto

---

## Funcionalidades

- Cadastrar usuários, com validação de CPF e idade  
- Listar todos os usuários cadastrados  
- Deletar usuário por CPF  
- Prevenção de duplicidade de CPF

---

## Tecnologias usadas

- Python 3  
- SQLite (banco de dados leve e integrado)  

---

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/EdBispoDev/crud_python_raiz.git
cd crud_python_raiz
