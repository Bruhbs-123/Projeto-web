# Plano de Integração com APIs Externas

Projeto: Sistema de Adoção de Animais
Tecnologias: Python, Django, Django REST Framework, SQLite

## 1. Objetivo

O sistema usa três APIs externas:

- **ViaCEP:** preencher o endereço do tutor a partir do CEP.
- **Dog API:** buscar a raça e a foto de cachorros no cadastro do animal.
- **Cat API:** buscar a raça e a foto de gatos no cadastro do animal.

Todas as chamadas têm timeout de 5 segundos. Se alguma API falhar, o sistema mostra uma mensagem de erro e o usuário pode preencher os dados manualmente.

## 2. ViaCEP

- URL: `https://viacep.com.br/ws/{cep}/json/`
- Autenticação: não precisa
- Nosso endpoint: `GET /tutores/cep/<cep>/`
- Código: função `buscar_endereco(cep)` em `tutores/services.py`

**Campos usados:** logradouro, bairro, localidade e uf (da ViaCEP). Nosso endpoint junta tudo em um texto único e devolve `cep` e `endereco`.

**Testes feitos:**

| Caso | URL testada | Status | Mensagem |
|---|---|---|---|
| CEP válido | /tutores/cep/01001000/ | 200 | JSON com cep e endereco |
| CEP inexistente | /tutores/cep/99999999/ | 400 | "CEP não encontrado." |
| CEP inválido | /tutores/cep/123/ | 400 | "CEP deve ter 8 dígitos." |
| Falha de rede ou timeout (5s) | confirmado nos testes automatizados | 400 | "A ViaCEP demorou demais para responder." |

**Erros tratados:**

- CEP com formato errado (diferente de 8 dígitos).
- CEP que não existe na base da ViaCEP.
- Falha de rede ou demora maior que 5 segundos.

**Uso no projeto:** no formulário do tutor, quando o usuário digita o CEP e sai do campo, o endereço é preenchido automaticamente. Se der erro, aparece uma mensagem e o endereço pode ser digitado manualmente.

## 3. Dog API

- URL base: `https://api.thedogapi.com/v1`
- Autenticação: header `x-api-key`

**Requisições testadas:**

| Requisição | Status |
|---|---|
| GET /breeds | 200 |
| GET /images/search?breed_ids=1 | 200 |

**Campos usados:** `id` e `name` da raça e `url` da foto.

**Erros tratados:**

- Timeout ou falta de internet.
- 401 (chave inválida).
- 429 (limite de requisições).
- Lista de imagens vazia.

## 4. Cat API

- URL base: `https://api.thecatapi.com/v1`
- Autenticação: header `x-api-key`

**Requisições testadas:**

| Requisição | Status |
|---|---|
| GET /breeds | 200 |
| GET /images/search?breed_ids=abys | 200 |

**Campos usados:** `id` e `name` da raça e `url` da foto.

**Erros tratados:** os mesmos da Dog API (timeout, 401, 429 e lista vazia).

## 5. Uso no cadastro de animal

1. O usuário escolhe a espécie (cachorro ou gato).
2. O sistema busca a lista de raças da API da espécie escolhida.
3. O usuário escolhe a raça.
4. O sistema busca a foto da raça e guarda a `url` no campo `foto_url`.
5. O animal é salvo com `raca` e `foto_url` preenchidos.

Se a API falhar, o usuário pode digitar a raça e deixar a foto em branco. Para a espécie "outro" não existe API, então tudo é preenchido manualmente.

As funções estão em `animais/services.py`: `listar_racas(especie)` e `buscar_foto(especie, raca_id)`. Os endpoints internos são `/animais/racas/<especie>/` e `/animais/foto/<especie>/<raca_id>/`.

## 6. Chaves de API

As chaves não ficam escritas no código nem vão para o GitHub. Elas são guardadas em variáveis de ambiente (`DOG_API_KEY` e `CAT_API_KEY`) e lidas no `settings.py` com `os.environ.get()`.

## 7. Testes automatizados

Os testes usam `unittest.mock` para simular as APIs, sem depender da internet. Comando: `python manage.py test`.

- `buscar_endereco` com CEP válido, inexistente, inválido, timeout e falha de rede.
- Endpoint `/tutores/cep/<cep>/` retornando 200 e 400.
- `listar_racas` e `buscar_foto` com resposta simulada, lista vazia, timeout, erro 401 e erro 429.
- Endpoints `/animais/racas/` e `/animais/foto/`.
- Validação de datas das vacinas e relatórios (adoções do mês e vacinas pendentes).

## 8. Riscos

| Risco | Solução |
|---|---|
| API fora do ar ou lenta | Timeout de 5s e preenchimento manual |
| Limite de requisições da conta gratuita | Tratar o erro 429 |
| Foto que não carrega | Mostrar uma imagem padrão |