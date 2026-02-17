import csv

total = 0
cont = 0

with open("notas.csv") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        total += int(fila["Nota"])
        cont += 1

print(total / cont)
