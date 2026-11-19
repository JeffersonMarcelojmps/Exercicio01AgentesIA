from src.graph.prompts.classify_prompt import (
    CLASSIFY_PROMPT,
    Intencao,
)
from src.graph.state import State
from src.utils.llm_adapter import get_llm


def classify(state: State) -> dict:
    llm = get_llm()

    structured_llm = llm.with_structured_output(
        Intencao,
        method="json_schema"
    )

    chain = CLASSIFY_PROMPT | structured_llm

    resultado = chain.invoke({
        "pergunta": state["pergunta"]
    })

    return {"intent": resultado.intent}