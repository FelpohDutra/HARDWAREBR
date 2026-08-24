frase = input("Digite uma frase legalzuda:\n")

teste = {}
contador = 0

listafrase = (frase.split())


for palavra in frase.split():
    teste[palavra] = 0

for palavra in teste:
    for outraPalavra in listafrase:
        if palavra == outraPalavra:
            teste[palavra] += 1

print(teste)
'''
Resolução do professor:

for palavra in frase.split():
    if palavra not in teste:
        teste[palavra] = 1
    else: teste[palavra]+=1
'''