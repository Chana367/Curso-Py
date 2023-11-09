import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ejercicios\\4-Graficos\\dataIngresos.csv")
#creando grafico
colores = ['blue', 'green', 'orange', 'red']

sns.barplot(x="fuente", y="ingresos", data=df, palette=colores)

totalIngresos =  df['ingresos'].sum()
print(f"Total ingresos: ${totalIngresos} USD")

#mostrando grafico
plt.show()