
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from src.graph.nodes.human_review import human_review
from src.graph.state import State
from src.graph.routing import route_by_intent
from src.graph.tools import TOOLS

from src.graph.nodes.receive import receive
from src.graph.nodes.classify import classify
from src.graph.nodes.decide import decide
from src.graph.nodes.format_output import format_output
from src.graph.nodes.answer_rules import answer_rules
from src.graph.nodes.refuse import refuse
from src.graph.nodes.prepare import prepare
from src.graph.nodes.analyze import analyze


def build_graph():
    graph = StateGraph(State)

    # Registro dos nós
    graph.add_node("receive", receive)
    graph.add_node("classify", classify)
    graph.add_node("decide", decide)
    graph.add_node("format_output", format_output)
    graph.add_node("answer_rules", answer_rules)
    graph.add_node("refuse", refuse)

    graph.add_node("prepare", prepare)
    graph.add_node("analyze", analyze)
    graph.add_node("tools", ToolNode(TOOLS))
    graph.add_node("human_review", human_review)

    # Fluxo inicial
    graph.add_edge(START, "receive")
    graph.add_edge("receive", "classify")

    # Roteamento por intenção
    graph.add_conditional_edges(
        "classify",
        route_by_intent,
        {
            "decide": "decide",
            "consultar_frota": "answer_rules",
            "outro": "refuse",
        }
    )

    # Caminho de cálculo do ETA - Exercício 1

    graph.add_edge("decide", "human_review")
    graph.add_edge("human_review", "format_output")
    graph.add_edge("format_output", END)

    # Caminho de análise com ferramentas - Parte B
    graph.add_edge("prepare", "analyze")

    graph.add_conditional_edges(
        "analyze",
        tools_condition
    )

    graph.add_edge("tools", "analyze")

    # Outros caminhos
    graph.add_edge("answer_rules", END)
    graph.add_edge("refuse", END)

    memory = MemorySaver()
    return graph.compile(checkpointer=memory)

