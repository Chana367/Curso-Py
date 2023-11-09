# dos listas con nombres y apellido, escribir los datos en un archivo de forma optima con un for

nombres= ["Francisco", "Cantina", "Eduardo", "Carla", "Pablo", "Lucia"]
apellidos= ["Paredes", "Dias", "Olivares", "Caceres", "Caliva", "Mesina"]

def escribirArchivo():
  with open ("ejercicios\\3\\archivos\\datos.txt", "a", encoding= "utf-8") as archivo:
   # for nom, apell, i in zip(nombres, apellidos,enumerate(nombres)):
   #   mensaje = f"Registro {i[0]+1} - {nom} {apell}"
   #   archivo.writelines(mensaje + "\n")
   #Forma optima
   [archivo.writelines(f"Registro {i[0]+1} - {nom} {apell}" + "\n") for nom,apell, i in zip(nombres,apellidos, enumerate(nombres))]

def leerArchivo():
  with open ("ejercicios\\3\\archivos\\datos.txt", "r", encoding= "utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)



escribirArchivo()
leerArchivo()   
    
    
    
