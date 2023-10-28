# crear funcion hola mundo
def saludar():
  print("Hola Mundo")
  
# crear funcion con parametro con adjetivo, nombre, sexo, el ad
def saludarV2(nombre, sexo):
  sexo = sexo.lower()
  if(sexo == "mujer"):
    adjetivo = "maestra"
  elif(sexo == "hombre"):
    adjetivo = "maestro"
  else:
    adjetivo = "coso"
    
  print(f"Hola {nombre} ¿Como estas {adjetivo}?")


saludarV2("Francisco", "hombre")
saludarV2("Carla", "mujer")
saludarV2("Lucas", "no binario")

def crear_contrasena_random(num):
  chars = "abcdefghijklmnopqrstuvwxyz"
  num = str(num)
  num = int(num[0])
  c1 = num - 2
  c2 = num
  c3 = num + 2
  contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
  return contrasena, c1

password, numero = crear_contrasena_random(98234795234)
print("password: ", password)
print("numero: ", numero)

