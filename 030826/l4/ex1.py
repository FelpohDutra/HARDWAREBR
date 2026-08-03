def isSenhaForte(senha):
    hasDigit = False
    senhaSize = len(senha)

    for i in range(0, senhaSize):
        if senha[i].isdigit() == True:
            hasDigit = True
            break

    if hasDigit == True and senhaSize>=8:
        return True
    
    return False



passwd = input("Digite sua senha para verificar se ela é forte:\n")
print(isSenhaForte(passwd))
