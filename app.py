"""Ponto de entrada do sentinela."""
from sentinela.verificador import Verificador, Resultado
from sentinela.banco import criar_banco, salvar
from sentinela.alertas import alertar
from sentinela.config import Config
from sentinela.ia import resumir_incidente



config = Config(
    urls=[
    "https://www.google.com",
    "https://httpstat.us/500",
    "https://naoexiste.invalido",
    ],
    sla_ms=1000,
)


sentinela = Verificador(sla_ms=config.sla_ms)
criar_banco()

for url in config.urls:
    resultado = sentinela.checar(str(url))
    salvar(resultado)
    if resultado.situacao !='Rodando':
        resumo = resumir_incidente(resultado)
        alertar(resumo)
    print(f'{resultado.situacao:12} | {resultado.url}')

