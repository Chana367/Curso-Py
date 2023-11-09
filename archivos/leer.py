# a la hora de ejecutar los metodos read, se puede hacer 1 sola vez por cada vez que se abra y cierra el archivo
archivo = open("archivos\\texto.txt", encoding="UTF-8")
# leer el archivo completo
#archivoSinLeer = archivo.read()

#leer una linea, el numero que le pasemos como parametro, indicara la cantidad de caracteres
#archivoSinLeer = archivo.readline()

#retorna un arreglo con totas las lineas, si le pasamos numero como param, indicara el length del array
archivoSinLeer = archivo.readlines()
archivo.close()


print(archivoSinLeer)