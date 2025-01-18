def adicionar_contato(lista, nome, telefone, email):
    contato = {"nome":nome, "telefone":telefone, "email":email, "favorito": False}
    lista.append(contato)
    print("Contato adicionado com sucesso!")
    return

def ver_contatos(lista):
    print("\nLista de Contatos:")
    for index, contato in enumerate(lista, start=1):
        print(f"{index}. Nome: {contato['nome']}; Telefone: {contato['telefone']}; email: {contato['email']}")
    return

def editar_contato(lista, indice, param, novo_item):
    indice_ajustado = indice - 1
    if indice_ajustado >= 0 and indice_ajustado < len(lista):
        lista[indice_ajustado][param] = novo_item        
        print("Contato atualizado com sucesso")
    return