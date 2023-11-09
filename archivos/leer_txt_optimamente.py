with open("archivos\\texto.txt", encoding="UTF-8") as archive:
  contenido= archive.read()
  print(contenido)
  
  #no es necesario cerrar el archivo