from langchain_core.prompts import ChatPromptTemplate

PROMPT_MELHORADO = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Você é um especialista em logística marítima.

        Calcule o tempo estimado de chegada de cada navio
        utilizando a fórmula:

        ETA = distância em milhas náuticas / velocidade em nós.

        O navio com o menor ETA chegará primeiro.

        Informe o ID do navio vencedor e seu ETA em horas.
        """
    ),
    (
        "human",
        "Dados da frota: {frota}"
    )
])