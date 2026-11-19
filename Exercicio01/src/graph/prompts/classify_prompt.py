from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel


class Intencao(BaseModel):
    intent: Literal["calcular_eta", "consultar_frota", "outro"]


CLASSIFY_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Classifique a pergunta do usuário em exatamente uma das intenções:
        - calcular_eta: pergunta sobre previsão de chegada, ETA ou qual navio
          chegará primeiro.
        - consultar_frota: pergunta sobre os navios ou dados da frota.
        - outro: qualquer assunto que não se enquadre nas opções anteriores.

        Retorne somente a saída estruturada definida pelo schema.
        """
    ),
    ("human", "{pergunta}"),
])