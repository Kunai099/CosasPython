while True:
    print("--- Calculadora ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    entrada = input("Ingresa una opcion: ").lower()

    if entrada == "suma" or entrada == "1":
        try:
            numero1 = int(input("Ingresa el primer numero: "))
            numero2 = int(input("Ingresa el segundo numero: "))
            print("El resultado es:", numero1 + numero2)
        except ValueError:
            print("Error: Debes ingresar solo números.")
    elif entrada == "resta" or entrada == "2":
        try:
            numero1 = int(input("Ingresa el primer numero: "))
            numero2 = int(input("Ingresa el segundo numero: "))
            print("El resultado es:", numero1 - numero2)
        except ValueError:
            print("Error: Debes ingresar solo números.")
    elif entrada == "multiplicacion" or entrada == "3":
        try:
            numero1 = int(input("Ingresa el primer numero: "))
            numero2 = int(input("Ingresa el segundo numero: "))
            print("El resultado es:", numero1 * numero2)
        except ValueError:
            print("Error: Debes ingresar solo números.")
    elif entrada == "division" or entrada == "4":
        try:
            numero1 = int(input("Ingresa el primer numero: "))
            numero2 = int(input("Ingresa el segundo numero: "))
            print("El resultado es:", numero1 / numero2)
        except ValueError:
            print("Error: Debes ingresar solo números.")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
    elif entrada == "salir" or entrada == "5":
        print("Saliendo...")
        break
    else:
        print("La opción no existe, intenta de nuevo.")
