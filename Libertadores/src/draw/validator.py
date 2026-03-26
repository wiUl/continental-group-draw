from groups import *
#return True = existe / return False = não existe
def grupo_existe(grupos, chave):
    if chave in grupos:
        return True
    else:
        return False
    
#return True = não pode adicionar / return False = pode adicionar
def grupo_cheio(grupos, chave):
    if len(grupos[chave]) == 4:
        return True
    else:
        return False
    
#return True = não pode adicionar / return False = pode adicionar
def mesmo_pote(grupos, chave, time_info):
    pote = time_info[0]
    
    for time in grupos[chave]:
        if pote in time:
            return True
    
    return False


#return True = não pode adicionar / return False = pode adicionar
def mesmo_pais(grupos, chave, time_info):
    pais = time_info[2]
    
    for time in grupos[chave]:
        if pais in time and time_info[3] == False:
            return True
    
    return False

#return True = pode adicionar o time naquele grupo / return False = não pode adicionar naquele grupo
def pode_adicionar(grupos, chave, time_info):
    if grupo_existe(grupos, chave):
        if grupo_cheio(grupos, chave) is False:
            if mesmo_pote(grupos, chave, time_info) is False:
                if mesmo_pais(grupos, chave, time_info) is False:
                    return True
    return False



"""
grupao = criar_grupos()

time1 = [1,"Flamengo","BRA",False]
time2 = [2,"Lanús","ARG",False]
time3 = [3,"Rosario Central","ARG",False]
time4 = [4,"Independiente Rivadavia","ARG",False]
time5 = [1,"Fluminense","BRA",False]
time6 = [2,"Corinthians","BRA",False]
time7 = [3,"Junior","COL",False]
time8 = [4,"Deportes Tolima","COL",True]

adicionar_time(grupao, "A", time1)
adicionar_time(grupao, "A", time7)
adicionar_time(grupao, "A", time2)
adicionar_time(grupao, "A", time8)
adicionar_time(grupao, "B", time5)


print(pode_adicionar(grupao, "B", time1))
print(pode_adicionar(grupao, "B", time2))
print(pode_adicionar(grupao, "B", time3))
print(pode_adicionar(grupao, "B", time4))
print(pode_adicionar(grupao, "B", time5))
print(pode_adicionar(grupao, "B", time6))
print(pode_adicionar(grupao, "B", time7))
print(pode_adicionar(grupao, "B", time8))


print(listar_times(grupao, "A"))
print(listar_times(grupao, "B"))
"""