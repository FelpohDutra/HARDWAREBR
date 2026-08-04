def isMaior(idade):
    if idade>=18:
        return "Maior"
    return "Menor"
    
x = int(input("Digite a sua idade para descobrir se voce eh maior ou nao de idade:\n"))
print(isMaior(x))