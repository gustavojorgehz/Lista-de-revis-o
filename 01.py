lista = [3,2,3,5,0,9,7,3]

def validacao(lista):
    return all(isinstance(i, int) and not isinstance(i, bool) for i in lista)

def maior(n):
    maior = n[0]
    for i in n:
        if i > maior:
            maior = i
    return maior

def menor(n):
    menor = n[0]
    for i in n:
        if i < menor:
            menor = i
    return menor

def media(lista):
    soma = 0
    for n in lista:
        soma += n
    return soma / len(lista)

def contar_pares(lista):
    contador = 0
    for n in lista:
        if n % 2 == 0:
            contador += 1
    return contador

def contar_impares(lista):
    contador = 0
    for n in lista:
        if n % 2 != 0:
            contador += 1
    return contador


print(maior(lista), "\n")
print(menor(lista), "\n")
print(media(lista), "\n")
print(contar_pares(lista), "\n")
print(contar_impares(lista), "\n")