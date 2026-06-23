nota = float(input("Digite a sua nota para ser classifica: \n"))

if nota >= 8:
    print(f"{nota} esta no grupo A")
elif nota >= 6 and nota <8:
    print(f"{nota} esta no grupo B")
else:
    print(f"{nota} esta no grupo C")