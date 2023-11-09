#import moduloSaludar as m_saludo
#import moduloSaludar 
#from moduloSaludar import saludar
import moduloSaludar as saludar


saludo = saludar.saludar("Chana")
print(saludo)
print(saludar.__name__) # este retorna el nombre del modulo del cual se importo la funcion, en este caso saludar