with open("datos.txt") as f:
    palabras = f.read().split()

frecuencia = {}
for p in palabras:
    frecuencia[p] = frecuencia.get(p, 0) + 1

print(frecuencia)
