# Cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("ejercicios\\3\\archivos\\datos2.csv")
#conviertiendo a string los datos de una columna
df['edad'] = df['edad'].astype(str)
#mostrando el tipo de dato
#print(type(df['edad'][0]))

#reemplazando valores 
df['apellido'].replace("Paredes", "DIAZ", inplace=True)
#print(df['apellido'])

#eliminar filas vacios
# dropna(axis=1) elimina columnas vacias 
df = df.dropna()


#eliminar duplicados
df = df.drop_duplicates()
print(df)
df.to_csv("ejercicios\\3\\archivos\\datosNuevos.csv")