def adicionar_contato(lista, nome, telefone, email):
    contato = {"nome":nome, "telefone":telefone, "email":email, "favorito": False}
    lista.append(contato)
    print("Contato adicionado com sucesso!")

def ver_contatos(lista):
    print("\nLista de Contatos:")
    for index, contato in enumerate(lista, start=1):
        print(f"{index}. Nome: {contato['nome']}; Telefone: {contato['telefone']}; email: {contato['email']}")