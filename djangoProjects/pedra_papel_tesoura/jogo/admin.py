from django.contrib import admin
from .models import Partida

# Register your models here.
@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = (
        "jogador", "computador",
        "resultado", "criada_em"
    )
    list_filter = ("jogador", )
    search_fields = ("jogador", "computador")