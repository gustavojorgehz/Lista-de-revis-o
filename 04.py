def fatorial(numero):
    if numero == 1 or numero == 0:
        return 1

    return numero * fatorial(numero - 1)

numero = int(input("Digite um número natural: "))

if numero < 0:
    print("Digite um número natural ")
    return False

if numero >= 0:
    resultado = fatorial(numero)
    print(f"Resultado: ${resultado}")

    # Caso base: linha 2
    # O que aconteceria se o caso-base não existisse: A função iria continuar se chamando infinitamente
    # Qual seria uma versão não recursiva do mesmo algoritmo:

# def fatorial(n):
#     resultado = 1

#     for i in range(1, n + 1):
#         resultado = resultado * i

#     return resultado


# numero = int(input("Digite um número inteiro não negativo: "))

# if numero < 0:
#     print("Erro: o número deve ser não negativo.")
# else:
#     resultado = fatorial(numero)
#     print(f"{numero}! = {resultado}")



