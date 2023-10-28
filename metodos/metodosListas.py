#creo una lista
lista = ["Francisco", "Paredes", 20, True]

#cantidad de elementos de una lista
cantElements = len(lista)

#agregar elementos a una lista

#al final de la lista
lista.append("Soltero")
#a un indice especifico
lista.insert(2, "Chana")
#agregar una lista a otra lista, o varios elementos a una lista
lista.extend(["juega a la pelota", 2003])

#eliminando elementos de una lista

# mediante su indice, los valores negativos, eliminan los ultimos valores de la lista
lista.pop(-2)
#eliminar un elemento por su valor
lista.remove("Chana")
#eliminar todos los elementos de una lista
lista.clear()

#ordenando una lista, para ordenar una lista no deben haber strings 
lista2 = [0,1,23,4,244,51,5555,2123,5]
#ordenar de forma asc(menor a mayor) 
lista2.sort()
#ordenar de forma desc(mayor a menor) 
lista2.sort(reverse=True)
#invierte cualquier lista independientemente si esta ordenada o no
lista2.reverse()


print(lista2)
