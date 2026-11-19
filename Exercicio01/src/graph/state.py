from typing import TypedDict


class State(TypedDict, total=False):
    pergunta: str
    frota: dict
    resposta_llm: str
    resultado: str
    intent: str
    messages: list
    recomendacao: str
    aprovado: bool
    nota: str