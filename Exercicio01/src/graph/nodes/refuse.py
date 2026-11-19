from src.graph.state import State


def refuse(state: State) -> dict:
    return {
        "resultado":
            "Desculpe, posso ajudar apenas com assuntos "
            "relacionados à logística marítima e à frota."
    }