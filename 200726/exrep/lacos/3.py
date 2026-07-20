while True:
    print("|                         |\n|     PROGRAMA INUTIL     |\n|                         |\n")
    print("|    *1: Repetidor de string     |\n|    *2: ChatGPT feito em 1 linha|\n|    *3: Sair                    |\n")
    x = int(input())
    match x:
        case 1:
            stringer = input("Digite a string a ser repetida:\n")
            print(f"\n{stringer}\n")
        case 2:
            pass
        case 3:
            break
        case _:
            print("Digite uma opção valida")
