from datetime import date, timedelta
from unittest.mock import Mock, patch

import requests
from django.test import TestCase
from django.urls import reverse

from . import services
from .models import Animal


def resposta_falsa(status=200, dados=None):
    resposta = Mock()
    resposta.status_code = status
    resposta.json.return_value = dados
    return resposta


def criar_animal(**extra):
    dados = dict(nome='Rex', especie='cachorro', idade=3, porte='M', cep='01001000')
    dados.update(extra)
    return Animal.objects.create(**dados)


class ServicesTests(TestCase):
    @patch('animais.services.requests.get')
    def test_listar_racas_retorna_id_e_nome_ordenados(self, mock_get):
        mock_get.return_value = resposta_falsa(200, [
            {'id': 'beng', 'name': 'Bengal'},
            {'id': 'abys', 'name': 'Abyssinian'},
        ])
        racas = services.listar_racas('gato')
        self.assertEqual(len(racas), 2)
        self.assertEqual(racas[0], {'id': 'abys', 'nome': 'Abyssinian'})

    @patch('animais.services.requests.get')
    def test_chamada_usa_timeout_de_5_segundos(self, mock_get):
        mock_get.return_value = resposta_falsa(200, [])
        services.listar_racas('cachorro')
        self.assertEqual(mock_get.call_args.kwargs['timeout'], 5)

    def test_especie_sem_api_gera_erro(self):
        with self.assertRaises(services.ErroAPI):
            services.listar_racas('outro')

    @patch('animais.services.requests.get')
    def test_timeout_gera_erro_tratado(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout
        with self.assertRaises(services.ErroAPI):
            services.listar_racas('gato')

    @patch('animais.services.requests.get')
    def test_falha_de_rede_gera_erro_tratado(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError
        with self.assertRaises(services.ErroAPI):
            services.listar_racas('gato')

    @patch('animais.services.requests.get')
    def test_chave_invalida_401(self, mock_get):
        mock_get.return_value = resposta_falsa(401, {})
        with self.assertRaises(services.ErroAPI):
            services.listar_racas('cachorro')

    @patch('animais.services.requests.get')
    def test_limite_de_requisicoes_429(self, mock_get):
        mock_get.return_value = resposta_falsa(429, {})
        with self.assertRaises(services.ErroAPI):
            services.buscar_foto('gato', 'abys')

    @patch('animais.services.requests.get')
    def test_buscar_foto_retorna_url(self, mock_get):
        mock_get.return_value = resposta_falsa(200, [{'url': 'https://exemplo.com/gato.jpg'}])
        self.assertEqual(
            services.buscar_foto('gato', 'abys'),
            'https://exemplo.com/gato.jpg',
        )

    @patch('animais.services.requests.get')
    def test_buscar_foto_lista_vazia_retorna_none(self, mock_get):
        mock_get.return_value = resposta_falsa(200, [])
        self.assertIsNone(services.buscar_foto('gato', 'abys'))


class EndpointsTests(TestCase):
    @patch('animais.services.listar_racas')
    def test_endpoint_racas_ok(self, mock_listar):
        mock_listar.return_value = [{'id': 'abys', 'nome': 'Abyssinian'}]
        resposta = self.client.get(reverse('animal-racas', args=['gato']))
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()['racas'][0]['nome'], 'Abyssinian')

    @patch('animais.services.listar_racas')
    def test_endpoint_racas_erro_da_api_retorna_400(self, mock_listar):
        mock_listar.side_effect = services.ErroAPI('A API demorou demais para responder.')
        resposta = self.client.get(reverse('animal-racas', args=['gato']))
        self.assertEqual(resposta.status_code, 400)
        self.assertIn('erro', resposta.json())

    @patch('animais.services.buscar_foto')
    def test_endpoint_foto_ok(self, mock_foto):
        mock_foto.return_value = 'https://exemplo.com/gato.jpg'
        resposta = self.client.get(reverse('animal-foto', args=['gato', 'abys']))
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()['foto_url'], 'https://exemplo.com/gato.jpg')

    @patch('animais.services.buscar_foto')
    def test_endpoint_foto_sem_imagem(self, mock_foto):
        mock_foto.return_value = None
        resposta = self.client.get(reverse('animal-foto', args=['gato', 'abys']))
        self.assertEqual(resposta.status_code, 200)
        self.assertIsNone(resposta.json()['foto_url'])


class RelatorioAdocoesTests(TestCase):
    def test_mostra_so_adocoes_do_mes_atual(self):
        hoje = date.today()
        mes_passado = hoje.replace(day=1) - timedelta(days=1)
        criar_animal(nome='AdotadoHoje', disponivel_adocao=False, data_adocao=hoje)
        criar_animal(nome='AdotadoAntigo', disponivel_adocao=False, data_adocao=mes_passado)
        criar_animal(nome='SemAdocao')

        resposta = self.client.get(reverse('animal-relatorio-adocoes'))

        self.assertEqual(resposta.status_code, 200)
        nomes = [a.nome for a in resposta.context['adotados']]
        self.assertEqual(nomes, ['AdotadoHoje'])

    def test_mes_invalido_nao_quebra(self):
        resposta = self.client.get(reverse('animal-relatorio-adocoes') + '?mes=abc')
        self.assertEqual(resposta.status_code, 200)