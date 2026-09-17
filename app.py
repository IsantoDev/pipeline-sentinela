"""Ponto de entrada do sentinela."""
from sentinela.verificador import Verificador, Resultado
from sentinela.banco import criar_banco, salvar
from sentinela.alertas import alertar



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
    if resultado.situacao !='Rodando':
        alertar(f"Alerta: Serviço {resultado.url} não se encontra saudável. Situação: {resultado.situacao}")
    print(f'{resultado.situacao:12} | {resultado.url}')

