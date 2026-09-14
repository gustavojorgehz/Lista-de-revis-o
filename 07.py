tarefas = []

while True:
    print("\n--- LISTA DE TAREFAS ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Buscar tarefa")
    print("4 - Alterar tarefa")
    print("5 - Remover tarefa")
    print("6 - Quantidade de tarefas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")

        tarefas.append([tarefa, False])

        print("Tarefa adicionada!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n--- TAREFAS ---")

            for i, tarefa in enumerate(tarefas):
                if tarefa[1]:
                    status = "Concluída"
                else:
                    status = "Pendente"

                print(f"{i + 1} - {tarefa[0]} ({status})")

    elif opcao == "3":
        busca = input("Digite o nome da tarefa: ")

        encontrada = False

        for tarefa in tarefas:
            if busca.lower() in tarefa[0].lower():
                print("Tarefa encontrada:", tarefa[0])
                encontrada = True

        if not encontrada:
            print("Tarefa não encontrada.")

    elif opcao == "4":
        numero = int(input("Digite o número da tarefa: "))

        if 1 <= numero <= len(tarefas):
            nova_tarefa = input("Digite a nova tarefa: ")

            tarefas[numero - 1][0] = nova_tarefa

            print("Tarefa alterada!")
        else:
            print("Tarefa inválida.")

    elif opcao == "5":
        numero = int(input("Digite o número da tarefa: "))

        if 1 <= numero <= len(tarefas):
            tarefas.pop(numero - 1)

            print("Tarefa removida!")
        else:
            print("Tarefa inválida.")

    elif opcao == "6":
        print("Quantidade de tarefas:", len(tarefas))

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")