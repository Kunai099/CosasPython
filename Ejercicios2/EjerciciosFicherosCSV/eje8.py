import csv

arriba = ["Nombre", "Edad", "Grado"]

estudiantes = [
    {"Nombre": "Juan", "Edad": "20", "Grado": "A"},
    {"Nombre": "Ana", "Edad": "22", "Grado": "B"},
    {"Nombre": "Luis", "Edad": "21", "Grado": "A"}
]

with open("estudiantes.csv", "w", encoding="utf-8", newline="") as archivo_csv:
    wr = csv.DictWriter(archivo_csv, fieldnames=arriba)
    wr.writeheader()
    wr.writerows(estudiantes)

print("Datos escritos en estudiantes.csv")