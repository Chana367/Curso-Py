#diferencia en porcentaje entre el curso actual y...
cursoActual = 1.5
cursoMin = 2.5
cursoPromedio = 4 
cursoMax= 7
 
diffConMin = 100 - (cursoActual / cursoMin  * 100)
diffConProm = 100 - (cursoActual / cursoPromedio * 100)
diffConMax = 100 - (cursoActual / cursoMax * 100)
diffConMax2 = 100 - (cursoActual * 1000 // cursoMax) / 10

diffMin = 100 - (cursoActual / cursoMin) * 100
diffProm = 100 - (cursoActual / cursoPromedio * 100)
diffMax = 100 - (cursoActual / cursoMax) * 100

diffMin = round(diffMin, 2)
diffProm = round(diffProm, 2)
diffMax = round(diffMax, 2)

#primero paso la coma del cursoActual == 1500
#luego lo divido por cursoMAX (7) = 214 que ignora los numeros despues de la coma
# Lo divido en 10 para agregarle la come = 21,4
# por ultimo a 100 se le resta 21,4 para obtener la diff en promedio

print(f"el curso Actual dura un {diffConMin}% MENOS que el curso mas rapido")
print(f"el curso Actual dura un {diffConProm}% MENOS que el curso promedio")
print(f"el curso Actual dura un {diffConMax:.2f}% MENOS que el curso mas lento LIMITANDO LA CADENA")
print(f"el curso Actual dura un {diffConMax2}% MENOS que el curso mas lento CAMBIANDO LA FORMULA")

print(f"NEW el curso Actual dura un {diffMin}% MENOS que el curso mas rapido")
print(f"NEW el curso Actual dura un {diffProm}% MENOS que el curso promedio")
print(f"NEW el curso Actual dura un {diffMax}% MENOS que el curso mas lento CAMBIANDO LA FORMULA")

print("----------------------------------------------------------------")

# B porcentaje de material crudo
crudoProm = 5
crudoActual = 3.5

diffCrudoProm = 100 - (cursoPromedio * 1000 // crudoProm) / 10
diffCrudoActual = 100 - (cursoActual * 1000 // crudoActual) / 10

crudoProm = 100 - (cursoPromedio / crudoProm) * 100
crudoActual = 100 - (cursoActual / crudoActual) * 100
crudoProm = round(crudoProm, 2)
crudoActual = round(crudoActual, 2)


print(f"el porcentaje de material inservible eliminado en un curso promedio es {diffCrudoProm}%")
print(f"el porcentaje de material inservible eliminado en un curso actual es {diffCrudoActual}%")

print(f"NEW el porcentaje de material inservible eliminado en un curso promedio es {crudoProm}%")
print(f"NEW el porcentaje de material inservible eliminado en un curso actual es {crudoActual}%")
print("----------------------------------------------------------------")

diffEsteCurso = round((cursoPromedio / cursoActual) * 10, 2)
diffOtrosCurso = round((cursoActual / cursoPromedio) * 100, 2)
print(f"ver 10 horas de este curso equivale a ver  {cursoPromedio * 1000 // cursoActual / 100}% horas de otros cursos")
print(f"ver 10 horas de otros cursos equivale a ver  {cursoActual * 1000 // cursoPromedio / 100}% horas de este curso")
print(f"NEW ver 10 horas de este curso equivale a ver  {diffEsteCurso}% horas de otros cursos")
print(f"NEW ver 10 horas de otros cursos equivale a ver  {diffOtrosCurso}% horas de este curso")



