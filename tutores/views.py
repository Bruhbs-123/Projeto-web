from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tutor
from django.http import JsonResponse
from .services import buscar_endereco, ViaCEPError

class TutorListView(ListView):
    model = Tutor

class TutorCreateView(CreateView):
    model = Tutor
    fields = "__all__"
    success_url = reverse_lazy("tutor-list")

class TutorUpdateView(UpdateView):
    model = Tutor
    fields = "__all__"
    success_url = reverse_lazy("tutor-list")

class TutorDeleteView(DeleteView):
    model = Tutor
    success_url = reverse_lazy("tutor-list")

def consultar_cep(request, cep):
    try:
        return JsonResponse(buscar_endereco(cep))
    except ViaCEPError as e:
        return JsonResponse({"erro": str(e)}, status=400)