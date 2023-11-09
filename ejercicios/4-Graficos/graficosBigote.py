import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ejercicios\\4-Graficos\\dataValor.csv")

sns.boxplot(x="Categoria", y="Valor", data=df)


#mostrando grafico
plt.show()