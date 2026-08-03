def desenharTriangulo():
    0

def desenharQuadrado():
    0


print("Desenhador de figuras chato para caramba de fazer meu deus do ceu:\n1 - Triangulo\n2 - Quadrado\n3 - Sair")

while opcao!=3:
    opcao = int(input())
    match opcao:
        case 1:
            desenharTriangulo()
        case 2:
            desenharQuadrado()
        case _:
            print("Digite um numero valido. Por favor. Nao me de mais trabalho do que eu ja tenho")