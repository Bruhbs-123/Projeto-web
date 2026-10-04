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
        dados = resposta.json()
    except requests.Timeout as exc:
        raise ViaCEPError("A ViaCEP demorou demais para responder.") from exc
    except (requests.RequestException, ValueError) as exc:
        raise ViaCEPError("Não foi possível consultar a ViaCEP.") from exc

    if dados.get("erro"):
        raise ViaCEPError("CEP não encontrado.")

    partes = [
        dados.get("logradouro"),
        dados.get("bairro"),
        dados.get("localidade"),
        dados.get("uf"),
    ]
    return {
        "cep": cep,
        "endereco": ", ".join(p for p in partes if p),
    }