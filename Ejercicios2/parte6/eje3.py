numero=7
minimo=80
maximo=200
for i in range(minimo, maximo):
    if i%numero==0:
        print(i)
        break
else:
    print("No hay ningun numero que cumpla las condiciones")