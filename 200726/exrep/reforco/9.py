print("Digite um numero e veja se o numero eh primo. Para sair do programa, digite 0")

while True:
    x = int(input())
    if x==0:
        break
    elif x<0:
        print("Digite um numero valido")
    else:
        for i in range(1, x):
            if x%i==0 and (i!=1 or i!=(x)):
                print("Numero nao eh primo")
        else:
            print("Numero primo")