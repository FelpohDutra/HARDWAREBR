print("Digite um numero e veja se o numero eh primo. Para sair do programa, digite 0")

while True:
    is_primo = True
    x = int(input())
    if x==0:
        break
    elif x<0:
        print("Digite um numero valido")
    else:
        for i in range(2, x):
            if x%i==0:
                is_primo = False
                break
    print(is_primo)

# Fazer o anti-teste, verificar se qualquer numero >1 e <x %==0, se sim, o numero nao é primo.