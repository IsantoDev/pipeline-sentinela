"""Testes da logica de classificação do Verificador."""
import pytest
from sentinela.verificador import Verificador

@pytest.fixture
def sentinela():
    """Fixture para criar uma instância do Verificador."""
    return Verificador()

def test_no_ar(sentinela):
    assert sentinela.avaliar(no_ar=True, latencia_ms=200) == 'Rodando'

def test_lento(sentinela):
    assert sentinela.avaliar(no_ar=True, latencia_ms=1500) == 'Lento'

def test_fora(sentinela):
    assert sentinela.avaliar(no_ar=False, latencia_ms=None) == 'Fora do ar'

def test_fora_lento(sentinela):
    assert sentinela.avaliar(no_ar=True, latencia_ms=None) == 'Fora do ar'