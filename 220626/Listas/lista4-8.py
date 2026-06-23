x = int(input())
y = int(input())
z = int(input())

if x<(y+z) and y<(z+x) and z<(y+x):
    print("Triangulo valido")
    if (x == y) and (y == z):
        print("Triangulo equilatero")
    elif (x == y and y!=z) or (y==z and z!=x) or (x==z and z!=y):
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")
else:
    print("Triangulo nao valido")