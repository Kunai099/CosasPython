import csv

with open("datos.csv", "r", encoding="utf-8", newline="") as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila)
