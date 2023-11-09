import pandas as pd
#df = pd.read_csv("archivos\\datos.csv", names=["names", "lastnames", "ages"])
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")


# ordenar data frame de menor a mayor
menor = df.sort_values("edad")
# ordenar data frame de mayor a menor
mayor = df.sort_values("edad", ascending=False)
#concatenar 2 data frames
dataConcatenada = pd.concat([df, df2])
#acceder a la 3 primer filas con head
tresPrimerFilas = df.head(3)
#acceder a la 3 ultimas filas con tail
tresUltimasFilas = df.tail(3)
#acceder a la cantidad de filas y columnas con shape
rows, columns = df.shape
#obtener datos estadisticos del frame
datosEstadisticos = df.describe()
#acceder a un elemento especifico con loc
element1 = df.loc[3:"edad"]
#acceder a todas los apellidos de una columna con loc}
element2 = df.loc[:, "apellido"]
#acceder a un elemento especifico con iloc
element3 = df.loc[2:2]
#acceder a todas los apellidos de una columna con ioc
element4 = df.iloc[:, 1]

#acceder a la fila 3 con iloc
element5 = df.iloc[3, :] 
#acceder a la fila 3 con loc
element6 = df.loc[3, :]

#acceder las filas donde la edad es mayor a 30 
filasMayores = df.loc[df["edad"] > 18, :]
print(filasMayores)



