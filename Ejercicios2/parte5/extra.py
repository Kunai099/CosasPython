try:
    base=int(input("Ingrese el tamaño de la base del triangulo: "))
    while True:
        if base < 1:
            print("Escribe un numero mayor")
        else:
            break
    for i in range(base):
        print("*"*i)
except ValueError:
    print("Error: Debes ingresar solo números.")