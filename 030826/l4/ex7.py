import os

def isAprovado(m):
    if m>=6:
        print("Aprovado!")
    else:
        print("Reprovado...")

def mediaNotas(n1, n2):
    return (n1+n2)/2

def lerNotas():
    x = float(input("Digite o valor da prova: \n"))
    while x>11 or x<0:
        x = float(input("Digite um numero válido entre 0 a 10.\n"))
    return x

os.system('cls')
main = 1
while main!=0:
    print(" - Programa para verificar se você esta aprovado ou não em uma matéria - \n - 1: Digitar notas (2)\n - 0: Sair")
    main = int(input())
    match main:
        case 1:
            os.system('cls')
            print(" - (1)")
            n1 = lerNotas()
            print(" - (2)")
            n2 = lerNotas()
            media = mediaNotas(n1,n2)
            isAprovado(media)
        case 0:
            break
        case _:
            print("Digite um numero valido")