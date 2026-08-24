frase = input("Digite uma frase legalzuda:\n")
frase2 = input("Digite uma segunda frase legalzuda:\n")

conj1 = set(frase.split())
conj2 = set(frase2.split())

print("Palavras que aparecem em ambos os textos")
print(conj1 & conj2)
print("Somente em A")
print(conj1 - conj2)
print("Somente em B")
print(conj2 - conj1)
print("Palavras que aparecem em exatamente em só um dos textos")
print((conj1 | conj2) - (conj1 & conj2))
