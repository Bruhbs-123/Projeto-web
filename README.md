Readme · MD
<div align="center">

# **Adote.anim**

**Plataforma web para adoção e acompanhamento de animais**

[![Status](https://img.shields.io/badge/status-em_desenvolvimento-yellow)]()
[![Versão](https://img.shields.io/badge/versão-0.1.0-blue)]()
[![Licença](https://img.shields.io/badge/licença-acadêmica-lightgrey)]()

</div>

---

**Instituição:** [CEUB]
**Curso:** [ADS]
**Disciplina:** Desenvolvimento Web
**Turma / Semestre:** [2026.02]
**Professor(a):** Felippe Pires Ferreira
**Status do projeto:** Em desenvolvimento
 
---
 
## Sumário
 
- [1. Descrição do projeto](#1-descrição-do-projeto)
- [2. Funcionalidades](#2-funcionalidades)
- [3. Demonstração](#3-demonstração)
- [4. Tecnologias utilizadas](#4-tecnologias-utilizadas)
- [5. Arquitetura](#5-arquitetura)
- [6. Organização dos diretórios](#6-organização-dos-diretórios)
- [7. Participantes](#7-participantes)
- [8. Como executar](#8-como-executar)
- [9. Configuração](#9-configuração)
- [10. Testes](#10-testes)
- [11. Uso de inteligência artificial](#11-uso-de-inteligência-artificial)
- [12. Contribuição e fluxo de trabalho](#12-contribuição-e-fluxo-de-trabalho)
- [13. Histórico de versões](#13-histórico-de-versões)
- [14. Limitações e próximos passos](#14-limitações-e-próximos-passos)
- [15. Licença, referências e contato](#15-licença-referências-e-contato)
---
 
## 1. Descrição do projeto
 
A AdoteApp é uma plataforma web que conecta ONGs e protetores de animais a possíveis adotantes, ao mesmo tempo em que ajuda tutores a organizar a rotina de cuidados dos seus pets. De um lado, abrigos e protetores cadastram animais disponíveis para adoção, com informações como espécie, porte, idade e localização. Do outro, tutores acompanham o histórico de vacinas e consultas de seus animais, com apoio de preenchimento automático de endereço e importação de dados de raça.
 
O problema que o projeto ataca é a dispersão de informações sobre animais para adoção e a dificuldade de acompanhar a saúde do pet após a adoção — informações que hoje costumam ficar espalhadas em redes sociais, planilhas ou na memória do tutor.
 
### Objetivos
 
- **Objetivo geral:** desenvolver uma aplicação web que centralize o cadastro de animais para adoção e o acompanhamento da rotina de cuidados (vacinas e consultas) dos pets já adotados.
- **Objetivos específicos:**
  - Permitir que ONGs/protetores cadastrem, editem e removam animais disponíveis para adoção.
  - Permitir que tutores registrem e consultem o histórico de vacinas e consultas de seus pets.
  - Buscar animais disponíveis por porte, idade, espécie ou localização (CEP).
  - Gerar relatórios de adoções realizadas no mês e de vacinas pendentes.
  - Expor uma API REST pública com a lista de animais disponíveis, consumível por sites parceiros.
  - Integrar a ViaCEP (preenchimento automático de endereço) e a Dog API / Cat API (dados e fotos de raças).
### Público-alvo
 
- ONGs e protetores independentes de animais
- Tutores de pets adotados, que precisam gerenciar vacinas e consultas
- Sites parceiros interessados em exibir animais disponíveis para adoção via API
---
 
## 2. Funcionalidades
 
| Funcionalidade | Descrição | Status |
| --- | --- | --- |
| Cadastro de animais | Criação, edição, exclusão e visualização de animais disponíveis para adoção | Implementada |
| Cadastro de tutores e abrigos | Registro de tutores e abrigos/protetores, com endereço preenchido via ViaCEP | Implementada  |
| Histórico de vacinas e consultas | Registro e consulta do histórico de saúde de cada animal | Implementada |
| Busca de animais | Filtro por porte, idade, espécie e localização (CEP) | Implementada |
| Relatório de adoções | Animais adotados no mês, com filtros | Implementada |
| Relatório de vacinas pendentes | Calendário de vacinas a vencer | Implementada |
| API REST própria | Endpoint público (`GET /api/animais`) para consumo por terceiros | Implementada |
| Importação de dados de raça | Consumo da Dog API / Cat API ao cadastrar um animal | Implementada |
| Identidade visual | Paleta, tipografia e logotipo aplicados de forma consistente | Implementada |
 
 
### Requisitos não funcionais
 
- **Desempenho:** [PREENCHER — ex.: respostas da API em menos de 2 segundos]
- **Segurança:** senhas armazenadas com hash; HTTPS em produção; `DEBUG=False`; segredos fora do repositório
- **Usabilidade:** interface responsiva para desktop e dispositivos móveis
- **Disponibilidade:** aplicação publicada em domínio/subdomínio acessível durante o período de avaliação
---
 
## 3. Demonstração
 
*Inclua capturas de tela reais em `images/` assim que as telas estiverem prontas.*
 
| Tela | Descrição |
| --- | --- |
| Lista de animais | Catálogo de animais disponíveis, com filtros de busca |
| Ficha do animal | Detalhes do pet, incluindo dados importados da Dog/Cat API |
| Cadastro de tutor/abrigo | Formulário com endereço preenchido automaticamente via ViaCEP |
| Painel de vacinas | Histórico e calendário de vacinas por animal |
 
**Protótipo visual:** [Figma — Adote.anim](https://www.figma.com/design/AH6WseuknkiNPtpfBXwWO6)

**Documentação da identidade visual:** [docs/prototipos/identidade-visual.md](docs/prototipos/identidade-visual.md)

**Documentação dos wireframes:** [docs/prototipos/wireframes.md](docs/prototipos/wireframes.md)

**Protótipos Desktop:** [docs/prototipos/desktop.md](docs/prototipos/desktop.md)
 
---
 
## 4. Tecnologias utilizadas
 
| Camada | Tecnologia | Versão |
| --- | --- | --- |
| Linguagem | Python | 3.13 |
| Backend | Django | 6.1.1 |
| API REST | Django REST Framework | 3.18.1 |
| Banco de dados | SQLite | embutido no Python 3.13 |
| Frontend | Templates Django + HTML/CSS | — |
| Testes | Django Test Runner (`unittest`) e `unittest.mock` | embutidos no Django 6.1.1 e no Python 3.13 |
| Infraestrutura | [PREENCHER — ex.: Docker, GitHub Actions] | — |
| Outras ferramentas | Git, VS Code, Postman | — |
| APIs externas | ViaCEP, Dog API / Cat API | — |
 
---
 
## 5. Arquitetura
 
A solução segue uma arquitetura em camadas típica de aplicações Django: apresentação (templates), aplicação (views), domínio (models) e persistência (banco de dados relacional). O backend também expõe uma API REST própria, consumida por terceiros, e consome duas APIs externas (ViaCEP e Dog/Cat API) para enriquecer o cadastro de tutores/abrigos e de animais.
 
```text
[Usuário / Site parceiro] → [Templates / API REST] → [Views Django] → [Models] → [Banco de dados]
                                                              ↓
                                          [ViaCEP]  [Dog API / Cat API]
```
 
**Decisões relevantes:**
 
- Uso de API REST própria (DRF) para permitir que sites parceiros consumam a lista de animais disponíveis.
- Persistência relacional, pois as entidades (Animal, Tutor, Abrigo, Vacina, Consulta, Adoção) têm relacionamentos bem definidos entre si.
- Integração com a ViaCEP no cadastro de tutores/abrigos, com o endereço resultante sendo usado depois na busca por localização — não é uma chamada isolada.
- Integração com a Dog API / Cat API no cadastro de animais, para sugerir dados e fotos de raça.
### Endpoints principais
 
| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/api/animais` | Lista animais disponíveis para adoção, com filtros de porte/idade/espécie/CEP |
| `GET` | `/api/animais/{id}` | Detalhes de um animal específico |
| `POST` | `/api/animais` | Cadastra um novo animal *(uso interno/autenticado)* |
| `PUT` | `/api/animais/{id}` | Atualiza um animal *(uso interno/autenticado)* |
| `DELETE` | `/api/animais/{id}` | Remove um animal *(uso interno/autenticado)* |
 
Documentação completa da API: [PREENCHER — link para Swagger/Redoc ou `docs/api.md`]
 
---
 
## 6. Organização dos diretórios
 
```text
.
├── README.md                 # Documentação principal do projeto
├── .env.example               # Modelo de variáveis de ambiente (sem segredos)
├── docs/                      # Modelagem e demais artefatos técnicos (PDF)
│   ├── README.pdf              # Índice da pasta docs/
│   ├── visao/                  # Documento de Visão
│   ├── casos-de-uso/           # Diagrama UML + especificações textuais
│   ├── arquitetura/            # Diagramas de componentes/implantação
│   ├── banco-de-dados/         # Modelo ER e modelo lógico
│   ├── api/                    # Contrato da API própria e referências da API externa
│   ├── prototipos/             # Identidade visual e protótipos de telas
│   ├── planejamento/           # Backlog, cronograma e responsabilidades
│   └── seguranca/              # Relatórios SAST/DAST
├── images/                    # Figuras da documentação geral
├── src/                       # Código-fonte da aplicação Django
│   ├── animais/                 # App: cadastro de animais
│   ├── tutores/                 # App: tutores e abrigos
│   └── saude/                   # App: vacinas e consultas
├── tests/                     # Testes automatizados
└── scripts/                   # Scripts auxiliares de setup, build ou deploy
```
 
| Diretório / arquivo | Função |
| --- | --- |
| `README.md` | Apresentação do projeto, objetivos, tecnologias e instruções de uso |
| `.env.example` | Lista das variáveis necessárias, sem credenciais reais |
| `docs/` | Artefatos de análise e modelagem |
| `docs/prototipos/` | Identidade visual, wireframes e protótipos de telas |
| `docs/planejamento/` | Cronograma e divisão de tarefas entre a equipe |
| `docs/seguranca/` | Relatórios SAST e DAST |
| `images/` | Figuras da documentação geral do repositório |
| `src/` | Código-fonte organizado por app Django |
| `tests/` | Casos de teste e evidências de verificação |
| `scripts/` | Automação de ambiente e execução |
 
---
 
## 7. Participantes
 
| Nome  Função no projeto |
| --- | --- | --- |
| Bruna  | Documentação / Visão |
| Rafael  | Arquitetura / Dados |
| Isadora  | Design / Identidade Visual |
| Ana Clara  | Dev Backend |
| Renata | Dev Integração (busca, relatórios, APIs externas) |
 
**Professor(a) responsável:** Felippe Pires Ferreira
 
---
 
## 8. Como executar
 
### Pré-requisitos
 
- Git
- Python 3.13
- [PREENCHER — outros pré-requisitos, ex.: Docker]
### Instalação e execução
 
```bash
# 1. Clonar o repositório
git clone [URL_DO_REPOSITORIO]
cd [NOME_DA_PASTA]
 
# 2. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
 
# 3. Instalar dependências
pip install -r requirements.txt
 
# 4. Configurar variáveis de ambiente
cp .env.example .env
# edite o arquivo .env com as credenciais locais
 
# 5. Aplicar migrations
python manage.py migrate
 
# 6. Executar a aplicação
python manage.py runserver
```
 
**Acesso local:** http://localhost:8000
 
### Implantação
 
- **Ambiente:** [PREENCHER — ex.: Render, Railway]
- **URL de produção:** [PREENCHER]
- **Observações:** [PREENCHER — ex.: configurar variáveis de ambiente no painel do provedor]
---
 
## 9. Configuração
 
| Variável | Obrigatória | Descrição | Exemplo |
| --- | --- | --- | --- |
| `SECRET_KEY` | Sim | Chave de segurança do Django | `[gerar localmente]` |
| `DEBUG` | Sim | Modo de depuração (deve ser `False` em produção) | `False` |
| `ALLOWED_HOSTS` | Sim | Hosts autorizados a servir a aplicação | `petmatch.exemplo.com` |
| `DATABASE_URL` | Sim | Conexão com o banco de dados | `postgresql://user:senha@localhost:5432/petmatch` |
| `VIACEP_BASE_URL` | Não | URL-base da ViaCEP (caso configurável) | `https://viacep.com.br` |
| `DOG_API_KEY` / `CAT_API_KEY` | Depende da API | Chave de acesso à Dog API / Cat API, se exigida | `[gerar na plataforma da API]` |
 
Credenciais reais devem ficar apenas no arquivo `.env` (não versionado).
 
---
 
## 10. Testes
 
```bash
python manage.py test
```
 
| Tipo | Ferramenta | O que verifica |
| --- | --- | --- |
| Unitários | Django Test Runner (`unittest`) e `unittest.mock` | Regras de negócio isoladas (ex.: cálculo de vacinas pendentes) |
| Integração | Django Test Client | API própria e integração com banco de dados |
| Manuais | Checklist em `docs/` | Fluxos principais: cadastro, busca, relatório, integração externa |
 
**Cobertura atual:** 38 testes automatizados, todos passando (porcentagem de cobertura não medida).
 
---
 
## 11. Uso de inteligência artificial
 
Este repositório segue a política de uso de IA da disciplina (semáforo pedagógico):
 
![Política de uso de IA — semáforo](images/semaforo.png)
 
| Situação | Significado |
| --- | --- |
| **Vermelho — uso proibido** | Atividades de autonomia intelectual (ex.: provas presenciais sem consulta). |
| **Amarelo — uso limitado** | IA pode ser ferramenta auxiliar, desde que haja declaração de uso. |
| **Verde — uso permitido** | Uso livre ao longo da atividade acadêmica. |
 
### Declaração de uso
 
> Este campo precisa ser preenchido honestamente pela equipe, refletindo o uso real feito durante o desenvolvimento. Não preenchi por vocês.
 
- **Houve uso de IA neste projeto?** [PREENCHER — Sim / Não]
- **Ferramentas utilizadas:** [PREENCHER — ex.: ChatGPT, GitHub Copilot, Claude — ou "nenhuma"]
- **Finalidade:** [PREENCHER — ex.: revisão de texto, geração de esboço de testes, dúvidas de sintaxe]
- **O que NÃO foi delegado à IA:** [PREENCHER — ex.: definição do problema, modelagem, implementação das regras de negócio, testes finais]
*Lembrete: a especificação do projeto (Documento de Visão, casos de uso, arquitetura etc.) precisa ser produzida individualmente por cada aluno, sem uso de IA generativa para gerar o conteúdo diretamente — conforme a orientação do próprio enunciado.*
 
---
 
## 12. Contribuição e fluxo de trabalho
 
### Branches
 
- `main` — versão estável para avaliação
- `develop` — integração do grupo *(opcional)*
- `feat/[nome]` — nova funcionalidade
- `fix/[nome]` — correção de defeito
- `docs/[nome]` — alterações só de documentação
### Commits
 
Use mensagens curtas e no imperativo, por exemplo:
 
- `feat: adiciona cadastro de animais`
- `fix: corrige filtro de busca por CEP`
- `docs: atualiza cronograma de planejamento`
### Passos sugeridos
 
1. Criar uma branch a partir de `main`.
2. Implementar e testar localmente.
3. Abrir um *pull request* para revisão do grupo.
4. Só então integrar à branch principal.
**Issues e quadro de tarefas:** [PREENCHER — link do GitHub Projects, Trello ou similar]
 
---
 
## 13. Histórico de versões
 
| Versão | Data | Descrição |
| --- | --- | --- |
| `0.1.0` | [PREENCHER] | Estrutura inicial do repositório e documentação da Fase 1 |
 
---
 
## 14. Limitações e próximos passos
 
### Problemas conhecidos
 
- [PREENCHER conforme o desenvolvimento avança]
### Roadmap
 
- [ ] Implementar autenticação de tutores e ONGs/abrigos
- [ ] Implementar API REST própria (`GET /api/animais`)
- [ ] Integrar ViaCEP no cadastro de tutores/abrigos
- [ ] Integrar Dog API / Cat API no cadastro de animais
- [ ] Executar e documentar análises SAST e DAST
- [ ] Publicar aplicação com HTTPS

tudo feito
---
 
## 15. Licença, referências e contato
 
**Licença:** Uso exclusivamente acadêmico
 
Este material destina-se a fins educacionais.
 
### Documentação complementar
 
- Índice da pasta `docs/`: [`docs/README.pdf`](docs/README.pdf)
- Casos de uso: [`docs/casos-de-uso/`](docs/casos-de-uso/)
- Diagrama de arquitetura: [`docs/arquitetura/`](docs/arquitetura/)
- Modelo de dados (ER): [`docs/banco-de-dados/`](docs/banco-de-dados/)
- Contrato da API: [`docs/api/`](docs/api/)
- Cronograma de planejamento: [`docs/planejamento/cronograma.docx`](docs/planejamento/cronograma.docx)
- Identidade visual: [`docs/prototipos/identidade-visual.md`](docs/prototipos/identidade-visual.md)
- Wireframes: [`docs/prototipos/wireframes.md`](docs/prototipos/wireframes.md)
- Protótipos Desktop: [`docs/prototipos/desktop.md`](docs/prototipos/desktop.md)
  
### Referências
 
- Uso de IAs como Claude, Gemini e do Figma]
### Contato
 

 
**Agradecimentos:** Professor Felippe Pires Ferreira
