texto1 = "Hola soy Francisco"
texto2 = "Chana s chana"

#Mayusculas
mayusculas = texto1.upper()
#minusculas
minusculas = texto1.lower()
#primer Letra mayuscula
primerLetra = texto1.capitalize()


# find, se encarga de buscar una cadena sobre otra, en caso de no coincidir, retorna -1
busqueda = texto1.find("saa")
#index, se encarga de buscar al igual que el anterior, pero en caso de no coincidir, retorna una exception
busquedaIndex = texto1.index("Hola")

#is Numeric, devuelve true en caso de encontrar numeros en la variable
isNumero  = texto2.isnumeric()
#is alphanumerico en caso de encontrar valores de la Aa-Zz, los espacios no los incluye 
isAlpha = texto2.isalpha()

#count cuenta la cantidad de coincidencias que existen en la cadena
cantCoincidencias = texto2.count("a s")
#len cuenta la cantidad de caracteres que tiene una cadena, este es una funcion y no un metodo
cantCaracteres = len(texto2)

#bandera si empieza o termina una cadena con otra cadena dada
empieza = texto2.startswith("Chana")
termina = texto2.endswith("chana")

#si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
nuevoTexto = texto2.replace("chana", "Chana")
# en caso de querer separar una cadena en una lista
textoSeparado = texto2.split(" ")
 
print(textoSeparado)


