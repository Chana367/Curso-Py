# encontrar el numero mas alto y el mas bajo en una lista con max y min
numeros = [2,24,511,52,3,5]

numerosMAX = max(numeros)
numerosMIN = min(numeros)

print(f"el numero mas bajo es {numerosMIN} y el mas alto es {numerosMAX}")

#redondear numero con decimales y redondearlo a 4 decimales
decimal = 233.45453987345798345789345746358345678678345
decimal = round(decimal, 2)
print(decimal)

#retorna False -> 0, vacio, False, None \ True -> distinto a 0, True, cadena, datos no vacio
resultado_bool = bool("sdsadsa")

#retorna True, si todos los valores son verdaderos
resultado_all = all([0,"true",[344,23]])

#suma todos los valores de un iterable
suma_total = sum(numeros)

print(suma_total)