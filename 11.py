class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self, unidades):
        if unidades <= 0:
            print("A quantidade deve ser maior que zero.")
            return

        self.quantidade += unidades
        print("Unidades adicionadas ao estoque!")

    def retirar_estoque(self, unidades):
        if unidades <= 0:
            print("A quantidade deve ser maior que zero.")
            return

        if unidades > self.quantidade:
            print("Erro: estoque insuficiente!")
            return

        self.quantidade -= unidades
        print("Unidades retiradas do estoque!")

    def alterar_preco(self, novo_preco):
        if novo_preco < 0:
            print("O preço não pode ser negativo.")
            return

        self.preco = novo_preco
        print("Preço alterado com sucesso!")

    def calcular_valor_estoque(self):
        return self.preco * self.quantidade

    def exibir_dados(self):
        print("\n===== DADOS DO PRODUTO =====")
        print("Código:", self.codigo)
        print("Nome:", self.nome)
        print(f"Preço: R$ {self.preco:.2f}")
        print("Quantidade em estoque:", self.quantidade)
        print(
            f"Valor total: R$ "
            f"{self.calcular_valor_estoque():.2f}"
        )


def cadastrar_produto(produtos):
    codigo = int(input("Digite o código: "))

    for produto in produtos:
        if produto.codigo == codigo:
            print("Já existe um produto com esse código!")
            return

    nome = input("Digite o nome: ")
    preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    if preco < 0 or quantidade < 0:
        print("Preço e quantidade não podem ser negativos.")
        return

    produto = Produto(codigo, nome, preco, quantidade)
    produtos.append(produto)

    print("Produto cadastrado com sucesso!")


def buscar_produto(produtos):
    codigo = int(input("Digite o código do produto: "))

    for produto in produtos:
        if produto.codigo == codigo:
            return produto

    print("Produto não encontrado.")
    return None


def listar_produtos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        produto.exibir_dados()


def manipular_estoque(produtos):
    produto = buscar_produto(produtos)

    if produto is None:
        return

    print("\n1 - Adicionar unidades")
    print("2 - Retirar unidades")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        unidades = int(input("Quantidade para adicionar: "))
        produto.adicionar_estoque(unidades)

    elif opcao == "2":
        unidades = int(input("Quantidade para retirar: "))
        produto.retirar_estoque(unidades)

    else:
        print("Opção inválida!")


def alterar_preco_produto(produtos):
    produto = buscar_produto(produtos)

    if produto is None:
        return

    novo_preco = float(input("Digite o novo preço: "))
    produto.alterar_preco(novo_preco)


def main():
    produtos = [
        Produto(1, "Pão", 9.00, 20),
        Produto(2, "Cereal", 15.00, 10),
        Produto(3, "Iogurte", 8.00, 7)
    ]

    while True:
        print("\n===== SISTEMA DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Adicionar ou retirar estoque")
        print("5 - Alterar preço")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(produtos)

        elif opcao == "2":
            listar_produtos(produtos)

        elif opcao == "3":
            produto = buscar_produto(produtos)

            if produto is not None:
                produto.exibir_dados()

        elif opcao == "4":
            manipular_estoque(produtos)

        elif opcao == "5":
            alterar_preco_produto(produtos)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida!")


main()