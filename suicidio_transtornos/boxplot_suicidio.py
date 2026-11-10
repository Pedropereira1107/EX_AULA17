import matplotlib.pyplot as plt
from dados_suicidio import df, col_suicidio


#Boxplot 1: taxa de suicídio x taxa de transtorno mental e uso de substâncias

df.boxplot(column = col_suicidio, by = "Taxa de transtorno", figsize = (10, 6))

plt.suptitle("")
plt.title("Taxa de suicídio x Taxa de transtorno mental e uso de substâncias")
plt.xlabel("Taxa de transtorno mental e uso de substâncias (por 100 mil pessoas)")
plt.ylabel("Suicídios por 100 mil pessoas")

plt.show()

#Boxplot 2: taxa de suicídio x quinquênio

df.boxplot(column = col_suicidio, by = "Quinquênio", figsize = (10, 6))

plt.suptitle("")
plt.title("Taxa de suicídio por quinquênio")
plt.xlabel("Quinquênio")
plt.ylabel("Suicídios por 100 mil pessoas")

plt.show()


