import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ejercicios\\4-Graficos\\datos.csv")
#creando grafico
sns.lineplot(x="fecha", y="wins", data=df)
#creando punto
plt.plot("01-03",445, "o")
#mostrando grafico
plt.show()