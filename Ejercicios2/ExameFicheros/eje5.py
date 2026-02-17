import csv

with open("empleados.csv") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        if int(fila["Salario"]) > 3000:
            print(fila)
