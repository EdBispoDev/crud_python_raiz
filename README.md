# CRUD Python Puro

Olá! 👋  
Este é um projeto simples de CRUD em Python, desenvolvido para fins de estudo. Aqui explorei conceitos de **orientação a objetos**, **SQLite** e boas práticas de **separação de responsabilidades**.

No futuro, pretendo implementar testes automatizados, adicionar Docker, usar um banco de dados mais robusto, melhorias de segurança e outras funcionalidades.

---

## Estrutura do projeto

- `core/` → Contém os modelos (por exemplo, `Usuario`)  
- `repository/` → Responsável pelo acesso ao banco de dados (CRUD usando SQLite)  
- `service/` → Contém a lógica de negócio, validações e regras de negócio  
- `controller/` → Faz a ponte entre o usuário e os serviços, valida entradas  
- `main.py` → Arquivo principal para testar e executar o projeto  

---

## Funcionalidades

- Cadastrar usuários, com validação de CPF, idade, nome e endereço  
- Listar todos os usuários cadastrados  
- Deletar usuário por CPF  
- Prevenção de duplicidade de CPF  
- Validação de entradas com mensagens de erro claras  

---

## Tecnologias usadas

- Python 3  
- SQLite (banco de dados leve e integrado)  
- Logging para monitoramento de operações  

---

## Como usar

Clone o repositório:

```bash
git clone https://github.com/EdBispoDev/crud_python_raiz.git
cd crud_python_raiz

Execute o projeto:
python -m main

Execute os testes automatizados:
python -m unittest discover -s tests -p "test_*.py"


Próximos passos

Implementar testes mais completos

Adicionar Docker para facilitar execução

Migrar para um banco de dados mais robusto

Implementar melhorias de segurança e autenticação

Mais...