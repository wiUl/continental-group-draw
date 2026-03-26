from bs4 import BeautifulSoup

from pathlib import Path

import requests
import pandas as pd
import re


html = requests.get("https://gol.conmebol.com/libertadores/es/news/sorteo-de-la-fase-de-grupos-de-la-conmebol-libertadores-2026-fecha-horario-clasificados").content

soup = BeautifulSoup(html, 'html.parser')


#trecho indicando os times que vieram da fase pre e que possuem critério de sorteio diferente dos demais
fase_pre = soup.find(
    lambda tag: tag.name == "p" and 
    "La cuarta línea se conformó de cuatro equipos provenientes de la Fase 3 (Independiente Medellín,"
    " Deportes Tolima, Sporting Cristal y Barcelona) más los cuatro equipos subsecuentes del Ranking de CLUBES CONMEBOL"
    " del 15 de diciembre de 2025." in tag.get_text(strip=True)
)

#tratamento para retirar somente o trecho entre parênteses que cita os times
txt_times = re.search(r"\((.+?)\)", fase_pre.get_text(strip=True))

txt_times = txt_times.group(1)

txt_times = txt_times.replace(" y ", ", ")

#lista com o nome dos times que vem da fase 3 ou fase pré
clubes_pre = []

clubes_pre = txt_times.split(",")
clubes_pre = txt_times.strip()

#cabeçalho de onde se encontra a lista de times divididos por pote 
cabecalho = soup.find(
    lambda tag: tag.name == "h3" and
    "¿Cómo están conformados los bolilleros de la CONMEBOL Libertadores?" in tag.get_text(strip=True)
)

# iteração até achar as linhas com os potes 1,2,3,4
primeiro_paragrafo = cabecalho.find_next("p")

segundo_paragrafo = primeiro_paragrafo.find_next("p")

pote1 = segundo_paragrafo.find_next("p")
pote2 = pote1.find_next("p")
pote3 = pote2.find_next("p")
pote4 = pote3.find_next("p")

linhas = [pote1.get_text(strip=True), pote2.get_text(strip=True), pote3.get_text(strip=True), pote4.get_text(strip=True)]

registros = []

for linha in linhas:
    #separa a parte Bolillero x : dos nomes dos times
    parte_pote, parte_times = linha.split(":", 1)

    #pega o número do trecho Bolillero 1,2,3,4
    pote = int(re.search(r"\d+", parte_pote).group())

    parte_times = parte_times.replace(" y ", ", ")
    parte_times = parte_times.replace(" e ", ", ")
    parte_times = parte_times.rstrip(".")

    #cria lista com os nomes dos clubes
    clubes = parte_times.split(",")

    for clube in clubes:
        clube = clube.strip()
        #separa o nome do time do pais que representa, Exemplo separa Fluminense (BRA) em Fluminense.group(1), BRA.group(2)
        match = re.search(r"(.+?)\s*\((.+?)\)", clube)
        if match:
            time = match.group(1).strip()
            pais = match.group(2).strip()

            #lista o registros
            registros.append({"pote": pote, "time": time, "pais": pais, "fase_pre": time in clubes_pre})

#cria o dataframe
df = pd.DataFrame(registros, columns=["pote", "time", "pais", "fase_pre"])
caminho = Path(r"C:\Users\wiul\Documents\Projetos\Continental-Group-Draw\Libertadores\data\processed")
df.to_csv(caminho /"times_por_pote_LA_2026.csv", na_rep="None", index=False)





