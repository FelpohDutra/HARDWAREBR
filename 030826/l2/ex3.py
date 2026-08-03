def tempoSegundos(h,m,s):
    return ((h*3600)+(m*60)+s)

print("Digite hora, minuto e segundos (um de cada vez) para ver o total em segundos:")
x1 = int(input(""))
x2 = int(input(""))
x3 = int(input(""))

print(f"O tempo total em segundos é de: {tempoSegundos(x1,x2,x3)}")