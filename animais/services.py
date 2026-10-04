import requests
from django.conf import settings

TIMEOUT = 5

APIS = {
    'cachorro': {'base': 'https://api.thedogapi.com/v1', 'chave': 'DOG_API_KEY'},
    'gato': {'base': 'https://api.thecatapi.com/v1', 'chave': 'CAT_API_KEY'},
}


class ErroAPI(Exception):
    """Erro ao consultar a Dog API ou a Cat API."""


def _get(especie, caminho, params=None):
    config = APIS.get(especie)
    if config is None:
        raise ErroAPI('Não há API de raças para essa espécie.')

    chave = getattr(settings, config['chave'], '')
    headers = {'x-api-key': chave} if chave else {}

    try:
        resposta = requests.get(
            config['base'] + caminho,
            headers=headers,
            params=params,
            timeout=TIMEOUT,
        )
    except requests.exceptions.Timeout:
        raise ErroAPI('A API demorou demais para responder.')
    except requests.exceptions.RequestException:
        raise ErroAPI('Não foi possível conectar à API.')

    if resposta.status_code == 401:
        raise ErroAPI('Chave da API inválida ou ausente.')
    if resposta.status_code == 429:
        raise ErroAPI('Limite de requisições da API atingido. Tente mais tarde.')
    if resposta.status_code != 200:
        raise ErroAPI(f'A API retornou o erro {resposta.status_code}.')

    try:
        return resposta.json()
    except ValueError:
        raise ErroAPI('Resposta inesperada da API.')


def listar_racas(especie):
    dados = _get(especie, '/breeds')
    if not isinstance(dados, list):
        raise ErroAPI('Resposta inesperada da API.')

    racas = []
    for item in dados:
        if 'id' in item and 'name' in item:
            racas.append({'id': str(item['id']), 'nome': item['name']})
    return sorted(racas, key=lambda r: r['nome'])


def buscar_foto(especie, raca_id):
    dados = _get(especie, '/images/search', {'breed_ids': raca_id})
    if not isinstance(dados, list) or len(dados) == 0:
        return None
    return dados[0].get('url')