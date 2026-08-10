def listaPares(lista):
    0

def listaImpares(lista):
    0

print("Digite numeros para descobrir quais deles são pares e quais são impares.\nDigite 0 para parar de ler")
num = int(input())
listaTotal = []
while num !=0:
    listaTotal.append(num)
    num = int(input())

print(listaPares(listaTotal))
print(listaImpares(listaTotal))
    