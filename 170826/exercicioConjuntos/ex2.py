cores = set()

print("Digite 5 cores, uma por vez, depois uma cor para remover")
i = 0
while i<5:
    i+=1
    coresDigitas = input()
    cores.add(coresDigitas)
coresDigitas = input("Agora remova uma cor: ")
cores.discard(coresDigitas)
print(cores)