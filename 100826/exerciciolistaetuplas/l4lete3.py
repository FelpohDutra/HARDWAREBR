def somarIemListas(l1, l2):
    soma = [l1[n]+l2[n] for n in range (len(l1))]

    return soma


lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]

print(somarIemListas(lista1, lista2))