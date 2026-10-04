from datetime import date

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from . import services
from .models import Animal

CAMPOS = ["nome", "especie", "raca", "idade", "porte", "descricao",
          "cep", "foto_url", "tutor", "disponivel_adocao", "data_adocao"]

class AnimalListView(ListView):
    model = Animal

class AnimalCreateView(CreateView):
    model = Animal
    fields = CAMPOS
    success_url = reverse_lazy("animal-list")

class AnimalUpdateView(UpdateView):
    model = Animal
    fields = CAMPOS
    success_url = reverse_lazy("animal-list")

class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy("animal-list")


def racas(request, especie):
    try:
        lista = services.listar_racas(especie)
    except services.ErroAPI as e:
        return JsonResponse({"erro": str(e)}, status=400)
    return JsonResponse({"racas": lista})


def foto(request, especie, raca_id):
    try:
        url = services.buscar_foto(especie, raca_id)
    except services.ErroAPI as e:
        return JsonResponse({"erro": str(e)}, status=400)
    if url is None:
        return JsonResponse({"foto_url": None, "aviso": "Essa raça não tem foto disponível."})
    return JsonResponse({"foto_url": url})


def relatorio_adocoes(request):
    hoje = date.today()
    mes_texto = request.GET.get("mes", hoje.strftime("%Y-%m"))

    try:
        ano, mes = map(int, mes_texto.split("-"))
        date(ano, mes, 1)
    except ValueError:
        ano, mes = hoje.year, hoje.month
        mes_texto = hoje.strftime("%Y-%m")

    adotados = (
        Animal.objects
        .filter(data_adocao__year=ano, data_adocao__month=mes)
        .select_related("tutor")
        .order_by("data_adocao")
    )

    return render(request, "animais/relatorio_adocoes.html", {
        "adotados": adotados,
        "mes_texto": mes_texto,
        "ano": ano,
        "mes": mes,
    })