from django.shortcuts import render
from .models import Partida
import random


# Create your views here.

def boas_vindas(request):
    return render(
        request,
        'jogo/boas_vindas.html'
    )

def historico(request):
    
    partidas = Partida.objects.order_by(
        "-criada_em",
    )
    
    #Mostrar somente partidas que o jogador escolheu pedra

    #partidas = Partida.objects.filter(jogador='pedra').order_by(
    #    "-criada_em"
    #)
    
    vitorias = Partida.objects.filter(resultado='vitoria').count()
    derrotas = Partida.objects.filter(resultado='derrota').count()
    empates = Partida.objects.filter(resultado='empate').count()

    return render(request,
                  "jogo/historico.html",
                  {
                      "partidas": partidas,
                      "vitorias": vitorias,
                      "derrotas": derrotas,
                      "empates": empates,
                  })

OPCOES = ['pedra', 'papel', 'tesoura']

def jogar(request):
    jogada_usuario = request.GET.get('jogada', None)
    ctx = {'jogada_usuario': jogada_usuario}

    if jogada_usuario in OPCOES:
        jogada_pc = random.choice(OPCOES)
        ctx['jogada_pc'] = jogada_pc

        if jogada_usuario == jogada_pc:
            resultado = 'empate'
        elif (
            (jogada_usuario == 'pedra' and jogada_pc == 'tesoura') or
            (jogada_usuario == 'papel' and jogada_pc == 'pedra') or
            (jogada_usuario == 'tesoura' and jogada_pc == 'papel')
        ):
            resultado = 'vitoria'
        else:
            resultado = 'derrota'

        ctx['resultado'] = resultado

        Partida.objects.create(
            jogador=jogada_usuario,
            computador=jogada_pc,
            resultado=resultado,
        )

    return render(
        request, 'jogo/jogar.html', ctx
    )

