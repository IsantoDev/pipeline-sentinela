"""Ponto de entrada do sentinela."""
from sentinela.verificador import Verificador, Resultado

servicos = [
    "https://www.google.com",
    "https://httpstat.us/500",
    "https://naoexiste.invalido",
]

sentinela = Verificador()

for url in servicos:
    resultado = sentinela.checar(url)
    print(f'{resultado.situacao:12} | {resultado.url}')