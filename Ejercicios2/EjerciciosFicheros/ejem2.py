import string

with open("datos.txt") as f:
    contenido = f.read()

    for signo in string.punctuation:
        contenido = contenido.replace(signo, "")

    palabras = contenido.lower().split()

diccionario = {}

for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1

print(diccionario)
