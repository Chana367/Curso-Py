import csv
with open("archivos\\datos.csv") as archivo:
  reader = csv.reader(archivo)
  for row in reader:
    print(row)

import os
import sys

print(os.path.dirname(sys.executable))