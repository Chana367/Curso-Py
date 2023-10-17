diccionario = {
  "nombre": "Francisco",
  "apellido" : "Paredes",
  "edad" : 20
}

#keys sirve para obtener un key_item, que son las claves creadas en el dict pero a su vez permite iterar
allClaves = diccionario.keys()
#get sirve para obtener un valor de una key en especifico del dict
#con get evito el error en caso de no encontrarlo
oneClave = diccionario.get("nombre")

#eliminar los elementos del dict
#diccionario.clear()
#eliminar un elemento del dict
result = diccionario.pop("clase", "No se encontro el elemento")

#obteniendo un elemento dict iterable
diccionarioIterable = diccionario.items()


print(diccionarioIterable)
