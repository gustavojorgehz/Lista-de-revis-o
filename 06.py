numeros = [10, 20, 5, 3]

def recursivo(lista):
    if len(lista) == 0:
        return 0

    return lista[0] + recursivo(lista[1:])

print(recursivo(numeros))

# [1:] significa que eu estou chamando todos os valores menos o primeiro da lista, no caso [20, 5, 3]