Agenda de Contatos: Crie um programa de terminal com menu interativo usando dicionários
que permita adicionar, buscar, atualizar e remover contatos (nome e telefone).


RESPOSTA:
agenda = {}

while True:
    opcao = input("\n[1] Adicionar [2] Buscar [3] Atualizar [4] Remover [0] Sair: ")
    if opcao == "0":
        break
    elif opcao == "1":
        nome = input("Nome: ")
        agenda[nome] = input("Telefone: ")
    elif opcao == "2":
        nome = input("Nome para busca: ")
        print(agenda.get(nome, "Contato não encontrado."))
    elif opcao == "3":
        nome = input("Nome para atualizar: ")
        if nome in agenda:
            agenda[nome] = input("Novo telefone: ")
        else:
            print("Contato não encontrado.")
    elif opcao == "4":
        nome = input("Nome para remover: ")
        agenda.pop(nome, None)
