import math

def calcular_distancias(p1, p2):
    distancia = math.sqrt((p1[1] - p1[0]) ** 2 + (p2[1] - p2[0]) ** 2)
    return distancia