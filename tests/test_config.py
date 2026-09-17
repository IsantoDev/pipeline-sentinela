"""Testes de validação do modelo Config."""
import pytest
from pydantic import ValidationError
from sentinela.config import Config


def test_config_valida():
    """Uma config correta é aceita."""
    config = Config(urls=["https://google.com"], sla_ms=1000)
    assert config.sla_ms == 1000.0


def test_sla_negativo_rejeitado():
    """Um sla_ms <= 0 deve ser recusado pelo pydantic."""
    with pytest.raises(ValidationError):
        Config(urls=["https://google.com"], sla_ms=-5)

 
def test_url_invalida_rejeitada():
    """Uma URL invalida deve ser recusada pelo pydantic."""
    with pytest.raises(ValidationError):
        Config(urls=["htp://invalid"], sla_ms=1000)