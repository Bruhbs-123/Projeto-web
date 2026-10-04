from unittest.mock import Mock, patch

import requests
from django.test import TestCase
from django.urls import reverse

from .services import ViaCEPError, buscar_endereco

DADOS_SE = {
    'cep': '01001-000',
    'logradouro': 'Praça da Sé',
    'bairro': 'Sé',
    'localidade': 'São Paulo',
    'uf': 'SP',
}


def resposta_falsa(dados):
    resposta = Mock()
    resposta.json.return_value = dados
    return resposta


class BuscarEnderecoTests(TestCase):
    @patch('tutores.services.requests.get')
    def test_cep_valido_retorna_endereco_completo(self, mock_get):
        mock_get.return_value = resposta_falsa(DADOS_SE)
        resultado = buscar_endereco('01001000')
        self.assertEqual(resultado['cep'], '01001000')
        self.assertEqual(resultado['endereco'], 'Praça da Sé, Sé, São Paulo, SP')

    @patch('tutores.services.requests.get')
    def test_cep_com_traco_e_limpo_antes_da_consulta(self, mock_get):
        mock_get.return_value = resposta_falsa(DADOS_SE)
        buscar_endereco('01001-000')
        self.assertEqual(
            mock_get.call_args.args[0],
            'https://viacep.com.br/ws/01001000/json/',
        )

    @patch('tutores.services.requests.get')
    def test_cep_inexistente_gera_erro(self, mock_get):
        mock_get.return_value = resposta_falsa({'erro': 'true'})
        with self.assertRaisesMessage(ViaCEPError, 'CEP não encontrado.'):
            buscar_endereco('99999999')

    @patch('tutores.services.requests.get')
    def test_cep_com_menos_de_8_digitos_gera_erro_sem_chamar_a_api(self, mock_get):
        with self.assertRaisesMessage(ViaCEPError, 'CEP deve ter 8 dígitos.'):
            buscar_endereco('123')
        mock_get.assert_not_called()

    @patch('tutores.services.requests.get')
    def test_cep_vazio_gera_erro(self, mock_get):
        with self.assertRaisesMessage(ViaCEPError, 'CEP deve ter 8 dígitos.'):
            buscar_endereco('')
        mock_get.assert_not_called()

    @patch('tutores.services.requests.get')
    def test_timeout_gera_erro_tratado(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout
        with self.assertRaisesMessage(ViaCEPError, 'A ViaCEP demorou demais para responder.'):
            buscar_endereco('01001000')

    @patch('tutores.services.requests.get')
    def test_falha_de_rede_gera_erro_tratado(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError
        with self.assertRaisesMessage(ViaCEPError, 'Não foi possível consultar a ViaCEP.'):
            buscar_endereco('01001000')

    @patch('tutores.services.requests.get')
    def test_resposta_http_com_erro_gera_erro_tratado(self, mock_get):
        resposta = Mock()
        resposta.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = resposta
        with self.assertRaises(ViaCEPError):
            buscar_endereco('01001000')

    @patch('tutores.services.requests.get')
    def test_resposta_que_nao_e_json_gera_erro_tratado(self, mock_get):
        resposta = Mock()
        resposta.json.side_effect = ValueError
        mock_get.return_value = resposta
        with self.assertRaises(ViaCEPError):
            buscar_endereco('01001000')

    @patch('tutores.services.requests.get')
    def test_chamada_usa_timeout_de_5_segundos(self, mock_get):
        mock_get.return_value = resposta_falsa(DADOS_SE)
        buscar_endereco('01001000')
        self.assertEqual(mock_get.call_args.kwargs['timeout'], 5)

    @patch('tutores.services.requests.get')
    def test_endereco_ignora_partes_vazias(self, mock_get):
        mock_get.return_value = resposta_falsa({
            'logradouro': '',
            'bairro': '',
            'localidade': 'Cidade Pequena',
            'uf': 'XX',
        })
        resultado = buscar_endereco('12345678')
        self.assertEqual(resultado['endereco'], 'Cidade Pequena, XX')


class EndpointCepTests(TestCase):
    @patch('tutores.views.buscar_endereco')
    def test_cep_valido_retorna_200(self, mock_buscar):
        mock_buscar.return_value = {'cep': '01001000', 'endereco': 'Praça da Sé, Sé, São Paulo, SP'}
        resposta = self.client.get(reverse('consultar-cep', args=['01001000']))
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()['cep'], '01001000')

    @patch('tutores.views.buscar_endereco')
    def test_cep_inexistente_retorna_400(self, mock_buscar):
        mock_buscar.side_effect = ViaCEPError('CEP não encontrado.')
        resposta = self.client.get(reverse('consultar-cep', args=['99999999']))
        self.assertEqual(resposta.status_code, 400)
        self.assertEqual(resposta.json()['erro'], 'CEP não encontrado.')

    def test_cep_invalido_retorna_400(self):
        resposta = self.client.get(reverse('consultar-cep', args=['123']))
        self.assertEqual(resposta.status_code, 400)
        self.assertEqual(resposta.json()['erro'], 'CEP deve ter 8 dígitos.')

    @patch('tutores.services.requests.get')
    def test_timeout_da_viacep_retorna_400(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout
        resposta = self.client.get(reverse('consultar-cep', args=['01001000']))
        self.assertEqual(resposta.status_code, 400)
        self.assertEqual(resposta.json()['erro'], 'A ViaCEP demorou demais para responder.')