from django.urls import path
from . import views

urlpatterns = [
    path("", views.AnimalListView.as_view(), name="animal-list"),
    path("novo/", views.AnimalCreateView.as_view(), name="animal-create"),
    path("<int:pk>/editar/", views.AnimalUpdateView.as_view(), name="animal-update"),
    path("<int:pk>/excluir/", views.AnimalDeleteView.as_view(), name="animal-delete"),
]