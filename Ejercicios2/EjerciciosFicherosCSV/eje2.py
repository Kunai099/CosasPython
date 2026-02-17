import csv

contador = 0
with open("datos.csv", "r", encoding="utf-8", newline="") as archivo_csv:
    lector = csv.reader(archivo_csv)

    next(lector)

    for fila in lector:
        contador += 1

print(contador)

