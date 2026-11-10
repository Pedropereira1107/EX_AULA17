import matplotlib.pyplot as plt
from dados_pizza import dados_agrupados


plt.pie(dados_agrupados.values, labels=dados_agrupados.index, autopct='%1.1f%%', startangle=90)

plt.title("Número de casos de Covid-19 pela Grande Região de São Paulo")

plt.show()
