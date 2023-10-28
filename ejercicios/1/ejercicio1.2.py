#ejercicio A

#una persona promedio habla 2 palabras por segundo, pedirle al usuario que diga cualquier texto real y calcular cuanto tardaria en decir esa frase y cuantas palabras dijo

texto = input("Indica el texto a calcular: ")
cantPalabras = len(texto.split(" "))
cantSegundos = cantPalabras / 2
print(f"El usuario tardara {cantSegundos} segundos en decir esa frase. Y dijo {cantPalabras} palabras" )

# ejercicio B si se tarda mas de 1 minuto decirle un mensaje
if cantSegundos > 60:
  print("para flaco tampoco te pedi un testamento")

# ejercicio C si alguien habla un 30% mas rapido cuanto tardaria el en decirlo}

diff = cantSegundos * 1000 // ((100 + 100 * 30 / 100) / 100) / 100
#    para obtener 2 decimales        obtengo el 1.3 (30%)     divido en 100 para mover coma
print(f"si hablas un 30% mas rapido, tardarias {diff} segundos en decirlo ")