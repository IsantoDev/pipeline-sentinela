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