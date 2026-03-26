def criar_grupos():
    grupos = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
    }

    return grupos

def adicionar_time(grupos, chave, valor):
    if valor not in grupos[chave]:
        grupos[chave].append(valor)
    
def listar_times(grupos, chave):
    lista_times = []
        
    for time in grupos[chave]:
        lista_times.append(time[1])
        
    return lista_times

def listar_paises(grupos, chave):
    lista_paises = []

    for time in grupos[chave]:
        if time[2] not in lista_paises:
            lista_paises.append(time[2])

    return lista_paises

def listar_potes(grupos, chave):
    lista_potes = []

    for time in grupos[chave]:
        if time[0] not in lista_potes:
            lista_potes.append(time[0])

    return lista_potes

def printar_grupos(grupos):
    for chave in grupos.keys():
        print(f"\nGrupo {chave}:")
        for time in grupos[chave]:
            print(f"  Pote {time[0]} | {time[1]} ({time[2]})")
