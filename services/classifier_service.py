from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def classificar_email(conteudo: str):
    prompt = f"""
    Você é um assistente especializado em análise e classificação de emails corporativos.
    Sua tarefa é ler o conteúdo de cada email e classificá-lo em uma das categorias abaixo:

    Categorias de Classificação:
    - Produtivo: Emails que requerem uma ação ou resposta específica.
      Exemplos: solicitações de suporte técnico, atualizações sobre casos em aberto, dúvidas sobre o sistema.
    - Improdutivo: Emails que não necessitam de uma ação imediata.
      Exemplos: mensagens de felicitações, agradecimentos.

    Regras:
    1. Leia atentamente o conteúdo do email.
    2. Determine a categoria mais adequada de acordo com as definições acima.
    3. Explique resumidamente em uma justificativa o motivo da classificação.
    4. Retorne a resposta exclusivamente em JSON, seguindo este formato:

    {{
      "categoria": "Produtivo ou Improdutivo",
      "justificativa": "Breve explicação da classificação",
      "confianca": 0.0 a 1.0
    }}
    
    Conteúdo do email:
    {conteudo}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente que classifica emails corporativos."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.5,
    )
    
    resposta_texto = response.choices[0].message.content.strip()

    if resposta_texto.startswith("```"):
        resposta_texto = resposta_texto.strip("`")
        if resposta_texto.lower().startswith("json"):
            resposta_texto = resposta_texto[4:].strip()

    try:
        resultado = json.loads(resposta_texto)
    except json.JSONDecodeError:
        resultado = {
            "categoria": "Indefinido",
            "justificativa": f"Erro ao processar resposta: {resposta_texto}",
            "confianca": 0.0
        }

    if "confianca" not in resultado:
        resultado["confianca"] = 0.5

    return resultado