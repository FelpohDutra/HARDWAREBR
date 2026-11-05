from django.db import models

class Partida(models.Model):
    OPCOES = [
        ("pedra", "Pedra"),
        ("tesoura", "Tesoura"),
        ("papel", "Papel"),
    ]

    jogador = models.CharField(
        max_length=10, choices=OPCOES
    )
    computador = models.CharField(
        max_length=10, choices=OPCOES
    )
    resultado = models.CharField(
        max_length=10, choices=OPCOES
    )
    resultado = models.CharField(max_length=10)
    criada_em = models.DateTimeField(auto_now_add=True)

