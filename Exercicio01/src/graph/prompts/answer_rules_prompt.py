from langchain_core.prompts import ChatPromptTemplate

ANSWER_RULES_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Você é um assistente especializado em logística marítima.

        Siga estas regras:
        1. Responda somente sobre logística marítima e informações da frota.
        2. Utilize exclusivamente os dados fornecidos no contexto.
        3. Não invente informações.
        4. Se os dados forem insuficientes, informe isso claramente.
        5. Seja objetivo e direto.
        """
    ),
    (
        "human",
        """
        Pergunta: {pergunta}

        Dados da frota: {frota}
        """
    )
])