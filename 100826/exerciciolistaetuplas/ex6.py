def cadastrarItem(nome, quantidade, valor):
    ''' Fazer tupla '''
    item = (nome, quantidade, valor)
    
    return item
    

estoque = []
escolha = int()
while escolha!=3:
    print("\n### ESTOQUE DO IF ###\n- 1: Cadastrar Item\n- 2: Listar Itens\n- 3: Sair")
    escolha = int(input(""))
    if escolha==1:
        nomeItem = input("\nDigite o nome do item: ")
        quantidadeItem = int(input(f"Digite a quantidade de {nomeItem}: "))
        valorItem = float(input(f"Digite o preço de {nomeItem}: "))
        estoque.append(cadastrarItem(nomeItem, quantidadeItem, valorItem))
    elif escolha==2:
        if not estoque:
            print("Estoque vazio")
        else:
            print("\nItens:")
            for item in estoque:
                print(f"{item[0]} | Quantidade: {item[1]} | Preço: R$ {item[2]:.2f} (R${(item[2] * item[1]):.2f})")
print("\n### Finalizando sistema ###")
