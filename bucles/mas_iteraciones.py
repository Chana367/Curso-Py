frutas= ["manzana", "naranja", "mandarina", "granada", "sandia"]
cadena = "Hola mundo"
numeros= [2,4,5,6,7,8,9,10,11,12]
for fruta in frutas:
  if fruta == "granada":
    continue
  print(fruta)
  
  

for fruta in frutas:
  if fruta == "naranja":
    break
  print(fruta)

print("Bucle terminado!!")


#recorrer cadena
for c in cadena:
  print(c)

#recorrer for en una sola linea

numerosDuplicados= [x*2 for x in numeros]
print("Numeros duplicados", numerosDuplicados)