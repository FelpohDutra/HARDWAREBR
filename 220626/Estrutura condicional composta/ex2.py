x = float(input("Digite um numero para compara-lo com outro \n"))
y = float(input("Agora digite o outro numero \n"))
maior = 0.0
menor = 0.0

if x > y :
    maior = x
    menor = y
else:
    maior = y
    menor = x

print(f"{maior} eh maior do que {menor}")
