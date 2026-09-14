historico = []

while True:
    print("\n--- HISTÓRICO DE PÁGINAS ---")
    print("1 - Visitar nova página")
    print("2 - Visualizar página atual")
    print("3 - Voltar para página anterior")
    print("4 - Exibir histórico")
    print("0 - Sair")

    opcao = input("Escolha uma opção pelo número: ")

    if opcao == "1":
        pagina = input("Digite o endereço da página: ")

        historico.append(pagina)

        print("Página visitada com sucesso!")

    elif opcao == "2":
        if len(historico) == 0:
            print("Nenhuma página foi visitada.")
        else:
            print("Página atual:", historico[-1])

    elif opcao == "3":
        if len(historico) <= 1:
            print("Não há página anterior.")
        else:
            historico.pop()
            print("Voltando para:", historico[-1])

    elif opcao == "4":
        if len(historico) == 0:
            print("Histórico vazio.")
        else:
            print("\n--- HISTÓRICO ---")

            for pagina in historico:
                print(pagina)

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")

# Uma pilha segue o LIFO (Last in, First out), que é "o último a entrar é o primeiro a sair",
# isso combina exatamente com o funcionamento do botão Voltar de um navegador.
# Se fosse uma fila FIFO (First In, First out), afinal queremos voltar para a última página visitada,
#não a primeira