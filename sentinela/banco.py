"""Persistência de dados: Guarda historico de verificações"""
import sqlite3
from datetime import datetime

caminho_banco = "sentinela.db"

def criar_banco():
    """Cria o banco de dados e a tabela de historico"""
    conexao = sqlite3.connect(caminho_banco)
    conexao.execute(
        """CREATE TABLE IF NOT EXISTS verificacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            no_ar INTEGER NOT NULL,
            status_code INTEGER,
            latencia_ms REAL,
            situacao TEXT NOT NULL,
            verificado_em TEXT NOT NULL
        )"""
    )
    conexao.commit()
    conexao.close()

def salvar(resultado):
    """Grava o resultado da verificação no banco de dados"""
    conexao = sqlite3.connect(caminho_banco)
    conexao.execute(
        """INSERT INTO verificacoes 
        (url, no_ar, status_code, latencia_ms, situacao, verificado_em)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (
            resultado.url,
            resultado.no_ar,
            resultado.status_code,
            resultado.latencia_ms,
            resultado.situacao,
            datetime.now().isoformat(),
        ),
    )
    conexao.commit()
    conexao.close()

def listar() -> list:
    """Retorna uma lista com todos os registros de verificações"""
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.execute(
        """SELECT id, url, no_ar, status_code, latencia_ms, situacao, verificado_em
        FROM verificacoes
        ORDER BY id"""
    )
    linhas = cursor.fetchall()
    conexao.close()
    return linhas

def uptime() -> float:
    """Calcula a % de checagem de serviços que estão no ar"""
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.execute(
        "SELECT COUNT(*),SUM(no_ar) FROM verificacoes"
    )
    total, total_no_ar = cursor.fetchone()
    conexao.close()
    if total == 0:
        return 0.0
    return (total_no_ar / total) * 100