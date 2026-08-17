pessoa = {"nome": "Felipe", "idade": 19, "cidade": "Mogi das Cruzes"}

print(pessoa)

pessoa["idade"] = 20
pessoa["profissao"] = "Estudante"
pessoa.pop("cidade", "sem cidade")
print(pessoa)