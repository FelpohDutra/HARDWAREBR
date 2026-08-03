def isPar(x):
    if x%2==0:
        return True
    return False

x = int(input("Digite um numero para verificar se ele é par:\n"))
print(isPar(x))