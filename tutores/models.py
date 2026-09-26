from django.db import models

class Tutor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return self.nome