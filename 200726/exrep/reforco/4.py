x = int(0)
quant = 0
soma = 0

print("Digite numeros positivos para fazer a media desses. Programa encerra com numeros negativos")
while x>=0:
    x = float(input())
    if x>=0:
        quant+=1
        soma+=x
    else:
        break
print(f"Media aritmetica dos numeros: {soma/quant:.2f}")