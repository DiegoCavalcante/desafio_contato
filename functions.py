def adicionar_contato(lista, nome, telefone, email):
    contato = {"nome":nome, "telefone":telefone, "email":email, "favorito": False}
    lista.append(contato)
    print("Contato adicionado com sucesso!")