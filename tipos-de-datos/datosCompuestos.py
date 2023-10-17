lista = ["Francisco", "Paredes", 20, 1.91, True]
tupla = ("Francisco", "Paredes", 20, 1.91, True) # tupla no se puede modificar


# el conjunto-set no puede tener datos duplicados y no se puede acceder mediante el indice como los anteriores
conjunto = {"Francisco", "Paredes", 20, 1.91, True}

# diccionario es similar a un JSON
diccionario = {
  'nombre': "Francisco",
  'apellido': "Paredes",
  'edad': 20,
  'altura': 1.91,
  'estado_animo': True
}
print(f"{diccionario['nombre']} de chana")
