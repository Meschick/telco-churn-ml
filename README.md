# Telco Churn Prediction

Projeto de machine learning para prever churn em telecomunicações.

## Objetivo

Construir uma solução simples, organizada e reproduzível para classificar clientes em risco de cancelamento.

## Estrutura do projeto

```text
project/
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── artifacts/
│   ├── models/
│   ├── metrics/
│   └── plots/
├── reports/
└── docs/
```

## O que cada pasta faz

- data/raw/: dados brutos do projeto
- data/processed/: dados tratados e prontos para treinamento
- notebooks/: análise exploratória e experimentos
- src/: código da solução
- artifacts/models/: modelos treinados
- artifacts/metrics/: métricas e validações
- artifacts/plots/: gráficos e visualizações
- reports/: relatórios finais
- docs/: material de apoio para estudo e entendimento

## Fluxo do projeto

1. carregar e entender os dados
2. analisar o comportamento do churn
3. limpar e preparar os dados
4. treinar modelos
5. comparar desempenho
6. interpretar os resultados
7. salvar artefatos e documentar a solução

## Requisitos

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Boas práticas adotadas

- organização por etapas
- separação entre dados, código e artefatos
- estrutura simples e fácil de manter
- foco em clareza e didática
