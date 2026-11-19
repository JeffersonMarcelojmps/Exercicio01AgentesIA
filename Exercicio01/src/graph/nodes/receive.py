import json
from pathlib import Path

from src.graph.state import State

ARQUIVO = Path(__file__).resolve().parents[2] / "dados" / "frota_simples.json"


def receive(state: State) -> dict:
    if not ARQUIVO.exists():
        raise FileNotFoundError(
            f"Arquivo da frota não encontrado: {ARQUIVO}"
        )

    frota = json.loads(ARQUIVO.read_text(encoding="utf-8"))
    return {"frota": frota}