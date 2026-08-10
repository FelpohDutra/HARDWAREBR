def gerar_confrontos(dupla1, dupla2):
    for pessoa in dupla1:
        for individuo in dupla2:
            print(f"{pessoa} x {individuo}")


dupla1 = ('Felipe', 'Caio')
dupla2 = ('Pedro', 'Ricardo')

gerar_confrontos(dupla1, dupla2)