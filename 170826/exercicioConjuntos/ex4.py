def notasUnicas(l1):
    notaUnica = set(l1)

    return sorted(notaUnica)

notas = [10, 9, 7.5, 5, 10, 8, 9, 6, 7, 7.5, 3, 9.5]
print(notasUnicas(notas))