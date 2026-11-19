import json
from pathlib import Path
from langchain.tools import tool

ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "frota_simples.json"

@tool
def consultar_navio(id_navio: str) -> str:
    """Consulta os dados de um navio pelo seu ID."""

    frota = json.loads(ARQUIVO.read_text(encoding="utf-8"))

    for navio in frota["navios"]:
        if navio["id"] == id_navio:
            return json.dumps(navio, ensure_ascii=False)

    return "Navio não encontrado."

@tool
def calcular_eta(distancia: float, velocidade: float) -> float:
    """Calcula o tempo estimado de chegada em horas."""

    if velocidade <= 0:
        return 0.0

    return distancia / velocidade

@tool
def consultar_frota() -> str:
    """Retorna os dados de todos os navios da frota."""

    frota = json.loads(ARQUIVO.read_text(encoding="utf-8"))

    return json.dumps(frota, ensure_ascii=False)

TOOLS = [
    consultar_navio,
    calcular_eta,
    consultar_frota
]