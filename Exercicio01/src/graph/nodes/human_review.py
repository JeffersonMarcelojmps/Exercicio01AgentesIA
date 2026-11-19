
from langgraph.types import interrupt

from src.graph.state import State


def human_review(state: State) -> dict:
    resposta = interrupt({
        "recomendacao": state["recomendacao"],
        "mensagem": "Aprovar ou rejeitar esta recomendação?",
    })

    return {
        "aprovado": resposta["aprovado"],
        "nota": resposta["nota"],
    }
