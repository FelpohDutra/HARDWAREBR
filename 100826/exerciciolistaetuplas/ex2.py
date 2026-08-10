def listaPares(lista):
    pares = [n for n in lista if n%2==0]

    return pares

def listaImpares(lista):
    impares = [n for n in lista if n%3==0]

    return impares

print("Digite numeros para descobrir quais deles são pares e quais são impares.\nDigite 0 para parar de ler")
num = int(input())
listaTotal = []
while num !=0:
    listaTotal.append(num)
    num = int(input())

print(listaPares(listaTotal))
print(listaImpares(listaTotal))
    