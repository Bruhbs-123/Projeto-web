from datetime import date, timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from animais.models import Animal

from .models import HistoricoVacina


def criar_animal():
    return Animal.objects.create(
        nome='Rex', especie='cachorro', idade=3, porte='M', cep='01001000',
    )


class ValidacaoVacinaTests(TestCase):
    def setUp(self):
        self.animal = criar_animal()

    def test_vacina_valida_passa(self):
        v = HistoricoVacina(
            animal=self.animal,
            nome_vacina='Antirrábica',
            data_aplicacao=date.today() - timedelta(days=10),
            proxima_dose=date.today() + timedelta(days=355),
        )
        v.clean()

    def test_proxima_dose_em_branco_passa(self):
        v = HistoricoVacina(
            animal=self.animal,
            nome_vacina='Giárdia',
            data_aplicacao=date.today(),
        )
        v.clean()

    def test_aplicacao_futura_gera_erro(self):
        v = HistoricoVacina(
            animal=self.animal,
            nome_vacina='V10',
            data_aplicacao=date.today() + timedelta(days=1),
        )
        with self.assertRaises(ValidationError):
            v.clean()

    def test_proxima_dose_antes_da_aplicacao_gera_erro(self):
        v = HistoricoVacina(
            animal=self.animal,
            nome_vacina='V10',
            data_aplicacao=date.today(),
            proxima_dose=date.today() - timedelta(days=1),
        )
        with self.assertRaises(ValidationError):
            v.clean()

    def test_proxima_dose_igual_a_aplicacao_gera_erro(self):
        v = HistoricoVacina(
            animal=self.animal,
            nome_vacina='V10',
            data_aplicacao=date.today(),
            proxima_dose=date.today(),
        )
        with self.assertRaises(ValidationError):
            v.clean()


class VacinasPendentesTests(TestCase):
    def setUp(self):
        self.animal = criar_animal()
        self.hoje = date.today()

    def pendentes(self):
        resposta = self.client.get(reverse('saude:vacinas_pendentes'))
        self.assertEqual(resposta.status_code, 200)
        return list(resposta.context['pendentes'])

    def test_vacina_com_proxima_dose_aparece(self):
        HistoricoVacina.objects.create(
            animal=self.animal, nome_vacina='Antirrábica',
            data_aplicacao=self.hoje - timedelta(days=60),
            proxima_dose=self.hoje - timedelta(days=30),
        )
        self.assertEqual(len(self.pendentes()), 1)

    def test_vacina_sem_proxima_dose_nao_aparece(self):
        HistoricoVacina.objects.create(
            animal=self.animal, nome_vacina='Giárdia',
            data_aplicacao=self.hoje - timedelta(days=60),
        )
        self.assertEqual(self.pendentes(), [])

    def test_pendencia_some_quando_vacina_e_reaplicada(self):
        HistoricoVacina.objects.create(
            animal=self.animal, nome_vacina='Antirrábica',
            data_aplicacao=self.hoje - timedelta(days=60),
            proxima_dose=self.hoje - timedelta(days=30),
        )
        HistoricoVacina.objects.create(
            animal=self.animal, nome_vacina='Antirrábica',
            data_aplicacao=self.hoje - timedelta(days=30),
        )
        self.assertEqual(self.pendentes(), [])