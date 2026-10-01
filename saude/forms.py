from django import forms

from .models import HistoricoVacina


class HistoricoVacinaForm(forms.ModelForm):
    class Meta:
        model = HistoricoVacina
        fields = ['animal', 'nome_vacina', 'data_aplicacao', 'proxima_dose']
        widgets = {
            'data_aplicacao': forms.DateInput(attrs={'type': 'date'}),
            'proxima_dose': forms.DateInput(attrs={'type': 'date'}),
        }