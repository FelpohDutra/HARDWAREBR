conta = float(input("Digite o valor total da conta: \n"))
dinheiro = float(input("Digite o valor que voce ira pagar: \n"))

if dinheiro<conta:
    print("Dinheiro insuficiente")
else:
    print("Conta paga")
    if dinheiro>conta:
        print(f"Troco: {dinheiro-conta:.2f}")