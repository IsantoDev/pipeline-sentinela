"""Verificador: checar a saúde de um serviço."""
import time 
from dataclasses import dataclass

import requests

@dataclass
class Resultado:
    """A verificação do sentinela"""
    url: str
    no_ar: bool
    status_code: int | None
    latencia_ms: float | None
    situacao: str # 'Rodando', 'Fora do ar - Conexão instável', 'Fora do ar - Erro na requisição'.


class Verificador:
    """Checagem de serviços e classificação de saude - conforme SLA de tempo de resposta."""

    def __init__(self, sla_ms: float = 1000.0) -> None:
        self.sla_ms = sla_ms

    def avaliar(self, no_ar: bool, latencia_ms: float | None) -> str:
        """Classifica a saúde: 'Fora do ar','Lento','Rodando','Fora do ar - Conexão instável','Fora do ar - Erro na requisição'."""
        if no_ar and latencia_ms is not None:
            if latencia_ms > self.sla_ms:
                return "Lento"
            else:
                return "Rodando"
        else:
            return "Fora do ar"

    def checar(self, url: str) -> Resultado:
        """Faz a requisição HTTP e retorna o resultado da verificação."""
        inicio = time.perf_counter()
        try:
            resposta = requests.get(url, timeout=5)
            latencia_ms = (time.perf_counter()- inicio)*1000
            no_ar = resposta.status_code < 400
            situacao = self.avaliar(no_ar, latencia_ms)
            return Resultado(url, no_ar, resposta.status_code, round(latencia_ms,1), situacao)
        except requests.Timeout:
            return Resultado(url, False, None, None, 'Fora do ar - Conexão instável')
        except requests.RequestException:
            return Resultado(url, False, None, None, 'Fora do ar - Erro na requisição')