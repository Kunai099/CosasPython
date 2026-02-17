frase = input("Introduce una frase: ")

palabras = frase.split()

clave = input("Introduce una palabra clave: ")

inicial = clave[0].lower()

filtradas = []
descartadas = []

for p in palabras:
    if p.lower().startswith(inicial):
        filtradas.append(p)
    else:
        descartadas.append(p)

cadena_filtrada = " | ".join(filtradas)
cadena_descartada_inversa = " | ".join(descartadas[::-1])

print("RESULTADOS:")
print("Frase original:", frase)
print("Palabra clave introducida:", clave)
print("Palabras filtradas:", filtradas)
print("Palabras descartadas:", descartadas)
print("Cadena filtrada:", cadena_filtrada)
print("Cadena descartada en orden inverso:", cadena_descartada_inversa)
