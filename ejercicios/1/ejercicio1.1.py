#diferencia en porcentaje entre el curso actual y...
cursoActual = 1.5
cursoMin = 2.5
cursoPromedio = 4 
cursoMax= 7
 
diffConMin = 100 - (cursoActual / cursoMin  * 100)
diffConProm = 100 - (cursoActual / cursoPromedio * 100)
diffConMax = 100 - (cursoActual / cursoMax * 100)
diffConMax2 = 100 - (cursoActual * 1000 // cursoMax) / 10
#primero paso la coma del cursoActual == 1500
#luego lo divido por cursoMAX (7) = 214 que ignora los numeros despues de la coma
# Lo divido en 10 para agregarle la come = 21,4
# por ultimo a 100 se le resta 21,4 para obtener la diff en promedio

print(f"el curso Actual dura un {diffConMin}% MENOS que el curso mas rapido")
print(f"el curso Actual dura un {diffConProm}% MENOS que el curso promedio")
print(f"el curso Actual dura un {diffConMax:.2f}% MENOS que el curso mas lento LIMITANDO LA CADENA")
print(f"el curso Actual dura un {diffConMax2}% MENOS que el curso mas lento CAMBIANDO LA FORMULA")

print("----------------------------------------------------------------")

# B porcentaje de material crudo
crudoProm = 5
crudoActual = 3.5

diffCrudoProm = 100 - (cursoPromedio * 1000 // crudoProm) / 10
diffCrudoActual = 100 - (cursoActual * 1000 // crudoActual) / 10


print(f"el porcentaje de material inservible eliminado en un curso promedio es {diffCrudoProm}%")
print(f"el porcentaje de material inservible eliminado en un curso actual es {diffCrudoActual}%")
print("----------------------------------------------------------------")

print(f"ver 10 horas de este curso equivale a ver  {cursoPromedio * 1000 // cursoActual / 100}% horas de otros cursos")
print(f"ver 10 horas de otros cursos equivale a ver  {cursoActual * 1000 // cursoPromedio / 100}% horas de este curso")



