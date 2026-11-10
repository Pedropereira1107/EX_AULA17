import matplotlib.pyplot as plt
from dados_polio import df_top5, col_casos


df_top5.boxplot(column = col_casos, by = "Cobertura vacinal", figsize = (10, 6))

plt.suptitle("")
plt.title("Casos de poliomielite x Cobertura vacinal (5 países com mais casos)")
plt.xlabel("Cobertura vacinal (% de crianças de 1 ano com 3 doses)")
plt.ylabel("Casos por milhão de habitantes")

plt.show()
