#hacer forma no optima
def calcular(numeros):
  resultado = 0 
  for num in numeros :
    resultado += num
  return resultado

print(calcular([1,2,3,42,12,13]))

#hacer forma con argss, con el parametro nombre
def calcular1(nombre, *numeros):
  return f"Hola {nombre} tu resultado es: {sum(numeros)}"

print(calcular1("Francisco", 1,32,4,213,42,2))

def calcular2(numeros):
    return f"Hola tu resultado2 es: {sum([*numeros])}"

print(calcular2([22,1,32,4,213,42,2]))


#hacer forma con args y listas