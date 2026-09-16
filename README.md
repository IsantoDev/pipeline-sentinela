# Sentinela 🛰️

Monitor de saúde de serviços e integrações: checa se estão no ar, guarda o
histórico e **avisa quando algo cai ou fica lento**.


## O problema
Automações dependem de serviços externos (APIs, sites). Quando um cai ou fica
lento, os robôs quebram — muitas vezes de madrugada, sem ninguém ver a tempo.

## O que faz

    serviços  →  checa status + latência  →  grava histórico (SQL)
              →  uptime %  →  se cair/estourar SLA  →  alerta (Teams/Discord)

## Stack (planejada)
Python · requests · pydantic · SQL · Docker · pytest · GitHub Actions

## Status
Sprint 1 — estrutura base (POO, testes, Docker).


## Como rodar

Pré-requisitos: **Python 3.14+** e, opcionalmente, **Docker**.

### Localmente

```bash
# 1. clonar o repositório
git clone https://github.com/IsantoDev/pipeline-sentinela.git
cd pipeline-sentinela

# 2. criar e ativar o ambiente virtual
py -m venv .venv
.\.venv\Scripts\Activate.ps1      # Windows (PowerShell)
# source .venv/bin/activate        # Linux / Mac

# 3. instalar as dependências
py -m pip install -r requirements.txt

# 4. rodar o Sentinela
py app.py

# 5. rodar os testes
pytest
```

### Com Docker

```bash
docker build -t sentinela .
docker run sentinela
```