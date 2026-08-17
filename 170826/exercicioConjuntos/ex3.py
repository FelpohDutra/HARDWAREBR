amigosPedro = {'Felipe', 'Caio', 'Ruan', 'Ricardo'}
amigosMaria = {'Felipe', 'Ruan', 'Bruna', 'Ana Julia'}

print(amigosMaria | amigosPedro)
print(amigosPedro - amigosMaria)
print(amigosMaria - amigosPedro)
print((amigosPedro | amigosMaria) - (amigosPedro & amigosMaria))