import csv

suma=0
cont=0
with open("datos.csv", "r", encoding="utf-8", newline="") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        suma+=int(fila["N"])
        cont+=1
    media=suma/cont
    print(media)
