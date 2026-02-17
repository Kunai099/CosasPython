import csv

input_file = "archivo_grande.csv"
lineas_por_fichero = 50

with open(input_file, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    cabecera = next(reader)

    fichero_idx = 1
    filas = []

    for i, fila in enumerate(reader, start=1):
        filas.append(fila)

        if i % lineas_por_fichero == 0:
            with open(f"salida_{fichero_idx}.csv", "w", newline="", encoding="utf-8") as out:
                writer = csv.writer(out)
                writer.writerow(cabecera)
                writer.writerows(filas)

            filas = []
            fichero_idx += 1

    if filas:
        with open(f"salida_{fichero_idx}.csv", "w", newline="", encoding="utf-8") as out:
            writer = csv.writer(out)
            writer.writerow(cabecera)
            writer.writerows(filas)
