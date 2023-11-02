# 1 alumno es profesor
# 1 alumno es asistente 

#A pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de mayor a menor 
def cargarAlumnos(cantidad):
  listaAlumnos = []
  for i in range(cantidad):
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    alumno = (nombre, edad)
    listaAlumnos.append(alumno)
  listaAlumnos.sort(key= lambda x: x[1], reverse=True)
  asistente  = listaAlumnos[-1][0]
  profesor= listaAlumnos[0][0]
  return profesor, asistente

#B el mayor es el profesor y el menor el asistente ¿Quien es quien?
profesor, asistente = cargarAlumnos(2)
print(f"El profesor se llama: {profesor}, y el asistente: {asistente}")