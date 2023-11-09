#Si el modulo se encuentra en la misma ruta, entonces se importa asi
#import funcionesBuenas.saludar as saludo2

# si el modulo se encuentra fuera de esta ruta
import sys
sys.path.append("C:\\Users\\pared\\Proyects\\Curso-Py\\funcionesBuenas")
import moduloSaludar as m_saludar
print(m_saludar.saludar("Chana"))