soma = 0
print("Digite numeros para serem somados.\nO NUMERO 0 ENCERRA A SOMA")
while True:
    n = float(input())
    soma=soma+n
    if n==0: break
print(f"Soma final: {soma:.2f}")