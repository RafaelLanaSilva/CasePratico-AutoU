from pydantic import BaseModel

class EmailRequest(BaseModel):
    conteudo: str

class EmailResponse(BaseModel):
    categoria: str
    resposta: str
    justificativa: str
    confianca: float
