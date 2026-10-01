from django.urls import path
from . import views

urlpatterns = [
    path("", views.TutorListView.as_view(), name="tutor-list"),
    path("novo/", views.TutorCreateView.as_view(), name="tutor-create"),
    path("<int:pk>/editar/", views.TutorUpdateView.as_view(), name="tutor-update"),
    path("<int:pk>/excluir/", views.TutorDeleteView.as_view(), name="tutor-delete"),
    path("cep/<str:cep>/", views.consultar_cep, name="consultar-cep"),
]