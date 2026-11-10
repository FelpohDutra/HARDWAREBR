from django.db import models

# Create your models here.

class Tarefas(models.Model):
    TIPOS = [
        ("baixa", "Baixa"),
        ("media", "Media"),
        ("alta", "Alta"),
    ]

    titulo = models.CharField(max_length=120)
    descricao = models.TextField(max_length=150)
    prioridade = models.CharField(max_length=10, choices=TIPOS)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo