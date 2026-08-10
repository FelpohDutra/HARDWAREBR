def pares(lista):
    pares = 0
    for num in lista:
        if num%2==0:
            pares=pares+1

    return pares

lista = []

for num in range(0,5):
    n = int(input())
    lista.insert(num, n)

print((pares(lista)))