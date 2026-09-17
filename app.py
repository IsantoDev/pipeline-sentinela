"""Ponto de entrada do sentinela."""
from sentinela.verificador import Verificador, Resultado
from sentinela.banco import criar_banco, salvar



servicos = [
    "https://www.google.com",
    "https://httpstat.us/500",
    "https://naoexiste.invalido",
]


sentinela = Verificador()
criar_bd = criar_banco()

for url in servicos:
    resultado = sentinela.checar(url)
    salvar(resultado)
    print(f'{resultado.situacao:12} | {resultado.url}')

