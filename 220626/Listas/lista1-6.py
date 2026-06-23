caracter = input("Digite uma unica letra \n")
if caracter[0] != ('a' or 'e' or 'i' or 'u') and len(caracter) == 1:
    print(f"{caracter} eh consoante")
elif caracter[0] == ('a' or 'e' or 'i' or 'u') and len(caracter) == 1:
    print(f"{caracter} eh vogal")
else:
    print("Voce digitou mais de um caracter")