from src.graph.state import State
from src.utils.llm_adapter import get_llm
from src.graph.tools import TOOLS


def analyze(state: State) -> dict:
    llm = get_llm().bind_tools(TOOLS)

    resposta = llm.invoke(state["messages"])

    return {"messages": [resposta]}