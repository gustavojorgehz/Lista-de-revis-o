def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b == 0: return print("Não é possível dividir por zero")
    return a / b

def potenciacao(a,b):
    a ** b

def resto(a,b):
    if b == 0: print("Não é possível dividir por zero")
    return a % b

def menu():
    print("\n Calculadora Modular")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - potenciação")
    print("6 - resto da divisão")
    print("0- encerrar programa")

def main():
    while true:
        menu()

        opcao = input("Escolha a opção pelo número: ")

        if opcao == 0:
            print("Programa encerrado.")
            break

        if opcao not in ["1","2","3","4","5","6"]:
            print("Opção inválida.")
            continue

        a = float(input("Digite um número: "))
        b = float(input("Digite outro número: "))

        if opcao == "1":
            resultado = soma(a,b)
       
        elif opcao =="2":
            resultado = subtracao(a,b)

        elif opcao == "3":
            resultado = multiplicacao(a,b)

        elif opcao == "4":
            resultado = divisao(a,b)

        elif opcao == "5":
            resultado = potenciacao(a,b)

        elif opcao == "6":
            resultado = resto(a,b)

        print(f"Resultado ${resultado}") 