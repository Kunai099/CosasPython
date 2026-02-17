import csv

with open("inventario.csv", "a", encoding="utf-8", newline="") as archivo_csv:
    wr = csv.writer(archivo_csv)
    wr.writerow(["Grapadora", "12.99", "50"])
    wr.writerow(["Bolígrafo", "0.99", "500"])
