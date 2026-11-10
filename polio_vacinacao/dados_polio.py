import pandas as pd

df = pd.read_csv("EX_AULA17/Dados/polio-rate-of-cases-vs-vaccination-coverage.csv")

col_casos = "Polio cases per 1 million population (WHO (2017))"
col_vacina = "Pol3 (% of one-year-olds immunized)"

#Removendo o que não é país (regiões não têm código e "World" é o total mundial)

df = df.dropna(subset = ["Code"])
df = df[df["Entity"] != "World"]

#Classificando a cobertura vacinal em 5 categorias

df["Cobertura vacinal"] = pd.cut(df[col_vacina],
                                 bins = [0, 20, 40, 60, 80, 100],
                                 labels = ["Muito baixa", "Baixa", "Média", "Alta", "Muito alta"],
                                 include_lowest = True)

print(df["Cobertura vacinal"].value_counts().sort_index())

#Selecionando os 5 países com mais casos (soma de todos os anos)

casos_por_pais = df.groupby("Entity")[col_casos].sum()

top5 = casos_por_pais.nlargest(5)

print(top5)

df_top5 = df[df["Entity"].isin(top5.index)]
