def calcular_estadisticas(numeros):

    minimo = None
    maximo = None
    suma = 0

    for numero in numeros:
        if minimo is None or numero < minimo:
            minimo = numero
        if maximo is None or numero > maximo:
            maximo = numero
        suma += numero

    media = suma / len(numeros)
    return (minimo, maximo, media)
