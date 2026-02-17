import math as m

def info_argumentos(*args):
    contador=0
    for i in args:
        contador+=1
    return contador

def divisibles3(*args):
    for i in args:
        try:
            if i%3==0:
                print(i)
        except ValueError:
            print("Debes introducir solo numeros")

def histograma(*args):
    for i in args:
        try:
            print(i*("*"))
        except ValueError:
            print("Debes introducir solo numeros")

def coste_envio(*args):
    precio=5
    try:
        peso=m.floor(args[0])
        if peso >= 1:
            precio = precio + (peso * 2)

        if args.__len__() > 1:
            if args[1]:
                precio = precio + ((precio * 30) / 100)

        return precio

    except ValueError:
        print("Debes introducir solo numeros")

def cantidad_segundos(horas,minutos,segundos):

    segundosTotales=horas*3600+minutos*60+segundos

    return segundosTotales