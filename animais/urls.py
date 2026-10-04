from django.urls import path
from . import views

urlpatterns = [
    path("", views.AnimalListView.as_view(), name="animal-list"),
    path("novo/", views.AnimalCreateView.as_view(), name="animal-create"),
    path("<int:pk>/editar/", views.AnimalUpdateView.as_view(), name="animal-update"),
    path("<int:pk>/excluir/", views.AnimalDeleteView.as_view(), name="animal-delete"),
    path("racas/<str:especie>/", views.racas, name="animal-racas"),
    path("foto/<str:especie>/<str:raca_id>/", views.foto, name="animal-foto"),
    path("relatorio/adocoes/", views.relatorio_adocoes, name="animal-relatorio-adocoes"),
]