import json

from src.graph.prompts.answer_rules_prompt import ANSWER_RULES_PROMPT
from src.graph.state import State
from src.utils.llm_adapter import get_llm


def answer_rules(state: State) -> dict:
    chain = ANSWER_RULES_PROMPT | get_llm()

    resposta = chain.invoke({
        "pergunta": state["pergunta"],
        "frota": json.dumps(
            state.get("frota", {}),
            ensure_ascii=False
        )
    })

    return {"resultado": resposta.content}