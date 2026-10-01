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
