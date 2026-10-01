from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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