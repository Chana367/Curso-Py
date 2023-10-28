#creanndo un diccionario con dict()

diccionario = dict()

#las listas no pueden ser keys y se usa frozenset para meter conjuntos como claves
diccionario = {frozenset(["Francisco", "Paredes"]): "es estudiante"}

#creando diccionario con fromkeys para dejar los valores en none
diccionario = dict.fromkeys(["nombre", "apellido"])
diccionario = dict.fromkeys("ABCDEF")

diccionario = dict.fromkeys(["nombre", "apellido"], "DESCONOCIDO")


print(diccionario)