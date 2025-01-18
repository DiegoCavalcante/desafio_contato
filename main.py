from menu import menu

condicao = True

while condicao:
    menu()
    escolha = input("Digite a sua escolha:")
    if escolha == "7":
        condicao = False