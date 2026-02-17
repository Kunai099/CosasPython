asignaturas={
    "matematicas" : 6,
    "fisica" : 5,
    "quimica" : 8
}

total=0

for x in asignaturas:
    print(x,"tiene",asignaturas[x],"creditos")
    total += asignaturas[x]

print("El total de créditos es:",total)