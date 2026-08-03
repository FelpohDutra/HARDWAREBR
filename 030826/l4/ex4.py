def desenharTriangulo():
    print("  #  \n ### \n#####\n")

def desenharQuadrado():
    print("#####\n#   #\n#   #\n#   #\n#####")


print("Desenhador de figuras chato para caramba de fazer meu deus do ceu:\n1 - Triangulo\n2 - Quadrado\n3 - Sair")
opcao = int(input())
while opcao!=3:
    print("Desenhador de figuras chato para caramba de fazer meu deus do ceu:\n1 - Triangulo\n2 - Quadrado\n3 - Sair")
    match opcao:
        case 1:
            desenharTriangulo()
        case 2:
            desenharQuadrado()
        case _:
            print("Digite um numero valido. Por favor. Nao me de mais trabalho do que eu ja tenho")
    opcao = int(input())