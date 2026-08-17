quadrantes = {1: "Primeiro", 2: "Segundo", 3: "Terceiro", 4:"Quarto", 5: "Meio"}


print(quadrantes)

for chaves in quadrantes:
    print(chaves)
print("\n")
for chaves in quadrantes:
    print(quadrantes[chaves])
print("\n")
if 3 in quadrantes:
    print(quadrantes[3])