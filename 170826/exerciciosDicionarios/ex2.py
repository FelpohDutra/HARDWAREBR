def inflacao(bateria, porcentual):
    bateria["preço"] = (bateria["preço"])*porcentual

    return bateria["preço"]


produto = {"nome": "Bateria", "preço": 1200, "quantidade": 2}
print("Formatação = aumento de 20% -> 1.2")
inflacaoValor = float(input(f"Digite o valor da inflação anual para ver o preço novo de uma bateria acustica (atualmente {produto["preço"]:.2f}):\n"))
produto["preço"] = inflacao(produto, inflacaoValor)

print(produto)