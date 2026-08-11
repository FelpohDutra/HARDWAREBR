def mostrarDados(lista):
    for i in lista:
        print(f"ITEM: {i[0]} | PREÇO POR UNIDADE: R${i[1]} | QUANTIDADE : {i[2]}")

def preçoEstoque(lista):
    soma = int()
    for i in lista:
        soma=soma+(i[1]*i[2])

    return soma

print("\n### SISTEMA DO MERCADINHO IF ###\n")

mercado = [('Pera', 1.60, 25), ('Abacate', 3, 10), ('Morango', 0.6, 150)]

mostrarDados(mercado)
print(f"Preço total do estoque: R${preçoEstoque(mercado)}")