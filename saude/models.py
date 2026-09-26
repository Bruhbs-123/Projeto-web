from django.db import models
from animais.models import Animal

class HistoricoVacina(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='vacinas')
    nome_vacina = models.CharField(max_length=100)
    data_aplicacao = models.DateField()
    proxima_dose = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome_vacina} - {self.animal.nome}"

class Consulta(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='consultas')
    data_consulta = models.DateTimeField()
    veterinario = models.CharField(max_length=100)
    diagnostico = models.TextField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consulta {self.animal.nome} em {self.data_consulta.strftime('%d/%m/%Y')}"
