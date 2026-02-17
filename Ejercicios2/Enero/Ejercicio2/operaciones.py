def calcularPosicion (n,datos):
    posicion=[]
    aparece=False
    contador=0
    for i in datos:
        contador+=1
        if i==n:
            posicion.append(contador)
            aparece=True

    if aparece:
        return posicion
    else:
        print(n,"no aparece en esta lista de datos")
        return -1


def calcularPosicionAñade (n,datos):
    posicion = []
    aparece = False
    contador = 0
    for i in datos:
        contador += 1
        if i == n:
            posicion.append(contador)
            aparece = True

    if aparece:
        return posicion
    else:
        datos.insert(n-1,n)
        return datos