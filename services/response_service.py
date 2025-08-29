def gerar_resposta(categoria: str) -> str:
    respostas = {
        "produtivo": (
            "Olá! Obrigado pelo seu contato. "
            "Sua mensagem foi recebida e encaminhada para o time responsável. "
            "Em breve você receberá um retorno detalhado."
        ),
        "improdutivo": (
            "Sua mensagem foi recebida. "
            "Neste momento, não é necessária nenhuma ação adicional. "
            "Obrigado pela compreensão."
        )
    }

    if not categoria:
        return "Seu e-mail foi processado. Em breve entraremos em contato."
    
    return respostas.get(categoria.strip().lower(), "Seu e-mail foi processado. Em breve entraremos em contato.")
