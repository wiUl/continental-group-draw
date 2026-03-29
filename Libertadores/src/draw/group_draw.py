from validator import *
from groups import *
import pandas as pd
import random

def inicialização():
    df = pd.read_csv("../../data/processed/times_por_pote_LA_2026.csv")
    grupos = criar_grupos()

    pote_1 = df.groupby("pote").get_group(1)
    pote_2 = df.groupby("pote").get_group(2)
    pote_3 = df.groupby("pote").get_group(3)
    pote_4 = df.groupby("pote").get_group(4)

    pote1 = pote_1.to_numpy().tolist()
    pote2 = pote_2.to_numpy().tolist()
    pote3 = pote_3.to_numpy().tolist()
    pote4 = pote_4.to_numpy().tolist()

    lista_pendentes = list(grupos.keys())

    #inclui o campeão no grupo A, campeão é o primeiro do pote 1
    campeao = pote1.pop(0)
    adicionar_time(grupos, "A", campeao)
    lista_pendentes.remove("A")


    return grupos, pote1, pote2, pote3, pote4, lista_pendentes

def alocar_times_em_grupo(grupos, times, ordem_grupos):
    times_ordenados = times[:]
    random.shuffle(times_ordenados)

    grupos_iniciais = ordem_grupos[:]

    def backtrack(idx, grupos_restantes):
        if idx == len(times_ordenados):
            return True

        sorteado = times_ordenados[idx]
        print(f"\nSorteado: {sorteado[1]}")

        for i, chave in enumerate(grupos_restantes):
            if pode_adicionar(grupos, chave, sorteado):
                adicionar_time(grupos, chave, sorteado)
                print(f"  → Tentando Grupo {chave}")

                novos_grupos_restantes = grupos_restantes[:]
                novos_grupos_restantes.pop(i)

                if backtrack(idx + 1, novos_grupos_restantes):
                    return True

                remover_time(grupos, chave, sorteado)
                print(f"  ↩ Backtracking: removido do Grupo {chave}")

        return False

    sucesso = backtrack(0, grupos_iniciais)

    if not sucesso:
        print("\n Não foi possível alocar todos os times deste pote.")

    return grupos, list(grupos.keys()), sucesso

        
grupos, timesP1, timesP2, timesP3, timesP4, lista_pendentes = inicialização()

grupos, lista_pendentes, flag1 = alocar_times_em_grupo(grupos, timesP1, lista_pendentes)
grupos, lista_pendentes, flag2 = alocar_times_em_grupo(grupos, timesP2, lista_pendentes)
grupos, lista_pendentes, flag3 = alocar_times_em_grupo(grupos, timesP3, lista_pendentes)
grupos, lista_pendentes, flag4 = alocar_times_em_grupo(grupos, timesP4, lista_pendentes)

"""print(listar_times(grupos, "A"))
print(listar_times(grupos, "B"))
print(listar_times(grupos, "C"))
print(listar_times(grupos, "D"))
print(listar_times(grupos, "E"))
print(listar_times(grupos, "F"))
print(listar_times(grupos, "G"))
print(listar_times(grupos, "H"))
"""
printar_grupos(grupos)










