def isNumberHere(num, tupla):
    for i in tupla:
        if num==i:
            return True

    return False

tupla = (3, 5, 9)
numero = int(input("Coloque um numero para verificar se ele esta presente na tupla: "))
print(isNumberHere(numero, tupla))