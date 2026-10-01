import re
import requests


class ViaCEPError(Exception):
    pass


def buscar_endereco(cep):
    cep = re.sub(r"\D", "", cep or "")
    if len(cep) != 8:
        raise ViaCEPError("CEP deve ter 8 dígitos.")

    try:
        resposta = requests.get(
            f"https://viacep.com.br/ws/{cep}/json/", timeout=5
        )
        resposta.raise_for_status()
    except requests.Timeout:
        raise ViaCEPError("A ViaCEP demorou demais para responder.")
    except requests.RequestException:
        raise ViaCEPError("Não foi possível consultar a ViaCEP.")

    dados = resposta.json()
    if dados.get("erro"):
        raise ViaCEPError("CEP não encontrado.")

    return {
        "cep": cep,
        "logradouro": dados.get("logradouro", ""),
        "bairro": dados.get("bairro", ""),
        "cidade": dados.get("localidade", ""),
        "uf": dados.get("uf", ""),
    }