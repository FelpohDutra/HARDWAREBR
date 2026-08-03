def maiorNum(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    return n3

print("Digite 3 numeros (um de cada vez) para verificar qual o maior:")
x1 = int(input(""))
x2 = int(input(""))
x3 = int(input(""))

print(maiorNum(x1,x2,x3))