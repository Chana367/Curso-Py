# la idea es meter un conjunto dentro de otro conjunto
conjunto = set(["dato1", "dato2"])
#asi se mete un conjunto dentro de otro conjunto
conjunto1= frozenset(["dato1", "dato2"])
conjunto2= set([conjunto1, "dato2"])
print(conjunto2)


#teoria de conjuntos 

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6}

#si es un subconjunto
resultado = conjunto1.issubset(conjunto2)
#equals 
resultado = conjunto2 <= conjunto1

#si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
#equals 
resultado = conjunto1 > conjunto2

#esta funcion es si almenos 1 numero de un conjunto se encuentra en otro , si no se encuentra retorna true, caso contrario false
resultado = conjunto1.isdisjoint(conjunto2)
print(resultado)