"""Geração de resumo de incidentes com IA."""
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")


def resumo_basico(resultado) -> str:
    """Gera um resumo básico a partir de um Resultado"""
    return (
        f"Serviço: {resultado.url}\n"
        f"Situação: {resultado.situacao}\n"
        f"Código HTTP: {resultado.status_code}\n"
        f"Latência (ms): {resultado.latencia_ms}"
    )


def resumir_incidente(resultado) -> str:
    """Gera um resumo apartir de um Resultado"""
    prompt = (
        "Você é um analista de plantão (SRE). Com base EXCLUSIVAMENTE nos dados "
        "abaixo, escreva um resumo de incidente curto (2 a 3 frases), objetivo e "
        "em português. NÃO invente nem altere números: use os valores exatamente "
        "como fornecidos. Se um campo estiver como 'None', trate como ausente "
        "(sem resposta HTTP). Estruture em: Incidente, Impacto provável, Ação sugerida.\n\n"
        "No final traga os campos abaixo de forma ordenada:"
        f"Serviço: {resultado.url}\n"
        f"Situação: {resultado.situacao}\n"
        f"Código HTTP: {resultado.status_code}\n"
        f"Latência (ms): {resultado.latencia_ms}"
    )
    if not API_KEY:
        print("API Key não configurada. Usando resumo básico.")
        return resumo_basico(resultado)
    try:
        cliente = genai.Client(api_key=API_KEY)
        resposta = cliente.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.2), 
        )
        return resposta.text
    except Exception:
        print("Erro ao gerar resumo de incidente. Usando resumo básico.")
        return resumo_basico(resultado)

