
from langgraph.types import Command

from src.graph.builder import build_graph
from src.utils.langfuse_client import run_config, flush


def main():
    print("\nIniciando análise automática da frota...\n")

    graph = build_graph()

    config = run_config(
        configurable={"thread_id": "main"}
    )

    # Primeira execução do grafo
    saida = graph.invoke(
        {
            "pergunta": "Qual navio chegará primeiro ao destino considerando o ETA?",
        },
        config=config
    )

    # Verifica se o grafo foi interrompido
    interrupcoes = saida.get("__interrupt__", [])

    if interrupcoes:
        dados_revisao = interrupcoes[0].value

        print("\n========== REVISÃO HUMANA ==========\n")
        print("Recomendação:")
        print(dados_revisao["recomendacao"])
        print("\n" + dados_revisao["mensagem"])

        # Solicita aprovação ou rejeição
        while True:
            aprovacao = input(
                "\nDeseja aprovar a recomendação? (s/n): "
            ).strip().lower()

            if aprovacao in ("s", "n"):
                break

            print("Resposta inválida. Digite s ou n.")

        nota = input("Digite uma observação: ").strip()

        decisao = {
            "aprovado": aprovacao == "s",
            "nota": nota
        }

        # Retoma o grafo
        saida = graph.invoke(
            Command(resume=decisao),
            config=config
        )

    # Exibe o resultado final
    print("\n========== RESULTADO FINAL ==========\n")

    print("Status:", "APROVADO" if saida.get("aprovado") else "DESAPROVADO")
    print("Observação:", saida.get("nota", "Não informada."))

    if "resultado" in saida:
        print("\n" + saida["resultado"])

    print("\n=====================================\n")

    flush()


if __name__ == "__main__":
    main()
