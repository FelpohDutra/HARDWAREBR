palavra = input()
for letra in palavra:
    if letra=='a':
        print(f"@")
    else:
        print(f"{letra}\n", end='')