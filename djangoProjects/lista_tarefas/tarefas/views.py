from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tarefas
from .forms import TarefaForm

# import random

def lista_tarefas(request):
    status = request.GET.get("status", "todas")

    tarefas = Tarefas.objects.all()
    if status == "pendentes":
        tarefas = tarefas.filter(concluida=False)
    elif status == "concluidas":
        tarefas = tarefas.filter(concluida=True)
    else:
        status = "todas"

    return render(request, "tarefas/lista.html", {
        "tarefas": tarefas,
        "status": status,
    })

def criar_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tarefas")
    else:
        form = TarefaForm()
    return render(request, "tarefas/formulario.html", {"form": form})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefas, pk=pk)
    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect("detalhe_tarefa", pk=tarefa.pk)
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, "tarefas/formulario.html", {"form": form, "tarefa": tarefa})

@require_POST
def alternar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefas, pk=pk)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect("detalhe_tarefa", pk=tarefa.pk)

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefas, pk=pk)
    if request.method == "POST":
        tarefa.delete()
        return redirect("lista_tarefas")
    return render(request, "tarefas/excluir.html", {"tarefa": tarefa})

def detalhe_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefas, pk=pk)
    return render(request, "tarefas/detalhe.html", {"tarefa": tarefa})