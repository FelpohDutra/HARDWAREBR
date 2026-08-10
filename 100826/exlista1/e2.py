def maiorNum(lista):
    maiorrNum=lista[0]
    for num in lista:
        if maiorrNum<=num:
            maiorrNum=num

    return maiorrNum

lista = []

for num in range(0,5):
    n = int(input())
    lista.insert(num, n)

print((maiorNum(lista)))
