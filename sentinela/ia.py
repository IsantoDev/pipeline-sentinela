"""Geração de resumo de incidentes com IA."""
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")


def resumir_incidente(resultado) -> str:
    """Gera um resumo apartir de um Resultado"""
    prompt = (
        "Você é um analista de plantão (SRE). Com base EXCLUSIVAMENTE nos dados "
        "abaixo, escreva um resumo de incidente curto (2 a 3 frases), objetivo e "
        "em português. NÃO invente nem altere números: use os valores exatamente "
        "como fornecidos. Se um campo estiver como 'None', trate como ausente "
        "(sem resposta HTTP). Estruture em: Incidente, Impacto provável, Ação sugerida.\n\n"
        f"Serviço: {resultado.url}\n"
        f"Situação: {resultado.situacao}\n"
        f"Código HTTP: {resultado.status_code}\n"
        f"Latência (ms): {resultado.latencia_ms}"
    )
    if not API_KEY:
       return "Chave da OpenAI não configurada. Por favor, configure a variável de ambiente OPENAI_API_KEY."
    try:
        cliente = genai.Client(api_key=API_KEY)
        resposta = cliente.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.3), 
        )
        return resposta.text
    except Exception as e:
        return f'Erro ao gerar resumo de incidente: {e}'

