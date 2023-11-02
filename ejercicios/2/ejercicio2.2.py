#crear una funcion que nos devuelva los numeros primos
# entre 0 y el argumento que pasamos

#funcion que verifica si un numero es primo
def isPrimo(num):
  for i in range(2, num - 1): # si empieza por 1, cualquier numero es divisible por si mismo, lo mismo -1 para que no se divida por si mismo
    if num%i == 0: return False
  return True

def recorrerPrimos(num):
  primos= []
  for i in range(3, num + 1):
    resultado = isPrimo(i)
    if(resultado): primos.append(i)
  return primos
    
resultado = recorrerPrimos(98)
print(resultado)