import pandas as pd

df = pd.read_csv("EX_AULA17/Dados/suicide-rates-vs-prevalence-of-mental-and-substance-use-disorders.csv")

col_suicidio = "Deaths - Self-harm - Sex: Both - Age: Age-standardized (Rate)"
col_transtorno = "Prevalence - Mental and substance use disorders - Sex: Both - Age: Age-standardized (Rate)"

#Removendo linhas sem dados de suicídio ou transtorno

df = df.dropna(subset = [col_suicidio, col_transtorno])

#Removendo o que não é país (sem código e "World" é o total mundial)

df = df.dropna(subset = ["Code"])
df = df[df["Entity"] != "World"]

#Classificando a taxa de transtorno mental e uso de substâncias em 5 categorias

df["Taxa de transtorno"] = pd.cut(df[col_transtorno],
                                  bins = 5,
                                  labels = ["Muito baixa", "Baixa", "Média", "Alta", "Muito alta"])

print(df["Taxa de transtorno"].value_counts().sort_index())

#Separando os anos em quinquênios (os dados vão de 1990 a 2017)

df["Quinquênio"] = pd.cut(df["Year"],
                          bins = [1990, 1995, 2000, 2005, 2010, 2015, 2020],
                          labels = ["1990-1994", "1995-1999", "2000-2004", "2005-2009", "2010-2014", "2015-2017"],
                          right = False)

print(df["Quinquênio"].value_counts().sort_index())
