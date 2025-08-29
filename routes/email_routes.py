from fastapi import APIRouter, UploadFile, File, HTTPException
from models.email_model import EmailRequest, EmailResponse
from services.classifier_service import classificar_email
from services.preprocessing_service import extrair_texto_pdf
from services.response_service import gerar_resposta
import traceback

router = APIRouter()

@router.get("/")
def check_status():
    return {"status": "ok", "message": "API de Automação ativa"}

@router.post("/processar-email", response_model=EmailResponse)
def processar_email_text(request: EmailRequest):
    try:
        resultado = classificar_email(request.conteudo)
        return {
            "categoria": resultado["categoria"],
            "resposta": gerar_resposta(resultado["categoria"]),
            "justificativa": resultado["justificativa"],
            "confianca": resultado["confianca"]
        }
    except Exception as e:
        print("ERRO:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/processar-email-arquivo", response_model=EmailResponse)
def processar_email_arquivo(arquivo: UploadFile = File(...)):
    try:
        if arquivo.filename.endswith(".pdf"):
            conteudo = extrair_texto_pdf(arquivo.file)
        else:
            conteudo = arquivo.file.read().decode("utf-8")
        
        resultado = classificar_email(conteudo)
        return {
            "categoria": resultado["categoria"],
            "resposta": gerar_resposta(resultado["categoria"]),
            "justificativa": resultado["justificativa"],
            "confianca": resultado["confianca"]
        }
    except Exception as e:
        print("ERRO:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
