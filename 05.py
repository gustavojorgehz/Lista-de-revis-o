# Versão recursiva
def recursivo(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return recursivo(n - 1) + recursivo(n - 2)


numero = int(input("Digite o valor de n: "))

if numero < 0:
    print("Erro: n deve ser um número não negativo.")
else:
    resultado = recursivo(numero)
    print(f"O {numero}º termo de Fibonacci é: {resultado}")


# Versão utilizando repetição

def repeticao(n):
    if n == 0:
        return 0

    a = 0
    b = 1

    for i in range(2, n + 1):
        proximo = a + b
        a = b
        b = proximo

    return b


numero = int(input("Digite o valor de n: "))

if numero < 0:
    print("Erro: n deve ser um número não negativo.")
else:
    resultado = repeticao(numero)
    print(f"O {numero}º termo de Fibonacci é: {resultado}")


# A versão que utiliza repetição é mais efeciente, 
# porque ela calcula cada valor elevado de n só uma vez,
# ja a versão recursiva calcula o n várias vezes.