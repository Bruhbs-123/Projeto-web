from datetime import date

from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import HistoricoVacinaForm
from .models import HistoricoVacina


class VacinaListView(ListView):
    model = HistoricoVacina
    context_object_name = 'vacinas'

    def get_queryset(self):
        return HistoricoVacina.objects.select_related('animal').order_by('-data_aplicacao')


class VacinaCreateView(CreateView):
    model = HistoricoVacina
    form_class = HistoricoVacinaForm
    success_url = reverse_lazy('saude:vacina_list')


class VacinaUpdateView(UpdateView):
    model = HistoricoVacina
    form_class = HistoricoVacinaForm
    success_url = reverse_lazy('saude:vacina_list')


class VacinaDeleteView(DeleteView):
    model = HistoricoVacina
    success_url = reverse_lazy('saude:vacina_list')


def vacinas_pendentes(request):
    hoje = date.today()

    aplicada_depois = HistoricoVacina.objects.filter(
        animal=OuterRef("animal"),
        nome_vacina=OuterRef("nome_vacina"),
        data_aplicacao__gt=OuterRef("data_aplicacao"),
    )

    pendentes = (
        HistoricoVacina.objects
        .filter(proxima_dose__isnull=False)
        .annotate(ja_aplicada=Exists(aplicada_depois))
        .filter(ja_aplicada=False)
        .select_related("animal")
        .order_by("proxima_dose")
    )

    return render(request, "saude/vacinas_pendentes.html", {
        "pendentes": pendentes,
        "hoje": hoje,
    })