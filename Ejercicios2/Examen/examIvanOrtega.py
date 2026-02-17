import operaciones as o

argumento1=(1,2,3,4,5,6,7,8,9,10,11,12)
argumento2=(3,7,2,9,10,12,15,16,18)
argumento3=(7,9,18,3,1,5)
argumento4=([2.7,False])
argumento5=([2.7,True])
argumento6=([2.7])

print("Numero argumentos:",o.info_argumentos(*argumento1))

print("Divisibles entre 3:")
o.divisibles3(*argumento2)

print("Histograma")
o.histograma(*argumento3)

print("Coste envio urgente false:",o.coste_envio(*argumento4))

print("Coste envio urgente true:",o.coste_envio(*argumento5))

print("Coste envio sin urgente:",o.coste_envio(*argumento6))

correcto=False

while not correcto:
    horas=input("Introduce las horas:")
    minutos=input("Introduce los minutos:")
    segundos=input("Introduce los segundos:")

    try:
        horas=int(horas)
        minutos=int(minutos)
        segundos=int(segundos)
    except ValueError:
        print("Introduce solamente numeros")
        continue
    
    if horas<0 or horas>23 or minutos<0 or minutos>59 or segundos<0 or segundos>59:
        print("Introduce valores validos (horas 0-23, minutos 0-59, segundos 0,59)")

    else:
        correcto=True
        
print("Cantidad de segundos totales:",o.cantidad_segundos(horas,minutos,segundos))