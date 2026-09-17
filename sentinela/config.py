"""Modelo de configuração do sentinela."""
from pydantic import BaseModel, HttpUrl, Field

class Config(BaseModel):
    """Configuração Validada do sentinela."""
    urls: list[HttpUrl]
    sla_ms: float = Field(gt=0)