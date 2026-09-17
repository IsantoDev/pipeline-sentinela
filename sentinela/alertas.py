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
    payload = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.2",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": mensagem,
                            "wrap": True
                        }
                    ]
                }
            }
        ]
    }
    try:
        requests.post(WEBHOOK_URL, json=payload, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar alerta: {e}")