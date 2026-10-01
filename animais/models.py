from django.db import models
from tutores.models import Tutor

class Animal(models.Model):
    PORTE_CHOICES = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]
    
    ESPECIE_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIE_CHOICES)
    raca = models.CharField(max_length=50, blank=True, null=True)
    idade = models.IntegerField(help_text="Idade em anos")
    porte = models.CharField(max_length=1, choices=PORTE_CHOICES)
    descricao = models.TextField(blank=True, null=True)
    cep = models.CharField(max_length=9, help_text="CEP de onde o animal se encontra")
    foto_url = models.URLField(blank=True, null=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True, blank=True, related_name='animais')
    disponivel_adocao = models.BooleanField(default=True)
    data_adocao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.especie})"