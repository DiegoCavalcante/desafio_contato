from menu import menu
from functions import adicionar_contato

condicao = True
contatos = []
while condicao:
    menu()
    escolha = input("Digite a sua escolha:")
    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        email = input("Digite o telefone do contato: ")
        telefone = input("Digite o email do contato: ")
        adicionar_contato(contatos, nome, email, telefone)
    if escolha == "7":
        condicao = False