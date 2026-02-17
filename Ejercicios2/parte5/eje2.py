while True:
    entrada = input("Ingresa un número (o 'salir' para terminar): ").lower()
    if entrada == "salir":
        print("Saliendo del programa...")
        break
    try:
        numero = int(entrada)
        for x in range(11):
            print (numero," * ", x, " = ", numero * x)
    except ValueError:
        print("Error: Debes ingresar solo números")