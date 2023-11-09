#crear funcion fibonacci

def calcularFibonacci(num):
  listaNumeros = [0]
  a,b = 0,1
  for i in range(num):
    if(b > num):return listaNumeros
    else:
      listaNumeros.append(b)
      a,b = b, a + b
  
resultado = calcularFibonacci(12)
#print(resultado)

primosHasta1 = lambda num: list(filter(lambda x: all(x % i !=0 for i in range(2, int(x**0.5) +1)), range(2,num)))
print(primosHasta1(15))