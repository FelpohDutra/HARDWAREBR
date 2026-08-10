def maiorTemp(lista):
    return max(lista)

def menorTemp(lista):
    return min(lista)

def mediaTemp(lista):
    return sum(lista)/len(lista)
    

lista = []

for num in range(0,7):
    n = int(input())
    lista.insert(num, n)

tempdays = tuple(lista)



print(f"{tempdays}\n")

print(maiorTemp(tempdays))
print(menorTemp(tempdays))
print(mediaTemp(tempdays))
