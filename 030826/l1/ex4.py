import time as tm

def pedirCafe(tipoCafe, tamanho="medio"):
    print(f"Seu pedido é um: {tipoCafe}, de tamanho {tamanho} ?")

print("Bem-vinda(o) ao IF café!")
tm.sleep(1)
print("Peça seu café, depois revisaremos o seu pedido.")
tm.sleep(1)
tipoCafe = input("Como voce quer seu café (Espresso, Machiato, Frappe, etc)? ")
pedirCafe(tipoCafe)