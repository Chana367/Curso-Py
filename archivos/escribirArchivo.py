with open("archivos\\texto.txt", "w", encoding="utf-8") as archivo:
  # En caso de no encotrar el archivo lo crea y si no, lo sobreescribe
  #archivo.write("Hola chana")
  archivo.writelines(["- Hola don pepito\n", "- Hola don jose\n"])
  
  