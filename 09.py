class Pessoa:
    def __init__(self, senha, nome, horario):
        self.senha = senha
        self.nome = nome
        self.horario = horario


def adicionar_pessoa(fila, proxima_senha):
    nome = input("\nDigite o nome: ")
    horario = input("Digite o horário de entrada: ")

    pessoa = Pessoa(proxima_senha, nome, horario)
    fila.append(pessoa)

    print("\nPessoa adicionada!")
    print("Senha:", pessoa.senha)

    return proxima_senha + 1


def chamar_proxima(fila):
    if len(fila) == 0:
        print("Não há pessoas aguardando.")
        return

    pessoa = fila.pop(0)

    print("\nChamando:")
    print("Senha:", pessoa.senha)
    print("Nome:", pessoa.nome)
    print("Horário:", pessoa.horario)


def consultar_proxima(fila):
    if len(fila) == 0:
        print("Não há pessoas aguardando.")
        return

    pessoa = fila[0]

    print("\nPróxima pessoa:")
    print("Senha:", pessoa.senha)
    print("Nome:", pessoa.nome)
    print("Horário:", pessoa.horario)


def exibir_fila(fila):
    if len(fila) == 0:
        print("Fila vazia.")
        return

    print("\n===== FILA DE ATENDIMENTO =====")

    for pessoa in fila:
        print(
            f"Senha: {pessoa.senha} | "
            f"Nome: {pessoa.nome} | "
            f"Horário: {pessoa.horario}"
        )


def main():
    fila = []
    proxima_senha = 1

    while True:
        print("\n===== SISTEMA DE ATENDIMENTO =====")
        print("1 - Adicionar pessoa")
        print("2 - Chamar próxima pessoa")
        print("3 - Consultar próxima pessoa")
        print("4 - Exibir fila")
        print("5 - Quantidade de pessoas")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            proxima_senha = adicionar_pessoa(
                fila, proxima_senha
            )

        elif opcao == "2":
            chamar_proxima(fila)

        elif opcao == "3":
            consultar_proxima(fila)

        elif opcao == "4":
            exibir_fila(fila)

        elif opcao == "5":
            print("Pessoas aguardando:", len(fila))

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida!")


main()