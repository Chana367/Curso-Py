animales = ["peces", "perros","gatos", "pajaros"]
cantidades = [2, 1, 1, 2]

for animal in animales:
  print(animal)
  
for cant in cantidades:
  print(cant)
  
print("\n================================")

for animal, cant in zip(animales, cantidades):
  print(f"Tengo {cant} {animal}")
  
print("\n================================")
  
for num in range(5, 8):
  print(num)
  
print("\n================================")
#forma no optima
for num in range(len(cantidades)): # en este no funciona en conjuntos
  print(cantidades[num])
  
#forma correcta, retorna tuplas

for num in enumerate(cantidades):
  indice = num[0]
  valor= num[1]
  print(f"el indice es {indice} y su valor es {valor}")
  
print("\n================================")
  
#reto
for indice, valor in enumerate(cantidades):
  print(f"el valor de la tupla es {valor} y su indice es {indice}")
else: 
  print("El bucle se termino")
  
  
#Funcionan en listas, tuplas y conjuntos