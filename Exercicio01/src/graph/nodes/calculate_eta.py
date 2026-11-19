
def calculate_eta(state):

    frota = state["frota"]

    for navio in frota:

        distancia = navio["distancia_milhas"]
        velocidade = navio["velocidade_nos"]

        if velocidade <= 0 or distancia < 0:
            raise ValueError(
                f"Dados inválidos para {navio['nome']}"
            )

        eta = distancia / velocidade

        navio["eta_horas"] = eta

    return {
        "frota": frota
    }
