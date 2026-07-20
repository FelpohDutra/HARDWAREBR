usuario = input("Digite seu nome do login\n")
senha = "senha"
print("Digite a senha correta. Ao acertar, o login no sistema sera feito.")
while True:
    n = input()
    if n==senha: break
print(f"Bem-vinda(o) ao sistema, {usuario}")