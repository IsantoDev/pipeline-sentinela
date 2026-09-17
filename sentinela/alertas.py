"""Envio de alertas via webhook quando um serviço não está saudável"""
import os
from dotenv import load_dotenv
import requests

load_dotenv()
WEBHOOK_URL = os.getenv("WEBHOOK_URL")


def alertar(mensagem: str) -> None:
    """Envia um alerta via webhook"""
    if not WEBHOOK_URL:
        print("Webhook URL não configurada. Ignorando alerta.")
        return
    try:
        requests.post(WEBHOOK_URL, json={"content": mensagem}, timeout=5)
    except requests.RequestException as e:
        print(f"Falha ao enviar alerta: {e}") 