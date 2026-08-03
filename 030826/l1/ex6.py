def tipoIngresso(idade):
    if idade<=12 or idade>=60:
        print("Preço do Ingresso é R$10,00")
    else:
        print("Preço do Ingresso é R$20,00")

i = int(input("CINEMA - Quantos anos você tem? "))

tipoIngresso(i)