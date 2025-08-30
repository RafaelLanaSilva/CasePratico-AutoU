from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import email_routes

app = FastAPI()

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui o router
app.include_router(email_routes.router)

@app.get("/")
def root():
    return {"message": "API online 🚀"}