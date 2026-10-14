# Continental Group Draw — simulador de sorteio de grupos

Projeto em Python que simula o **sorteio da fase de grupos da CONMEBOL Libertadores 2026**: coleta os times por pote em uma página oficial da CONMEBOL e distribui os 32 clubes em 8 grupos de 4, respeitando as restrições do sorteio por meio de **backtracking**.

**Estado:** em desenvolvimento. O sorteio da Libertadores funciona; a parte da Champions League ainda não foi iniciada.

## O que está implementado

- **Coleta dos times** (`Libertadores/scripts/run_scrapping.py`): lê a página de notícias da CONMEBOL sobre o sorteio, extrai os 4 potes e gera o arquivo `times_por_pote_LA_2026.csv` com as colunas `pote`, `time`, `pais` e `fase_pre`. A coluna `fase_pre` marca os clubes vindos das fases prévias, que têm critério de sorteio diferente.
- **Dados prontos** (`Libertadores/data/processed/times_por_pote_LA_2026.csv`): 32 clubes, 8 por pote, de 10 países.
- **Sorteio** (`Libertadores/src/draw/`):
  - `groups.py` — estrutura dos grupos A a H e funções para adicionar, remover e listar times.
  - `validator.py` — regras de validação de cada inserção:
    - o grupo deve existir e ter menos de 4 times;
    - não pode haver dois times do mesmo **pote** no grupo;
    - não pode haver dois times do mesmo **país** no grupo, exceto para clubes marcados como `fase_pre`.
  - `group_draw.py` — monta os potes, coloca o campeão (primeiro clube do pote 1) no grupo A e sorteia cada pote em ordem aleatória; se um time não tem grupo válido, **volta atrás (backtracking)** e tenta outra combinação. Ao final, imprime os grupos.

## Estrutura do repositório

```text
.
├── Libertadores/
│   ├── data/processed/times_por_pote_LA_2026.csv
│   ├── scripts/
│   │   ├── run_scrapping.py     # coleta dos potes
│   │   └── run_draw.py          # ainda vazio
│   └── src/
│       ├── draw/                # groups.py, validator.py, group_draw.py, rules.py (vazio)
│       └── models/team.py       # arquivo vazio
├── Champions League/            # estrutura inicial (arquivo vazio)
├── .env.example
├── requirements.txt
└── README.md
```

## Como executar o sorteio

Requer Python 3 e `pandas`.

```bash
pip install pandas
cd Libertadores/src/draw
python group_draw.py
```

O script precisa ser executado **de dentro de `Libertadores/src/draw/`**, pois lê o CSV por caminho relativo (`../../data/processed/`). A cada execução o resultado muda, pois a ordem do sorteio é aleatória. A saída lista os grupos A a H, cada um com 4 times (pote, nome e país), além do registro das tentativas e dos retornos do backtracking.

## Limitações conhecidas

- `Libertadores/scripts/run_draw.py` e `Libertadores/src/draw/rules.py` estão vazios; o sorteio roda diretamente por `group_draw.py`.
- A pasta `Champions League/` contém apenas um arquivo vazio.
- O script de coleta grava o CSV em um **caminho absoluto fixo** (pasta do computador do autor) e tem o endereço da página no código; é preciso ajustá-los antes de executá-lo em outro ambiente. O arquivo `.env.example` define variáveis de configuração que o script de coleta ainda não utiliza.
- O código aplica apenas as restrições de pote e de país descritas acima; qualquer outra regra do sorteio oficial não está implementada (`rules.py` está vazio).
- Não há testes automatizados.
- `requirements.txt` é uma listagem completa de pacotes de um ambiente e inclui bibliotecas que o projeto não utiliza; para o sorteio basta `pandas`, e para a coleta, `beautifulsoup4`, `requests` e `pandas`.

## Tecnologias

Python · pandas · BeautifulSoup · requests

## Autor

Willian Gomes — https://github.com/wiUl
