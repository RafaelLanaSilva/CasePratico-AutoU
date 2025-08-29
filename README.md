# 📧 Classificação Automática de Emails com OpenAI 

Este projeto é uma **Prova de Conceito (POC/MVP)** para classificação de emails usando **IA**, com retorno de **categoria (Produtivo / Improdutivo)**, **justificativa** e uma **resposta sugerida**.  

O sistema é composto por:  
- **Backend**: API em **FastAPI (Python)** para processamento, classificação e geração de resposta com integração com a OpenAI.  
- **Frontend**: Interface simples em **HTML + Bootstrap + JavaScript**, que consome os endpoints da API.  

---

## 🚀 Tecnologias Utilizadas  

- **Python 3.11+**  
- **FastAPI** (framework backend)  
- **Uvicorn** (servidor ASGI)  
- **PyPDF2** (extração de texto de PDFs)  
- **Bootstrap 5** (estilização do frontend)  
- **Fetch API (JS)** (requisições para o backend)
- **OpenAI** (Inteligência Artificial que lê, analisa e classifica os emails)

---

## ⚙️ Configuração do Ambiente  

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/classificador-emails.git
cd classificador-emails
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a API
```bash
uvicorn main:app --reload
```

A API ficará disponível em:  
👉 `http://127.0.0.1:8000`  

A documentação Swagger em:  
👉 `http://127.0.0.1:8000/docs`  

---

## 💻 Frontend  

1. Abra a pasta `view/`.  
2. Abra o arquivo `index.html` no navegador (ou use o **Live Server** do VS Code).  
3. O frontend está configurado para consumir a API na porta **8000**.  

⚠️ Importante: Se a API rodar em outro host/porta, ajuste as URLs do `fetch` no `index.html`.  

---

## 📌 Endpoints da API  

- **`POST /processar-email`**  
  - Entrada: JSON com campo `conteudo` (texto do email).  
  - Saída: Categoria, justificativa, resposta sugerida e confiança.  

- **`POST /processar-email-arquivo`**  
  - Entrada: Arquivo `.pdf` ou `.txt`.  
  - Saída: Mesma estrutura do endpoint acima.  

---

## ✅ Fluxo de Funcionamento  

1. O usuário **cola o conteúdo** ou **envia um arquivo** PDF/TXT pelo frontend.  
2. O backend faz o **preprocessamento** (extração do texto).  
3. O texto é enviado ao **classificador** (regra/IA).  
4. O sistema retorna:  
   - **Categoria** (Produtivo ou Improdutivo)  
   - **Justificativa da classificação**  
   - **Resposta automática sugerida**  

---

## 📖 Exemplo de Resposta da API  

```json
{
  "categoria": "Produtivo",
  "justificativa": "O email contém termos relacionados a agendamento de reunião.",
  "resposta": "Olá, obrigado pelo contato! Vamos agendar conforme sugerido.",
  "confianca": 0.92
}
```

---

## 📂 Estrutura do Projeto  

```
├── backend/
│   ├── main.py
│   ├── models/
│   ├── services/
│   ├── routes/
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── css/
└── README.md
```
