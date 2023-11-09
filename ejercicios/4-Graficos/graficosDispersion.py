import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ejercicios\\4-Graficos\\dataGanancias.csv")

sns.scatterplot(x="tiempo", y="dinero ", data=df)


#mostrando grafico
plt.show()