import json

from src.graph.prompts.choose_ship import PROMPT_MELHORADO
from src.graph.state import State
from src.utils.llm_adapter import get_llm


def decide(state: State) -> dict:
    chain = PROMPT_MELHORADO | get_llm()

    resposta = chain.invoke({
        "frota": json.dumps(state["frota"], ensure_ascii=False)
    })

    return {
    "resposta_llm": resposta.content,
    "recomendacao": resposta.content
}