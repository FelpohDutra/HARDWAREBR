print("## CALCULADORA SO DE INTEIROS ##")

n1 = int((input("Digite o primeiro numero: \n")))
n2 = int((input("Digite o segundo numero: \n")))
op = input("Digite o operando (+, -, * ou /) \n")

match op:
    case "+":
        print(f"{n1+n2}")
    case "-":
        print(f"{n1-n2}")
    case "*":
        print(f"{n1*n2}")
    case "/":
        print(f"{n1/n2}")
    case _:
        print("Voce nao digitou um operando valido")