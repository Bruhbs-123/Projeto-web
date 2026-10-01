from django.urls import path

from . import views

app_name = 'saude'

urlpatterns = [
    path('vacinas/', views.VacinaListView.as_view(), name='vacina_list'),
    path('vacinas/nova/', views.VacinaCreateView.as_view(), name='vacina_create'),
    path('vacinas/<int:pk>/editar/', views.VacinaUpdateView.as_view(), name='vacina_update'),
    path('vacinas/<int:pk>/excluir/', views.VacinaDeleteView.as_view(), name='vacina_delete'),
]