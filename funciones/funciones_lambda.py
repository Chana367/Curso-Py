#crear array de numeros 
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
#crear lambda que multiplique por 2 esos numeros
multiplicacion = lambda x: x * 2;
print(f"La multiplicacion es : {multiplicacion(6)}")
#crear funcion que diga si es par
def isPar(numero):
  if(numero%2 == 0):
    return True
#crear filter que cree una lista con los numeros pares
numerosPares = filter(isPar, numeros)
print(f"La pares con funcion es : {list(numerosPares)}")

#hacer lo mismo pero con una funcion lambda
numerosPares2 = filter(lambda numero:numero%2 == 0, numeros)
print(f"La pares con lambda es : {list(numerosPares2)}")

numerosImpares = filter(lambda numero:numero%2 == 1, numeros)
print(f"La impares con lambda es : {list(numerosImpares)}")
