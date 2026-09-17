"""Testes da camada de persistência do sentinela (banco de dados)."""
import pytest
from sentinela import banco
from sentinela.verificador import Resultado

@pytest.fixture
def banco_temp(tmp_path, monkeypatch):
    """Cria um banco de dados temporário para os testes."""
    caminho = tmp_path / 'teste.db'
    monkeypatch.setattr(banco, 'caminho_banco', str(caminho))
    banco.criar_banco()
    return caminho

def test_salvar(banco_temp):
    banco.salvar(Resultado("http://teste", True, 200, 50.0, "Rodando"))
    assert len(banco.listar()) == 1

def test_uptime_vazio(banco_temp):
    assert banco.uptime() == 0.0

def test_meio(banco_temp):
    banco.salvar(Resultado("http://ok", True, 200, 50.0, "Rodando"))
    banco.salvar(Resultado("http://fora", False, None, None, "Fora do ar"))
    assert banco.uptime() == 50.0
