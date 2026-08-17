def verificarProva(t1, t2):
    acertos = int()
    i = 0
    for resposta in aluno:
        if resposta == gabarito[i]:
            acertos=acertos+1
        i=+1
    
    return acertos

gabarito = ('a', 'b', 'a', 'c', 'e', 'd', 'e', 'b', 'a', 'd')

aluno=('a', 'b', 'e', 'e', 'd', 'c', 'b', 'a', 'd', 'd')

print(verificarProva(gabarito, aluno))