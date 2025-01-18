from menu import menu, menu_edicao
from functions import adicionar_contato, ver_contatos, editar_contato, modificar_favorito, ver_favoritos, deletar_contato

condicao = True
contatos = []
while condicao:
    menu()
    escolha = input("\nDigite a sua escolha:")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        email = input("Digite o telefone do contato: ")
        telefone = input("Digite o email do contato: ")
        adicionar_contato(contatos, nome, email, telefone)
        
    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        
        indice = input("\nEscolha o número do contato para editar: ")
        try:
            indice_ajustado = int(indice)
        except Exception as e:
            print(e)
        else:
            condicao_edicao = True
            while condicao_edicao:
                menu_edicao()
                escolha_edicao = input("\nEscolha qual item do contato para editar: ")
                if escolha_edicao == "1":
                    novo_nome = input("Digite o novo nome:")
                    editar_contato(contatos, indice_ajustado, "nome", novo_nome)
                elif escolha_edicao == "2":
                    novo_telefone = input("Digite o novo telefone:")
                    editar_contato(contatos, indice_ajustado, "telefone", novo_telefone)
                elif escolha_edicao == "3":
                    novo_email = input("Digite o novo email:")
                    editar_contato(contatos, indice_ajustado, "email", novo_email)
                elif escolha_edicao == "4":
                    condicao_edicao = False
    elif escolha == "4":
        ver_contatos(contatos)
        indice = input("\nEscolha um contato para marcar/desmarcar como favorito: ")
        try:
            indice_ajustado = int(indice)
        except Exception as e:
            print(e)
        else:
            modificar_favorito(contatos, indice_ajustado)

    elif escolha == "5":
        ver_favoritos(contatos)
    
    elif escolha == "6":
        ver_contatos(contatos)
        indice = input("Digite o número do contato que deseja deletar: ")
        try:
            indice_ajustado = int(indice)
        except Exception as e:
            print(e)
        else:
            deletar_contato(contatos, indice_ajustado)
           
    elif escolha == "7":
        condicao = False