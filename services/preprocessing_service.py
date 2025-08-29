from PyPDF2 import PdfReader

def extrair_texto_pdf(arquivo):
    try:
        reader = PdfReader(arquivo)
        texto = ""
        for pagina in reader.pages:
            pagina_texto = pagina.extract_text()
            if pagina_texto:
                texto += pagina_texto + "\n"
        texto = texto.strip()
        return texto
    except Exception as e:
        return f"[ERRO] Falha ao extrair texto do PDF: {str(e)}"


def preprocessar(entrada, tipo="texto"):
    if tipo == "pdf":
        return extrair_texto_pdf(entrada)
    return entrada
