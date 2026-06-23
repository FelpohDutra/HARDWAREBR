idade = int(input("Digite a sua idade para saber suas informacoes da eleicao \n"))

if idade >= 18:
    print("Voce eh obrigado a votar")
elif idade >=16 and idade < 18:
    print("Voce pode votar, opcional")
else:
    print("Voce nao possui idade suficiente para votar")