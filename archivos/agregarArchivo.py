with open("archivos\\texto.txt", "a", encoding="utf-8") as archivo:
  # En caso de no encotrar el archivo lo crea y si no, lo sobreescribe
  #archivo.write("Hola chana")
  #archivo.writelines(["- Hola soy carlos\n"])
  
  for i in range(5): archivo.writelines(f"-Linea {i} agregada\n")
  
  