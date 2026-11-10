import pandas as pd

df = pd.read_csv("EX_AULA17/Dados/Dados-covid-19-municipios.csv", sep=";", encoding="latin-1")

#Limpando colunas vazias

df = df.dropna(axis = 1, how = "all")

print(df.shape)
print(df.columns)

#Juntando os dados 

dados_agrupados = df.groupby("Grande região")["Mun_Total de casos"].sum()

print(dados_agrupados)

