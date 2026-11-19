from src.graph.state import State


def route_by_intent(state: State) -> str:
    intent = state.get("intent")

    if intent == "calcular_eta":
        return "decide"

    elif intent == "consultar_frota":
        return "consultar_frota"

    else:
        return "outro"